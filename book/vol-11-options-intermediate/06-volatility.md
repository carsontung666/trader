# 11.6 波动率策略

> 一句话：Long Volatility 要买到的实现波动超过已付权利金；Short Volatility 要卖出的实现波动小于已收权利金。两者都不是「IV 会跌所以必赚」。

![Long Straddle 中间亏权利金；Short Straddle 中间赚权利金](../assets/straddle.svg)

## 11.6.1 Short Straddle 与 Short Strangle

### Short Straddle

同一 Strike、同一到期日：

- Short ATM Call；
- Short ATM Put。

若共同 Strike 为 \(K\)，总 Credit 为 \(c\)，乘数 \(m\)：

- 最大利润：\(m\,c\)，到期股价恰好为 \(K\)；
- 下方盈亏平衡：\(K-c\)；
- 上方盈亏平衡：\(K+c\)；
- 上涨亏损理论无上限；
- 下跌亏损很大但有限，标的最低为零。

两张期权的总权利金共同形成上下缓冲。股价偏离 Strike 越远，利润越少。到期停在 Strike 才达到最大利润，属于非常窄的结果。课程称「两侧损失都无限」不准确：下方最大损失有限，上方才理论无上限。

到期每股：

\[
c-|S_T-K|
\]

### Short Strangle

同一到期日：

- Short OTM Put \(K_P\)；
- Short OTM Call \(K_C\)，且 \(K_P<K_C\)。

总 Credit 为 \(c\)：

- 最大利润区间：\(K_P\) 到 \(K_C\)；
- 下方盈亏平衡：\(K_P-c\)；
- 上方盈亏平衡：\(K_C+c\)。

两 Strikes 之间两腿都到期 OTM，可保留全部 Credit。Strikes 更远通常提高到期获利区间，但收到的 Credit 更少。更高胜率不等于更高期望值。OTM 尾部可能因 Skew 看起来昂贵，但跳空损失仍可能远超多次权利金。

Straddle 收得更多、中心利润更高，但盈亏平衡更近。Strangle 收得更少、容许区间更宽。两者都是 Short Gamma、Short Vega、通常正 Theta。行情移动后会产生明显 Delta，不是持有期间始终「无方向」。

Iron Condor 不是「两个胜率相加」，而是需要标的到期留在中间区间。四腿结构有更多 Bid–Ask、费用和指派管理。

## 11.6.2 IV Crush 交易

财报前，近月期权可能含有事件溢价；公布后，事件不确定性消失，IV 常明显下降。卖 Straddle / Strangle 的交易观点实际是：

\[
\text{之后实现的价格变动和波动} < \text{开仓价格所隐含的变动}
\]

并不是只判断「IV 会跌」。股价跳空可能轻易超过收到的 Credit。

高 IV、预期回落只是开仓条件之一。「方向中性」只表示初始 Delta 可能接近零。Short Gamma 会让上涨后变成负 Delta、下跌后变成正 Delta。使用保证金最少不应成为选裸卖结构的理由。

### 标的与期限

不熟悉的股票更难判断跳空分布和处理方式。低波动标的不一定没有溢价，高波动标的也不一定更值得卖。比较的是 Implied Move 与自己对 Realized Move 的估计。单股财报具有不可分散跳空，仓位必须远小于日常方向交易。

短期限事件期权的事件方差更集中，财报后 IV Crush 更直观；但短期限也有更高 Gamma。课程说「短期期权对 IV 更敏感」不严谨：绝对 Vega 通常是长期期权更高。

### Expected Move

ATM Straddle 的总价格可作为市场定价变动幅度的快速参考：

\[
\text{Expected Move heuristic}\approx
C_{\text{ATM}}+P_{\text{ATM}}
\]

它不是准确概率边界，也不是严格的 68% 区间。要同时看：到期时间是否刚好覆盖事件、Bid–Ask、股息和利率、波动率 Skew。过去事件跳空只是样本，不是上限。

### 退出

开仓目标若是 IV Crush，事件结束后应重新评估，不应无条件持有到期。Roll 会把一次事件交易变成更长的 Short Volatility 风险。止损单无法保证跨夜跳空成交价。最有效的风险控制是在开仓时限定最大亏损和缩小仓位。

课程建议 Straddle 次日开盘即平、短期 Strangle 可等到到期。更稳妥的规则是：事件溢价释放后重新评估剩余收益 / 尾部风险，并避免依赖自动到期。

## 11.6.3 把裸卖风险改成定义风险

![Iron Condor 把 Short Strangle 的尾部截断](../assets/iron-condor.svg)

### Iron Butterfly

以 Short Straddle 为核心，在两侧买入更远 OTM Put 和 Call。最大利润下降，但上下最大损失由 Wings 限定。

### Iron Condor

以 Short Strangle 为核心，在两侧买入更远 OTM Put 和 Call。它等于一组 Put Credit Spread 加一组 Call Credit Spread。

设两侧宽度相同为 \(W\)，净 Credit 为 \(c\)：

- 最大利润：\(m\,c\)；
- 最大亏损：\(m(W-c)\)。

两侧宽度不同时，最大亏损取较宽一侧的 \(W-c\)（再乘乘数），不要只写总 Credit。

