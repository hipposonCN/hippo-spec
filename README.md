# Hippo Spec

Hippo Spec V2 是一个 continuation-first 的薄路由器：根任务只判断一次是否需要持久 specification，随后把固定的 `Hippo Spec Context` 交给执行者，不在每个高风险阶段重复启动完整生命周期。

在已启用 OpenSpec 的项目中，[OpenSpec](https://github.com/Fission-AI/OpenSpec) 是唯一的行为与 change 权威。[Matt Pocock Skills](https://github.com/mattpocock/skills) 仅作为按需工程方法库，不形成第二套 spec、ticket 或流程权威。

## 六条路径

| 路径 | 适用情况 | 行为 |
|---|---|---|
| `skip` | 清晰、局部、可逆，一个反馈循环可完成 | 不创建规划产物；状态查询、简单 review 和机械修改保持在此 |
| `light` | 仍有一个会改变结果的关键决策未解决 | 只探索该决策，不创建持久 change |
| `full:new` | 新增尚未记录的持久行为、公共契约、权限或所有权决策，且需要跨会话协调 | 通过项目已有 OpenSpec 流程创建最小 change |
| `continue` | 已有同一 intent 的 OpenSpec change | 继承 change、scope、当前切片和验收证据，不重建 proposal/design/spec/tasks |
| `repair` | 已冻结行为中的缺陷或回归 | 复现 → 最小反馈循环 → 回归测试 → 最小修复 → 原症状验证 |
| `review-only` | 固定 PR、commit range、diff 或 `HEAD` 的终审 | 只消费已有规范和固定代码，不修改规划产物 |

路由优先续接既有 intent。跨仓库、安全、发布、迁移或多项验证本身都不会触发 `full:new`；它们只改变当前切片需要的验收证据。

## 一次判定，一路继承

根任务输出一次：

```yaml
hippo_spec_context:
  lane: continue
  active_change: exact-change-id
  scope_lock: authorized files and exclusions
  current_slice: one immediate objective
  acceptance_evidence: required checks and readbacks
```

子任务和后续执行者直接继承该上下文，不再次调用 Hippo Spec、不重新选 lane，也不自行扩大 scope。新的 intent 返回根任务另行判断。

## 工程方法与评审边界

`domain-modeling`、`tdd`、`diagnosing-bugs` 和 `code-review` 仅在对应阶段且已安装时使用；缺失时使用内置精简 fallback。在 OpenSpec 项目中不默认运行 Matt 的 `to-spec`、`to-tickets` 或完整 `implement` 链，也不增加强制运行时依赖。

Review finding 只有在包含可复现测试失败、明确引用规范的行为缺失，或明确引用仓库规则的违规时才阻塞。无证据建议和主观 code smell 不阻塞；最终双轴 review 原则上只运行一次，修复后只复查对应证据。

## 完成边界

- **artifact truth**：权威 specification/change 已存在且有效；
- **implementation truth**：实现满足当前切片并通过对应检查；
- **operational truth**：需要时，目标 release、进程、外部状态、receipt 或 fresh readback 已生效。

三者不能互相替代。commit、PR、merge、测试通过或任务勾选都不自动证明发布和 readback 完成。

## 安装

```bash
npx skills@latest add hipposonCN/hippo-spec
```

在 Codex 中可以明确调用：

```text
$hippo-spec 只做一次 lifecycle 判定；优先续接已有 change，并输出可继承的 Hippo Spec Context。
```

`full:new` 需要项目已经配置 OpenSpec；若尚未配置，Hippo Spec 会先征求授权，不会自行初始化。

## 仓库结构

```text
SKILL.md
agents/openai.yaml
references/full-lifecycle.md
references/engineering-discipline.md
references/routing-examples.md
```

## License

MIT
