# 期权：当前规则与风险细节

> 核对日期：2026-07-30  
> 适用范围：课程主要讨论的美国上市股票、ETF 和指数期权。具体合约规格、券商规则和账户权限以交易时的官方资料为准。

这份附录用来校正课程中容易被简化的操作规则，不构成投资、法律或税务建议。

## 先读官方风险披露

交易前应完整阅读 OCC 的 [Characteristics and Risks of Standardized Options](https://www.theocc.com/getmedia/dd6200a7-5982-4226-90e4-1f2d32a89911/june_2024_riskstoc.pdf)。OCC 明确说明期权并不适合所有投资者；券商也会按投资经验、知识、财务状况和风险承受能力审批期权权限。

辅助资料：

- [SEC Investor Bulletin: An Introduction to Options](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-63)
- [SEC Investor Bulletin: Opening an Options Account](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-77)
- [FINRA: Options](https://www.finra.org/investors/investing/investment-products/options)

## 不要套用单一合约规则

- 美国标准股票期权通常一张对应 100 股，但公司行动、调整合约和其他产品可能不同；
- 美国股票和 ETF 期权通常为 American Style，可在到期前被行权；
- 部分指数期权为 European Style，且以现金结算；
- 不同产品的最后交易时间、结算价格、AM/PM Settlement 和税务处理可能不同；
- 下单前应在 OCC、交易所和券商页面核对当前 Contract Specifications。

FINRA 的 [Options A to Z](https://www.finra.org/investors/insights/options-z-basics-greeks) 对股票/ETF 与指数期权的行权风格和结算差异有集中说明。

## 买方、卖方和保证金

- Long Option 买方最多通常损失已付 Premium、费用和滑点；
- Short Put 收到的 Premium 是最大收益，不是最大亏损；
- Naked Short Call 的损失理论上无上限；
- Covered Call 仍承担股票从现价跌向零的大部分风险；
- 保证金只是券商当前要求的抵押，不是最大损失；
- 波动加剧时，券商可提高保证金，并可能在未提前通知的情况下处置仓位。

多腿组合只有在各腿都正常存在、可成交且被券商按组合识别时，风险边界才与静态 Payoff 图一致。单腿提前指派、停牌或流动性消失都可能临时改变仓位。

## Exercise、Assignment 与 Expiration

Short American-Style Option 在到期前任何时候都可能被指派。临近除息日、深度价内、剩余时间价值很少或股票难借时，提前指派风险通常更值得关注。

到期前应主动确认：

1. 券商的 Exercise/Do-Not-Exercise 截止时间；
2. 哪些价内合约会被自动行权；
3. 账户是否有足够现金买入股票或有足够股票交付；
4. 多腿组合若只指派一腿，剩余仓位会变成什么；
5. 周末前后新闻导致股价越过 Strike 时如何处理。

不要把“到期最大收益”理解为收盘前一定能按该金额平仓，也不要依赖券商自动替你得到理想结果。参见 FINRA 的 [Understanding Assignment](https://www.finra.org/investors/insights/trading-options-understanding-assignment)。

## Roll、止损与限定风险

- Roll = 平掉旧仓 + 建立新仓；旧仓盈亏已经实现，不会被删除；
- Stop Order 不能防止隔夜跳空，也不能保证成交价；
- Defined-Risk Spread 的理论最大亏损仍应加上费用、滑点和到期操作风险；
- “零成本”只描述初始净现金流，不表示没有尾部风险、资金占用或机会成本；
- “高胜率”必须与平均盈利、平均亏损和成本一起判断。

## Options Flow 与内幕信息

公开成交数据只能显示市场活动，不能单独证明谁在买、为何交易或是否违法。Call 大单可能是价差的一腿或对冲，Volume 也不能在盘中证明 Open Interest 已增加。

非法内幕交易通常涉及违反信义或保密义务、基于重大非公开信息交易；向他人泄露信息以及接收提示后交易也可能构成违法。若自己接触到可能的重大非公开信息，应停止交易并寻求合规或法律意见。参见 SEC 的 [Insider Trading](https://www.investor.gov/introduction-investing/investing-basics/glossary/insider-trading)。

## 每次下单前

- [ ] 我能逐腿说清 Buy/Sell、Call/Put、Strike、Expiry 和 Quantity；
- [ ] 我已算出净 Debit/Credit、合约乘数和费用；
- [ ] 我知道最大亏损，且账户能承受跳空后无法止损；
- [ ] 我知道 Short Leg 被指派后需要多少现金或股票；
- [ ] 我核对过 Expiration、Settlement、除息日和公司行动；
- [ ] 我检查过 Bid–Ask、Open Interest 和组合限价；
- [ ] 我写下价格、时间和波动率三种失效条件；
- [ ] 我不会把课程案例、回测或大单当成收益保证。
