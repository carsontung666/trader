# 第 8 课：股票同步（Leader–Laggard）策略

> 对应视频：`08-leader-laggard-strategy.mp4`  
> 视频时长：19:21  
> 核心问题：当多只股票受同一新闻或同一市场主题驱动时，怎样利用它们之间几秒到几分钟的反应差，观察先动的股票并交易尚未完全反应的股票？

## 配图阅读方法

实盘截图左右并排显示 GME 与 AMC，中间是 Level 2。每张图按固定顺序看：

1. 先确认左、右分别是哪只股票；
2. 比较两边 K 线的**相对时序**，不要比较绝对股价；
3. 找出谁先破 high / low，谁仍停在原区间；
4. 最后看被交易股票自己的 entry、support、resistance 和 stop。

静态截图无法完整表达几秒钟的先后关系，所以正文会说明前一刻发生了什么、截图时差异在哪里、随后哪一个条件让交易退出。

## 一、什么叫“股票同步”

若多只股票因为相同原因受到资金关注，它们的价格可能在一段时间内：

- 同方向上涨或下跌；
- 一只突破支撑后，其他股票随后跌破；
- 一只进入 volatility halt，其他股票立刻加速；
- 一只反弹后，另一只延迟几秒才跟随。

这类方法通常叫 **leader–laggard**：

- Leader：先给出方向信息的股票；
- Laggard：尚未完全反应、可能随后跟随的股票。

“Leader”和“laggard”不是永久身份。同一时段中，GME 可能先动；几分钟后 AMC 又可能成为先动的一只。

![图 8-1：股票同步与 Leader–Laggard 的基本概念，视频约 00:00](<assets/08-leader-laggard-strategy/frame_001.jpg>)

**图 8-1 怎么看：**

- 并不是两家公司基本面相同，而是同一主题让资金同时关注它们；
- 图中列出的“共同突破、共同暂停、共同上涨”都是可能关系，不是固定规则；
- Leader 只是当前几秒或几分钟先给出信息的一只；
- 如果两只股票后来不再反应，策略依据就消失。

## 二、为什么会有时间差

即使共同催化相同，每只股票仍有独立差异：

- Float；
- 股价；
- 成交量和 spread；
- 当时订单簿；
- 个股自己的 support/resistance；
- Volatility halt 的触发区间和暂停时间；
- Borrow availability；
- 不同交易者关注度。

因此，同步不意味着 K 线逐 tick 完全相同。可利用的正是短暂偏离：

`共同驱动仍有效 + 一只已移动 + 另一只尚未反应`

## 三、什么时候更容易同步

视频给出的典型环境：

- GME 与 AMC 受同一 meme-stock 主题推动；
- 同一行业受政策或新闻影响；
- 新闻刚发生的头几天；
- 开盘后成交量最高的时段；
- 出现大幅突破、flush 或 volatility halt 时。

后半天 volume 下降后，同步关系可能变弱，只在极端 K 线或 halt 附近短暂恢复。

讲师提到自己历史上使用该方法曾有 80%–90% 左右胜率。这是个人口头经验，不是本视频提供统计样本得出的可验证结果，不能据此自动扩大 size。

## 四、先确认“真同步”，不要只凭一对相似 K 线

盘前/盘中检查：

1. 两只股票是否有同一催化或清楚的共同主题？
2. 是否已连续出现多次同方向反应？
3. 谁先突破、谁后跟随，时间差是否相对稳定？
4. 当一只反向时，另一只是否也反向？
5. Volume 是否仍高？
6. 当前各自是否被独立 support/resistance 阻挡？

至少观察多次反应后，才把同步作为辅助优势。一次巧合不足以建立策略。

![图 8-2：视频对同步策略适用环境与局限的说明，视频约 01:40](<assets/08-leader-laggard-strategy/frame_006.jpg>)

**图 8-2 怎么看：**

- 视频强调开盘和高量阶段更常出现同步，后半天低量时关系变弱；
- 右侧示意图只展示一次相似运动，单次相似不能证明稳定关系；
- 讲师口述的 80%–90% 是个人经验，没有样本量、成本和失败交易明细；
- 因此这张图应被读成“何时值得观察”，不是策略胜率证明。

## 五、无 Halt 时的做空流程

假设已确认 AMC 与 GME 当天同步：

1. 两张相同 time frame 的图并排；
2. 标出两只股票各自的前 low / support；
3. 观察其中一只先接近破位；
4. 若另一只仍停在较高位置，它可能是 laggard；
5. 在 laggard 寻找更好的 short entry；
6. Leader 真正跌破后，等待 laggard 跟随；
7. Leader 假跌破或快速反弹，则立即 cover laggard；
8. Laggard 到达自己的 support 后，不应只因为 leader 还弱就无限持有。

### 关键原则

Leader 提供方向线索，但实际交易的股票仍有自己的：

