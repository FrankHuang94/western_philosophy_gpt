# Western Philosophy Knowledge Base

本仓库包含一个结构化的西方哲学思想数据库。主体内容位于
[`philosophy-db/`](philosophy-db/README.md)，覆盖古希腊罗马哲学、中世纪哲学、近代早期哲学、启蒙运动、德国唯心主义、现象学、分析哲学、批判理论、后结构主义、后现代主义与当代政治哲学等章节。

当前状态：正文、结构化数据、附录和校验脚本均已完成。按 `philosophy-db/scripts/word_count.py` 统计，总中文字数为 182,031，超过 150,000 字目标。

## 快速入口

- [项目说明与导航](philosophy-db/README.md)
- [总览与流派谱系](philosophy-db/docs/00-overview/README.md)
- [启蒙运动核心章节](philosophy-db/docs/04-enlightenment/README.md)
- [跨流派主题对照](philosophy-db/docs/15-cross-cutting/README.md)
- [附录](philosophy-db/docs/appendix/README.md)

## 校验

在 `philosophy-db` 目录下运行：

```bash
python3 scripts/validate.py
python3 scripts/word_count.py
python3 scripts/build_index.py
```
