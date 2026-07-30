# Live Review 06：Other Examples B

> 对应视频：v0165–v0186，共 22 段
> 本组集中在 scalp、long/short 切换、bear flag、news 与 squeeze halt。核心问题不是最终金额，而是每次方向变化是否有独立触发。

## v0165：Win、loss、再到 larger winner

![DTSS 等多笔先后结果](../../assets/small-cap/live/v0165-01.jpg)

**图怎么看：**

- 一天内小赢、小亏、再出现较大 winner，展示 P&L 路径而非单笔。
- 第三笔不能因前两笔结果而改变 size，除非预先有 tier rule。
- 最终盈利会掩盖中间是否 revenge trade。

**视频内容：** 画面中 DTSS、XNET 与当日订单/仓位窗口同时可见，标题所说的 “win—loss—larger winner” 是按时间发生的三段结果，而不是一个 setup。学习时应在不知道第三笔会赢的情况下停在第二笔结束处，检查剩余 daily risk、情绪和第三笔触发是否仍满足规则；只有答案为是，第三笔才是独立好交易。

**复盘：** 对每笔单独打 decision grade；移除最终结果后再评价第三笔是否仍应做。

## v0166：2018-11-14 session

![ANY 等标的的 live workspace](../../assets/small-cap/live/v0166-01.jpg)

**图怎么看：**

- ANY chart 呈现急涨和高位整理，文件名只有日期。
- 旧市场、旧佣金和旧平台影响短线净收益。
- 高位横盘可同时演变为 continuation 或 failed breakout。

**视频内容：** 2018-11-14 的画面以 ANY 为主，保留 1m、5m、daily 和订单簿；价格先拉升、在高位整理，较长周期仍显示这只是更大历史结构中的一段。视频适合做双情景练习：向上突破时需要什么成交量/acceptance，向下跌破平台时在哪失效。没有后续走势前，两种路径都必须成立。

**复盘：** 只用当时可见 high/low 定两套 scenario；不因后续方向重写。

## v0167：2019-02-05 session

![MBOT 等多标的日内交易](../../assets/small-cap/live/v0167-01.jpg)

**图怎么看：**

- MBOT 多周期显示强势 move 与回撤，其他候选也活跃。
- 日级 archive 应识别 profit 是否集中在一个 symbol。
- 同时多次报警不等于多个 independent setup。

**视频内容：** 主工作区可确认 MBOT，同时还有其他 scanner 候选；MBOT 已经出现一段明显 expansion，随后回撤并再次靠近高位。日级录像应拆成 opening drive、first pullback、later attempt 三类触发，并核对是否同一只股票贡献了绝大部分 P&L。若是，日结果不能代表多 setup 都有效。

**复盘：** 报告 top ticker contribution、trade count 与重复 entry 次数。

## v0168：2017-02-07 session

![旧版平台上的快速 breakout](../../assets/small-cap/live/v0168-01.jpg)

**图怎么看：**

- 旧界面与成交环境说明样本距今较久。
- 右图 breakout 后立即大幅波动，K 线回测会低估执行难度。
- 缺少描述性标题时不能推断 catalyst。

**视频内容：** 旧 SpeedTrader 界面把订单、Level 2、Time & Sales 与多周期图并排；主图在低位长时间横盘后突然放量拉升，随后立刻出现大幅回撤/再测试。可学习的是 breakout 前后的流动性变化与止损距离，而不是猜 2017 年 2 月 7 日的新闻。历史样本只保留结构与执行，不外推今日 fees 或 route。

**复盘：** 标记 `historical-platform`；仅保留结构学习，不用其 fees/fill 估计当前表现。

## v0169：2017-02-08 session

![另一段旧版 live trading](../../assets/small-cap/live/v0169-01.jpg)

**图怎么看：**

- 价格先大幅上行再横盘，典型 late-stage continuation 候选。
- Late-stage entry 与 first pullback 分开。
- 旧数据可能经过 split adjustment。

**视频内容：** 画面显示股票已完成一段近乎垂直的上涨，之后在高位形成横向区间，并在右侧再次尝试抬高。这里至少包含两个完全不同的 entry：早期 first pullback 的 stop 靠近趋势结构，晚期突破面对更高成本、更多 trapped traders 和更小剩余空间。把它们混成一个“continuation”会掩盖 sequence risk。

**复盘：** 记录 sequence number 和 adjusted/unadjusted price，避免历史名义价误导。

## v0170：MTSL only

![MTSL 单票多周期](../../assets/small-cap/live/v0170-01.jpg)

**图怎么看：**

- 单票 focus 减少 symbol-switching，但容易过度交易同一股票。
- 右侧图显示冲高、回撤、再测试，不同 entry 不能用全天趋势统一解释。
- 一只股票反复 alert 会强化 familiarity bias。

