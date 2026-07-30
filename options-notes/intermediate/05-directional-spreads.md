# 中级 05：Vertical Spreads

> 覆盖视频：中级第 29–33 讲  
> 本章时长：约 52 分钟

## 第 29 讲：为什么增加第二条腿

Vertical Spread（垂直价差）由：

- 同一标的；
- 同一到期日；
- 同为 Call 或同为 Put；
- 不同 Strike；
- 一买一卖

组成。

对 Long Option，加一条 Short Option 可以降低净成本，同时封顶一部分潜在收益；对 Short Option，加一条更远的 Long Option 可以限定尾部损失，同时减少收到的权利金。

![用第二条腿降低 Long Put 成本](<../assets/intermediate/chapter-05-directional-spreads/lesson-29/frame-01-0261s.jpg>)

**图怎么看：**

- 买 450 Put 后再卖 430 Put，表示只购买 450 到 430 区间的下跌收益；
- 跌破 430 后，两条 Put 的 Delta 逐渐抵消，收益封顶；
- 卖出第二条腿降低成本，同时放弃极端下跌继续获利；
- 下单时应按组合净价成交，避免先成交一腿产生裸露风险。

![用第二条腿限定 Short Call 风险](<../assets/intermediate/chapter-05-directional-spreads/lesson-29/frame-02-0462s.jpg>)

**图怎么看：**

- Short Call 收权利金，Long Higher-Strike Call 设定最大损失；
- 少收一部分净 Credit，换来 Defined Risk；
- 最大损失不是图上直观看到的 Strike 差，还要减去净 Credit；
- Long 保护腿不能随意单独卖掉，否则会重新变成 Naked Short Call。

## 第 30 讲：四种垂直价差

| 方向 | 结构 | 开仓现金流 |
|---|---|---|
| Bull Call Spread | Long 低 Strike Call + Short 高 Strike Call | 通常 Debit |
| Bull Put Spread | Short 高 Strike Put + Long 低 Strike Put | 通常 Credit |
| Bear Put Spread | Long 高 Strike Put + Short 低 Strike Put | 通常 Debit |
| Bear Call Spread | Short 低 Strike Call + Long 高 Strike Call | 通常 Credit |

![Bull Call 与 Bull Put 的相似到期收益](<../assets/intermediate/chapter-05-directional-spreads/lesson-30/frame-01-0234s.jpg>)

**图怎么看：**

- 两种 Bull Spread 都在两条 Strike 之间随股价上涨而获利；
- 低于下方 Strike 和高于上方 Strike 时，盈亏都封顶；
- 相同 Strikes 的 Call 与 Put 版本，到期 payoff 可通过平价关系对应；
- 但开仓现金流、提前指派、股息、保证金和税务并非完全相同。

![Call Spread 与 Put Spread 的选择](<../assets/intermediate/chapter-05-directional-spreads/lesson-30/frame-02-0420s.jpg>)

**图怎么看：**

- 先确定方向和愿意交易的价格区间，再选 Call 或 Put；
- 不能因为 Credit Spread “先收钱”就认为更划算；
- Debit 占用现金，Credit 会锁定相应风险额度；
- 应比较整组 Bid–Ask、流动性和提前指派风险。

## 第 31 讲：最大盈亏与盈亏平衡

设两 Strike 的宽度为：

\[
W=K_{\text{high}}-K_{\text{low}}
\]

### Debit Spread

净 Debit 为 \(d\)：

- 最大亏损：\(d\times100\)；
- 最大利润：\((W-d)\times100\)；
- Bull Call 盈亏平衡：\(K_{\text{low}}+d\)；
- Bear Put 盈亏平衡：\(K_{\text{high}}-d\)。

![Debit Spread 的三处关键点](<../assets/intermediate/chapter-05-directional-spreads/lesson-31/frame-01-0257s.jpg>)

**图怎么看：**

- 图例为 Bear Put Debit Spread；
- 高 Strike Put 是 Long Leg，低 Strike Put 是 Short Leg；
- 股价高于高 Strike 时亏掉全部 Debit；
- 股价低于低 Strike 时赚到宽度减 Debit。

### Credit Spread

净 Credit 为 \(c\)：

- 最大利润：\(c\times100\)；
- 最大亏损：\((W-c)\times100\)；
- Bull Put 盈亏平衡：Short Put Strike \(-c\)；
- Bear Call 盈亏平衡：Short Call Strike \(+c\)。

