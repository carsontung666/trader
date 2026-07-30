# Live Review 05：Other Examples A

> 对应视频：v0143–v0164，共 22 段
> 阅读重点：这些 archive 跨不同年份、平台与 market regime。标题金额只作定位；评价统一换成 entry、risk、fill、R multiple 与 rule adherence。

## v0143：DRYS

![DRYS 旧版平台的 live trade](../../assets/small-cap/live/v0143-01.jpg)

**图怎么看：**

- 旧版 Level 2、Time & Sales 与多周期 chart 说明这是历史执行环境。
- DRYS 等历史高波动标的经历 corporate actions，旧 chart 不能与当前名义价格直接比较。
- 突破后回撤幅度大，固定股数/固定美分 stop 不适用。

**复盘：** 核验 split-adjusted data、当时 catalyst 与真实 fills；不从存活到今天的 ticker 状态推断旧行情。

## v0144：2019-05-10 多标的早盘

![BLIN、UBER 等多标的工作区](../../assets/small-cap/live/v0144-01.jpg)

**图怎么看：**

- 同时监控 IPO/小盘候选，右侧图显示急跌后恢复和高位整理。
- 时间戳标题没有策略说明，不能凭结果给它补一个 setup。
- 多窗口切换增加错 symbol 与过度交易风险。

**复盘：** 从成交记录逐笔重新贴 setup；无法贴到预定义规则的交易归为 discretionary/other。

## v0145：ATAI ABCD scalp

![ATAI、MRIN 的实盘窗口](../../assets/small-cap/live/v0145-01.jpg)

**图怎么看：**

- ATAI 图出现 impulse、pullback 与再上攻，符合 ABCD/continuation context。
- 标题的 scalp 金额不表示标准仓位。
- 同时观察 MRIN 可能分散对 primary trade 的执行注意。

**复盘：** 标 A/B/C、entry、C-low invalidation，并计算 scalp exit 与持有到 D 的差异。

## v0146：AKTX 开盘半整数位 scalp

![AKTX 与其他开盘候选](../../assets/small-cap/live/v0146-01.jpg)

**图怎么看：**

- AKTX 早盘快速上行并在关口附近波动。
- “Half-dollar out of the gates” 同时暴露于开盘 spread 和心理价位假突破。
- 右侧多个大 candle 表明 entry 到结构 stop 可能远于名义半美元位。

**复盘：** 单独统计开盘前 5 分钟，加入 spread、slippage 与 first-halt exposure。

## v0147：CNR squeeze halt（副本 1）

![CNR halt 前的旧版执行画面](../../assets/small-cap/live/v0147-01.jpg)

**图怎么看：**

- 源文件没有音轨，本段只能按屏幕和标题复盘。
- 价格垂直扩张并进入 halt，Level 2 不能代表恢复后的 depth。
- 买入 halt 前无法用普通 stop 管理下一跳。
- 标题重复提示这可能与下一段为同一源。

**复盘：** 与 v0148 做 hash/内容去重；即使重复，最终资料只把它当同一案例的两个来源记录。

## v0148：CNR squeeze halt（副本 2）

![CNR 重复画面的另一份源视频](../../assets/small-cap/live/v0148-01.jpg)

**图怎么看：**

- 这个副本同样没有音轨，不能从口述确认任何 entry/exit 理由。
- 界面、时间与价格结构与 v0147 高度相似。
- 重复视频不能在样本统计中计两次，否则夸大该 setup 权重。
- 恢复价、partial fill 和 halt duration 才是关键。

**复盘：** 样本表设置 `duplicate_group=CNR-halt`，只保留一条 expectancy 记录。

## v0149：DXR class example

![DXR 与多标的 Level 2](../../assets/small-cap/live/v0149-01.jpg)

**图怎么看：**

- DXR 图显示大幅扩张后的整理，旁边仍有其他候选。
- Class example 可能选择了教学上清楚的片段，存在 selection bias。
- 高位 continuation 必须标第几次 pullback。

**复盘：** 补入同日未成功 breakout；只用精选 winner 无法估计胜率。

## v0150：Day 134

![ANY 等股票的日内多窗口](../../assets/small-cap/live/v0150-01.jpg)

**图怎么看：**

- ANY 出现快速拉升并在高位整理，其他图走势不同。
- 文件名只有 day number，没有清楚策略；应从成交重建，而不猜测。
- Session-level recap 要区分各 ticker 的独立 risk。

**复盘：** 按时间排序所有 trades，标出第一笔后 size/P&L 是否影响后续决策。

## v0151：历史多标的 momentum

![OPGN、TOPS 等旧版 live workspace](../../assets/small-cap/live/v0151-01.jpg)

**图怎么看：**

- 源文件名不具描述性，画面显示多个旧 small-cap momentum ticker。
- OPGN 已经扩张后横盘，追价需要上方空间和明确 low。
- 旧平台与旧佣金环境会改变 scalp 的净收益。

**复盘：** 不根据文件名生成故事；用实际 symbol、fills 和 fees 建档。

## v0152：LYFT IPO

![LYFT IPO 交易的多窗口](../../assets/small-cap/live/v0152-01.jpg)

**图怎么看：**

- IPO 初期历史图短、price discovery 强，传统日线水平有限。
- 图中急跌与反弹表明首日/早期波动两向都大。
- IPO order behavior、halt 与可借股状态可能特殊。

**复盘：** 记录 IPO age、首日 high/low、发行价、float、spread；不与成熟 large cap 混合。

## v0153：两只股票合计亏损案例

![多个 breakout/pullback 的亏损日](../../assets/small-cap/live/v0153-01.jpg)

**图怎么看：**

- 多个图同时出现快速扩张与回落，标题明确是亏损案例。
- 亏损样本比 winner 更适合检查追价、重复尝试和 market regime。
- 单看结束截图无法区分正常 stop 与违规扩大 stop。