Long Wings 把尾部损失截断。Wings 越近，最大损失越小，但 Credit 和盈利区间也改变。四腿结构可以 Roll，并非「不能」，只是成交成本和决策复杂度更高。Defined Risk 仍可能亏到最大值，到期还存在 Pin / Assignment Risk。

课程的另一种方法是给 Short Straddle / Strangle 加相应股数，形成 Covered Straddle / Strangle。它只覆盖 Short Call 的交付，并没有限制整体下跌：

- 股票下跌会亏；
- Short Put 同时会亏并可能再接相应股数；
- 极端下跌时，下行敞口可能接近普通持股的两倍。

因此它不是普通意义的「降总风险」，而是把上行裸 Call 风险转换成更强的下行多头风险。

「Jade Lizard」通常指 Short Put 加 Short Call Spread；要实现无上方亏损，净 Credit 需至少覆盖 Call Spread 宽度。不能只因加了一张 Call 就默认风险已完全处理。

## 11.6.4 Long Straddle 与 Long Strangle

### Long Straddle

Long ATM Call + Long ATM Put，同 Strike、同到期。总 Debit 为 \(d\)：

- 最大亏损：\(m\,d\)，到期停在 Strike；
- 下方盈亏平衡：\(K-d\)；
- 上方盈亏平衡：\(K+d\)；
- 上涨利润理论无上限；
- 下跌利润在标的跌到零时达到上限。

### Long Strangle

Long OTM Put \(K_P\) + Long OTM Call \(K_C\)：

- 最大亏损：总 Debit，发生在 \(K_P\) 到 \(K_C\) 之间；
- 下方盈亏平衡：\(K_P-d\)；
- 上方盈亏平衡：\(K_C+d\)。

两侧超过盈亏平衡后才开始净盈利。Strangle 初始成本较低，但需要更大价格移动。Long Straddle / Strangle 都是 Long Gamma、Long Vega、通常负 Theta。「一定有一腿归零」不妨碍组合盈利，判断应看总净值。

Long Volatility 要赚钱，需要实现变动或 IV 上升足以超过已支付的权利金和时间损耗。已知事件前买入往往很贵，事件后即使大幅波动也可能不及市场原先定价。

日内持有减少隔夜时间暴露，但 Bid–Ask 和两腿手续费占比更高。开盘波动大并不保证超过 Straddle 成本。交易必须在开仓前写出需要移动到哪两个价格才盈利。个案低损耗不能推广为 Long Straddle 的稳定优势。

## 11.6.5 事件交易检查

- [ ] 期权到期日是否覆盖事件？
- [ ] ATM Straddle 定价了多大的上下移动？
- [ ] 过去同类事件的跳空分布如何？
- [ ] 若跳空两倍于 Expected Move，最大损失是多少？
- [ ] 是裸卖还是 Iron Condor / Butterfly？
- [ ] 四腿能否按组合净价成交？
- [ ] 事件公布后何时退出？
- [ ] 是否把 IV Crush 错当成必赚条件？
- [ ] Covered Straddle 是否被误写成「降总风险」？

财报的开仓时点、样本偏差和持股保护，放到第 12 卷第 04 章。

## 11.6.6 用数字把四张图钉死

现价 100，乘数 100，忽略费用。

**Short Straddle：** 卖 100 Call 收 3.10，卖 100 Put 收 3.00，总 \(c=6.10\)。

```text
最大利润 = 610，仅当到期恰好 100
下方平衡 = 93.90
上方平衡 = 106.10
跌到 0 ≈ 亏 (100 − 6.10) × 100 = 9,390
涨到 130 = 亏 (30 − 6.10) × 100 = 2,390，且仍可继续扩大
```

**Short Strangle：** 卖 95 Put 收 1.40，卖 105 Call 收 1.50，总 \(c=2.90\)。

```text
最大利润区间 = 95 到 105
下方平衡 = 92.10
上方平衡 = 107.90
```

区间更宽、Credit 更少。跳到 80 或 130 时，亏损仍远大于 290。

**Iron Condor：** 在上面再买 90 Put 付 0.60、买 110 Call 付 0.70，净 \(c=1.60\)，两侧宽度 \(W=5\)。

```text
最大利润 = 160
最大亏损 = (5 − 1.60) × 100 = 340
```

尾部被截断。340 仍可能亏满。四腿点差和到期 Pin 还在。

**Long Straddle：** 买回同一组 ATM，总 Debit 6.10。最大亏损 610，平衡仍是 93.90 / 106.10。财报前若 Implied Move 已经是 6 美元，你需要实现波动超过这个数（还要覆盖 Theta 和点差）才净赚。方向对但只动 3 美元，到期仍亏。

## 11.6.7 Covered Straddle 为什么不是「降风险」

100 股 + Short ATM Straddle：Short Call 被股票覆盖，Short Put 没有。下跌时股票亏、Put 也亏，极端情况下下行接近两倍持股。它只是把 Naked Call 的上侧换成更重的下侧。不要写进「保险」栏。

Jade Lizard（Short Put + Short Call Spread）要让净 Credit ≥ Call Spread 宽度，上侧到期才不会亏。少一分钱就仍有缺口。加一张 Call 本身不等于风险处理完毕。

