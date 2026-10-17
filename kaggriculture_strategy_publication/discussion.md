# 结合生产路线与有界市场优化的 Kaggriculture 农场代理

这份中文笔记介绍最终代理如何组织生产与交付、保护经营资源，并优化成交顺序。内容包含可运行教学例子、真实函数摘录、来源署名和可核验的构建流程。

> 发布前，请在这里补充自己已经公开的 Notebook 与 GitHub 链接。

## 策略原理

生产控制器根据已揭示商店和实时农场状态选择继承路线，协调作物、动物、饲料、工人和运输。末期按需进行有界采集与交付规划。

市场控制器投影单位行动后的仓库库存，预留已承诺资源，再按保守库存和价格约束添加现金产品卖单。采购重排受到资金、容量和状态依赖检查保护，避免挤占生产投入。

最后的纯卖单收尾考虑连续两至四条 SELL，使用继承的逐单位成交模型与镜像对手队列估计相对收入。四单每次最多二十四种排列，外层最多四次，行动稳定或重复时停止。

搜索保持数量和单位指令，不跨越固定采购位置。任意卖单块超过四条时，该收尾层保留继承行动。实际返回的队列同步到状态记录，避免估计器继续使用过时订单。

## 笔记内容与限制

- 从生产到现金的概念流程。
- 明确区别于官方公式的教学市场。
- 真实的纯卖单封装函数与中文说明。
- 历史执行检查、文件哈希核验与来源说明。
- Kaggle 自包含版与 GitHub 轻量版。

默认离线运行，不自动安装依赖、启动比赛或提交。历史检查明确标注，不当作刚运行的新比赛。对手模型是近似，扩大搜索不能纠正所有假设，成交优化也不能弥补全部产销错配。不承诺评分、名次或奖牌。

## 来源与署名

生产路线与继承成交模型不是本地原创。主要来源为
[Master Hybrid](https://www.kaggle.com/code/haideptry/the-2965-master-hybrid-engine)、
[Demand-Preserving Turn Sale Timing](https://www.kaggle.com/code/tetsutani/demand-preserving-turn-sale-timing)、
[Your Market List Is an Order Book](https://www.kaggle.com/code/shiiin9/your-market-list-is-an-order-book)
及 [Kaggle 官方环境](https://github.com/Kaggle/kaggle-environments)。

完整作者署名、Apache-2.0 LICENSE、版权声明原文与已知数据来源限制均保留。
