# 11.1 Greeks

> 一句话：Greeks 是期权价格在「当前这一点」对不同输入的局部敏感度，不是保证。

Greeks 来自模型。不同平台的模型、利率和股息输入可能略有差异。标的、时间和 IV 同时变化时，不能只拿一个 Greek 直接预测最终盈亏。大幅跳空之后，Greeks 立刻过时。

本卷沿用第 10 卷的符号：\(V\) 是期权价格（每股），\(S\) 是标的价格。账户上的美元敏感度还要乘张数和合约乘数。乘数常见为 100，调整合约先核规格。

## 11.1.1 Greeks 在量化什么

影响期权价格的主要维度可以先分成：

- 标的价格：Delta、Gamma；
- 时间：Theta；
- 隐含波动率：Vega；
- 利率：Rho，股票期权里通常不是主矛盾，长期合约更相关。

专业风险管理还会看 Vanna、Charm 等交叉导数。初学不需要据此堆指标。先能解释 Delta、Gamma、Theta、Vega 在不同价格与期限下如何变化，已经够用。

实际盈亏还包括合约数量、乘数、买卖价差和成交价格。平台显示的 Greeks 是估计值，要看整个头寸的净值。

## 11.1.2 Delta

Delta 是期权价格对标的价格的一阶敏感度：

\[
\Delta=\frac{\partial V}{\partial S}
\]

若一张 Long Call 的 Delta 为 0.43，标的瞬间上涨 1 美元，其他条件近似不变时，期权理论价格约上涨 0.43 美元/股，即一张标准合约约 43 美元。这是当前点附近的近似，不是永远「股票每涨 1 美元，期权涨 0.43」。

符号：

- Long Call：通常 \(0\) 到 \(1\)；
- Long Put：通常 \(-1\) 到 \(0\)；
- Short Option：对应 Long Option 的相反数；
- 100 股股票：Delta = \(100\)，若用「每股单位」则为 \(1\)。

Call Delta 为正，Put Delta 为负，反映标的上涨时两者理论价格的相反方向。课程口误把卖出 0.43 Delta Call 说成 \(-0.33\)，正确应约为 \(-0.43\)。Delta 只对很小的价格变动作局部近似；标的大幅移动后必须用 Gamma 更新。

组合 Delta 可以相加。若持有 \(n_i\) 张、合约乘数为 \(m_i\)，组合 Dollar Delta 的简单表示为：

\[
\sum_i n_i m_i \Delta_i
\]

同一到期日下，一般规律是：

- Deep OTM Call 的 Delta 接近 0；
- ATM Call 的 Delta 常接近 0.5；
- Deep ITM Call 的 Delta 接近 1；
- Deep OTM Put 的 Delta 接近 0；
- ATM Put 的 Delta 常接近 -0.5；
- Deep ITM Put 的 Delta 接近 -1。

Strike 越高，Put 越深入 ITM，Delta 趋近 \(-1\)。曲线而非直线意味着不同位置的敏感度变化速度不同。ATM Delta 不保证恰好为 \(\pm 0.5\)，利率、股息、期限和波动率偏斜都会造成偏离。

用 Delta 选 Strike，本质是选择方向敏感度和成本，不是选择一个确定胜率。低 Delta 常意味着更 OTM、归零概率更高、点差百分比更宽。不能把「便宜」当作风险低。

## 11.1.3 组合 Delta 与概率近似

同到期、同 Strike 的 Long Call + Short Put 是 Synthetic Long。其 Delta 通常接近 1，因此每组组合约有接近 100 股的方向敞口（乘数 100 时）。第 10 卷第 07 章已经写过：净权利金很小不等于只承担很小风险。

课程还把 Delta 解释成「到期 ITM 概率」。它只能作为快速经验值，不能当作真实概率：

- 在基础 BSM 中，Call Delta 常写作 \(N(d_1)\)；
- 风险中性 ITM 概率更接近 \(N(d_2)\)；
- 真实世界概率还取决于风险溢价和实际收益分布；
- Put、股息、美式提前行权和波动率偏斜会进一步改变解释。

`Delta = 0.1` 可粗略理解为低概率 OTM 合约，但不是「10% 必然 ITM」。`Delta = 0.9` 也不保证 90%。「固定卖 0.30 Delta 最划算」没有跨标的、跨时期的普遍保证。Strike 决策还必须同时看权利金、最大亏损、事件、流动性和组合整体风险。

Covered Call 若 100 股按每股单位记 Delta = 1，卖出一张 Call：

