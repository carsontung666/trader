# 高级 03：SBS（Short Bullish Straddle）

> 覆盖视频：高级第 19–22 讲  
> 本章时长：约 42 分钟

本章的 SBS 是课程自定义名称：把 Short Straddle 的共同 Strike 放在现价上方，使 ITM Short Put 的正 Delta 大于 OTM Short Call 的负 Delta，形成初始净看涨的 Short Straddle。

它仍然包含 Naked Short Call，上方亏损理论无上限。课程最后称 SBS “比 Covered Call 风险更低、是所有策略中风险最低”，这个结论错误，不能用于实盘风控。

## 第 19 讲：结构与到期收益

同一 Strike \(K\)、同一到期日：

- Short Put；
- Short Call；
- \(K\) 设在当前股价上方；
- 收到总 Credit \(c\)。

到期盈亏为：

\[
\text{P/L per share}=c-|S_T-K|
\]

- 最大利润：\(100c\)，仅在到期股价等于 \(K\) 时；
- 下方盈亏平衡：\(K-c\)；
- 上方盈亏平衡：\(K+c\)；
- 上涨亏损理论无上限；
- 下跌最大亏损为 \(100(K-c)\)，发生于股价归零。

![SBS 是向上移动 Strike 的 Short Straddle](<../assets/advanced/chapter-03-advanced-value-investing-strategies/lesson-19/frame-01-0239s.jpg>)

**图怎么看：**

- Strike 高于现价时，Short Put 更 ITM，净 Delta 可为正；
- “Bullish”只描述开仓局部 Delta；
- 股价上涨穿过 Strike 后，净 Delta 会继续下降并可能变负；
- 到期收益仍是倒 V，绝不是普通长期持股曲线。

课程把它解释成“Covered Call 中用 Short Put 替换 100 股”，目的是同时收两份权利金。

![SBS 与动态 Covered Call 的关系](<../assets/advanced/chapter-03-advanced-value-investing-strategies/lesson-19/frame-02-0478s.jpg>)

**图怎么看：**

- 两条腿都是 Short Option，净 Short Gamma、Short Vega、通常正 Theta；
- 所谓“双倍 Edge”只是收两条腿权利金，不代表期望值翻倍；
- 负 Gamma 和双侧尾部也同时增加；
- 组合保证金是否等于单腿保证金完全取决于券商风险模型，课程表述不能通用。

## 第 20 讲：开仓参数

课程建议：

- 选择熟悉、流动性高、波动相对可控的标的；
- 到期约 4–7 周；
- 初始组合 Delta 约 0.3–0.5；
- 高杠杆时使用更低目标 Delta。

![期限在 Theta 与 Gamma 间取舍](<../assets/advanced/chapter-03-advanced-value-investing-strategies/lesson-20/frame-01-0279s.jpg>)

**图怎么看：**

- 更短期限 Theta 集中，同时 Gamma 更尖；
- 更长期限 Gamma 较缓，但 Vega 和事件暴露更长；
- 4–7 周只是课程折中，没有证明最优；
- 期限不能解决 Naked Call 的无上限风险。

### 用两腿 Delta 计算净方向

例如现价约 150：

- Short 155 Put Delta 约 +0.615；
- Short 155 Call Delta 约 -0.394；
- 净 Delta 约 +0.221。

提高共同 Strike 会提高 Put Delta、降低 Call 绝对 Delta，使组合更看涨，但同时改变盈亏平衡和上方裸 Call 距离。

![期权链中 SBS 两腿的 Delta](<../assets/advanced/chapter-03-advanced-value-investing-strategies/lesson-20/frame-02-0528s.jpg>)

**图怎么看：**

- Delta 是当前局部值，不是整个期限固定敞口；
- 组合 Delta 接近目标，不代表两侧最大亏损对称或可控；
- 必须同时看净 Gamma、Vega、Theta 和压力损失；
- Call 与 Put 若改用不同 Strikes，就变成 Short Strangle；不同期限则是更复杂的 Calendar/Diagonal，不能继续套同一到期公式。

