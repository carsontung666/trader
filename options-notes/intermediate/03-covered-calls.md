# 中级 03：Covered Call 的四种用法

> 覆盖视频：中级第 14–20 讲  
> 本章时长：约 78 分钟

## 第 14 讲：卖方有没有天然优势

卖方收取权利金、买方支付权利金，这类似保险费与风险赔付。部分市场和时期存在波动率风险溢价：隐含波动率平均可能高于之后实现的波动率。但这不是每一张期权都让卖方占优。

![课程用 IV 与历史波动率验证卖方 Edge](<../assets/intermediate/chapter-03-covered-calls/lesson-14/frame-01-0301s.jpg>)

**图怎么看：**

- 比较应使用相同标的、相近期限与一致口径的 IV 和 Realized Volatility；
- OTM Put 的 IV 高于 ATM，可能来自波动率 Skew 和尾部保险需求，不能直接视为免费 Edge；
- 卖方的小额高频盈利可能被一次跳空、并购或暴涨亏损反转；
- Edge 若存在，也必须在交易成本、保证金、仓位限制和尾部损失后仍为正。

“卖期权胜率高”不是充分理由。先问亏损分布是否能承受，再谈胜率。

## 第 15 讲：Covered Call 基本结构

Covered Call = 100 股股票 + 1 张 Short Call。

假设股票成本 \(S_0=150\)，卖出 Strike \(K=160\) 的 Call，收到 \(c=3\)：

- 最大利润：\((160-150+3)\times100=1,300\) 美元；
- 盈亏平衡点：\(150-3=147\) 美元；
- 股价跌到零的最大损失：约 \(147\times100=14,700\) 美元；
- 到期高于 160 时，股票通常会被按 160 卖出。

![Covered Call 的最大收益与盈亏平衡点](<../assets/intermediate/chapter-03-covered-calls/lesson-15/frame-01-0321s.jpg>)

**图怎么看：**

- 权利金把盈亏平衡点向下移动 3 美元；
- 右侧收益封顶，不再参与 160 以上涨幅；
- 左侧仍近似股票下行，只减少 3 美元/股；
- 相对单纯持股，Short Call 没有新增无上限下跌，但显著改变了上涨收益和指派结果。

## 第 16 讲：用 Covered Call “收租”

“收租”是方便记忆的比喻，不应理解为固定收益。每轮权利金都来自承担：

- 股票下跌；
- 上涨被封顶；
- Short Gamma；
- IV 上升；
- 提前指派与操作失误。

![课程示例中的周期 Covered Call](<../assets/intermediate/chapter-03-covered-calls/lesson-16/frame-01-0305s.jpg>)

**图怎么看：**

- 图中每周卖 Call 的历史结果不能直接推导未来年化收益；
- 短期限 Theta 较集中，同时 Gamma、盯盘和滚仓频率也更高；
- “只选稳定股票”不能消除财报、新闻和跳空；
- 更重要的前提是：本来愿意持股，也愿意在 Strike 卖股。

课程回顾了麦当劳案例：Call 被股价突破后，以更高价格买回会形成 Short Call 亏损。这不是策略失败的异常情况，而是上涨封顶的正常成本。

![麦当劳 Covered Call 历史操作](<../assets/intermediate/chapter-03-covered-calls/lesson-16/frame-02-0615s.jpg>)

**图怎么看：**

- 图上标出的成功交易是个案，不构成可重复收益率；
- 若股票长期落后市场，权利金可能只是部分弥补持股机会成本；
- 回购 Call 保留股票，相当于主动放弃原来的封顶并确认期权损失；
- 再卖更远 Call 是一笔新交易，不会自动消除旧亏损。

### 期限与 Strike

- 周度：Theta 集中、调整频繁、Gamma 与 Pin Risk 更高；
- 月度：管理频率较低，但一次承诺上涨空间的时间更长；
- 近 Strike：权利金和初始对冲较多，上涨空间少；
- 远 OTM：保留上涨空间多，权利金和保护少。

固定卖 0.20 Delta 只能作为一致化规则，不能替代情景判断。

### 到期与滚仓

到期前有三类选择：

1. 接受指派，按 Strike 卖出股票；
2. 买回 Call，保留股票；
3. 买回原 Call，同时卖出更远到期或不同 Strike 的新 Call，即 Roll。

![正股与 Short Call 应作为整体决策](<../assets/intermediate/chapter-03-covered-calls/lesson-16/frame-03-0879s.jpg>)

**图怎么看：**

- 课程强调别为追回一笔 Call 亏损而牺牲更多股票上涨，这一点合理；
- Roll 应按净借记/贷记、新 Strike、新到期日和新增风险评估；
- “滚到不亏”为止属于心理记账，不改变市场价值；
- 原 Call 尚未平仓时再卖一张，可能暂时形成超额 Short Call，不能机械重叠。

若到期时股价接近 Strike，不要只等自动失效。收盘后价格变化仍可能影响行权，最终是否被指派具有不确定性。

## 第 17 讲：用 Covered Call 止盈

课程区分两种想法：

- **被动止盈**：尚未决定现在卖出，只在未来达到目标价时愿意卖；
- **主动止盈**：已经想卖，但希望在等待交割时多收外在价值。

### 被动止盈

把 OTM Call 的 Strike 设为愿意卖出的目标价。优点是计划明确；代价是在大涨穿越目标价后不再参与额外上涨。

![被动止盈的 Strike、期限与标的选择](<../assets/intermediate/chapter-03-covered-calls/lesson-17/frame-01-0301s.jpg>)

**图怎么看：**

- Strike 是愿意成交的卖出价，不是预测的最高价；
- 到期日是承诺有效期；
- 高波动股票虽然权利金高，也更容易迅速穿越 Strike；
- 课程建议“一月以上”是经验值，不是统一最优期限。

