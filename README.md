# SEU_Action_Report
![Stars](https://img.shields.io/github/stars/quzard/SEU_Action_Report.svg)
![Forks](https://img.shields.io/github/forks/quzard/SEU_Action_Report.svg)

**利用GitHub的action进行健康上报**

支持定时上报以及start上报（star一下自己fork后的项目就会启动上报action）

如有使用问题，请发issue![issue](/img/4.png)

## 使用步骤

1. fork 该项目![fork](/img/1.png)

2. 设置自己的信息

   Setting→Secrets→New repository secret

   ![Secrets](/img/2.png)

| Secret     | 解释                                                         |
| ---------- | ------------------------------------------------------------ |
| ID         | 一卡通号                                                     |
| PASSWORD   | 一卡通密码                                                   |
| NAME       | 姓名（可选）                                                 |
| KU         | 酷推的Skey（可选）可用于qq推送上报通知。学习链接https://cp.xuthus.cc/ |
| SERVERCHAN | 新版server酱的Skey（可选）可用于微信推送上报通知。学习链接https://sct.ftqq.com/ |

3. 如果需要修改上报时间，修改 **.github/workflows/auto_temperature.yml**
![cron](/img/3.png)

## Stargazers over time
[![Stargazers over time](https://starchart.cc/Quzard/SEU_Action_Report.svg)](https://starchart.cc/Quzard/SEU_Action_Report)