课程说相同宽度下“Credit 越多，成功概率越低；Debit 越少，成功概率越低”。这常与 Strike 离现价更近或更远相关，但不能只用 Credit/Debit 推出准确概率。券商显示的 Probability of Profit 也是基于模型和 IV 的估计。

![课程对 Debit 与 Credit 成功率的示意](<../assets/intermediate/chapter-05-directional-spreads/lesson-31/frame-02-0543s.jpg>)

**图怎么看：**

- 较高潜在回报通常对应更难达到的价格区间；
- 但概率、赔率和期望值是三个不同指标；
- 显示 52% 不代表 52% 会实现，也不包含滑点和提前退出；
- 最大亏损必须在下单前独立核算，不能只看平台绿色概率。

## 第 32 讲：怎么实际构建

课程案例一是 Bear Call Credit Spread：用 Long Higher-Strike Call 限定 Naked Short Call 的上行损失。

课程案例二是 Bull Call Debit Spread：用 Short Higher-Strike Call 降低 Long Call 在高 IV 环境中的成本。

![Bull Call Spread 的实例](<../assets/intermediate/chapter-05-directional-spreads/lesson-32/frame-01-0254s.jpg>)

**图怎么看：**

- Long 140 Call 提供主要看涨敞口；
- Short 155 Call 降低成本，同时把最大收益封在 155；
- 第二条腿也减少部分 Vega、Theta 和 Gamma，但抵消比例会动态变化；
- 开仓理由应是“愿意只赚到 155”，不是单纯觉得第二条腿有收入。

### Spread 宽度

![宽 Spread 与窄 Spread](<../assets/intermediate/chapter-05-directional-spreads/lesson-32/frame-02-0495s.jpg>)

**图怎么看：**

- Strikes 离得远：更像原来的单腿，成本/风险较大，潜在收益更高；
- Strikes 离得近：净成本/最大损失较小，盈利区间和最大收益也较小；
- 窄 Spread 的手续费和 Bid–Ask 占最大收益比例可能更高；
- 宽窄没有统一最优，要比较期望值和账户损失上限。

课程说 Spread 只适合短期投机、不适合系统交易，这是个人风格，不是产品性质。Vertical Spread 可用于短期、长期或系统化策略，关键是期限、定价和风险控制。

### 退出与到期

![到期前该不该处理 Spread](<../assets/intermediate/chapter-05-directional-spreads/lesson-32/frame-03-0707s.jpg>)

**图怎么看：**

- 标的在两 Strikes 之间时，一条腿可能 ITM、另一条 OTM，最容易产生非预期股票；
- 即使两腿都 ITM，也可能因行权截止、账户资金或提前指派产生暂时敞口；
- “赚到最大利润 80% 就走”是管理规则示例，不是最优定律；
- 最稳妥做法通常是按组合限价平仓，不依赖自动行权替你管理。

不要拆保护腿。若确实要拆，必须把剩余头寸当作全新 Naked/Long Option，重新核算保证金和最大亏损。

## 第 33 讲：用 Greeks 理解第二条腿

Vertical Spread 的 Greeks 是两腿之和。因为两腿同类型、方向相反，Delta、Gamma、Theta 和 Vega 会部分抵消。

![第二条腿抵消部分 Greeks](<../assets/intermediate/chapter-05-directional-spreads/lesson-33/frame-01-0280s.jpg>)

**图怎么看：**

- Strikes 越近，两腿敏感度通常越相似，净 Greeks 越小；
- Strikes 越远，保护腿影响越小，组合越像单腿；
- “只剩 Delta”是近似说法，时间和 IV 在持有过程中仍可能显著影响 Spread；
- 极窄 Spread 只需很少现金，但净 Delta 和最大利润也小，不能把低成本误认成高效率无风险杠杆。

## 下单前检查

- [ ] 两腿标的、类型和到期日是否完全一致？
- [ ] 方向和 Strike 顺序是否正确？
- [ ] 净 Debit/Credit 是否按整组限价？
- [ ] 最大利润、最大亏损和盈亏平衡是否手算一致？
- [ ] Short Leg 是否存在提前指派或除息风险？
- [ ] 到期股价落在两 Strike 之间时如何处理？
- [ ] 平仓是否按组合进行，避免留下裸腿？