- Entry；
- Stop；
- Support/resistance；
- Liquidity；
- Risk/reward。

不能用 GME 的图替 AMC 设置所有价格。

![图 8-3：无暂停时的同步 Short 操作流程，视频约 03:00](<assets/08-leader-laggard-strategy/frame_010.jpg>)

**图 8-3 怎么看：**

- 并排图先确认两只股票确实在同方向运动；
- Leader 先接近或跌破自己的 low，laggard 仍较高时才出现时间差；
- 做空的是 laggard，因此 entry、stop 和 cover 都必须落在 laggard 自己的图上；
- Leader 如果假跌破并快速收回，应立即重新评估，而不是等待 laggard 替自己证明判断。

## 六、无 Halt 时的做多流程

把上述逻辑反过来：

1. Leader 先突破 high 或从 support 反弹；
2. Laggard 尚未上涨；
3. 在 laggard 上寻找 long；
4. Leader 继续上涨，支持持有；
5. Leader 失败/回落，立即重新评估；
6. Laggard 接近自己的 resistance 时止盈。

这不是看到 leader 涨就无条件 market buy laggard；必须确认时间差尚未被套利完、且 laggard 的进场位置仍有合理 stop。

## 七、有 Volatility Halt 时

视频中的“涨停/跌停”指美国个股因剧烈波动触发的 volatility halt / LULD pause 语境，不是中国市场整日固定涨跌幅限制。

### 为什么 Halt 会产生更长时间差

- 股票 A 已暂停，价格暂时不更新；
- 股票 B 仍在正常交易，继续吸收共同信息；
- A resume 时，可能一次性重估到新价格；
- 两只股票的暂停先后和区间不同，时间差可从几秒扩大到几分钟。

### 视频的操作逻辑

假设：

- GME 先 halt up；
- 随后 AMC 冲高失败并 halt down；
- 共同主题仍然成立。

此时 AMC 的弱势为仍在 halt 的 GME 提供新的负面信息。GME resume 时可能向下重估。视频演示提前准备 short market order，在 resume 时成交。

### 这一做法的额外风险

Halt resume 的第一笔成交可能：

- 大幅 gap；
- Spread 极宽；
- Fill 远离预期；
- 再次立刻 halt；
- Market order 出现极端 slippage。

因此，课程案例应当理解为“同步信息如何传递”，而不是鼓励不加限制地在 resume 前放大 market order。

## 八、GME / AMC 实战案例一：反复交易短暂偏离（05:00–08:50）

### Trade 1：GME 先走弱，Short AMC

- GME K 线先表现较弱；
- AMC 仍在较高位置；
- 讲师 short AMC，预期其跟随 GME；
- GME 跌破前 low，AMC 随后下跌；
- GME 接近 halt-down level 但没有真正进入，出现“假跌停”；
- 讲师担心 leader 反弹，马上 cover AMC。

这里的 exit 并不等 AMC 自己完全反转，而是 leader 的弱势信号失效。

![图 8-4：第一轮 GME 先走弱、AMC 尚未完全跟随，视频约 05:00](<assets/08-leader-laggard-strategy/frame_016.jpg>)

**图 8-4 怎么看：**

- 两侧图表处在同一时段，左侧先出现更明确的向下 K；
- 另一只仍停在相对较高位置，形成可以尝试的 lag；
- 中间 Level 2 是执行工具，不负责证明两股相关；
- 如果先跌的一侧马上反弹，这个时间差可能不是机会，而是同步关系已经失败。

### Trade 2：GME 再次 Flush，Short AMC 2,000 股

- GME 又一波 flush 接近 halt-down level；
- 讲师在 AMC short 2,000 股；
- AMC 迅速跟跌；
- GME 再次未能真正 halt，出现反弹；
- AMC short 随即 cover。

![图 8-5：GME 第二次 Flush 后 AMC 跟跌，视频约 07:00](<assets/08-leader-laggard-strategy/frame_022.jpg>)

**图 8-5 怎么看：**

- GME 先出现新的快速下跌，给出方向信息；
- AMC 随后补跌，说明这一次 lag 很短；
- 一旦 GME 在 halt-down 附近没有继续并反弹，继续持有 AMC short 的原始理由变弱；
- 这里的 cover 是根据信息源失效，不是等 AMC 自己走出完整反转结构。

### Trade 3：GME 反弹、AMC 仍下跌，Long AMC

- GME 已经反弹；
- AMC 尚未跟随，出现短暂 divergence；
- 讲师 long AMC，预期它补涨；
- GME 的反弹没有继续加强，AMC 又接近 $9.50 resistance；
- 讲师先卖出；
- AMC 随后确实跟涨，但课程强调“错过后续无所谓”，不为卖早而追单。