## 第 21 讲：课程的动态 Roll 方法

课程先设目标 Delta，再设容许区间，例如：

- 目标 0.5：范围 0.25–0.75；
- 目标 0.3：范围 0.10–0.50。

正常情况下在剩余约 3–4 周时 Roll 到下一月，并让净 Delta 至少向目标移动 0.1。

![按目标 Delta 选择下一组 Strikes](<../assets/advanced/chapter-03-advanced-value-investing-strategies/lesson-21/frame-01-0298s.jpg>)

**图怎么看：**

- 课程例子把 290/290 两腿 Roll 到下一月 300/300；
- 一次要关闭两腿、开启两腿，至少四笔成交；
- 应使用组合订单并检查净 Debit/Credit；
- Roll 只重置敞口，不删除旧 Straddle 的实现盈亏。

课程还允许只 Roll 一腿，让另一腿继续赚近月 Theta。

![只 Roll Call 后形成不同到期日](<../assets/advanced/chapter-03-advanced-value-investing-strategies/lesson-21/frame-02-0540s.jpg>)

**图怎么看：**

- 一腿延期后已不再是同到期 Straddle；
- 两个期限的 Vega、Gamma 和事件暴露不同；
- 近月腿的 Theta 更快，但临近到期 Gamma 也更高；
- 只看净 Delta 可能掩盖 Calendar Basis Risk。

股价大涨使净 Delta 接近或低于区间下界时，课程建议 Roll Up-and-Out；股价大跌使净 Delta超过上界时，建议更大幅度地 Roll Down-and-Out。任何一种调整都无法保证在跳空前成交。

## 第 22 讲：为什么这套结构风险很高

SBS 比动态 Covered Call 更频繁触发 Delta 边界，因为两条 Short Legs 都贡献负 Gamma。

![SBS 的 Delta 更快离开目标区间](<../assets/advanced/chapter-03-advanced-value-investing-strategies/lesson-22/frame-01-0238s.jpg>)

**图怎么看：**

- 同为初始 0.5 Delta，SBS 可能只需较小股价移动就碰到 0.75；
- 更频繁调整意味着更多滑点、手续费和决策错误；
- 大涨后净 Delta 可变负，继续上涨时产生越来越大损失；
- 止损或 Roll 都不能封住隔夜跳空。

课程总结称 SBS 的优点是更强卖方 Edge，缺点是“双倍负 Gamma”。

![课程对 SBS 的最终总结](<../assets/advanced/chapter-03-advanced-value-investing-strategies/lesson-22/frame-02-0433s.jpg>)

**图怎么看：**

- “SBS 风险低于 Covered Call”与到期 payoff 冲突；
- Covered Call 上涨风险被股票覆盖，SBS 的 Short Call 是 Naked；
- 初始 Delta 较低只说明小幅行情下的局部敏感度，不代表尾部较低；
- 收益风险比优于 CC/Sell Put 的说法没有本章独立回测或实盘证据。

## 实盘上更合理的替代

若交易观点是“温和看涨 + 卖波动”，先考虑定义风险：

- Bull Put Spread：保留看涨 Short Volatility，但限定下跌；
- Broken-Wing Iron Butterfly / Condor：按不对称观点限定双侧；
- Covered Call：若已有股票，用股票覆盖 Short Call；
- Short Straddle/Strangle 加 Long Wings：把尾部封住。

无论如何，不应仅靠 Delta 阈值管理裸 Short Call。

## SBS 风险检查

- [ ] 上方股价翻倍时会亏多少？
- [ ] 下方归零时会亏多少？
- [ ] 券商在 IV 翻倍时要求多少保证金？
- [ ] 财报和重大事件是否落在期限内？
- [ ] 四腿 Roll 的最差成交滑点是多少？
- [ ] 一腿提前指派后会留下什么股票头寸？
- [ ] 是否可以加 Long Wings 把最大亏损写死？

如果任何一项不能明确计算，就不应把它当“长期低风险策略”。