### 主动止盈

课程用 XOP 示例：股价约 98.5，卖出 95 Strike 的 ITM Call，希望到期被指派，并收取时间价值。

![用 ITM Covered Call 等待股票被卖出](<../assets/intermediate/chapter-03-covered-calls/lesson-17/frame-02-0596s.jpg>)

**图怎么看：**

- 只要到期股价高于 95，组合到期价值被锁在 Strike 加收到的权利金；
- 但如果股价跌破 95，股票不会被卖走，原本“现在卖出”可锁定的利润会回吐；
- 多出的时间价值就是继续承担这段下跌风险的补偿，并非无风险多赚；
- 如果确实必须立即退出，直接卖股更符合目标。

ITM Call 还可能因股息而提前被行权。税务、持有期和账户规则也可能使“等指派”与直接卖股结果不同。

## 第 18 讲：降低开仓成本

同时买入股票并卖 Call，净现金成本确实减少，但更准确的名称是“降低盈亏平衡点”，因为卖出的上涨权利具有价值。

![Covered Call 开仓的具体条件](<../assets/intermediate/chapter-03-covered-calls/lesson-18/frame-01-0326s.jpg>)

**图怎么看：**

- 课程设定为基本面可接受、短期仍可能承压；
- 高 IV 能提高权利金，也意味着市场定价了更大波动；
- “恐慌下跌后不会暴涨”并不可靠，反弹正是 Covered Call 的主要机会成本；
- 若不愿在 Strike 卖出，就不能把较低盈亏平衡点当作免费折扣。

开仓记录应写成：

\[
\text{Breakeven}=S_0-c
\]

\[
\text{Max Profit}=K-S_0+c
\]

不要不断用后续权利金改写“成本价”来掩盖股票真实买入价和每轮期权盈亏；税务与绩效记录应分开。

## 第 19 讲：把 Covered Call 当弱对冲

Short Call 的权利金只能提供固定缓冲。因此：

- Protective Put 在 Strike 以下继续增加保护；
- Covered Call 最多缓冲收到的权利金；
- 股价继续下跌后，Short Call Delta 向 0 靠近，动态对冲强度反而减弱。

![股价高位时用 Covered Call 弱对冲](<../assets/intermediate/chapter-03-covered-calls/lesson-19/frame-01-0331s.jpg>)

**图怎么看：**

- 6 美元权利金对应约 3.6% 的缓冲，不等于限制最大跌幅为 3.6%；
- 跌幅超过权利金后，组合继续近似持股亏损；
- 上涨时却从 Strike 开始封顶；
- 是否对冲不应只靠预测短期顶部，还应来自账户可接受回撤和明确风险预算。

![Covered Call 与 Protective Put 的保护取舍](<../assets/intermediate/chapter-03-covered-calls/lesson-19/frame-02-0616s.jpg>)

**图怎么看：**

- ATM Call 收到更多权利金、初始 Short Delta 更大，但上涨空间最少；
- OTM Call 保护较弱，保留更多上涨；
- Covered Call 不是灾难保险；
- 对无法承受的大跌，应减仓、买 Put 或使用定义风险结构，而不是只卖 Call。

课程主张对冲只能在预测会跌时临时使用，这是一种主动择时观点，不是普遍规则。长期、系统性对冲是否合理，取决于目标回撤、负债、杠杆和投资期限。

## 第 20 讲：Strike 的本质是组合 Delta

若 100 股按每股单位记 Delta = 1，卖出一张 Call：

\[
\Delta_{\text{CC}}=1-\Delta_{\text{Long Call}}
\]

例如：

- 卖 0.30 Delta OTM Call：组合 Delta 约 0.70；
- 卖 0.50 Delta ATM Call：组合 Delta 约 0.50；
- 卖 0.70 Delta ITM Call：组合 Delta 约 0.30。

![Strike 与 Covered Call 初始 Delta](<../assets/intermediate/chapter-03-covered-calls/lesson-20/frame-01-0244s.jpg>)

**图怎么看：**

- OTM Call 保留更多正 Delta，也就是更多上涨和下跌敞口；
- ITM Call 降低组合 Delta，提供更强初始缓冲，但收益更早封顶；
- 图中“对冲强度”只是局部 Delta，不等于最大亏损被限定；
- 课程画面里的“买 Call”是口误，Covered Call 这一腿是卖 Call。

Delta 会动态变化：

- 股价上涨：Call Delta 增大，组合 Delta 减小；
- 股价下跌：Call Delta 减小，组合 Delta 增大。

![持有过程中必须考虑 Delta 变化](<../assets/intermediate/chapter-03-covered-calls/lesson-20/frame-02-0487s.jpg>)

**图怎么看：**

- 股票下跌时，Short Call 提供的对冲会越来越少；
- 股票上涨时，组合越来越接近被封顶；
- 这是一种负 Gamma 结构；
- 不能只按开仓 Delta 计算整个持有期保护。

## 四种用途放在一起

| 用途 | 核心目标 | 主要代价 |
|---|---|---|
| 收权利金 | 在愿意持股时卖出部分上涨 | 跳涨机会成本、滚仓 |
| 被动止盈 | 到目标价自动卖股 | 超过目标价不再参与 |
| 主动止盈 | 等待被指派时收外在价值 | 等待期间仍会回吐 |
| 弱对冲/降盈亏平衡 | 用权利金缓冲小跌 | 大跌仍亏、上涨封顶 |

最终只问一个硬问题：**到期时股票高于 Strike，我是否愿意不找借口地交出 100 股？** 如果不愿意，这张 Call 就不该卖。