![图 8-6：GME 与 AMC 并排观察的标准布局，视频约 05:20](<assets/08-leader-laggard-strategy/frame_017.jpg>)

**图 8-6 怎么看：**

- 两张图必须使用相同或可比较的 time frame；
- 纵轴绝对价格不同，所以比较的是拐点出现顺序，不是蜡烛高度；
- 中间盘口可以帮助执行，但主要信号来自左右价格结构；
- 最好在复盘记录中写明“Leader 先动几秒、Laggard 入场时距自身支撑多远”。

## 九、实战案例二：AMC 先 Flush，Short GME（08:53–11:34）

背景：

- GME 接近 $50 whole-dollar resistance；
- 讲师本来就在找 short；
- AMC 突然出现 false breakout 后下跌；
- AMC 与仍较高的 GME 出现不同步。

执行：

1. AMC 准备跌破前 low；
2. 讲师在 GME 尝试 short 1,000 股，实际 fill 900 股；
3. AMC 先 flush；
4. GME 随后跟跌；
5. AMC 接近 halt-down level；
6. GME 自身 halt level 仍在更低的约 $47；
7. 讲师在 GME 接近 $47.50 时先 cover；
8. 随后 GME 反弹。

这里有三层依据：

- 共同主题同步；
- AMC 的领先弱势；
- GME 自己的 $50 resistance。

多重依据比单纯看到 AMC 下跌更有意义。

![图 8-7：AMC 先 Flush，GME 仍在较高位置，视频约 09:00](<assets/08-leader-laggard-strategy/frame_028.jpg>)

**图 8-7 怎么看：**

- AMC 已经向下扩张，GME 尚未完成同等幅度的下跌；
- GME 同时接近自己的 $50 whole-dollar resistance，使 short 不只依赖相关性；
- 讲师实际只成交 900 股，说明预设数量与真实 fill 可能不同；
- Cover 仍要参考 GME 自己约 $47.50 的位置，而不能只等 AMC 继续下跌。

## 十、实战案例三：Leader 暂停时先观望（11:35–13:10）

AMC 已在 halt 中，没有继续更新的信息。讲师没有强行交易 GME，而是：

1. 等 AMC resume；
2. 观察 GME 在等待期间没有继续破 low；
3. AMC resume 后尝试 dip buy；
4. AMC 反弹后先卖；
5. 看到 AMC 已走强、GME 仍在低位，再观察 GME 的 $49 breakout；
6. 实际突破发生时 risk/reward 已变差，因此没有追。

这个片段很重要：同步策略也包含“不交易”。当信息源暂停或 entry 已经太迟，优势可能不存在。

![图 8-8：Leader 暂停期间另一只股票缺少新方向信息，视频约 11:00](<assets/08-leader-laggard-strategy/frame_034.jpg>)

**图 8-8 怎么看：**

- 一只股票进入 halt 后，屏幕不再产生连续成交，不能继续当实时 leader；
- 另一只没有立即破 low，说明等待期间并未确认弱势延续；
- 此时强行用停牌前最后一根 K 推断未来，等于把旧信息重复使用；
- 讲师选择等待 resume，是同步策略中的有效“空仓状态”。

## 十一、实战案例四：差一点被 Stop 的 Short（13:19–14:55）

- GME 开始下跌；
- 讲师随后 short AMC；
- 但 AMC 已经先跌了一段，entry 较差；
- AMC 附近又有 support；
- 若 GME 反弹或 AMC 突破前一根 K 顶部，计划 stop；
- GME 继续跌破，AMC 最终同步破 low；
- 讲师 cover。

课程明确承认这不是理想 entry。同步方向正确不代表任何位置都能下单；追得太低会让 risk/reward 变差。

![图 8-9：方向判断正确但入场靠近支撑，视频约 13:40](<assets/08-leader-laggard-strategy/frame_042.jpg>)

**图 8-9 怎么看：**

- Leader 已经先跌，但被交易股票也已经走过一段；
- 距离自身 support 越近，可继续下跌的空间越小，而止损可能仍要放在上一根 K 顶部；
- 这会让 reward 缩小、risk 不变；
- 因此“它大概率会跟”与“现在还有好位置”必须分开判断。

## 十二、实战案例五：Halt Resume（14:58–16:55）

- AMC 先出现 false breakout 并 halt down；
- GME 同时处于 halt up；
- 讲师在 GME 准备 1,000 股 short market order；
- GME resume 后成交并迅速下跌；
- 接近 halt-down level 时，Level 2 的挂单减少，像是假跌停；
- 为防反弹，讲师 cover；
- 之后订单又补回，GME 最终真的 halt down。

卖早不等于错误。讲师当时面对的信息是“可能假跌停并立即反弹”，cover 是风险决策；后面继续跌是事后结果。

![图 8-10：一只 Halt Down、另一只 Halt Up 后的 Resume 交易，视频约 15:00](<assets/08-leader-laggard-strategy/frame_046.jpg>)

