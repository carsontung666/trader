# 高级 06：期权异动与 Options Flow

> 覆盖视频：高级第 30–31 讲  
> 本章时长：约 19 分钟

期权大单可以提示“有人在承担某种风险”，却不能仅凭成交量推出买卖方向、完整组合，更不能证明内幕交易。本章应当作为异常活动的调查框架，而不是跟单信号。

## 第 30 讲：如何理解期权异动

课程用突发的大额 OTM Call 和随后出现的利好作为案例，说明异动可能早于新闻。

![LVS OTM Call 大单与随后股价上涨的案例](<../assets/advanced/chapter-06-unusual-options-activity/lesson-30/frame-01-0254s.jpg>)

**图怎么看：**

- 图中先出现 Call 大单，三天后出现政策消息并伴随上涨；
- 时间先后只说明相关性，不能证明交易者掌握了内幕；
- 大单也可能属于对冲、价差、股票替代、做市库存或平仓；
- 只展示命中的案例会产生幸存者偏差，还需统计所有未命中异动。

把一笔异动升级为“值得研究”，至少要补齐：

1. 标的当日新闻、财报、产品审批、投资者日和宏观事件；
2. Expiry、Strike、Moneyness、成交量与报价质量；
3. 成交发生在 Bid、Ask 还是中间价附近；
4. 是否与其他期权腿或股票同时成交；
5. 次日 Open Interest 是否变化；
6. 同期限 Skew 与整条 IV 曲面是否同步变化；
7. 若跟进，最大亏损和失效时间是什么。

### 合规边界

根据公开市场数据观察成交并研究其含义，与持有重大非公开信息交易是两回事。若自己获得了可能属于 Material Nonpublic Information 的内容，不应交易、提示他人交易或把它当成“信息优势”；应停止操作并咨询合规或律师。

课程中的历史故事和个案不能当作对具体交易者违法行为的认定。是否构成 Insider Trading 需要证据和监管、司法程序，而不是从期权图表推断。

## 第 31 讲：四类过滤条件

课程提出四项筛选：

1. Relative Volume 与 Open Interest 上升；
2. Delta 约 0.2–0.4；
3. IV 上升；
4. Option Flow 与推测方向一致。

这些指标可用于缩小研究范围，但每一项都有数据限制。

### 1. Volume 与 Open Interest

Volume 是当天成交合约数；Open Interest 是尚未结束的合约数。二者不是同一口径：

- 大多数数据源在交易日结束后才更新 Open Interest；
- 当天 Volume 大于昨日 Open Interest，不等于全部是新开仓；
- 一买一卖才形成成交，屏幕上的“买单”通常只是根据成交价相对 Bid/Ask 的分类；
- 若同一合约同时有开仓与平仓，次日 OI 只显示净变化。

所以应把“当日异常 Volume”与“次日 OI 验证”分成两个步骤，不能在盘中声称两者已经同步上升。

### 2. Delta 区间

0.2–0.4 Delta 的 OTM Options 兼具杠杆和一定触达概率，但该区间不是内幕交易者的统计定律：

- Delta 不是精确的到期价内概率；
- 深度 OTM 合约便宜，也更可能全部归零；
- ITM Call 可能用于替代股票，低 Delta Put 可能是灾难保险；
- 最合适的 Strike 取决于事件幅度、期限和 IV，而非固定阈值。

### 3. IV 与 Skew

![用 Volatility Skew 观察需求集中在哪一侧](<../assets/advanced/chapter-06-unusual-options-activity/lesson-31/frame-01-0314s.jpg>)

**图怎么看：**

- 高 Strike Call 的 IV 相对抬升，说明该区域报价变贵；
- 可能原因包括方向性买盘、事件预期、做市调整或低流动性；
- 应比较相同 Expiry、相近 Delta，并检查整条曲面，不能混用期限；
- IV 抬升说明期权价格变贵，不自动说明之后股价会按该方向运动。

### 4. Option Flow 方向

Flow 平台通常用成交价靠近 Ask/Bid 来推测主动买/卖，再汇总成 Bullish/Bearish。常见误判包括：

- 一张 Call 是多腿 Spread 的 Short Leg；
- 买 Call 同时卖股票，整体可能只是 Delta-Neutral；
- 卖 Put 可能是看涨，也可能是关闭原有 Long Put；
- 大宗交易通过中间价成交，方向无法可靠分类；
- 多个系统重复上报同一复杂订单。

因此，Flow 方向最多是概率性标签。没有完整订单上下文时，不应把 Call 等同于看涨、Put 等同于看跌。

![IMAX 大单案例中的成交、Delta 与 OI](<../assets/advanced/chapter-06-unusual-options-activity/lesson-31/frame-02-0596s.jpg>)

**图怎么看：**

- 图中大额 Call、约 0.3 Delta 与后续 OI 增长符合课程筛选条件；
- OI 增加支持“有新仓进入”，仍无法知道所有持仓的净方向；
- 平时成交稀少会让相对倍数特别醒目，也意味着退出滑点更大；
- 后续上涨是一个成功案例，不能据此计算该方法的长期胜率。

## 更可靠的研究记录

对每个异动建立一行记录：

| 字段 | 要记录什么 |
|---|---|
| 发现时间 | 精确到分钟，避免事后挑图 |
| 合约 | Ticker、Expiry、Strike、Call/Put |
| 市场状态 | Spot、Bid、Ask、IV、Delta、成交量 |
| 交易上下文 | 单腿/价差/股票组合、成交方向可信度 |
| 已知事件 | 财报、监管决定、宏观数据、除息 |
| 次日验证 | OI 变化、新闻是否出现 |
| 交易规则 | 入场价、最大亏损、截止时间、退出条件 |
| 最终结果 | 包括未命中与无法成交的样本 |

只有保留全部信号，才能计算：

\[
\text{Expectancy}
=P(\text{win})\times \overline{\text{win}}
-P(\text{loss})\times \overline{\text{loss}}
-\text{costs}
\]

异动跟单更适合使用 Long Option 或 Defined-Risk Spread，把最大亏损限制在净 Debit。不能因为“大单看起来确定”就放大仓位，更不能用 Naked Short Option 跟随一个尚未确认的方向。

