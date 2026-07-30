# 高级 02：动态管理 Covered Call

> 覆盖视频：高级第 14–18 讲  
> 本章时长：约 54 分钟

本章不是普通“持股收租”，而是一套课程自定义的动态 Covered Call：把股票和 Short Call 当作整体，用组合 Delta 触发 Roll，并主动把组合维持在约 0.5 Delta。它实质上是不断卖出凸性、调整方向敞口，操作和税务都比普通 Covered Call 复杂。

## 第 14 讲：为什么把 Covered Call 当整体

课程看中三点：

- 历史波动可能低于持股；
- Short Option 可能获得波动率风险溢价；
- 股票与期权分开实现盈亏，可能提供税务时点弹性。

![课程列出的 Covered Call 长期优势](<../assets/advanced/chapter-02-equity-value-investing-strategies/lesson-14/frame-01-0292s.jpg>)

**图怎么看：**

- 较低波动来自上涨被封顶和权利金缓冲，不是免费降低风险；
- 卖方 Edge 不是固定收益；
- 个股 IV 高也意味着个股跳空和永久损失风险高；
- 税务效果取决于税务居民地、持股期限、Strike、到期日和是否被指派，不能从图中直接得出。

### 用 Synthetic 关系理解

同 Strike、同到期日下：

\[
\text{Covered Call}\approx\text{Cash-Secured Put}
\]

两者的到期 payoff 相似，因此 ATM Covered Call 仍是正 Delta 看涨结构，而不是“希望股票不涨”。

![Covered Call 与 Short Put 的对应](<../assets/advanced/chapter-02-equity-value-investing-strategies/lesson-14/frame-02-0561s.jpg>)

**图怎么看：**

- Covered Call 应看组合总盈亏，不应要求股票腿和 Call 腿同时盈利；
- ITM Covered Call 对应更 OTM 的 Cash-Secured Put，整体仍偏多；
- 现金、融资、股息和提前指派会造成实际差异；
- 课程所谓“持有过程始终优势”仍取决于动态 Greeks 和真实成交。

该结构最大的弱点是负 Gamma：

- 股价上涨，Call Delta 增大，组合 Delta 下降，越涨参与越少；
- 股价下跌，Call Delta 减小，组合 Delta 上升，越跌暴露越多。

## 第 15 讲：开仓与正常 Roll

课程初始规则：

- 持有 100 股；
- 卖约 4–6 周到期 ATM Call；
- 初始组合 Delta 约 0.5；
- 在剩余约 2–3 周时提前 Roll；
- 尽量让新组合 Delta 向 0.5 靠近。

![动态 Covered Call 的目标状态](<../assets/advanced/chapter-02-equity-value-investing-strategies/lesson-15/frame-01-0326s.jpg>)

**图怎么看：**

- ATM 通常外在价值较多，但“Edge 最高”没有普遍证明；
- 离到期过近，ATM Gamma 上升，组合 Delta 更不稳定；
- 期限过长，Gamma 较小但 Vega、资本承诺和调整成本不同；
- 4–6 周是课程经验，不是统一最佳 DTE。

正常 Roll 时，课程不要求一步精确回到 0.5，而是至少向 0.5 移动约 0.1，以减少调仓时点偶然性。

![渐进式把组合 Delta 拉回 0.5](<../assets/advanced/chapter-02-equity-value-investing-strategies/lesson-15/frame-02-0656s.jpg>)

**图怎么看：**

- 当前组合 Delta 0.3，Roll 后提高到约 0.4；
- 当前组合 Delta 0.7，Roll 后降低到约 0.6；
- 保持相同 Strike、延长到期日有时就会改变 Delta；
- 每次 Roll 都应记录旧 Call 实现盈亏和新 Call 的独立 Credit，不能只记录净现金。

## 第 16 讲：大涨、大跌与 Delta 触发

课程用组合 Delta 0.25–0.75 作为管理区间：

- 组合 Delta 接近 0.25：通常代表股票大涨、Short Call 深入 ITM；
- 组合 Delta 接近 0.75：通常代表股票大跌、Short Call 变 OTM。

### 大跌时

课程选择 Roll Down-and-Out，提高新 Call Delta，从而把组合 Delta 降回约 0.5。它确实降低即时方向风险，但代价是：

- 在股票下跌后卖出更低 Strike 的上涨权利；
- 反弹时更早被封顶；
- Roll Down 可能确认旧 Call 利润，却增加后续机会成本；
- 连续下跌时可能不断延长期限。

### 大涨时

