# 中级 01：Option Greeks

> 覆盖视频：中级第 1–8 讲  
> 本章时长：约 52 分钟

Greeks 是期权价格在“当前这一点”对不同输入的局部敏感度。它们是估算工具，不是保证：标的、时间和 IV 同时变化时，不能只拿一个 Greek 直接预测最终盈亏。

## 第 1 讲：Greeks 在量化什么

课程把影响期权价格的主要维度分为：

- 标的价格：Delta、Gamma；
- 时间：Theta；
- 隐含波动率：Vega；
- 利率：Rho，本课程未重点展开。

![Greeks 与期权定价输入](<../assets/intermediate/chapter-01-option-greeks/lesson-01/frame-01-0141s.jpg>)

**图怎么看：**

- 表中箭头表示其他条件不变时的大致方向；
- Delta、Gamma、Theta、Vega 都会随市场状态变化，不是固定常数；
- 实际盈亏还包括合约数量、100 股乘数、买卖价差和成交价格；
- Greeks 来自模型，不同平台的模型、利率和股息输入可能略有差异。

## 第 2 讲：Delta

Delta 是期权价格对标的价格的一阶敏感度：

\[
\Delta=\frac{\partial V}{\partial S}
\]

若一张 Long Call 的 Delta 为 0.43，标的瞬间上涨 1 美元，其他条件近似不变时，期权理论价格约上涨 0.43 美元/股，即一张标准合约约 43 美元。

符号：

- Long Call：通常 \(0\) 到 \(1\)；
- Long Put：通常 \(-1\) 到 \(0\)；
- Short Option：对应 Long Option 的相反数；
- 100 股股票：Delta = \(100\)，若用“每股单位”则为 \(1\)。

![期权链中的 Delta](<../assets/intermediate/chapter-01-option-greeks/lesson-02/frame-01-0221s.jpg>)

**图怎么看：**

- Call Delta 为正，Put Delta 为负，反映标的上涨时两者理论价格的相反方向；
- 图中每股价格变化要乘合约乘数，才是账户的美元 Delta；
- 课程口误把卖出 0.43 Delta Call 说成 \(-0.33\)，正确应约为 \(-0.43\)；
- Delta 只对很小的价格变动作局部近似；标的大幅移动后必须用 Gamma 更新。

组合 Delta 可以相加。若持有 \(n_i\) 张、合约乘数为 \(m_i\)，组合 Dollar Delta 的简单表示为：

\[
\sum_i n_i m_i \Delta_i
\]

## 第 3 讲：Delta 与行权价

同一到期日下，一般规律是：

- Deep OTM Call 的 Delta 接近 0；
- ATM Call 的 Delta 常接近 0.5；
- Deep ITM Call 的 Delta 接近 1；
- Deep OTM Put 的 Delta 接近 0；
- ATM Put 的 Delta 常接近 -0.5；
- Deep ITM Put 的 Delta 接近 -1。

![Put Delta 随行权价变化](<../assets/intermediate/chapter-01-option-greeks/lesson-03/frame-01-0263s.jpg>)

**图怎么看：**

- 横轴是 Strike，纵轴是 Put Delta；
- Strike 越高，Put 越深入 ITM，Delta 趋近 \(-1\)；
- 曲线而非直线意味着不同位置的敏感度变化速度不同；
- ATM Delta 不保证恰好为 \(\pm0.5\)，利率、股息、期限和波动率偏斜都会造成偏离。

用 Delta 选 Strike，本质是选择方向敏感度和成本，不是选择一个确定胜率。

## 第 4 讲：组合 Delta 与概率近似

同到期、同 Strike 的 Long Call + Short Put 是 Synthetic Long。其 Delta 通常接近 1，因此每组组合约有接近 100 股的方向敞口。

课程还把 Delta 解释成“到期 ITM 概率”。它只能作为快速经验值，不能当作真实概率：

- 在基础 BSM 中，Call Delta 常写作 \(N(d_1)\)；
- 风险中性 ITM 概率更接近 \(N(d_2)\)；
- 真实世界概率还取决于风险溢价和实际收益分布；
- Put、股息、美式提前行权和波动率偏斜会进一步改变解释。

![把 Delta 当作 ITM 概率的课程示意](<../assets/intermediate/chapter-01-option-greeks/lesson-04/frame-01-0262s.jpg>)

**图怎么看：**

- `Delta = 0.1` 可粗略理解为低概率 OTM 合约，但不是“10% 必然 ITM”；
- `Delta = 0.9` 也不保证 90%；
- “固定卖 0.30 Delta 最划算”没有跨标的、跨时期的普遍保证；
- Strike 决策还必须同时看权利金、最大亏损、事件、流动性和组合整体风险。

## 第 5 讲：Gamma

Gamma 是 Delta 对标的价格的敏感度：

\[
\Gamma=\frac{\partial \Delta}{\partial S}
=\frac{\partial^2 V}{\partial S^2}
\]

若 Delta 为 0.30、Gamma 为 0.05，标的小幅上涨 1 美元后，Delta 可粗略估算为 0.35。由于 Gamma 也会变化，这仍只是局部近似。

