# Hippo Spec

Hippo Spec 统一接住软件需求，选择最小工作方式，并依据证据完成收口。目标和权限有边界，设计可以随证据更新；流程不会因跨仓库、会话切换或发布而反复重启。

## 使用原则

- 先明确本轮交付结果：诊断、修复、合并或上线，按实际授权推进。
- 只维护一份行为与任务权威。已有 OpenSpec 的项目继续使用 OpenSpec；其他项目沿用现有文档或任务约定，无须安装框架。
- 行为变化决定是否更新规范，会话数量只决定是否需要交接。
- 只续接仍有效、未被替代且符合本轮范围的 change。历史任务不会自动成为本轮待办。
- 新证据可以修正设计假设和任务顺序，但不能自行增加功能、扩大权限或放宽验收。
- 通过短反馈循环验证行为；只在实际需要时增加集成检查、独立评审和运行回读。
- 完成本轮要求后，同步相应规范和任务状态；只关闭有证据完成或明确被替代的工作。

## 工作模式

| 模式 | 用途 |
|---|---|
| `skip` | 不改变行为契约的清晰局部修改，直接做并检查 |
| `light` | 调查问题并答复，随后继续已授权实施；只读诊断不修改文件 |
| `repair` | 复现已有行为的缺陷，最小修复并验证原症状 |
| `continue` | 接续有效 change 的下一段授权工作 |
| `full:new` | 记录尚未覆盖的行为差异，优先更新现有记录，然后进入 `continue` |
| `review-only` | 评审固定代码范围，报告发现，不修改实现或规划 |

模式描述当前工作，不是必须逐一通过的关卡。普通修改不需要输出路由表或建立任务文件。跨执行者或会话时，才传递已有的 `Hippo Spec Context`：有效记录、范围、当前切片和验收证据。

难定位的缺陷、间歇性故障或性能回退，优先使用已安装的 Matt Pocock [`diagnosing-bugs`](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs)；定义或修改领域术语、实体关系、责任边界时，优先使用 [`domain-modeling`](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)。普通修改不必启动这些方法。技能缺失时使用内置精简指引，Hippo Spec 始终保留本轮范围、授权与收口规则。

[OpenSpec](https://github.com/Fission-AI/OpenSpec) 项目使用其已有 schema 与同步、归档机制，不另建 spec/ticket 流程。领域词汇和 ADR 保存术语与决策理由，不替代行为规范。

## 完成意味着什么

需要留档时，规范应反映已授权的行为；需要实现时，行为应通过相应检查；要求上线或交付时，应取得运行或外部回读证据。任务勾选和测试通过不能代替后者。

一个已验收的小切片可以关闭，所属大 change 可以保留；若用户要求完成整个 change，就应继续剩余的授权工作。被替代的任务记录替代原因与去向，不能假装已实现。历史清理不自动并入本轮。

## 调用

正常描述任务即可，也可以明确调用：

```text
$hippo-spec 按现有规范完成这个改动；必要时随证据调整方案，保持范围，并用适用的验收证据收口。
```

安装：

```bash
npx skills@latest add hipposonCN/hippo-spec
```

技能入口见 [SKILL.md](SKILL.md)；行为验证样例见 [routing-examples.md](references/routing-examples.md)。

## License

MIT