Roll Up-and-Out，降低 Short Call Delta，让组合 Delta 从 0.25 提高。它恢复上涨参与，但往往需要回购已亏损的 Call。

![暴涨时恢复组合 Delta](<../assets/advanced/chapter-02-equity-value-investing-strategies/lesson-16/frame-01-0309s.jpg>)

**图怎么看：**

- Call 越 ITM，组合上涨参与越少；
- 向上 Roll 是用现金或更长期限换取新的上涨空间；
- “收益潜力最重要”不等于必须追涨调整；
- 应比较直接接受指派、平掉组合和 Roll 三种结果。

### 杠杆

课程建议约 1.5 倍起步、个人使用约 2 倍，理由是组合 Delta 多数约 0.5。

![课程对 Covered Call 加杠杆的逻辑](<../assets/advanced/chapter-02-equity-value-investing-strategies/lesson-16/frame-02-0633s.jpg>)

**图怎么看：**

- `杠杆 × Delta` 只近似小幅日常波动，不等于完整风险；
- 个股跳空时 Delta 会改变，Gamma、相关性和保证金同时恶化；
- 2 倍名义个股 + Short Call 不能视为与 1 倍持股同风险；
- 杠杆应按整个账户压力损失限制，不能按当前 Delta 倒推“安全”。

## 第 17 讲：极端行情下的局限

大涨大跌时，组合 Delta 频繁穿越阈值，反复 Roll 会产生 Whipsaw、滑点和税务事件。课程提出暂时去掉 Short Call，并把 100 股减为 50 股。

![极端行情中从 Covered Call 切换为半仓股票](<../assets/advanced/chapter-02-equity-value-investing-strategies/lesson-17/frame-01-0262s.jpg>)

**图怎么看：**

- 大跌时：平 Short Call、卖 50 股可快速降低约到 0.5 Delta；
- 大涨时：平 Short Call、保留 50 股反而可能提高当时很低的组合 Delta；
- 这会产生真实股票交易、税务和择时风险；
- “波动恢复正常后再切回”需要一个事先定义、可验证的信号，否则不是系统规则。

极端行情里最可靠的保护仍是开仓前限制账户名义金额和最大压力损失，而不是假设盘中总能按模型 Delta 调整。

## 第 18 讲：Covered Call 与 Short Put

课程把两套方法放进 Core–Satellite：

- 指数 Short Put：较被动的 Core；
- 个股动态 Covered Call：较主动的 Satellite。

![两套策略的管理方式](<../assets/advanced/chapter-02-equity-value-investing-strategies/lesson-18/frame-01-0231s.jpg>)

**图怎么看：**

- 指数分散度更高，不代表 Short Put 可以“大仓位大胆做”；
- 个股 Covered Call 需要监控基本面、财报、除息和跳空；
- 主动调整更多，犯错、成本和税务事件也更多；
- 两者风险应在账户层合并，不应分开看作独立安全仓。

### 税务不能照抄课程结论

课程称 Covered Call 的股票浮盈可递延、Call 亏损可抵税，因而一定优于 Short Put。实际情况复杂：

- Call 被指派会触发股票出售；
- 某些 Deep ITM 或不合格 Covered Call 可能影响股票持有期；
- Straddle、Wash Sale、Constructive Sale 等规则可能影响损益认定；
- 期权损益的短期/长期性质依合约和处理方式而异；
- Margin Interest 是否可抵扣受到用途、收入和当地规则限制。

![课程所说的税务时点差异](<../assets/advanced/chapter-02-equity-value-investing-strategies/lesson-18/frame-02-0433s.jpg>)

**图怎么看：**

- “浮盈不纳税、期权亏损抵税”不是无条件组合；
- 税务不能替代经济盈亏：Call 亏损通常对应股票上涨被封顶；
- 不同国家并非“大体相同”；
- 执行前必须按本人税务居民地和账户类型确认。

## 这套动态 CC 最容易犯的错

- 把组合 Delta 当最大风险；
- 下跌后持续 Roll Down，锁死反弹；
- 上涨后持续 Roll Up，为追回上涨反复付费；
- 用高频调整掩盖策略没有明确退出条件；
- 用 1.5–2 倍杠杆放大个股相关性；
- 依赖未经实盘成本验证的“ATM Edge”；
- 为税务理由保留已经失效的持股逻辑。

如果要使用，先以无杠杆、单一小仓位记录完整一轮，独立计算股票与每次 Call 的实现/未实现盈亏，再决定这套管理复杂度是否真的增加价值。
