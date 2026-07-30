# 日内交易：当前规则、平台差异与风险

> 核对日期：2026-07-30  
> 用途：核对视频录制后可能变化的监管规则、券商功能、平台行为与实盘风险。

## 1. 这套视频不是“当前规则说明书”

视频中出现了不同年份的录屏、旧版券商界面和个人经验参数。以下内容都可能随时间、券商、账户类型或软件版本变化：

- Pattern Day Trader（PDT）认定和保证金要求；
- 券商的可借股票库存、Locate 报价和 Credit 规则；
- DAS Trader 的订单路由、Hotkey 语法及券商支持范围；
- Level 2 的显示单位和盘口深度；
- 交易暂停后的恢复方式；
- 手续费、平台费、借股费和融资成本。

因此，本资料中的数字优先解释为“视频录制当时的案例”，真实交易前必须再次查看自己的券商协议和当前官方说明。

## 2. 日内交易和保证金风险

**2026 年已经发生重大变化。** FINRA 的新盘中保证金要求于 2026-06-04 生效，取代以交易次数认定 Pattern Day Trader 和统一要求 25,000 美元最低权益的旧框架。新框架按账户盘中实际风险检查足够权益；用于杠杆交易的最低权益通常仍为 2,000 美元，券商也可设更高要求。

但券商获准在 2027-10-20 前完成迁移。因此在当前过渡期：

- 已迁移券商不再以旧 PDT 交易次数和 25,000 美元门槛为核心；
- 尚未迁移的券商可能继续执行旧规则；
- 券商可以实时阻止会造成盘中保证金缺口的订单，也可能事后发出 deficit；
- 反复未及时补足盘中保证金缺口，账户可能被限制最多 90 天；
- 非美国券商实体、现金账户和不同产品还可能适用其他规则。

所以视频中“国际版无 PDT、美国版必须 25,000 美元”的陈述已经不能代表当前全部账户。开户或增加频率前直接向自己的券商确认采用哪套制度：

