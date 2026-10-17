# Kaggriculture：结合生产路线与有界市场优化的农场代理

本材料只介绍最终策略的生产、运输、资源保护与成交顺序搜索，不包含迭代历史或版本编号，也不承诺排行榜评分、奖牌和最终名次。

## 阅读与使用

- [策略笔记](kaggriculture_strategy.ipynb)：适合 GitHub 阅读的轻量版。
- [网页阅读版](kaggriculture_strategy.html)：已执行正文，隐藏长编码输入。
- [Kaggle 笔记](kaggle/kaggriculture_strategy.ipynb)：可单文件导入的自包含版。
- [Discussion 发帖稿](discussion.md)：最终策略的中文摘要。
- [完整源码](main.py)：公开入口为 `submission_agent`，本地说明注释为中文。

两版恢复相同归档。GitHub 版读取 `artifacts/submission.tar.gz`，Kaggle 版内嵌归档。默认离线运行，不安装依赖、不启动比赛、不自动提交或发布。

## 最终策略做了什么

1. 根据已揭示商店与农场状态安排生产路线和工人行动。
2. 协调采集、运输及末期有界交付。
3. 投影单位行动后的仓库库存，保留已承诺资源。
4. 按可用库存和保守价格约束增加现金产品卖单。
5. 用资金、容量和订单依赖检查保护生产采购。
6. 使用继承的逐单位成交模型评估交易顺序。
7. 对连续两至四条 SELL 搜索排列，纯卖单收尾最多四次。
8. 行动稳定或重复时停止，同步实际返回的队列并记录诊断信息。

纯卖单收尾保持数量和单位指令，不跨越固定采购位置。任意卖单块超过四条时，该收尾层保留继承行动。对手镜像模型是近似，不保证真实收益或胜负。

## 运行笔记

打开笔记并从第一格运行。需要命令行执行时，可在独立环境安装工具：

```bash
python -m pip install -r requirements-notebook.txt
python -m jupyter nbconvert --to notebook --execute kaggriculture_strategy.ipynb --output strategy_executed.ipynb
```

文件写入 `strategy_outputs/`。同名文件内容不同时拒绝覆盖，保护读者自己的修改。

可选完整对局检查使用独立的 Python 3.11 环境：

```bash
python -m pip install -r requirements-engine.txt
python run_match.py --seed 20261015 --opponent random
```

这是对内置对手的功能检查，不是竞技实力评估，也没有宣称建议种子已经运行。历史引擎为 `kaggle-environments==1.32.7`。

## 验证与来源

`evidence/complete_game_checks.json` 保存最终策略的执行检查，每场 719 次回调。笔记会重汇总历史记录，默认不重跑历史比赛。中文说明调整后的决策代码和同观测行动一致性分别核验，见 `manifest.json`、`evidence/action_equivalence.json` 和 `notebook_validation.json`。

公开路线和继承模型不是本地原创，主要来源为
[Master Hybrid](https://www.kaggle.com/code/haideptry/the-2965-master-hybrid-engine)、
[Demand-Preserving Turn Sale Timing](https://www.kaggle.com/code/tetsutani/demand-preserving-turn-sale-timing)、
[Your Market List Is an Order Book](https://www.kaggle.com/code/shiiin9/your-market-list-is-an-order-book)
和 [Kaggle 官方环境](https://github.com/Kaggle/kaggle-environments)。

正文、教学注释、运行提示和本地源码注释使用中文。上游原始代码说明、作者署名、Apache-2.0 LICENSE 和版权声明保留来源信息及原文。上游已声明的部分路线数据来源清单缺失问题继续保留，不补造来源，不暗示原作者认可本发布副本。

整理日期：2026 年 10 月 17 日（Asia/Shanghai）。未代为公开发布。