**视频内容：** MTSL 与 GBR、BLIN 等同屏，但标题强调 only，说明实际复盘应围绕同一票的多次尝试。图中能分出首次冲高、深回撤、重新站回关键位和后续再测试；每次重新进入都应有新的 trigger，而不是因为已经熟悉 MTSL 就默认它会再涨。

**复盘：** 设同票最大尝试次数与累计 loss；第三次 entry 仍需独立 A setup。

## v0171：CALI

![CALI 急涨和旧版订单窗口](../../assets/small-cap/live/v0171-01.jpg)

**图怎么看：**

- 价格快速抬升，Level 2 depth 相对有限。
- 旧版 route/order defaults 不能照抄。
- 高速 squeeze 中 market order 的最坏价格不可控。

**视频内容：** CALI 与 FENC、ERMS、MARA 等候选并列，CALI 主图显示快速上冲与短促整理，Level 2 深度相对有限。视频的重点是从 scanner 发现到发单的短时间窗口：若突破价附近只显示少量 shares，大订单的平均成交会跨越多档；屏幕上的 best ask 不能当作整个仓位的预计成本。

**复盘：** 从 prints 重建实际 slippage；若深度不足计划 size，capacity-adjusted size 应更小。

## v0172：Day 132

![MRIN 等多标的 live session](../../assets/small-cap/live/v0172-01.jpg)

**图怎么看：**

- 多只股票出现异动，主图有冲高后长时间整理。
- Day number 不说明 setup，需要逐笔贴标签。
- 午后/后段整理与开盘 momentum 不能混合。

**视频内容：** 关键帧可确认 MBRX、AAOI、TANH、ZN 等多票，而不是单一 MRIN 案例；其中有的已拉升后高位横盘，有的仍在低位或走弱。Day 132 应按时间段重建：哪些是开盘即时 momentum，哪些是后段 range breakout，哪些只在 scanner 中出现。时段不同，volume、spread 和预期持有时间也不同。

**复盘：** 按 time bucket 统计，找出交易是否在 edge 时段外增加。

## v0173：NFEC

![NFEC 旧版 halt/squeeze 场景](../../assets/small-cap/live/v0173-01.jpg)

**图怎么看：**

- 画面结合旧平台与急涨图，属于 high-halt-risk 标的。
- Visible seller/bid 可能在 resume 时消失。
- 同一 NFEC 还出现在 v0185，需检查是否重复。

**视频内容：** 旧平台同时显示 XNTN、NFEC、OPTT 等 ticker，NFEC 的关键图形是快速上冲并靠近/进入暂停；订单/成交列表保留在左侧。由于同事件另有 v0185，无论某个剪辑看起来多完整，都不能把两个文件分别计入胜率。真正应记录的是同一次 squeeze 中的 halt 前价格、恢复价与可成交数量。

**复盘：** 建 `duplicate_group=NFEC-halt`，比较时间戳/成交后只计独立事件。

## v0174：RKDA short

![RKDA parabolic 后的 short](../../assets/small-cap/live/v0174-01.jpg)

**图怎么看：**

- RKDA 从低位垂直扩张，short 方向面临继续 squeeze。
- Top guess、false breakout short 与 trend-shift short 必须区分。
- Borrow、SSR、locate fee 未显示在 chart。

**视频内容：** RKDA 与 DXR、KOOL、ACMR 同屏，RKDA 主图已经从低位急速扩张，随后才出现回落/整理。若在第一根红柱就做空，交易属于 top guess；只有 lower high、关键支撑跌破和反抽失败陆续出现后，才更接近 trend-shift short。两个 entry 的价格可能不同，但统计类别和尾部 squeeze 风险也完全不同。

**复盘：** 加入 borrow cost、halt gap、short entry tier 和 cover liquidity。

## v0175：SLS

![SLS 的快速上行与盘口](../../assets/small-cap/live/v0175-01.jpg)

**图怎么看：**

- SLS 主图近乎垂直，普通 pullback 很浅。
- Micro pullback 对 hotkey/latency 敏感。
- 右上其他股票的走势不应干扰 primary risk。

**视频内容：** SLS 主图显示连续陡峭绿柱与很浅的 micro pullback，旁边还有 FIT、AVGR、GENI 等候选。浅回撤意味着看似容易保持动能，却使结构 stop 很难靠近；追入后只要一根正常扩幅红柱就可能超过预算。学习时应逐帧区分“真正停顿形成 micro high”与“仍在同一根冲刺 K 线中”。

**复盘：** 保存秒级 fills；无法获得则只作极端行情示例，不计可复现 setup。

## v0176：FIT news long

![FIT news trade 与订单深度](../../assets/small-cap/live/v0176-01.jpg)

**图怎么看：**

