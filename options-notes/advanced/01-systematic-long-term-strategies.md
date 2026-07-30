# 高级 01：系统化 Short Put 模型

> 覆盖视频：高级第 1–13 讲  
> 本章时长：约 115 分钟

本章试图用 2000–2020 年数据设计长期 SPY Short Put 策略。课程展示的数字适合帮助理解仓位、Strike 和 Roll 的关系，但模型存在明显的实盘外推限制，不能把“历史最优”直接当未来参数。

## 第 1 讲：长期策略的筛选

课程先比较 Long Call、Short Put、Bull Spread 和 Short Straddle，最后选择 Short Put 作为系统化看涨核心。

![课程回测的基础设定](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-01/frame-01-0298s.jpg>)

**图怎么看：**

- 标的是 SPY，使用 ATM 期权并定期换月；
- 忽略交易成本会系统性高估高频换仓结果；
- 用同样合约名义金额比较，不等于用相同 Delta、波动或尾部风险比较；
- 回测结论依赖期权价格数据质量，不能只看最终资金曲线。

![课程对“卖方 Edge”的解释](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-01/frame-02-0548s.jpg>)

**图怎么看：**

- 投资者愿意为凸性和灾难保险支付溢价，可能形成 Variance Risk Premium；
- 这不是做市商“错误定价”的直接证据；
- 卖方收益是承担负偏度、跳空、流动性和保证金风险的补偿；
- Edge 随标的、期限和市场制度变化，不保证长期固定为 2%–20%。

## 第 2 讲：为什么建模型

课程要测试四组变量：

1. 仓位 / 杠杆；
2. Short Put Strike；
3. Roll 方法；
4. 市场环境。

![课程模型的四组变量](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-02/frame-01-0165s.jpg>)

**图怎么看：**

- 收益、波动率、最大回撤和 Sharpe 是输出；
- 四组输入存在交互，不能逐项优化后假设组合仍最优；
- 参数越多，Data Snooping 风险越高；
- 应预先写规则，并保留完全未参与调参的 Out-of-Sample 区间。

## 第 3 讲：模型顶层设计

基础规则大致为：

- 初始资金 1,000 万美元；
- 现金按无风险资产处理；
- 每月卖出约一个月到期的 SPY ATM Put；
- 到期后平掉或换到新的 ATM Put；
- 按 `Strike × 100 × 合约数` 计算名义仓位。

![每月滚动 ATM Put 的基础规则](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-03/frame-01-0225s.jpg>)

**图怎么看：**

- 每次换到新 ATM，相当于重置约 0.5 的初始 Delta；
- 到期日和实际 DTE 需要明确，不能只写“每月底”；
- 现金担保 Put 的国债收益是总回报的重要组成；
- 实盘需区分现金担保、Reg T Margin 和 Portfolio Margin。

![课程模型采用的历史区间](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-03/frame-02-0470s.jpg>)

**图怎么看：**

- 2000–2020 同时包含科技泡沫、金融危机、长牛和疫情冲击；
- 但只有一条美国大盘历史路径；
- 在整段数据上挑最优参数，再用同一段数据报告表现，属于 In-Sample；
- 还应做滚动训练、留出测试、不同起点和其他指数验证。

### 最大的方法问题

课程用 BSM 理论价格而不是真实成交价格，并称其与真实价格“99% 吻合”。需要谨慎：

- 用市场 IV 代回 BSM 得到市场价格，接近本身具有循环性；
- 股票期权是美式，存在股息和提前行权；
- OTM Put Skew 不能用单一波动率处理；
- Bid–Ask、滑点、手续费、离散 Strike 和盘中执行都被省略。

这些问题足以改变相邻参数谁更好。

## 第 4 讲：Short Put 与持有 SPY

课程报告基础 Short Put 在样本期总收益约 174.3%，SPY 约 156.5%；Short Put 年化波动较低，最大回撤也较低。

![课程的收益与风险统计](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-04/frame-01-0211s.jpg>)

**图怎么看：**

- 课程表中的 Sharpe 使用平均收益、无风险利率和标准差；
- Sharpe 对负偏度和尾部损失不敏感，不能称为唯一最好指标；
- 最大回撤补充了路径风险，但历史最大值不是未来上限；
- 应同时看 Sortino、Expected Shortfall、最差月份、恢复时间和流动性压力。

![为什么基础 Short Put 波动更低](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-04/frame-02-0444s.jpg>)

**图怎么看：**