**图 8-10 怎么看：**

- 左右股票在暂停前给出相反的短时状态，形成重新定价风险；
- AMC 的向下信息被用来推测 GME resume 后可能走弱；
- 但 resume 第一笔可能跳空，market order 的实际成交价不可控；
- 这张盈利案例没有展示所有可能的坏 fill，因此暂停交易应单独降仓，不能按普通同步交易估算风险。

## 十三、实战案例六：等待新 K，避免在低位追空（17:07–19:15）

- 两只股票都在 downtrend、接近 EMA 20；
- AMC 先跌；
- GME 已在当前 K 的较低位置，直接 short 容易遇到下一根回拉；
- 讲师等新 K 出现、价格稍反弹后再找 short；
- Stop 放在前一根 K 顶部；
- AMC 跌破前 low，GME 随后跌破约 $36.50；
- 当 AMC 开始反弹时，讲师 cover GME。

这再次说明：leader 给方向，entry 仍由 laggard 的自身结构决定。

![图 8-11：等待新 K 反弹后再 Short，避免在低位追单，视频约 17:00](<assets/08-leader-laggard-strategy/frame_052.jpg>)

**图 8-11 怎么看：**

- 两只股票都已处于 downtrend，直接在长红 K 底部追空容易遇到回拉；
- 讲师等待新 K、价格稍反弹，再用前一根 K 顶部定义 stop；
- Leader 后续跌破前 low 才继续支持持仓；
- 这个等待改善的是 entry 位置，不是改变相关性本身。

![图 8-12：AMC 开始反弹后 Cover GME，视频约 19:00](<assets/08-leader-laggard-strategy/frame_058.jpg>)

**图 8-12 怎么看：**

- Leader 的下跌没有继续，开始出现反弹；
- 即使 GME 仍可能再次走低，原始同步 short 的即时优势已经下降；
- Cover 是对入场依据的对称处理：用 leader 进入，也用 leader 的失效离开；
- 复盘不能因为后来可能继续下跌，就把当时按计划退出评价为错误。

## 十四、策略失效条件

出现以下情况时，不应继续假设同步：

- 共同新闻影响已经衰减；
- 一只出现新的个股独立新闻；
- Volume 明显下降；
- 两只股票连续多次不再互相跟随；
- Leader 自己的 breakout/breakdown 失败；
- Laggard 被强 support/resistance 阻挡；
- 一只流动性、borrow 或 halt 状态完全改变；
- 时间差已经消失，追入后 risk/reward 很差。

## 十五、风险管理

### 1. 不因口头胜率扩大仓位

个人案例的 80%–90% 不是可迁移保证。自己的 size 必须来自：

`最大允许亏损 ÷ 每股 stop 距离`

### 2. 同步不是对冲

只交易 laggard 仍承担完整方向风险；即使同时交易两只，也可能在相关性突然断裂时两边都亏。

### 3. Leader 失效就处理

若 entry 的主要理由是 leader 破位，leader 迅速收回时，不能继续持有并改口说“laggard 自己看起来还会跌”。

### 4. Halt 风险单独降仓

Resume、market order 和连续 halt 都增加无法控制 fill 的风险。

## 十六、实战检查表

- [ ] 两只股票确实共享同一催化；
- [ ] 已观察到不止一次同步；
- [ ] 当前谁是 leader，谁是 laggard；
- [ ] Leader 的确认 level；
- [ ] Laggard 的 entry、stop、target；
- [ ] Laggard 自己是否临近 support/resistance；
- [ ] 当前同步是否仍处于高量时段；
- [ ] Halt 时是否接受 gap/slippage；
- [ ] Leader 失败后立即退出的规则；
- [ ] Position size 没有因“感觉胜率高”失控。

## 十七、复习题

1. 为什么 leader 与 laggard 的身份会改变？
2. 无 halt 时，leader 假跌破后应该怎样处理 laggard short？
3. 为什么 halt 会把几秒的反应差扩大到几分钟？
4. 共同方向判断正确，为什么 entry 仍可能很差？
5. 为什么个人口头胜率不能直接用来放大 position size？

### 答案摘要

1. 每只股票独立的订单流、流动性和技术位不断变化，谁先动也会变化。
2. 同步依据失效，应快速 cover/重新评估。
3. 一只暂停不更新，另一只继续吸收信息；resume 时才集中重定价。
4. Laggard 可能已移动、临近自身 support，导致 stop 远、目标近。
5. 没有样本量、定义和成本统计，无法证明可重复性，也不一定适合另一个交易者。

## 十八、一句话总结

**股票同步不是“看到 A 跌就追空 B”，而是先证明共同驱动仍在，再用先动股票确认方向，同时只在后动股票自身仍有清楚 entry、stop 和空间时交易。**
