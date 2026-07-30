# 中级 04：Short Put、指派与卖方风控

> 覆盖视频：中级第 21–28 讲  
> 本章时长：约 84 分钟

## 第 21 讲：Short Put 的基本结构

卖出 Put 后，卖方收到权利金，同时承担在被指派时按 Strike 买入 100 股的义务。

设 Strike 为 \(K\)，收到权利金 \(p\)，到期股价为 \(S_T\)：

\[
\text{P/L per share}=p-\max(K-S_T,0)
\]

- 最大利润：\(100p\)；
- 盈亏平衡点：\(K-p\)；
- 最大亏损：\(100(K-p)\)，发生于标的跌到零；
- 到期高于 \(K\)：保留全部权利金；
- 到期低于 \(K\)：通常被指派买入 100 股。

![Short Put 的到期收益图](<../assets/intermediate/chapter-04-short-put-strategies/lesson-21/frame-01-0244s.jpg>)

**图怎么看：**

- 右侧水平线表示利润最多只有权利金；
- 跌破 Strike 后盈亏线向左下延伸；
- 权利金只提供固定缓冲，不会限制大跌损失；
- 一张 420 Put 收 9.45 美元的法定最大亏损仍是 41,055 美元。

![Short Put 最大亏损的课程示例](<../assets/intermediate/chapter-04-short-put-strategies/lesson-21/frame-02-0440s.jpg>)

**图怎么看：**

- “SPY 不可能在短期跌到零”可以用于设计压力情景，不能用于删除最大亏损；
- 压力测试至少应包含历史崩盘、单股跳空和 IV 飙升；
- Delta 只能粗略作概率参考，不能保证成功率；
- Put Delta 若为 -0.37，Short Put Delta 约 +0.37，不是 3.7% 风险。

## 第 22 讲：Short Put 的应用逻辑

课程把它用于长期看涨、持续收权利金和“下跌时滚仓”。更严格的前提是：

- 愿意按 Strike 买入 100 股；
- 账户已为指派准备现金或明确融资额度；
- 即使公司永久下跌，也能承担损失；
- 权利金相对承担的尾部风险足够；
- 不依赖“股票总会涨回来”。

![课程总结的 Short Put 逻辑](<../assets/intermediate/chapter-04-short-put-strategies/lesson-22/frame-01-0299s.jpg>)

**图怎么看：**

- 看涨、收权利金和滚仓是三种描述，不是三层保险；
- Roll 会平掉旧合约并开新合约，旧亏损已经实现；
- 新收到更多权利金通常意味着延长风险时间或改变 Strike；
- 现金流为正不等于总盈亏为正。

### 到期日

![期限选择的取舍](<../assets/intermediate/chapter-04-short-put-strategies/lesson-22/frame-02-0600s.jpg>)

**图怎么看：**

- 短期限 Theta 集中，但 Gamma、到期管理和滑点更集中；
- 长期限一次收取权利金更多，但资金承诺更久、Vega 更大；
- 课程偏好月度是管理习惯，不是数学最优；
- 期限应与观点持续时间和可接受指派时间匹配。

### Strike

![不同市场观点对应不同 Strike](<../assets/intermediate/chapter-04-short-put-strategies/lesson-22/frame-03-0838s.jpg>)

**图怎么看：**

- OTM Put：较低 Delta、较少权利金和较低接货价；
- ATM Put：Theta 常较高，同时到期 Gamma 风险也高；
- ITM Put：更强正 Delta、更多权利金，但被指派概率和下跌敞口更高；
- 固定卖 0.30 Delta 只能统一流程，不能证明风险收益最优。

## 第 23 讲：苹果案例说明了什么

课程展示两个时点：

1. 大跌、IV 上升时，卖较长期、接近 ATM 的 Put，意图同时获取反弹、Theta 和 IV 回落；
2. 平稳回调时，选择不同期限和 OTM Strike。