![期权链中的 Delta 与 Gamma](<../assets/intermediate/chapter-01-option-greeks/lesson-05/frame-01-0228s.jpg>)

**图怎么看：**

- 相邻 Strike 的 Delta 差异帮助直观看到 Gamma；
- Long Vanilla Option 通常为正 Gamma，标的向有利方向移动时 Delta 增大，反向移动时方向敞口缩小；
- Short Vanilla Option 通常为负 Gamma，行情移动后会形成不利的 Delta 变化；
- “正 Gamma 有利”不等于一定盈利，因为它通常需要用负 Theta 购买。

Gamma 常在短期限、接近 ATM 时最高。

![临近到期 ATM 区域的 Gamma 峰值](<../assets/intermediate/chapter-01-option-greeks/lesson-05/frame-02-0498s.jpg>)

**图怎么看：**

- 尖峰表示临近到期时，ATM 附近的 Delta 可能因很小的股价变化而剧烈改变；
- 对 Short Gamma，方向敞口可能快速恶化；对 Long Gamma，收益也可能快速反转；
- Gamma 高不是单独的“风险分数”，还要乘仓位、合约乘数和标的变动幅度；
- 提前平仓是控制方法之一，但不是所有 ATM 近月期权都必须机械平仓。

二阶近似可以写成：

\[
\Delta V \approx \Delta\Delta S+\frac12\Gamma(\Delta S)^2
\]

## 第 6 讲：Theta

Theta 衡量时间经过对期权理论价格的影响：

\[
\Theta=\frac{\partial V}{\partial t}
\]

平台常显示“经过一天”的理论变化。若 Theta = -0.063，其他输入不变，Long Option 一张标准合约的理论日损耗约为 6.30 美元。

![期权链中的 Theta](<../assets/intermediate/chapter-01-option-greeks/lesson-06/frame-01-0281s.jpg>)

**图怎么看：**

- 图中 ATM Call 的 Theta 是某一时点的模型估计；
- Theta 不是每天从账户机械扣除的费用，而是价格随剩余期限缩短的一个分量；
- 周末也在模型时间内，但周末衰减会提前反映在报价和 IV 中，不能简单认为每个周末都白赚两天；
- 股价或 IV 的变化可能轻易盖过 Theta。

Long Vanilla Option 通常为负 Theta，Short Vanilla Option 通常为正 Theta，但利率、股息和深度 ITM 情形可能出现例外。组合 Theta 要把各腿和数量相加。

## 第 7 讲：Gamma 与 Theta 的交换

Long Option 通常：

- 买入正 Gamma 的凸性；
- 同时承担负 Theta 的持有成本。

Short Option 通常：

- 收取正 Theta；
- 同时承担负 Gamma 和尾部行情风险。

![买方与卖方在 Gamma、Theta 上的取舍](<../assets/intermediate/chapter-01-option-greeks/lesson-07/frame-01-0117s.jpg>)

**图怎么看：**

- 买方付权利金获得选择权和凸性；
- 卖方收权利金承担履约义务；
- 正 Theta 不是“稳定收益”，它是承担负 Gamma、跳空和波动率风险的补偿；
- 课程所说“永远不能同时正 Gamma、正 Theta”可作为普通静态 Vanilla 组合的直觉，但不能当成适用于所有资产、期限结构和动态交易的数学定理。

## 第 8 讲：Vega

Vega 衡量 IV 变动对期权理论价格的影响。市场通常按 IV 变化 1 个百分点报价：

\[
\text{Vega}\approx \frac{\Delta V}{\Delta \sigma_{\text{1 vol point}}}
\]

例如 Vega = 0.161，IV 从 22.4% 上升到 23.4%，其他条件近似不变，期权理论价格约增加 0.161 美元/股，即每张约 16.10 美元。

一般规律：

- Long Call、Long Put 通常为正 Vega；
- Short Call、Short Put 通常为负 Vega；
- 接近 ATM、期限较长的合约通常有较大 Vega；
- 组合 Vega 是各腿按数量和乘数相加。

![财报前后与 IV Crush](<../assets/intermediate/chapter-01-option-greeks/lesson-08/frame-01-0341s.jpg>)

**图怎么看：**

- 财报前不确定性使近月 IV 常被抬高；
- 公布后事件不确定性消失，IV 可能快速下降；
- Long Option 即使方向正确，也可能被 IV Crush 抵消；
- Short Vega 可能从 IV 下跌受益，但同时承担财报跳空和负 Gamma。

## 组合风险速查

| Greek | 它回答的问题 | 不能单独告诉你的 |
|---|---|---|
| Delta | 标的小幅变化时，价格先变多少 | 大幅行情后的新 Delta |
| Gamma | 标的变化时，Delta 改变多快 | 最终方向和完整尾部损失 |
| Theta | 时间经过的局部价格影响 | 实际每天必赚或必亏多少 |
| Vega | IV 变化 1 点的局部影响 | IV 会往哪里走 |

开仓前至少记录：组合 Delta、Gamma、Theta、Vega，标的上下移动情景，IV 上下变化情景，以及到期最大盈亏。