- 新闻触发的 gap/快速 candle 与普通 technical breakout 不同。
- 图中平台显示快速价格重估，晚到 entry 可能已消耗 edge。
- 方向正确仍可能因 headline reversal 亏损。

**视频内容：** FIT 的关键帧同时展示 news-driven 直线拉升、Level 2 与订单面板，右侧较长周期可见它并非普通盘整自然突破。新闻公布到第一笔成交之间的延迟决定了交易性质：早期参与者承担 headline 真伪风险，晚到参与者则承担价格已重估和追高风险。两者不能用同一回测规则评价。

**复盘：** 保存原始新闻、发布时间、entry latency、source quality 和后续更正。

## v0177：FRAN long 后转 short

![FRAN 先多后空的图表](../../assets/small-cap/live/v0177-01.jpg)

**图怎么看：**

- Long thesis 失败后转 short，若没有新 trigger 容易成为 revenge reversal。
- Rejection、trend shift 与 borrow availability 都需重新确认。
- 第一个亏损不能提高第二笔 size。

**视频内容：** FRAN 与 TROV、HOME 同屏，FRAN 主图先完成向上推进，随后在高位失败并回到更低区域；“先多后空”因此包含两套相反 thesis。Long 的退出只说明原计划失效，不自动触发 short；short 至少要重新确认 lower high/支撑跌破、borrow 与新的 stop，且仓位按第二笔自己的风险计算。

**复盘：** 两笔之间强制写新计划；若只因 P&L/愤怒反向，第二笔标违规。

## v0178：MDGS Gap & Go scalp

![MDGS 强势 gapper 的多窗口](../../assets/small-cap/live/v0178-01.jpg)

**图怎么看：**

- MDGS 出现放量冲高和高位结构，属于经典 Gap & Go context。
- 标题 winner 金额可能由大 share size 驱动。
- Scanner、chart 与 Level 2 分工清楚，但上方日线空间仍需核验。

**视频内容：** MDGS 主图先出现放量 expansion，随后在高位形成短整理；CODA、FRLI、CALI 等候选同时可见。Gap & Go scalp 应把盘前高点/开盘 high 作为触发候选，把首次有序回撤低点作为 invalidation，并核对日线是否马上遇到阻力。若 entry 已在延伸后段，它不再与 first break 属于同一样本。

**复盘：** 以每股 risk/R 重算；比较 first pullback 与追 HOD 的结果。

## v0179：RKDA live trading

![RKDA 另一段 live trade](../../assets/small-cap/live/v0179-01.jpg)

**图怎么看：**

- 左侧成交列表与右侧 RKDA/KOSS 图可用于对齐 entry。
- 同 ticker 出现多段 archive，不一定是同一天。
- Parabolic RKDA 样本相关性高，不能视为完全独立。

**视频内容：** 画面显示 RKDA 与 SRAX，旁边保留 scanner 与成交列表；RKDA 先从低位急升，随后在高位发生宽幅回撤和再测试。与 v0174 的 short 视角相比，本段更适合重建同一类 parabolic 标的在 long/short 两侧的不同风险：long 害怕 flush，short 害怕继续 squeeze，二者都不能只靠“涨太多”决定方向。

**复盘：** 加 date/event ID；同一 squeeze 的多个剪辑只计一个 market event。

## v0180：SES 22.50→26 squeeze

![SES squeeze 和高位整理](../../assets/small-cap/live/v0180-01.jpg)

**图怎么看：**

- 价格跨越多个整数/半整数位，目标不能因下一个整数存在就自动延伸。
- 高价 small cap 的每股风险与滑点绝对值更大。
- 高位整理可能继续，也可能快速 flush。

**视频内容：** SES 与 BIMI、YUMA、GBR 同屏，SES 从约 `$22.50` 一带继续向 `$26` 区域推进，途中跨过多个整数/半整数关口并形成短整理。每个关口只是潜在流动性集中处，不是自动 target；真正要记录的是触发时离最近 higher low 多远，以及该止损距离对应的 dollar size。

**复盘：** Size 按 dollar stop；测试在 22.5、23、24 等关口追入的风险收益。

## v0181：ARCI 先亏后赚回

![ARCI 等标的的恢复日](../../assets/small-cap/live/v0181-01.jpg)

**图怎么看：**

- 标题以 “losing then making back” 叙事，容易强化 recovery goal。
- 后续 winner 是否 A setup 与此前 loss 无关。
- 赚回更多不能证明继续交易的决定普遍正确。

**视频内容：** ARCI、SESN、MOXC 等同时出现在工作区，标题把 session 叙述成“先亏后赚回”。画面里的后续 mover 确实提供了新机会，但学习时必须在前一亏损结束处重新判断：daily stop 是否已触发、下一只股票是否原本就在 watchlist、entry 是否有独立价位。如果任一答案是否定的，最后赚钱也不能洗掉过程问题。