- [FINRA：Understanding the New Intraday Margin Requirements](https://syndication.finra.org/content/understanding-new-intraday-margin-requirements)
- [FINRA Rule 4210：Margin Requirements](https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210)

SEC 的风险提示强调，日内交易可能造成严重损失，杠杆还会放大亏损。生活费、应急资金、学费或退休资金不应被当作可承受损失的交易本金：

- [SEC：Day Trading — Your Dollars at Risk](https://www.sec.gov/about/reports-publications/investorpubsdaytipshtm)

## 3. 视频中的 “Halt” 是什么

课程中的 halt、halt up 和 halt down，主要是在美国市场个股短时间剧烈波动时出现的临时交易暂停。它不等于中国 A 股每日固定涨跌幅限制。

LULD（Limit Up–Limit Down）机制使用随市场更新的价格带，目的是避免 NMS 股票在常规交易时段成交于价格带之外。触发暂停后，所有交易场所的该股票交易都会暂时停止，恢复价格也可能与暂停前价格存在明显差异。

当前官方资料：

- [LULD Plan 官方概览](https://www.luldplan.com/)
- [NYSE：Trading Halts](https://www.nyse.com/trade/trading-halts)

对课程案例最重要的现实含义是：

- 暂停期间无法依靠普通卖单或止损单立即退出；
- 屏幕上的参考恢复价仍可能变化；
- 常见的 5 分钟不是恢复时间保证；重新开放的竞价和失衡可能延长暂停；
- 不同数据源可能在恢复瞬间短暂不同步；
- 恢复后可能直接跳空；
- 因此，仓位必须在进入暂停前就考虑最坏情况。

## 4. 做空、Locate 与 Credit

做空不是“先点 Sell，之后再说”。对于不容易借到的股票，券商通常需要先完成 Locate。FINRA 对做空的基础解释是：投资者通过保证金账户卖出自己并不持有的股票，券商会在执行前寻找可交割的股票：

- [FINRA：Short Interest — What It Is, What It Is Not](https://www.finra.org/investors/insights/short-interest)

TradeZero 当前资料说明，其工具会聚合 hard-to-borrow 库存、显示每股费用，并允许把不再需要的 locate 重新提供给其他客户，**可能**收回部分费用。是否能获得 Credit、能退回多少、何时失去资格，都取决于库存、Locate 类型和实际使用情况：

- [TradeZero：Active Trading and Locates](https://tradezero.com/en-us/active-trading)

因此，进阶第 6 课和基础第 9 课中的界面与价格只能用于学习概念。实际操作时，应逐项确认：

1. 当前股票是否 Easy to Borrow；
2. Locate 报价是每股还是总价；
3. 购买的是哪一种 Locate 类型；
4. 已使用和未使用的库存分别是多少；
5. Credit 是否需要其他用户接手，是否保证成交；
6. 隔夜借股费、强制回补和库存召回规则。

## 5. Hotkey 和自动订单

进阶第 7 课和基础第 3 课保留了视频中的 DAS Hotkey 逻辑，是为了理解订单流程，而不是鼓励直接复制到真实账户。

DAS 当前官方帮助明确说明：

- 部分命令区分大小写；
- Hotkey Script Builder 提供当前可用命令；
- 示例脚本需要按账户、路由和订单类型调整；
- 使用前应先测试，确认它完全符合预期。
- 同一功能通过不同 DAS broker、IBKR 或 Schwab 使用时，支持程度和订单路径可能不同。

资料入口：

- [DAS：How do I use hotkeys?](https://dastrader.com/docs/how-do-i-use-hotkeys/)
- [DAS：User Guide and Manuals](https://dastrader.com/docs/das-user-guide-and-manuals/)
- [DAS：Supported Functions by Broker](https://mirror.dastrader.com/docs/supported-functions-by-das-ib-and-td-ameritrade/)

至少应在模拟环境验证：

- 买卖方向是否正确；
- 数量使用固定值还是当前仓位；
- 是否可能反向开仓；
- Stop Market、Stop Limit、Range Order 的触发和成交行为；
- 部分成交后剩余订单如何处理；
- 断线、延迟或券商不支持某个命令时会发生什么。

## 6. Level 2 的安全边界

Level 2 展示的是可见订单，不是所有真实买卖意愿：

- 订单可以撤销或修改；
- 同一参与者可能分拆订单；
- 隐藏单无法完整显示；
- 显示大单不保证会成交；
- 快速行情中，画面可能已经落后于真实市场；
- 不同数据源和平台显示深度可能不同。

所以，第 4 课和第 9 课里的 Level 2 数字应理解为讲师在特定股票、特定时刻观察到的上下文信号，不能当作固定阈值。

## 7. Market、Limit、Stop 与 Stop-Limit

视频中的订单类型需要保留以下边界：

- **Market order** 优先争取执行，但不保证价格，也不保证在暂停期间或没有对手盘时成交；
- **Limit order** 限制最差价格，但不保证成交或全部成交；
- **Stop order** 达到触发条件后通常变为市价单，触发价不是保证成交价；
- **Stop-limit order** 触发后变为限价单，控制最差价格，但快速越过限价时可能无法退出；
- 券商可能用 last sale 或 quotation 等不同方式判断 stop 是否触发；
- 盘前盘后、暂停和特定路由支持的订单类型可能不同。

官方基础说明：

- [SEC：Trading Basics](https://www.sec.gov/file/trading101basicspdf)
- [SEC：Stop Order](https://www.sec.gov/answers/stopord.htm)

## 8. SSR / Regulation SHO Rule 201

Short Sale Restriction 不是“不能做空”。Rule 201 的核心是：

1. 上市市场确认股票在常规时段较前一常规时段收盘价下跌至少 10%；
2. 触发后，普通短卖单不能在当前 National Best Bid 或更低价格显示或执行；
3. 限制持续到触发日结束和下一交易日；
4. 若下一日再次下跌至少 10%，可以重新触发并继续延长；
5. 触发判定只发生在常规时段，但生效后可在存在持续 NBBO 的扩展时段适用；
6. 法规存在特定例外，普通交易者不应自行把订单标成 short exempt。

因此 SSR 可能改变短卖成交位置，却不保证股价上涨、制造 squeeze 或阻止继续下跌：

- [SEC：Rule 201 of Regulation SHO FAQ](https://www.sec.gov/rules-regulations/staff-guidance/trading-markets-frequently-asked-questions-7)

## 9. 盘前与盘后

美国股票常规时段通常为美东 09:30–16:00。券商和交易场所自行决定向客户开放多长的盘前、盘后或 overnight session，课程画面里的具体时间不是统一规则。

盘外时段的主要风险：

- 成交量与价格竞争较少；
- Spread 更宽、波动更大；
- 不同系统可能展示不同报价；
- 订单路由与最优执行处理可能不同；
- 很多券商只接受限价单；
- 未成交订单是否进入下一时段取决于 Time-in-Force。

资料入口：

- [SEC：After-Hours Trading Investor Bulletin](https://www.sec.gov/files/afterhourtrading.pdf)
- [DAS：Available Time-in-Force Values](https://dastrader.com/docs/what-tifs-are-available-on-das/)

## 10. Offering、IPO 与稀释

课程把 offering 简化成 IPO 后的“二次发行”，容易混淆：

- IPO 是公司股票第一次向公众发行；
- Primary offering 中公司发行新股并获得资金，可能稀释现有股东；
- Secondary offering/resale 可能由现有股东出售，出售所得归股东，不一定增加公司股本；
- 一次交易也可能同时包含 primary 与 secondary 部分；
- Shelf registration 只是建立未来发行能力，不一定等于当日已经完成出售；
- ATM、warrants 和可转债会带来不同的潜在供给。

看到 “offering” 时应打开注册声明、prospectus supplement 和定价公告，核对谁在卖、多少股、何时可售和谁取得款项，而不是只看新闻标题：

- [SEC：Registered Offering 定义](https://www.sec.gov/resources-small-businesses/glossary)
- [SEC：Investing in an IPO](https://www.sec.gov/file/ipo-investorbulletinpdf)

## 11. 本资料的使用原则

1. 先学会描述发生了什么，再判断是否要交易；
2. 任何入场都必须先定义最大可承受损失；
3. 使用暂停策略时，把“无法退出”计入仓位；
4. 不把个人胜率、单次盈利或幸运脱困当作未来保证；
5. 所有自动订单先在模拟账户测试；
6. 在过渡期内向自己的券商确认适用保证金制度；
7. 真实规则以监管机构、交易所、券商和平台的当前文件为准。

本资料只用于课程整理和交易教育，不构成投资建议，也不保证任何策略能盈利。
