# 发布中文策略笔记

## Kaggle

1. 新建 Notebook，导入 `kaggle/kaggriculture_strategy.ipynb`。
2. CPU 即可，默认不需要联网或额外数据集。
3. 从头运行并保存公开版本。
4. 将真实链接补入 `discussion.md`，再在 Discussion 发布摘要。

Discussion 用于分享说明与链接，不是笔记执行环境。恢复的归档位于 `strategy_outputs/submission.tar.gz`，不会自动提交或发布。

## GitHub

解压发布包后上传目录内容。根目录笔记为轻量版，读取 `artifacts/` 中的归档；`kaggle/` 中的笔记为自包含版。两版讲解同一最终策略。

保留源码、LICENSE、NOTICE 和归档。网页阅读版无需启动笔记内核。验证结果见 `notebook_validation.json` 与 `evidence/action_equivalence.json`。

正文、教学注释和运行提示为中文；许可证与上游版权声明保留原文。不包含迭代历史，不代为发帖、上传或推送仓库。
