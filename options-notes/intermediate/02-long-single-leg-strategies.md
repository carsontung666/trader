# 中级 02：Long Option、LEAPS 与 Protective Put

> 覆盖视频：中级第 9–13 讲  
> 本章时长：约 54 分钟

## 第 9 讲：学策略前先统一分析方法

![策略不是死记名称](<../assets/intermediate/chapter-02-long-single-leg-strategies/lesson-09/frame-01-0108s.jpg>)

**图怎么看：**

- 策略名称只是若干腿的简称；
- 真正要掌握的是每条腿的现金流、Greeks 和到期义务；
- 同一个收益图可以由不同组合合成，但资本占用和提前指派并不一定相同；
- 不存在跨市场环境“永远最好”的策略。

每学一个策略，都按同一模板记录：

1. 市场观点：方向、幅度、时间、波动率；
2. 到期 payoff 与盈亏平衡点；
3. 最大利润、最大亏损和指派义务；
4. Delta、Gamma、Theta、Vega；
5. 开仓、止损、止盈和到期处理；
6. 流动性、保证金、股息和事件风险。

## 第 10 讲：单腿买 Call / Put

Long Call 用于看涨，Long Put 用于看跌。它们的共同特点：

- 最大亏损为支付的全部权利金；
- Long Gamma、Long Vega、通常为负 Theta；
- 方向判断正确仍可能因时间和 IV 变化亏损；
- 盈亏按权利金的百分比波动很大。

![Long Option 的 Vega 敞口](<../assets/intermediate/chapter-02-long-single-leg-strategies/lesson-10/frame-01-0252s.jpg>)

**图怎么看：**

- 图中 Put 在股价下跌时同时受 Delta 和 IV 上升推动；
- 这只是特定行情组合，不是“股价跌，IV 必涨”的定律；
- Long Option 的 Vega 为正，但买入时若 IV 已很高，后续 IV 回落会造成损失；
- 方向、速度和开仓时 IV 必须一起判断。

### 到期日怎么选

课程偏好买 1–1.5 个月到期、持有 1–2 周。这是讲师的操作习惯，不是普遍最优参数。

![课程对到期日选择的取舍](<../assets/intermediate/chapter-02-long-single-leg-strategies/lesson-10/frame-02-0550s.jpg>)

**图怎么看：**

- 短期限通常权利金较低，但 Theta 和 Gamma 更集中；
- 长期限 Theta 每日占权利金比例通常较低，但 Vega 和总成本更大；
- 选择期限应覆盖观点兑现所需时间，并给判断误差留缓冲；
- 用情景分析比较“标的移动 + IV 变化 + 时间经过”，不能只比较单个 Greek。

### Strike 怎么选

- Deep OTM：成本低、Delta 小、归零概率高；
- ATM：方向敏感度与时间价值都较高；
- ITM：Delta 更高、内在价值占比更大，但本金更多。

课程提出避免 Delta 小于 0.30 的 OTM 合约，可作为防止“彩票化”的个人纪律，但不是风险边界。真正边界是：亏掉全部权利金时，对总账户影响是否可接受。

![单腿买方的三个核心问题](<../assets/intermediate/chapter-02-long-single-leg-strategies/lesson-10/frame-03-0772s.jpg>)

**图怎么看：**

- 方向观点要足够明确，但“强烈相信”不能代替概率和赔率；
- 持有多久应在开仓前定义；
- IV 是否便宜要和同一标的自身历史、期限结构及事件比较；
- 盈利后换成更便宜的 OTM 合约，只是取回部分本金，同时会降低 Delta、提高归零概率，不是“用利润免费赌”。

## 第 11 讲：Deep ITM LEAPS Call

LEAPS 通常指距离到期一年以上的长期上市期权。Deep ITM LEAPS Call 常被用作股票替代，因为：

- Delta 可能接近 1；
- 大部分权利金是内在价值；
- 投入现金少于购买 100 股；
- 最大损失限于权利金。

![Deep ITM LEAPS 的内在价值与 Delta](<../assets/intermediate/chapter-02-long-single-leg-strategies/lesson-11/frame-01-0257s.jpg>)

**图怎么看：**

- 示例中 Strike 60、股价约 154，Call 的大量价格来自内在价值；
- Delta 0.982 表示当前小幅股价变化时近似 98.2 股敞口；
- 它不是永久保持 0.982，股价下跌或期限缩短后会变化；
- 与股票相比，没有投票权，通常不收股息，并且有到期日。

### 与融资买股的比较

LEAPS 把最大美元损失锁在权利金内，不会因该 Long Call 本身产生追加保证金；融资买股则可能遇到动态保证金和强平。但不能因此说 LEAPS “完全消除尾部风险”：

- 权利金可能 100% 归零；
- 高杠杆使账户百分比损失更快；
- 到期前若观点未兑现，必须退出或滚仓；
- 宽 Bid–Ask 会造成明显隐性成本；
- Deep ITM Call 在除息前还可能涉及提前行权判断。

![LEAPS 与 Margin 的风险对比](<../assets/intermediate/chapter-02-long-single-leg-strategies/lesson-11/frame-02-0504s.jpg>)

**图怎么看：**

