# 附录 A 当前规则核对

> 核对日期：2026-08-26。下面是对照监管/交易所**公开投资者材料**后的摘要，不是法律意见，也不是你券商的内部手册。开户、加仓、做空、到期前，读券商协议和原文。

课程笔记里的界面、佣金、PDT 口诀、halt 时钟和「国际版没有规则」都可能过时。**冲突时以本附录链接的官方文本为准，不以视频为准。**

---

## 1. 日内交易风险（SEC）

[SEC：Day Trading — Your Dollars at Risk](https://www.sec.gov/about/reports-publications/investorpubsdaytipshtm)（文首日期 2005，风险结论仍被 SEC 挂着）：

- 合法，但可能严重亏损；
- 不要用生活费、退休金、学费；
- 不要信轻松盈利的广告；
- 教你交易的人，可能在你开户后获利。

这比任何课程的收益案例优先。

---

## 2. 保证金与 PDT → 盘中保证金（FINRA，2026）

FINRA 投资者说明：[Understanding the New Intraday Margin Requirements](https://syndication.finra.org/content/understanding-new-intraday-margin-requirements)（同一内容也在 finra.org 投资者栏目）。规则文本：[Rule 4210](https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210)。

公开要点（2026-08 核对）：

| 项 | 官方说法 |
|---|---|
| 生效 | **2026-06-04**；券商可迁到 **2027-10-20** |
| 旧 PDT | 按交易次数贴「Pattern Day Trader」标签，并常要求约 **25,000 美元**最低权益 |
| 新框架 | **不再**用数日内笔数贴 PDT 标签；**取消** 25,000 美元作为日内最低权益门槛 |
| 改成什么 | 盘中权益要覆盖未平仓位的风险；不够就是 intraday margin deficit，应尽快补足 |
| 反复不补 | 投资者材料写：可能被限制最多约 **90 天**。不是「第一次缺口就锁死整个账户」。细则、何时起算、限制范围（例如是否禁止新增借方/空头）以 Rule 4210 和券商执行为准 |
| 杠杆最低权益 | 用杠杆做保证金交易，最低权益通常仍是 **2,000 美元**；不到 2,000 时，材料写可以在保证金账户里用自有现金做无杠杆交易，仍以券商为准 |
| 维持保证金 | 材料把盘中维持保证金的基准之一写成多头保证金股票市值的 **25%**；券商可以更高。空头、期权、低价股、集中仓通常是**另一套**数字，不要把 25% 套到所有仓位 |
| 0DTE | 新要求通常覆盖保证金账户当天的活动，包括 0DTE 用到的保证金 |
| 券商怎么执行 | 可以实时挡住会造成缺口的订单，也可以盘后追缴，或两者都用 |

过渡期内：已迁移走新规则，未迁移可能仍走旧 PDT。同一品牌的美国实体与国际实体可以完全不同。**问自己的券商，不要背视频。**

旧 PDT 的完整口径（只用于读旧课）：五个营业日内 **四次或以上**日内交易，且日内交易超过同期总交易的 **6%**，才可能被标 PDT。视频里常漏掉 6%。

---

## 3. 结算：T+1（SEC，2024-05-28）

SEC 2023-29：[缩短标准结算周期的最终规则](https://www.sec.gov/newsroom/press-releases/2023-29)。合规日 **2024-05-28**：多数经纪商证券交易从 T+2 改为 **T+1**。

部分 SEC 旧文（含 Regulation SHO 投资者概述）仍写 T+2。读机制时有用，读结算日时以 2024 年规则为准。

期权、部分国债、基金产品的结算周期本来就可以不同。现金账户用未结算资金再买、再卖，可能触发 good faith violation / freeriding；名称和处罚以券商为准。

---

## 4. LULD / 停牌（LULD Plan）

原文：[luldplan.com](https://www.luldplan.com/)。2012 试点，2019-04-11 起为常设计划。适用于常规时段美东 **09:30–16:00** 的 NMS 股票（权证等除外）。

机制（计划概述）：

- Reference Price ≈ 此前约五分钟合格成交的算术均价；
- 价格带 = 参考价 ±（参考价 × 百分比参数），四舍五入到分；
- 碰到带子：报价可被标成不可执行；进入 **Limit State**；
- 约 **15 秒**内若无法离开 Limit State，主上市交易所可宣布约 **5 分钟** Trading Pause，还可以再延约 5 分钟；
- **最后 10 分钟**若仍在 Trading Pause：主交易所**不再**重开到连续交易，改走**收盘程序**。这不是「今天再也没有价格」。

官方页上的举例：Tier 1、前收 **25 美元** → 上沿 26.25、下沿 23.75，即 **±5%**。其它价格区间和 Tier 2 的百分比不同；临近收盘（材料写常规时段最后约 25 分钟）部分证券的带子会加倍。**课程里的旧静态表不要背。** 下单看实时 band 和官方 halt feed。

LULD 不是 A 股每日固定涨跌停。新闻停牌（T1/T2 等）是另一套时钟，不要拿五分钟去猜。Nasdaq 代码表会改：[Trading Halt Codes](https://www.nasdaqtrader.com/Trader.aspx?id=TradeHaltCodes)。

暂停期间普通止损单不能让你退出。

---

## 5. 做空、Locate、SSR（Regulation SHO）

- Locate：成交前，券商须有合理依据相信能借到并在交割日交付。[Reg SHO 概述](https://www.sec.gov/investor/pubs/regsho.htm)（结算日可能仍写 T+2）。做市商有限例外，普通账户没有。
- Locate ≠ 可卖库存 ≠ 已经成交的空头。Cover 是买回平仓；释放未用 locate 不是平仓。
- **Rule 201**：[Staff FAQ](https://www.sec.gov/divisions/marketreg/rule201faq.htm)（页面显示更新至 2026-06-26）。

Rule 201 要点：

- 是否触发由**上市市场**根据常规时段 consolidated last-sale 相对**前一常规时段收盘**是否跌至少 **10%** 来定，再通知 SIP 发布。你自己屏幕先显示「跌了 10%」不等于已经 SSR。
- 触发后，普通空单不能在当前 **NBB 或以下**显示或执行（须高于 NBB）。市场 crossed 时 FAQ 另有例外。
- 持续当天剩余 + **下一个交易日**（周五触发则管到下周一）。次日再跌 10% 可再触发、再延长。没有次数上限。
- 只能在常规时段**触发**；一旦触发，在仍有持续 NBBO 的扩展时段也可以适用。
- IPO 首日通常没有「前收」，Rule 201 从第二个交易日起才适用。
- 普通交易者不要自行把订单标成 short exempt。该标记是 Rule 201 价格限制的例外，不是 locate 例外。

SSR **不是**禁止做空，**不保证**上涨，也不等于 squeeze。

---

## 6. 订单

[SEC Stop Order](https://www.sec.gov/answers/stopord.htm)：

- 市价：倾向成交，不保证价格；停牌或没有对手盘时可能不成交；
- 限价：锁最差价格，不保证成交或全部成交；
- Stop：触发价不是保证成交价；触发后通常变市价；
- Stop-limit：越过限价可能完全出不去。

券商用 last sale 还是 quotation 判断 stop，可能不同。

---

## 7. 期权：行权、指派、自动行权（OCC / FINRA）

- OCC：[Characteristics and Risks of Standardized Options](https://www.theocc.com/getmedia/dd6200a7-5982-4226-90e4-1f2d32a89911/june_2024_riskstoc.pdf)
- [FINRA Options](https://www.finra.org/investors/investing/investment-products/options)
- [FINRA：Understanding Assignment](https://www.finra.org/investors/insights/trading-options-understanding-assignment)

比课程更准确的说法：

- 美式股票/ETF 期权：**到期前的任一交易日，买方都可以提交行权**。卖方因此**可能在到期前被指派**。OCC 对会员的指派、券商对客户的再分配，通常在行权通知处理之后（常见是收盘后/夜间），不是「盘中某一秒随机把你打成股票仓」那种卡通。你当天开着盘，仍可能在盘后才看到指派通知。
- 欧式指数期权通常只能到期行权，且常为现金结算。风格、结算、最后交易时间是三件事。
- Exercise by Exception：到期时达到 OCC 规定价内幅度的合约通常会被**自动行权**，除非及时提交相反指令。股票期权常见阈值是很小一档价内（历史上多用每股至少 0.01 美元价内这一量级），**以 OCC 当期规则为准**。券商截止时间往往早于 OCC。购买力不足时，券商可能提前平仓或提交不行权。
- 乘数通常 100，公司行动后的调整合约可以不是。
- 裸卖 Call 亏损理论上不封顶。Covered Call 仍承担股票大跌。保证金不是最大亏损。
- 公开的大单 / flow 不能证明谁在买、是不是价差的一腿，更不是内幕。

---

## 8. 期货税务（IRS）

受监管期货等可能属于 IRC **Section 1256**：年底视同售出，净损益常按 60% 长期 / 40% 短期。Form 6781。不是「所有期货、所有身份、所有州」都一样。课程 2019 税率表作废。见 [IRS Publication 550](https://www.irs.gov/publications/p550)、[Form 6781](https://www.irs.gov/forms-pubs/about-form-6781)。不是税务建议。

---

## 9. 盘外与发行

常规时段：美东 09:30–16:00。盘前盘后、隔夜能做多久，由场所和券商决定。量更低、点差更宽，很多券商只接受限价单。

IPO ≠ primary offering ≠ secondary resale ≠ shelf ≠ ATM。读文件：[SEC 小企业术语](https://www.sec.gov/resources-small-businesses/glossary)

---

## 10. 热键

平台命令、大小写、券商支持范围以**当前**手册为准。课程脚本不是可粘贴生产配置。
