# 高级 05：Risk Reversal 抄底与海鸥对冲

> 覆盖视频：高级第 28–29 讲  
> 本章时长：约 23 分钟

本章介绍两个看似“低成本”的组合。低成本只是开仓现金流较小，不代表风险较小：Risk Reversal 用卖 Put 承担下跌义务来购买上涨机会；海鸥用放弃一部分上涨和极端下跌保护来降低 Put 成本。

## 第 28 讲：用 Risk Reversal 博反弹

课程中的 Bullish Risk Reversal 使用相同到期日：

- 买入一张 OTM Call，行权价 \(K_C>S_0\)；
- 卖出一张 OTM Put，行权价 \(K_P<S_0\)；
- 通常调整 Strikes，使净 Debit 接近零。

到期盈亏可以写成：

\[
\Pi_T=\max(S_T-K_C,0)-\max(K_P-S_T,0)-D
\]

其中 \(D\) 是开仓净 Debit；如果收到 Credit，\(D\) 为负数。

![下跌时 Put 较贵、反弹时 Call 可能变贵](<../assets/advanced/chapter-05-other-strategies/lesson-28/frame-01-0268s.jpg>)

**图怎么看：**

- 下跌期间 Put Skew 常较陡，卖 Put 可能收到较多权利金；
- 反弹时 Call 价格可能同时受 Delta 和 IV/Skew 变化推动；
- 这只是可能的定价环境，不是稳定套利；
- Skew 若继续向 Put 侧走陡，Short Put 会同时遭受方向和波动率损失。

### “零成本”最容易造成的误解

课程把 Call 和 Put 权利金配成接近相同，并据此描述为 Theta 被抵消。更准确的理解是：

- 开仓净权利金接近零，不代表两腿 Theta 始终相等；
- 股价、IV、Skew 和剩余期限变化后，两腿 Greeks 会不断变化；
- Put 跌入价内时，组合越来越接近持有 100 股的下跌风险；
- Short Put 可能被提前指派，并占用现金或保证金；
- 标的跌到零时，每组组合仍可能亏损约 \(100\times K_P\)，再加净 Debit。

因此，这不是“免费 Call”，而是用“愿意在 \(K_P\) 买入 100 股”的义务换取 Call。

![先按可承受下跌选择 Short Put，再决定 Call](<../assets/advanced/chapter-05-other-strategies/lesson-28/frame-02-0475s.jpg>)

**图怎么看：**

- 课程先把 Short Put 放在预计不会跌破的位置，再用其权利金购买 Call；
- “预计不会跌破”不是风险边界，坏消息可以造成连续跳空；
- Call Strike 能否碰到仍会显著影响到期收益；
- 选择前应先算 Put 被指派后是否真能买下 100 股，而不是先追求零成本。

### 建仓与退出

课程建议给反弹至少三个月，并在股价跌破 Put Strike 时认错，在到期不足一个月前处理。可以把它改写为更可执行的流程：

1. 先写清楚基本面或价格反转条件；
2. 按标的跌至零的压力情景确定合约数；
3. 检查两腿 Bid–Ask、Skew、除息和财报日期；
4. 用组合限价同时成交；
5. 预先指定价格失效、时间失效和波动率失效条件；
6. 平仓时同时处理两腿，避免留下意外 Naked Position。

“跌破 Put Strike 才止损”也不能保证只亏到某个金额：隔夜跳空可能直接越过止损位。

## 第 29 讲：用海鸥结构做短期对冲

对已有 100 股股票，课程使用：

- Long Stock；
- Long ATM Put，行权价 \(K_M\)；
- Short OTM Put，行权价 \(K_L<K_M\)；
- Short OTM Call，行权价 \(K_H>K_M\)。

其中 Long Put + Short Lower Put 是 Put Debit Spread；Short Call 再补贴其成本。它可以看作“有限区间保护的 Collar”。

### 保护到底覆盖哪里

假设股票现价 150，组合为：

- Long 150 Put；
- Short 140 Put；
- Short 160 Call。

忽略净权利金，到期效果为：

- \(140\le S_T\le150\)：股票从 150 到 140 的跌幅被 Put Spread 抵消；
- \(150<S_T<160\)：继续享受股票上涨；
- \(S_T\ge160\)：Short Call 把总价值封顶在 160 附近；
- \(S_T<140\)：Put Spread 已达到最大价值，股票损失重新按每跌 1 美元亏 1 美元扩大。

所以它只保护 150 到 140 这一段，不是给股票设定 140 的永久底价。

![QQQ 海鸥对冲的真实案例](<../assets/advanced/chapter-05-other-strategies/lesson-29/frame-01-0318s.jpg>)

**图怎么看：**

- Long 305 Put 与 Short 285 Put 只提供 20 美元/股的最大保护；
- Short 325 Call 用来降低成本，同时封顶 325 以上的上涨；
- QQQ 最终跌到 273 后，Put Spread 已赚满，但 285 以下仍由原持仓承担；
- 图中的 1,700 美元是对冲腿收益，不代表整个组合盈利。

课程用 QQQ 对冲一篮子股票，这属于 Cross Hedge。若持仓与 QQQ 的行业、Beta 或盘后走势不同，会出现 Basis Risk，不能简单按一比一张数配对。

### 短期与持续保护

课程强调海鸥更适合围绕短期事件、接近到期观察结果。原因是保护区间主要由到期 Payoff 决定。若需要持有过程中持续降低 Delta：

- Protective Put 的保护更直接；
- Collar 可把下方风险真正封住，但会封顶上涨；
- Put Spread Collar 成本低，却只保护有限区间；
- 直接减仓最简单，也没有 Greeks 和指派风险。

![课程对海鸥持仓调整的讨论](<../assets/advanced/chapter-05-other-strategies/lesson-29/frame-02-0602s.jpg>)

**图怎么看：**

- 股价涨过 Short Call 后，继续持有会锁住更多上涨；
- 股价靠近 Short Put 时，Put Spread 尚可能有大量时间价值，不能把到期最大收益当成当前可得收益；
- Roll Call 或 Put Spread 都是在关闭旧交易后重开新交易，旧盈亏不会消失；
- 若任何 Short Leg 留到期，应准备好被指派和 Pin Risk。

### 开仓前必须回答

- [ ] 对冲的是同一只股票，还是相关指数？若是后者，Beta 如何估计？
- [ ] 需要保护的具体价格区间是什么？
- [ ] 跌破下方 Put 后，剩余股票损失能否承受？
- [ ] 上涨超过 Short Call 后，是否愿意按 Strike 卖出股票？
- [ ] 净 Debit、最大区间保护和极端下跌损失分别是多少？
- [ ] 财报、除息、流动性和提前指派是否已检查？
- [ ] 到期前是主动平仓，还是有足够资金接受指派？