**复盘：** 使用 counterfactual：若按 daily stop 停止，长期期望和回撤会怎样；不以单日恢复定规则。

## v0182：FCSC scalp loss

![FCSC/RBZ 的快速 breakout](../../assets/small-cap/live/v0182-01.jpg)

**图怎么看：**

- FCSC 图上有快速扩张和长 wick，容易产生 breakout slippage。
- 正常小亏是策略成本，前提是止损符合计划。
- 右侧另一个标的上涨不能成为换票追单理由。

**视频内容：** FCSC、RBZ、MOGO 同屏，FCSC 的短周期图在快速扩张后出现长 wick/回落；这正是 breakout order 可能成交在高位、stop 又落到低位的环境。视频应按计划价、实际 fill、结构 stop 和退出 fill 四个点学习：若亏损主要来自 bid/ask 与滑点，问题在 capacity/执行；若 entry 前就没有空间，问题在 setup。

**复盘：** 将 loss 拆成 planned risk 与 execution slippage；若在预算内，decision grade 仍可为 A。

## v0183：RHE scalp winner

![RHE 的强势日内 move](../../assets/small-cap/live/v0183-01.jpg)

**图怎么看：**

- RHE 图显示上行趋势和多次 pullback。
- Winner 金额必须结合 shares 和 stop 才有意义。
- 最漂亮的趋势也包含 late entry 风险。

**视频内容：** RHE 与 SSLJ、ARCI、MBIO 同屏，RHE 主图先完成突破，再沿较高低点推进并出现多次回撤。每次 pullback 的低点、离 VWAP/均线距离和上方空间不同；因此“RHE 是赢家”不能替代 entry 序号。最值得学习的是哪一次形成了清楚 invalidation，哪些后段只是追随已经成熟的趋势。

**复盘：** 标 sequence number；比较只做 first/second pullback 与全天所有 entry。

## v0184：Bear flag short

![Breakdown 后的 bear flag](../../assets/small-cap/live/v0184-01.jpg)

**图怎么看：**

- 主图先下跌、弱反弹整理，再尝试 continuation，结构比 top-guess short 清楚。
- Stop 参考 flag high，目标参考前 low/日线支撑。
- 做空仍要加 borrow/SSR，而不是只看形态。

**视频内容：** 画面中的候选包括 CCNI、PHAS、VIVE、BIMI；主图先有明显下跌，随后反弹幅度较弱、量能/高度不足，再尝试向前低延续。Bear flag 的教学顺序应写成 `impulse down → weak bounce → lower high → support break`，而不是只因一根红 K 就追空。若反弹越过 flag high，short thesis 失效。

**复盘：** 记录 locate cost 和 fill；对比 bear flag 与 false-breakout short 的 MAE。

## v0185：NFEC squeeze halt

![NFEC halt 的旧版平台](../../assets/small-cap/live/v0185-01.jpg)

**图怎么看：**

- 源文件没有音轨，因此只保留屏幕可验证的 halt 结构。
- 价格进入近垂直走势，订单可能在 halt 时冻结。
- 与 v0173 可能是同一事件的不同剪辑。
- Halt 前盈利无法保证恢复后仍盈利。

**视频内容：** 旧版画面再次显示 NFEC 的同一类垂直 squeeze、暂停附近报价与订单列表，且没有音轨可提供新的口述背景。它的用途是补充观察 pause 前后的 UI 状态，不是增加一个策略案例；任何 entry/exit 意图都不能从静态界面反向编造。

**复盘：** 去重后只保留一条 event；记录每次 halt/resume，而不是把整段当连续 K。

## v0186：BPTH 47→72 squeeze

![BPTH 高价 parabolic squeeze](../../assets/small-cap/live/v0186-01.jpg)

**图怎么看：**

- 每股移动约 25 美元，使用普通 small-cap share size 会造成灾难性风险。
- 图中高点与低点之间的 spread/halts 未被静态图表达。
- “Watch” 案例不代表一定实际成交到完整 move。

**视频内容：** BPTH 与 ALT、GTXI 等同时可见，BPTH 主图从约 `$47` 区域向 `$72` 方向形成多段近乎垂直的推进；高价使一档跳动就对应很大的 dollar risk。视频标题是 watch/squeeze 定位，不能假设讲者从起点持有到终点；学习时应只记录可验证的 halt、pullback 和恢复结构，并用实际 fills 判断参与区间。

**复盘：** 用最小单位和 max gap stress 评估；无法承受一次 5–10 美元 resume gap 就不交易。

## 本组结论

- Long→short 需要全新 thesis；
- “赚回来”不是 setup；
- 同一事件多剪辑必须去重；
- News 保存原始来源和 latency；
- 高价/parabolic 按 dollar risk，不按惯用 shares；
- Rule-following loss 可以是好决策，winner 也可能是坏决策。
