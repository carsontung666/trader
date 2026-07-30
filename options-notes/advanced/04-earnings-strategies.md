# 高级 04：财报事件交易与保护

> 覆盖视频：高级第 23–27 讲  
> 本章时长：约 46 分钟

财报交易同时包含跳空、IV Crush、流动性和执行风险。本章课程把它分为卖波动、赌方向和持股保护三类。最重要的修正是：高胜率不等于有正期望，Expected Move 也绝不是最大损失边界。

## 第 23 讲：卖财报波动率

财报前期权包含事件方差，公布后这部分不确定性消失，近月 IV 常快速下降。Short Straddle/Strangle 盈利的真实条件是：

\[
\text{实际跳空和之后波动} < \text{开仓权利金已经定价的波动}
\]

![课程对财报卖方 Edge 的解释](<../assets/advanced/chapter-04-earnings-strategies/lesson-23/frame-01-0289s.jpg>)

**图怎么看：**

- 买方为凸性和有限亏损付费，卖方承担尾部；
- 这可能形成风险溢价，不是每次财报都“错误定价”；
- 卖方收益有限，上方 Naked Call 损失理论无上限；
- 一次超预期跳空可能吃掉多次小利润。

### Expected Move

ATM Call + ATM Put 的总价格常被用作到期价格变动的近似尺度：

\[
\text{Expected Move heuristic}\approx
C_{\text{ATM}}+P_{\text{ATM}}
\]

但它不是严格的 68% 概率区间，也会受到利率、股息、Skew、期限和报价口径影响。

课程用一天约 20 家公司的样本得出“90% 实际波动低于预期”，样本太小，不能证明策略胜率或期望值。

![高盛财报 Short Straddle 案例](<../assets/advanced/chapter-04-earnings-strategies/lesson-23/frame-02-0599s.jpg>)

**图怎么看：**

- 财报前卖 380 Straddle 收约 1,110 美元；
- 次日用约 800 美元回购，个案盈利来自跳空较小和 IV Crush；
- 若股价跳空超过盈亏平衡，结果会反向；
- 单次成功案例没有展示最坏跳空、保证金和跨夜无法止损的问题。

## 第 24 讲：开仓、期限和退出

课程建议财报当天临近收盘开仓，以减少财报前其他行情暴露。这能缩短持有时间，但无法消除：

- 收盘前 Bid–Ask 扩大；
- 财报推迟或公布时间变化；
- 盘后跳空无法交易期权；
- 次日开盘熔断、停牌或报价失真。

### 标的选择

历史 Earnings Move 可以帮助建立情景，但过去没有爆雷不代表下一次安全。股价高低也不是风险本身；应按组合在不同百分比跳空下的美元损失和账户比例判断。

![按账户承受能力选择财报仓位](<../assets/advanced/chapter-04-earnings-strategies/lesson-24/frame-01-0305s.jpg>)

**图怎么看：**

- 100 美元股票并不自动只亏几百美元；
- Naked Call 在收购、药物数据或极端业绩下可能跳空数倍；
- 合约乘数是 100，五张合约会把风险放大五倍；
- 最安全的做法是先用 Long Wings 写死最大损失。

### Straddle 还是 Strangle

![Straddle 与 Strangle 的 Strike 选择](<../assets/advanced/chapter-04-earnings-strategies/lesson-24/frame-02-0589s.jpg>)

**图怎么看：**

- Straddle 收更多 Credit，盈亏平衡较近；
- Strangle Strikes 更远，Credit 更少，仍有上方无上限风险；
- 0.15 Delta 没有普遍“最优”证明；
- 用 Expected Move 选 Strike 只是市场基准，不是保险。

课程建议 Straddle 次日开盘即平、短期 Strangle 可等到到期。更稳妥的规则是：事件溢价释放后重新评估剩余收益/尾部风险，并避免依赖自动到期。

## 第 25 讲：把风险写成 Defined Risk

