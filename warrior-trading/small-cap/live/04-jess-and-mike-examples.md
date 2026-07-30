# Live Review 04：Jess and Mike Examples

> 对应视频：v0139–v0142，共 4 段
> 重点：使用 broker statement 对账、把高速 momentum 与 large-cap/VIAC 这类较慢走势分开。

## v0139：Jess live trading 与成交对账

![Chart、成交列表与 broker statement](../../assets/small-cap/live/v0139-01.jpg)

**图怎么看：**

- 左侧 chart 标出 entry/exit，右侧是详细成交/账户记录。
- Chart 标记必须由真实 fills 生成，不能用理想 candle price 代替。
- 多次 partial fill 应计算加权平均，而不是挑最好的一笔。
- Statement 可能包含 account identifiers；公开资料需脱敏，但本图未保留可登录凭据。

**视频内容：** 画面将 TD Ameritrade 图表中的买卖标记与浏览器里的成交/账户记录并列，正好展示“图上理想位置”和 broker 实际 fills 的差别。学习时要从 statement 逐笔重建：同方向 partial fills 合并成加权均价，反向成交决定真实退出，手续费从 gross 中扣除，再把这些时间点贴回 K 线；不能先在图上画漂亮箭头再找订单支持。

**复盘：** 以 statement 为 source of truth，重算 gross、fees、net、shares、hold time 和 slippage。

## v0140：Jess intermediate / CREG

![CREG 多周期与 Level 2 交易](../../assets/small-cap/live/v0140-01.jpg)

**图怎么看：**

- CREG 短周期上行并在高位整理，旁边是 depth 和 prints。
- Momentum 已经扩张后，entry 需要 pullback/flat-top 结构，不能只因涨幅榜排名。
- 图中多周期来自同一价格，不能算多个独立确认。
- Intermediate 的真正门槛是能处理 partial fill、false break 与 changing spread。

**视频内容：** CREG 的 1 分钟图在开盘直线上冲后形成高位窄平台，5 分钟图则把这段动作压缩成更少的 K 线；Level 2/Time & Sales 用来观察突破时是否真正成交。Intermediate 的学习点是等待平台 high 被接受、用平台 low 做 invalidation，并在突破没有立即延续时处理 partial exit，而不是因为两个周期都绿色就直接加仓。

**复盘：** 标出第几次 pullback、到 VWAP/日线阻力的距离，以及 breakout 后接受时间。

## v0141：Mike 多标的 large-cap 观察

![Mike 的四图工作区与盘口](../../assets/small-cap/live/v0141-01.jpg)

**图怎么看：**

- 多个 large-cap chart 同时显示，走势幅度比低 float momentum 更慢。
- 多标的同时打开会产生 market/sector correlation；并非四个独立机会。
- 先选 primary candidate，再把其他图作为 relative-strength 参照。
- 高频切换 symbol 增加错单风险。

**视频内容：** 工作区同时显示 TWTR、FB、ROKU、AAPL/相关 large-cap 图和 VIAC 盘口，目的是对比市场与个股，而不是同时做四笔。正确流程是先选 primary ticker，其他图只回答“板块是否同步、谁更强/更弱”；真正下单前还要再次确认 active symbol、account、shares 和 order type，防止多屏切换把观察对象变成误单。

**复盘：** 对每笔记录 market、sector、relative strength 与当前激活窗口；设 symbol confirmation。

## v0142：VIAC 约 1k 案例

![VIAC 趋势与关键水平](../../assets/small-cap/live/v0142-01.jpg)

**图怎么看：**

- 源视频音轨是数字静音，因此本段只按可见图表、文件标题和可验证市场结构整理，不补写讲者意图。
- 图中价格沿均线/水平位移动，属于相对更慢的 trend/level trade。
- 标题金额不说明风险；`$1k` 对不同 account/size 含义完全不同。
- VIAC/公司事件与 sector context 应在入场前核验。
- Large-cap 也会因 headline 发生 gap，不能只依赖技术线。

**视频内容：** 无声画面仍能确认 VIAC 的盘口与多周期走势：价格先发生快速向下跳动，之后在低位缓慢横盘/继续走弱，右侧较长周期提供更大趋势背景。因为缺少口述，不能声称讲者为何买卖；能学习的是如何用订单簿、关键水平和 slower trend 复盘，并明确把未知的 entry/exit 理由留空。

**复盘：** 用 R multiple、notional、MAE/MFE 代替金额比较，避免被受访者 P&L 误导。

## 共同结论

- Statement 优先于手画标记；
- Jess 的 small-cap speed 与 Mike 的 large-cap 节奏分开；
- 多屏不等于多 edge；
- 金额标题全部换算成 planned/realized R；
- 每个 workspace 都要防 symbol/account 错误。