\[
\Delta_{\text{CC}}=1-\Delta_{\text{Long Call}}
\]

例如卖 0.30 Delta OTM Call，组合 Delta 约 0.70；卖 0.50 ATM，约 0.50；卖 0.70 ITM，约 0.30。这是开仓局部值。股价上涨时 Call Delta 增大，组合 Delta 减小；股价下跌时 Call Delta 减小，组合 Delta 增大。这是负 Gamma。

## 11.1.4 Gamma

Gamma 是 Delta 对标的价格的敏感度：

\[
\Gamma=\frac{\partial \Delta}{\partial S}
=\frac{\partial^2 V}{\partial S^2}
\]

若 Delta 为 0.30、Gamma 为 0.05，标的小幅上涨 1 美元后，Delta 可粗略估算为 0.35。由于 Gamma 也会变化，这仍只是局部近似。相邻 Strike 的 Delta 差异帮助直观看到 Gamma。

Long Vanilla Option 通常为正 Gamma：标的向有利方向移动时 Delta 增大，反向移动时方向敞口缩小。Short Vanilla Option 通常为负 Gamma：行情移动后会形成不利的 Delta 变化。「正 Gamma 有利」不等于一定盈利，因为它通常需要用负 Theta 购买。

Gamma 常在短期限、接近 ATM 时最高。临近到期时，ATM 附近的 Delta 可能因很小的股价变化而剧烈改变。对 Short Gamma，方向敞口可能快速恶化；对 Long Gamma，收益也可能快速反转。Gamma 高不是单独的「风险分数」，还要乘仓位、合约乘数和标的变动幅度。提前平仓是控制方法之一，但不是所有 ATM 近月期权都必须机械平仓。

二阶近似可以写成：

\[
\Delta V \approx \Delta\,\Delta S+\frac12\Gamma(\Delta S)^2
\]

大跳空时这个近似也会坏。路径风险不能只用开仓 Delta 概括。

## 11.1.5 Theta

Theta 衡量时间经过对期权理论价格的影响：

\[
\Theta=\frac{\partial V}{\partial t}
\]

平台常显示「经过一天」的理论变化。若 Theta = -0.063，其他输入不变，Long Option 一张标准合约的理论日损耗约为 6.30 美元。Theta 不是每天从账户机械扣除的费用。周末也在模型时间内，但周末衰减会提前反映在报价和 IV 中，不能简单认为每个周末都白赚两天。股价或 IV 的变化可能轻易盖过 Theta。

Long Vanilla Option 通常为负 Theta，Short Vanilla Option 通常为正 Theta，但利率、股息和深度 ITM 情形可能出现例外。组合 Theta 要把各腿和数量相加。

如果 swing 论点需要两周才实现，购买只剩几天的合约会让时间容错极低。临近到期、接近 ATM 时衰减形状可能更陡。

## 11.1.6 Gamma 与 Theta 的交换

Long Option 通常：

- 买入正 Gamma 的凸性；
- 同时承担负 Theta 的持有成本。

Short Option 通常：

- 收取正 Theta；
- 同时承担负 Gamma 和尾部行情风险。

买方付权利金获得选择权和凸性；卖方收权利金承担履约义务。正 Theta 不是「稳定收益」，它是承担负 Gamma、跳空和波动率风险的补偿。课程所说「永远不能同时正 Gamma、正 Theta」可作为普通静态 Vanilla 组合的直觉，但不能当成适用于所有资产、期限结构和动态交易的数学定理。

## 11.1.7 Vega

Vega 衡量 IV 变动对期权理论价格的影响。市场通常按 IV 变化 1 个百分点报价：

\[
\text{Vega}\approx \frac{\Delta V}{\Delta \sigma_{\text{1 vol point}}}
\]

例如 Vega = 0.161，IV 从 22.4% 上升到 23.4%，其他条件近似不变，期权理论价格约增加 0.161 美元/股，即每张约 16.10 美元。单位要从平台确认，不要口头把小数位抄错。

一般规律：

- Long Call、Long Put 通常为正 Vega；
- Short Call、Short Put 通常为负 Vega；
- 接近 ATM、期限较长的合约通常有较大 Vega；
- 组合 Vega 是各腿按数量和乘数相加。

财报前不确定性使近月 IV 常被抬高；公布后事件不确定性消失，IV 可能快速下降。Long Option 即使方向正确，也可能被 IV Crush 抵消。Short Vega 可能从 IV 下跌受益，但同时承担财报跳空和负 Gamma。