![大跌环境中的 Short Put 案例](<../assets/intermediate/chapter-04-short-put-strategies/lesson-23/frame-01-0245s.jpg>)

**图怎么看：**

- 股价下跌和 IV 上升使 Put 权利金变高；
- 高权利金不是便宜，恰恰说明市场定价了更大下行；
- Short Put 在反弹、IV 回落和时间经过时三项可能同时有利；
- 若继续跳空下跌，Delta、Vega 和保证金也会同时恶化。

![平稳环境下选择期限和 Strike](<../assets/intermediate/chapter-04-short-put-strategies/lesson-23/frame-02-0467s.jpg>)

**图怎么看：**

- 先写清楚是想接货，还是只想赚权利金；
- 想接货时，Strike 应以愿意支付的有效买入价为核心；
- 不想接货却靠不断 Roll 规避指派，会把短期交易变成长时间风险承诺；
- 单一历史案例的收益不能证明长期策略收益。

## 第 24 讲：三种后续状态

### 股价下跌

选择：

- 接受指派，转为持有 100 股；
- 买回平仓，确认亏损；
- Roll Out 或 Roll Down-and-Out，延长时间或降低 Strike；
- 把裸 Put 改成 Defined-Risk Spread。

![指派后转 Covered Call 的 Wheel 思路](<../assets/intermediate/chapter-04-short-put-strategies/lesson-24/frame-01-0256s.jpg>)

**图怎么看：**

- 接货后卖 Call 是新的 Covered Call，不会抹去 Short Put 亏损；
- 新 Call 的 Strike 若低于股票有效成本，可能在反弹时锁定总亏损；
- Wheel 只是 Put 与 Covered Call 循环，不是稳赚机制；
- 公司基本面若变坏，继续卖期权可能只是延迟止损。

![下跌后的三种判断](<../assets/intermediate/chapter-04-short-put-strategies/lesson-24/frame-02-0516s.jpg>)

**图怎么看：**

- 继续持有、Roll 或退出都必须重新写投资论点；
- “股价一定回来”不能成为 Roll 的依据；
- Roll 的净 Credit 应拆成旧腿已实现亏损和新腿未来权利金；
- 调整不能突破原先账户最大风险预算。

### 股价上涨

可以持有到期，也可以在剩余权利金很少时提前回购，释放风险额度。提前平仓是否合理，应比较：

\[
\frac{\text{剩余可赚权利金}}{\text{仍承担的压力损失与占用时间}}
\]

而不是只看“已经赚了 90%”。

### 接近 Strike

短期 ATM 同时有高 Theta 和高 Gamma。提前 Roll 可以降低临近到期不确定性，但会放弃剩余 Theta 并建立新仓。

![接近到期时的处理原则](<../assets/intermediate/chapter-04-short-put-strategies/lesson-24/frame-03-0727s.jpg>)

**图怎么看：**

- 若明确愿意接货，可以接受指派；
- 若不愿接货，应在流动性尚可时主动处理；
- 不要等到最后几分钟才处理，Bid–Ask 和 Pin Risk 可能恶化；
- 所有调整都要先假设原仓已经独立结束，再判断新仓是否值得开。

## 第 25 讲：提前指派

美式 Put 可能在到期前被行权。Deep ITM、剩余外在价值很少、利率和借券等因素都可能提高提前行权动机。它不只发生在最后两三天，也没有课程所说的固定概率。

![提前指派后的经济处理](<../assets/intermediate/chapter-04-short-put-strategies/lesson-25/frame-01-0214s.jpg>)

**图怎么看：**

- Short Put 被指派后，账户得到 100 股并支付 \(100K\)；
- 立即卖股可恢复现金，但会有隔夜波动、滑点和税务结果；
- 再卖一张 Put 是一笔新交易，不是让指派“像没发生过”；
- 先检查账户是否能承受股票购买金额，不能把处理建立在事后融资上。