- 左侧突出 Long Call 无追加保证金，右侧突出融资头寸可能被强平；
- 比较必须使用相同的实际 Delta 或相同美元敞口；
- “风险更小”取决于用省下的现金做什么；若再建立更多头寸，账户总风险可能更高；
- 课程使用的 2% 融资利率只是历史例子，不能继续沿用。

### 成本怎么估

不能把当前一天的 Theta 直接乘 365，当成一年的精确成本，因为 Theta 会随股价、IV 和期限改变。更直接的方法是：

\[
\text{Extrinsic Value}=\text{Call Premium}-\max(S_0-K,0)
\]

再同时评估：

- 放弃的股息；
- 行权资金的隐含融资；
- Bid–Ask；
- 手续费；
- 滚仓成本；
- 税务差异。

![选择更深 ITM 以减少外在价值](<../assets/intermediate/chapter-02-long-single-leg-strategies/lesson-11/frame-03-0741s.jpg>)

**图怎么看：**

- Strike 越低，Delta 通常越高、外在价值占比越低；
- 但支付的绝对权利金也越大，杠杆随之降低；
- 期限很长的合约可能报价稀疏，必须使用限价单；
- 最低成本不是唯一目标，还要保证退出时有可执行流动性。

## 第 12 讲：Protective Put

Protective Put = 100 股股票 + 1 张 Long Put。设买股价 \(S_0\)、Put Strike \(K\)、权利金 \(p\)：

- 到期最低组合价值：\(100K\)；
- 最大亏损：\(100(S_0-K+p)\)；
- 盈亏平衡点：\(S_0+p\)；
- 上涨收益保留，但需先赚回权利金。

![ATM 与 OTM Protective Put 的成本](<../assets/intermediate/chapter-02-long-single-leg-strategies/lesson-12/frame-01-0313s.jpg>)

**图怎么看：**

- 450 Put 比 440 Put 贵，但保护从更高位置开始；
- 低 Strike 不是同样保险的折扣版，而是提高了自留损失；
- OTM Put 最大亏损包含 `股价到 Strike 的跌幅 + 权利金`；
- 保护是到期结构；到期前的市值对冲强度会随 Delta、IV 和时间改变。

### 用 Delta 看持有过程

100 股 Delta 为 +100。若买入一张 Delta -0.50 的 Put，组合初始 Delta 约 +50；若 Put Delta 为 -0.30，组合约 +70。

![Protective Put 的动态对冲强度](<../assets/intermediate/chapter-02-long-single-leg-strategies/lesson-12/frame-02-0601s.jpg>)

**图怎么看：**

- 股价下跌、Put 深入 ITM 时，Put Delta 的绝对值通常增大，组合 Delta 向零靠近；
- ATM Put 起始保护更强，OTM Put 的保护启动更晚；
- “弹簧”比喻只解释 Delta，实际价格还受 IV 和 Theta 影响；
- 股价跳空穿过 Strike 时，开盘成交与理论保护价值仍受流动性影响。

不要把一个月权利金简单年化为 12 倍后断言保险是否划算。Protective Put 的价值取决于尾部损失容忍度、事件窗口、相关性和替代减仓成本。

## 第 13 讲：降低 Protective Put 成本

### 方法一：在 IV 相对低时买保护

这是减少权利金的一种条件，但“IV 低往往等于市场高点”并不可靠。保护需求与期权价格之间仍需权衡，不能为了等便宜保险而暴露无法承受的风险。

### 方法二：Put Spread 保护

持股 + Long Put \(K_1\) + Short Put \(K_2\)，其中 \(K_1>K_2\)。

卖出低 Strike Put 降低成本，但只把 \(K_1\) 到 \(K_2\) 的下跌区间锁住；跌破 \(K_2\) 后，股票下行风险重新出现。

### 方法三：1×2 Put Ratio 结构

持股 + 1 张 Long Put \(K_1\) - 2 张 Short Put \(K_2\)。

它可能进一步降低成本，但跌破 \(K_2\) 后，两张 Short Put 会使下行风险快速放大，并可能增加保证金。课程把它作为普通“扩大保护区间”的方式，风险说明不够：这不是初学者默认应使用的低成本保险。

### 方法四：Collar

持股 + Long Put + Short Call。卖 Call 的权利金补贴 Put，同时牺牲 Strike 以上的上涨。

![用 Short Call 为 Protective Put 降低成本](<../assets/intermediate/chapter-02-long-single-leg-strategies/lesson-13/frame-01-0365s.jpg>)

**图怎么看：**

- 图中文字“再买 Call”是口误，Collar 的第三条腿应为卖出 Call；
- Put 划定下方保护，Call 划定上方封顶；
- 两者权利金接近时可能形成低净成本或 Zero-Cost Collar；
- “零成本”只指初始净权利金，仍有机会成本、交易成本和提前指派风险。

## 开仓前总检查

- [ ] 观点需要多久兑现，期限是否留出缓冲？
- [ ] 最大亏损是否按每张 100 股计算？
- [ ] Long Option 若归零，账户损失比例是多少？
- [ ] LEAPS 是否计入股息、外在价值和 Bid–Ask？
- [ ] Protective Put 的自留损失是多少？
- [ ] 降成本后，哪一段保护被交换掉？
- [ ] 是否误把 1×2 Ratio 结构当成 Defined Risk？