**复盘：** 分解每笔 planned loss、actual loss、slippage、re-entry 次数；不要只写总额。

## v0154：大额亏损日

![SOLQ、ESTR 等多标的亏损交易](../../assets/small-cap/live/v0154-01.jpg)

**图怎么看：**

- 同时交易多只 high-volatility 股票可能形成相关 momentum exposure。
- 账户 P&L 大并不说明 market “欠反弹”。
- 如果总损失超过预设 daily stop，后续每笔都应标 rule violation。

**复盘：** 建时间线：何时触及 warning、daily stop、继续交易原因以及若当时停止的差异。

## v0155：带讲解的 winner

![VXRT/AKTX 等 live trade 与 commentary](../../assets/small-cap/live/v0155-01.jpg)

**图怎么看：**

- 画面展示强势 pullback/continuation，与同步讲解结合。
- Narration 可能改变执行注意和交易行为。
- Winner 金额不展示未成交/滑点和同日其他风险。

**复盘：** 对照讲解前写的计划，区分实时 prediction 与事后 explanation。

## v0156：三只股票组合结果

![ACB、DFFN 等三标的执行](../../assets/small-cap/live/v0156-01.jpg)

**图怎么看：**

- 多笔结果汇总可能掩盖某一笔大 winner 覆盖其他 loser。
- DFFN 出现垂直 move，单次异常可支配日收益。
- 不同 setup 不应因同一天交易而合并。

**复盘：** 每票计算 R 与 expectancy，再汇总；报告 profit concentration。

## v0157：15 秒 scalp

![SPI 等快速突破的 15 秒交易](../../assets/small-cap/live/v0157-01.jpg)

**图怎么看：**

- 15 秒持仓高度依赖 alert-to-order latency、hotkey 和实际 depth。
- Chart candle 无法展示秒内成交顺序。
- 极快 winner 对 simulator fill assumptions 很敏感。

**复盘：** 保存逐笔 timestamps、expected/actual fill、fees；无法复现这些数据就不作为普通学习者 setup。

## v0158：从潜在亏损到小赢

![WORK 等标的的回撤与恢复](../../assets/small-cap/live/v0158-01.jpg)

**图怎么看：**

- 价格先不利后恢复，最终小赢不能证明 holding loser 正确。
- 应比较当时是否仍守住原 invalidation。
- “转赢”结果最容易强化扩大 stop 的坏习惯。

**复盘：** 若 price 曾破 stop，这笔按规则应记 loss；后续恢复只作 counterfactual，不改 decision grade。

## v0159：连续 circuit-breaker halts

![CTXR/NVIV 与 halt 交易记录](../../assets/small-cap/live/v0159-01.jpg)

**图怎么看：**

- 多次 halt 造成离散价格路径，订单状态和 chart 都可能滞后。
- 连续向上 halt 也可能突然向下恢复。
- 标题结果说明大额盈利不消除 tail risk。

**复盘：** 单列 halt count、每次 resume gap、可退出时间与最大理论亏损。

## v0160：ZKIN Gap & Go

![ZKIN 强势 Gap & Go](../../assets/small-cap/live/v0160-01.jpg)

**图怎么看：**

- ZKIN 在开盘后沿短均线上行，出现多个 pullback。
- 最早 entry 与后段追高风险完全不同。
- Gap & Go 需补 catalyst、premarket volume 和 daily room。

**复盘：** 标第一/第二/后续 pullback 的独立结果，避免用全天趋势证明任一 entry。

## v0161：Day 133 亏损

![AEZS 等多标的亏损 session](../../assets/small-cap/live/v0161-01.jpg)

**图怎么看：**

- 一只股票急涨，另一只可能下跌，说明 market 不统一。
- 总亏损应拆成 setup loss 与 context-switching cost。
- 日编号本身不提供交易逻辑。

**复盘：** 统计每笔前是否已有计划、是否在前一笔情绪未恢复时进入。

## v0162：ITCI

![OPGN/ITCI 相关的盘中窗口](../../assets/small-cap/live/v0162-01.jpg)

**图怎么看：**

- 主窗口同时出现异动股与多周期图，ITCI 结果金额较小。
- 小额 loss 仍可揭示 entry timing 或 spread 问题。
- 不因为金额小就跳过复盘。

**复盘：** 将亏损换算 R；判断是正常统计 loss 还是 setup 不成立。

## v0163：OPTT 大额 loss

![OPTT/EVGN 等急涨急跌](../../assets/small-cap/live/v0163-01.jpg)

**图怎么看：**

- OPTT 先急涨后明显回落，属于容易追高和重复 dip 的路径。
- 多票同屏可能诱使从一个 loser 跳到另一个 mover。
- 大额 loss 需要检查 size 是否按 stop distance 缩减。

**复盘：** 重建所有 add，计算每次 add 后总 open risk；检查是否 average down。

## v0164：SES 与 BIMI 极端 squeeze

![SES/BIMI 的数百百分比波动](../../assets/small-cap/live/v0164-01.jpg)

**图怎么看：**

- 两只股票都呈 parabolic move，普通 ATR/stop 参数失效。
- 百分比涨幅很大不等于可实现相同比例收益。
- Halt、wide spread 和 liquidity disappearance 是主要风险。

**复盘：** 归入 `parabolic-regime`，从普通 Gap & Go 样本中剔除，并以最坏 resume gap 做 stress test。

## 本组结论

- 重复源只计一个统计样本；
- 无描述性文件名就从 fills 重建，不猜；
- 结果金额全部换算 R；
- Winner 也检查是否破过 stop；
- Halt、IPO、parabolic 与普通 momentum 分桶；
- Session 总额不能替代逐笔复盘。