从经济敞口看，Deep ITM Short Put 本来已接近 +100 Delta；指派把模型敞口变成真实股票和现金支付。关键不是恐慌，而是及时核对数量、现金、股息和下一步风险。

## 第 26 讲：Strike 的本质是 Delta 与接货价

Short Put Delta 为正：

- 更高 Strike / 更 ITM：Delta 更高，更像持股；
- 更低 Strike / 更 OTM：Delta 更低，但仍保留尾部跳空；
- 股价下跌时 Put Delta 绝对值增大，Short Put 正 Delta 增大；
- 股价上涨时 Delta 减小，方向收益逐渐封顶。

![Short Put 的动态 Delta](<../assets/intermediate/chapter-04-short-put-strategies/lesson-26/frame-01-0326s.jpg>)

**图怎么看：**

- 下跌时仓位会“自动加大”正 Delta，这是负 Gamma；
- 上涨时仓位会“自动减小”正 Delta；
- Roll Up 是重新增加 Delta，不是追回踏空的免费操作；
- Strike 同时决定有效接货价 \(K-p\)，不能只看 Delta。

Cash-Secured Put 与同 Strike、同期限 Covered Call 的到期 payoff 等价，但股息、提前指派、税务和资金占用可能不同。

## 第 27 讲：Naked Short Call

裸卖 Call：

- 最大利润为权利金；
- 股价上涨时理论亏损无上限；
- Short Delta、Short Gamma、Short Vega；
- 保证金可能随股价和 IV 快速增加。

![Short Put 与 Naked Short Call 风险对比](<../assets/intermediate/chapter-04-short-put-strategies/lesson-27/frame-01-0342s.jpg>)

**图怎么看：**

- Short Put 的下界是标的跌到零，Short Call 没有对应价格上界；
- 不能因此认为 Short Put 风险小：单股归零仍可造成接近全额 Strike 损失；
- Covered Call 的 Call 有 100 股覆盖，裸 Call 没有；
- 新手应优先使用 Call Credit Spread 等定义风险结构，而不是依赖止损填补跳空。

## 第 28 讲：保证金与账户级风险

课程用“约 Strike × 100 × 20%”估算保证金。它不是通用规则。实际要求取决于券商、Reg T/Portfolio Margin、标的、OTM 金额、集中度、IV 和 House Rules。

![保证金会随不利行情增加](<../assets/intermediate/chapter-04-short-put-strategies/lesson-28/frame-01-0268s.jpg>)

**图怎么看：**

- 开仓显示的保证金不是最大亏损；
- 不利行情中，期权浮亏和保证金要求可能同时上升；
- 券商可随时提高 House Margin；
- 风控必须按压力情景估算，而不是把开仓保证金用满。

课程还给出 `(股票市值 + 期权最大亏损) / NLV` 的“杠杆率”。这不是行业统一指标，而且会把方向相反或组合限定风险的头寸粗暴相加。

![课程的账户杠杆计算示意](<../assets/intermediate/chapter-04-short-put-strategies/lesson-28/frame-02-0548s.jpg>)

**图怎么看：**

- NLV 是账户净清算价值，不等于可随意承受损失的现金；
- Covered Call 最大亏损不是“当前股票市值”，而是股票成本减收到的权利金，极端下限接近标的归零；
- Naked Put 可同时记录 `Strike × 100` 指派名义金额和 `Strike × 100 - premium` 最大亏损；
- 账户还要做相关性、跳空、IV 上升和保证金倍增的联合压力测试。

## 卖 Put 的最小安全版本

初学阶段优先按 Cash-Secured Put 管理：

- 每张预留 \(K\times100\) 现金；
- 只卖愿意实际持有的 100 股；
- 单股归零仍不破坏账户；
- 到期前写清接货、平仓和 Roll 条件；
- Roll 后不隐藏旧亏损；
- 不把收到的权利金当作可立即消费的收益。
