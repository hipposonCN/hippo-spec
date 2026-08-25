# Hippo Spec

让 Agent 在长项目开始前，先判断规格流程是否值得使用，再选择最小合适路径。

Hippo Spec 保留 [OpenSpec](https://github.com/Fission-AI/OpenSpec) 作为行为与变更的唯一账本，并吸收 [Matt Pocock Skills](https://github.com/mattpocock/skills) 中互补的领域建模、垂直切片 TDD、困难 Bug 诊断和双轴评审方法。

## 三条路径

| 路径 | 适用情况 | 行为 |
|---|---|---|
| `skip` | 清晰、局部、可逆、单会话可完成 | 不创建规格，直接做最小变更并验证 |
| `light` | 有重要不确定性，但暂不需要持久规格 | 先探索关键分支，不创建 OpenSpec change |
| `full` | 跨会话、跨仓库/运行时、迁移、发布或多重验收 | 进入完整 OpenSpec 生命周期 |

自动触发时，小任务会静默 `skip`；只有 `light` 或 `full` 才会说明判断理由。

## 安装

```bash
npx skills@latest add hipposonCN/hippo-spec
```

在 Codex 中也可以明确调用：

```text
$hippo-spec 先判断这个项目应该走 skip、light 还是 full，再采用最小合适流程。
```

`full` 路径需要项目已配置 OpenSpec；如果尚未配置，Hippo Spec 会先解释原因并征求确认，不会擅自初始化。

## 设计边界

- OpenSpec main specs 表示当前约定行为，单个 change 表示目标增量。
- `CONTEXT.md` 只保存术语；ADR 只保存难以逆转且存在真实权衡的决策。
- Issue 可以链接 OpenSpec change，但不能成为第二套规格真相。
- OpenSpec 校验、代码实现和实际运行状态是三种不同证据。
- commit、测试通过或任务勾选，不自动等于 release、进程、receipt 或 fresh readback 已完成。

## 仓库结构

```text
SKILL.md
agents/openai.yaml
references/full-lifecycle.md
references/engineering-discipline.md
```

入口保持精简；完整生命周期和工程方法仅在对应阶段按需加载。

## License

MIT