- ATM Short Put 初始 Delta 约 +0.5，而 100 股 Delta 为 +1；
- 同名义本金比较时，Short Put 起初方向暴露更低，波动更低并不意外；
- 下跌后 Delta 向 +1 增加，是负 Gamma；
- 更公平的比较要说明是相同名义、相同初始 Beta，还是相同目标波动。

## 第 5 讲：固定杠杆

课程按 `Put 名义接货金额 / 账户净值` 定义杠杆，并测试约 0.8–2.5 倍。

![不同固定杠杆的历史结果](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-05/frame-01-0312s.jpg>)

**图怎么看：**

- 杠杆提高会同时放大收益、回撤和保证金压力；
- 课程据历史回撤建议 1–1.8 倍，后来又偏好 1.5–2 倍，这不是安全认证；
- 2.5 倍在疫情冲击中几乎抹去长期累计收益；
- 超过 1 倍表示极端指派金额大于账户净值，无法把所有 Put 当 Cash-Secured。

历史最大回撤无法涵盖未来更大跳空、券商提保和成交冻结。实盘杠杆应由可承受的压力损失反推，不应由回测收益最大化反推。

## 第 6 讲：Dynamic Weighting

课程测试用 RSI、均线和 VIX 调仓，最后采用：

- VIX 高时减仓；
- VIX 低时加仓；
- 杠杆限制在预设上下界；
- 模型中每天调整合约数量。

![按 VIX 每日调整名义仓位](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-06/frame-01-0321s.jpg>)

**图怎么看：**

- 这是 Volatility Targeting 的一种简化形式；
- VIX 是未来 30 天 SPX 隐含波动指标，不是当前绝对风险；
- VIX 与股价常负相关但不是“严格反比”；
- VIX 飙升后减仓可能在下跌后卖出，能控波动但有 Whipsaw 和换仓成本。

课程以 `基础 VIX / 当前 VIX` 推导杠杆，并在样本内寻找基础值 25。

![基础 VIX 参数的课程选择](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-06/frame-02-0632s.jpg>)

**图怎么看：**

- 25 是这段历史上的调参结果，不是市场常数；
- VIX 制度、利率和期权供需变化后，阈值可能漂移；
- 实盘用整数合约会产生阶梯式仓位；
- 每日调整在小账户中会被手续费、税务和 Bid–Ask 放大。

## 第 7 讲：Roll 到新 ATM，还是 Hold the Strike

- **Constant Delta / New ATM**：每次换月都按新股价选 ATM；
- **Hold the Strike (HTS)**：保留旧 Strike，只延长到期日。

![HTS 与重置 ATM 的历史对比](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-07/frame-01-0350s.jpg>)

**图怎么看：**

- 股价下跌时，HTS 的 Put 变 ITM，正 Delta 上升，等于越跌越加风险；
- 股价上涨时，HTS 变 OTM，Delta 下降，等于越涨越减风险；
- 所以 HTS 在长牛里可能放大收益，在持续熊市里回撤极大；
- Roll 不是无损续期：旧腿盈亏、净 Credit 和新风险都要分别记录。

课程回测认为重置 ATM 的跨周期风险收益比更稳。该结论仍需用真实价格和样本外数据验证。

## 第 8 讲：0.30、0.50、0.70 Delta

课程比较 OTM、ATM 和 ITM Short Put，并报告样本期 OTM 的历史收益风险比最好。

![Strike 选择是风险收益配比](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-08/frame-01-0236s.jpg>)

**图怎么看：**

- OTM 初始 Delta 较低，更多月份可保留全部权利金；
- ITM 初始 Delta 高，更接近杠杆持股；
- OTM Put 的 Skew 可能带来较高 IV，但理论价格模型若没准确建 Skew，结论会偏；
- 课程样本前半段长期震荡，使 OTM 特别占优，存在 Regime Dependence。

“OTM 最优”不能脱离目标收益、真实报价和尾部风险单独使用。

## 第 9 讲：把所有参数放进一张表

课程同时比较仓位、动态调仓、Roll 和 Strike，最后在样本内偏好：

- VIX 上升时减仓；
- 约 1.5–2 倍名义杠杆；
- OTM Put；
- Roll 时重置 Delta。

![课程的参数热力图](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-09/frame-01-0283s.jpg>)

**图怎么看：**

- 最深颜色只代表这份回测表中的最好；
- 同一数据既选参数又评价，会产生 Multiple-Testing Bias；
- 最大回撤 44% 并不代表可接受，账户是否能在回撤中满足保证金更关键；
- 应先设风险上限，再从满足约束的候选里选，不应先追求总收益。