课程说「短期期权对 IV 更敏感」不严谨：绝对 Vega 通常是长期期权更高。短期限事件期权的事件方差更集中，财报后 IV Crush 更直观，但短期限也有更高 Gamma。不同 expiration / strike 构成波动率曲面，不能只看单一 「IV」 数字。

Rho 是期权价格对利率的敏感度，长期合约更相关。入门可以先放在检查清单末尾，不要用它解释日内盈亏。

## 11.1.8 组合风险速查

| Greek | 它回答的问题 | 不能单独告诉你的 |
|---|---|---|
| Delta | 标的小幅变化时，价格先变多少 | 大幅行情后的新 Delta |
| Gamma | 标的变化时，Delta 改变多快 | 最终方向和完整尾部损失 |
| Theta | 时间经过的局部价格影响 | 实际每天必赚或必亏多少 |
| Vega | IV 变化 1 点的局部影响 | IV 会往哪里走 |

开仓前至少记录：组合 Delta、Gamma、Theta、Vega，标的上下移动情景，IV 上下变化情景，以及到期最大盈亏。入场、每日收盘、退出各保存一份快照：

```text
标的价格
期权 Bid / Ask / Mid / Last
到期日和剩余天数
行权价与 moneyness
IV
Delta / Gamma / Theta / Vega
未平仓 / 成交量
事件日历
头寸级 Greeks
```

复盘时才能分解：到底是方向、时间、IV，还是成交成本导致盈亏。

## 11.1.9 四个情景矩阵

对 Long Call 至少计算：

| 标的路径 | IV | 时间 | 可能结果 |
|---|---|---|---|
| 快速上涨 | 上升 | 少量流逝 | 通常最有利 |
| 缓慢上涨 | 下降 | 大量流逝 | 方向对仍可能亏 |
| 横盘 | 上升 | 流逝 | Vega 可能暂时抵消 Theta |
| 下跌 | 下降 | 流逝 | 多因素同时不利 |

再对 Long Put、Credit / Debit Spread 重做，不要假设完全镜像。Greeks 是模型输出，不是市场欠你的收益。

## 11.1.10 一张标准合约的美元换算

平台上的 Greeks 多数是「每股」。账户上要乘乘数和张数。设乘数 100、持有 3 张 Long Call：

| Greek | 屏幕 | 账户近似 |
|---|---|---|
| Delta 0.40 | 标的 +1 美元，每股约 +0.40 | \(0.40 \times 100 \times 3 = 120\) 美元 |
| Gamma 0.05 | Delta 约变为 0.45 | 下一美元再加约 15 美元敏感度 |
| Theta −0.08 | 一天约 −0.08/股 | \(−8 \times 3 = −24\) 美元 |
| Vega 0.12 | IV +1 个点约 +0.12/股 | \(12 \times 3 = 36\) 美元 |

标的跳 5 美元、IV 同时掉 4 个点、再过两天，不能把三行数字简单相加当最终盈亏。二阶项、曲面移动和点差都会改结果。这笔账的用处是开仓前做情景，不是盘中精确预测。

## 11.1.11 组合相加时的符号

100 股 + 1 张 Short 0.30 Delta Call：

```text
股票 Delta      +100
Short Call      −30
组合            +70
```

再加一张 Delta −0.45 的 Protective Put：

```text
组合 Delta      +70 − 45 = +25
```

下跌时 Put 的 \|Delta\| 通常变大，组合 Delta 继续下降，保护增强；上涨时 Put Delta 靠近 0，组合 Delta 回升。Short Call 则相反：上涨时它的 \|Delta\| 变大，组合更早封顶。这就是「正 Gamma 保险」和「负 Gamma 收租」在同一账户里会互相拉扯的原因。

垂直价差两腿同类型、方向相反，Greeks 部分抵消。Strikes 越近，净 Greeks 越小；越远，越像单腿。Iron Condor 四腿再抵消一层，但到期附近短腿周围 Gamma 仍会尖起来。

## 11.1.12 不要用单个 Greek 选策略

- 只看 Theta 高就卖：忽略了负 Gamma 和跳空。
- 只看 Delta 当胜率：\(N(d_1)\) 不是真实世界概率。
- 只看 Vega 大就买财报：事件溢价可能已经贵过你要的跳空。
- 只看 Gamma 高就做日内：点差和两腿手续费可能先吃掉凸性。

开仓记录里四个 Greeks 都要在，并且各自配一个「如果反向走，我亏多少」的句子。