课程把“两倍 Expected Move 外的距离”当作最大亏损参考。这只能叫压力情景，不是最大亏损。实际跳空可超过 2 倍、3 倍甚至更多。

![AMD 两倍 Expected Move 情景](<../assets/advanced/chapter-04-earnings-strategies/lesson-25/frame-01-0203s.jpg>)

**图怎么看：**

- ATM Straddle 约 5 美元，只说明市场报价中的变动尺度；
- 50–70 是一个假设区间，不是价格边界；
- 55/65 Short Strangle 跳到 80、100 或更高时仍持续亏损；
- 已有 AMD 多头时，再卖 Put 会叠加下跌风险。

风险结构：

- 上方加 Long Call：把 Short Call 改成 Call Credit Spread；
- 下方加 Long Put：把 Short Put 改成 Put Credit Spread；
- 两侧都加 Wings：Iron Condor / Iron Butterfly。

“Jade Lizard”通常指 Short Put 加 Short Call Spread；要实现无上方亏损，净 Credit 需至少覆盖 Call Spread 宽度。不能只因加了一张 Call 就默认风险已完全处理。

## 第 26 讲：用 Vertical Spread 赌方向

若对财报方向有明确观点，课程建议：

- 看涨：Long ATM Call + Short Higher-Strike Call；
- 看跌：Long ATM Put + Short Lower-Strike Put；
- 使用覆盖财报的近期期限；
- 财报前临近收盘开仓。

![Long ATM + Short OTM 的方向价差](<../assets/advanced/chapter-04-earnings-strategies/lesson-26/frame-01-0257s.jpg>)

**图怎么看：**

- Short OTM Leg 降低财报前昂贵权利金；
- 同时封顶方向判断正确后的收益；
- Vertical Spread 的 Vega、Theta、Gamma 会部分抵消，不是完全消失；
- 最大亏损是净 Debit，最大利润是宽度减 Debit。

课程称到期越短越好、应尽量等到到期兑现。实际还要比较：

- 财报后已经达到最大利润的比例；
- 剩余几天的反转风险；
- 两腿 Bid–Ask；
- 标的落在两 Strikes 之间时的到期指派。

## 第 27 讲：财报前保护已有股票

课程推荐财报前卖 ATM Covered Call。它最多用权利金缓冲下跌，并不能限定股票崩盘损失。

![Airbnb 财报前 Covered Call](<../assets/advanced/chapter-04-earnings-strategies/lesson-27/frame-01-0236s.jpg>)

**图怎么看：**

- 收到 5.8 美元只提供 5.8 美元/股缓冲；
- 股票跌 13% 时仍会有显著净亏损；
- ATM Call 从现价开始封顶全部上涨；
- 这属于“弱保护 + 卖事件波动”，不是灾难保险。

如果真正目标是限定财报暴雷：

- Protective Put：明确底价，但财报前贵；
- Collar：卖 Call 补贴 Put，同时设上下边界；
- 减仓：没有 IV Crush，也没有指派复杂度；
- Put Spread Collar：降低成本，但只保护某一段。

![课程对财报期限的选择](<../assets/advanced/chapter-04-earnings-strategies/lesson-27/frame-02-0444s.jpg>)

**图怎么看：**

- 短期限把事件溢价集中，Gamma 也最集中；
- 财报后大跌不代表“短期不会反弹”，不能据此机械等到期；
- 股价上涨或横盘后尽快回购 Call，是恢复上涨敞口的一种选择；
- 所有处理都应基于原先保护目标，而不是结果出来后改故事。

## 财报前一页检查

- [ ] 是卖波动、赌方向，还是保护持股？
- [ ] 组合最大亏损能否写成确定数字？
- [ ] 上下跳空 10%、20%、50% 分别亏多少？
- [ ] 财报发布时间、到期日和除息日是否确认？
- [ ] 次日无法及时平仓能否承受？
- [ ] 是否使用组合限价和 Long Wings？
- [ ] 是否预先禁止“投机失败改长期投资”？