## 第 10 讲：牛熊分段

课程事后把 2000–2009 称为弱市、2009–2020 称为强市，并观察到：

- OTM 在弱市更好、强市容易踏空；
- ITM 在强市更好、弱市风险大；
- ATM 相对折中；
- HTS 强市收益高、弱市损失极大；
- VIX 上升减仓的规则跨两段较稳。

![不同行情下的 Strike 回测](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-10/frame-01-0253s.jpg>)

**图怎么看：**

- 这是用已经知道的历史终点划分 Regime；
- 实盘无法提前知道当前是长牛起点还是熊市中继；
- 如果市场状态信号也从同一数据调参，仍会过拟合；
- ATM 是折中，不代表任何未来区间最优。

![HTS 与 Constant-Delta 在牛熊中的差异](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-10/frame-02-0481s.jpg>)

**图怎么看：**

- HTS 的高收益来自更强、动态增加的方向敞口；
- 这不是独立 Alpha，部分是隐含杠杆；
- 课程也承认自己没能及时判断 2022 年环境转换；
- 因此不能把“确认是牛市再用 HTS”当成可执行系统规则。

## 第 11 讲：标的、期限和 Strike

课程实操建议：

- 先用 SPY 等流动性高的指数 ETF；
- 使用月度合约；
- 默认 ATM；
- 个股只用于非常熟悉且流动性高的公司。

![课程建议先用月度合约](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-11/frame-01-0288s.jpg>)

**图怎么看：**

- 月度合约通常较容易管理，Gamma 比极短期限分散；
- 周度/日度不是只在牛市才可用，它们只是风险更集中；
- 指数 ETF 能降低单公司归零风险，但不能消除市场崩盘；
- ATM 是课程最终折中，与前一讲 In-Sample OTM 最优并不相同。

## 第 12 讲：把模型变成实盘规则

课程建议每月第三个星期五附近 Roll，通常重置到 ATM；名义杠杆按 VIX 阶梯调整。

![杠杆与历史回撤矩阵](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-12/frame-01-0299s.jpg>)

**图怎么看：**

- 红色区域说明高杠杆在历史压力期接近或超过 100% 损失；
- 线性放大历史数据不能完整模拟强平、成交失败和波动率曲面；
- 杠杆下限设为 1 倍意味着风险极高时仍不进一步减仓；
- 更安全的规则应允许现金仓位，并按 Expected Shortfall 或压力损失限制。

![课程的 VIX 阶梯仓位例子](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-12/frame-02-0584s.jpg>)

**图怎么看：**

- 示例把 VIX 14、17、20、25 映射到不同 Put 数量；
- 合约整数化会让实际杠杆偏离目标；
- 跨阈值反复交易会产生 Turnover；
- 规则必须包含账户净值下降后的重新计算、保证金缓冲和暂停条件。

## 第 13 讲：真正可保留的结论

![长期复利更怕大回撤](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-13/frame-01-0253s.jpg>)

**图怎么看：**

- 亏 50% 需要涨 100% 才回本；
- 控制毁灭性回撤通常比追逐最高单年收益重要；
- 但低历史波动的 Short Put 仍可能有负偏度；
- 不能用 Sharpe 较高掩盖尾部义务。

![课程对仓位控制的总结](<../assets/advanced/chapter-01-systematic-long-term-strategies/lesson-13/frame-02-0516s.jpg>)

**图怎么看：**

- 风险高减仓、风险低加仓是可测试的框架；
- “风险低”不能只由低 VIX 定义，因为低波动可能伴随拥挤和高估值；
- 杠杆不会天然保持收益风险比，融资、非线性和强平会破坏线性；
- 纪律应包括停止条件和模型失效检查，而不只是机械执行。

## 如果要真正复现这套模型

至少补齐：

- 真实历史 Bid/Ask 或可执行 Mid 加滑点；
- 每个期限/Strike 的 IV Surface；
- 股息、利率、提前指派和现金利息；
- 手续费与合约整数；
- 账户保证金和强平规则；
- Walk-Forward 与 Out-of-Sample；
- 参数敏感性，而不是只报最佳点；
- 与 PUT、PUTW 等公开 Put-Write 基准及股票 Beta-Matched 组合比较。

在这些验证完成前，本章最可靠的收获是理解参数如何改变敞口，而不是照抄 1.5–2 倍杠杆或 VIX 25 阈值。
