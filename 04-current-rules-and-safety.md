# 当前规则与安全边界

> 核对日期：2026-07-30  
> 用途：把视频中的教学案例与当前仍需自行确认的规则、平台功能和风险分开。

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

FINRA 当前的投资者页面将日内交易定义为：在保证金账户中，于同一天买卖或卖空后买回同一证券，以尝试从小幅价格变化中获利。

截至本次核对日期，FINRA 页面仍说明了 Pattern Day Trader 的认定和 25,000 美元最低权益等要求，但规则提案、券商内部要求和账户处理方式都可能变化。不要只根据本课程或网上旧文章决定账户操作，应在实际交易前查看：

- [FINRA：Day Trading](https://www.finra.org/investors/investing/investment-products/stocks/day-trading)
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
- 恢复后可能直接跳空；
- 因此，仓位必须在进入暂停前就考虑最坏情况。

## 4. 做空、Locate 与 Credit

做空不是“先点 Sell，之后再说”。对于不容易借到的股票，券商通常需要先完成 Locate。FINRA 对做空的基础解释是：投资者通过保证金账户卖出自己并不持有的股票，券商会在执行前寻找可交割的股票：

- [FINRA：Short Interest — What It Is, What It Is Not](https://www.finra.org/investors/insights/short-interest)

TradeZero 当前资料将 Locate 描述为当日做空借股预留；其产品还可能区分 Locate、Pre-Borrow 和 Single Use。是否能把未使用的 Locate 标记为 Credit、能退回多少费用、何时失去资格，都取决于 Locate 类型和实际使用情况：

- [TradeZero：Short Selling Tools & Locates](https://tradezero.com/en-us/locates)
- [TradeZero Developer Portal：Short Locates](https://developer.tradezero.com/docs/documentation/locates)

因此，第 6 课中的界面和价格只能用于学习概念。实际操作时，应逐项确认：

1. 当前股票是否 Easy to Borrow；
2. Locate 报价是每股还是总价；
3. 购买的是哪一种 Locate 类型；
4. 已使用和未使用的库存分别是多少；
5. Credit 是否需要其他用户接手，是否保证成交；
6. 隔夜借股费、强制回补和库存召回规则。

## 5. Hotkey 和自动订单

第 7 课保留了视频中的 DAS Hotkey 模板，是为了忠实记录课程，而不是鼓励直接复制到真实账户。

DAS 当前官方帮助明确说明：

- 部分命令区分大小写；
- Hotkey Script Builder 提供当前可用命令；
- 示例脚本需要按账户、路由和订单类型调整；
- 使用前应先测试，确认它完全符合预期。

资料入口：

- [DAS：How do I use hotkeys?](https://dastrader.com/docs/how-do-i-use-hotkeys/)
- [DAS：User Guide and Manuals](https://dastrader.com/docs/das-user-guide-and-manuals/)

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

## 7. 本资料的使用原则

1. 先学会描述发生了什么，再判断是否要交易；
2. 任何入场都必须先定义最大可承受损失；
3. 使用暂停策略时，把“无法退出”计入仓位；
4. 不把个人胜率、单次盈利或幸运脱困当作未来保证；
5. 所有自动订单先在模拟账户测试；
6. 真实规则以监管机构、交易所、券商和平台的当前文件为准。

本资料只用于课程整理和交易教育，不构成投资建议，也不保证任何策略能盈利。

