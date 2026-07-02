# 西方哲学思想数据库

本项目面向哲学与社会科学研究生，目标是从思想史、流派谱系、概念演化与跨流派批判关系四个层面，构建一个可阅读、可导航、可校验的西方哲学知识库。

正文目标总量不少于 150,000 中文字，计划内容约 178,000 中文字。启蒙运动及之后章节 `04-enlightenment` 至 `14-political-phil` 是核心部分，目标篇幅不少于全书正文的 70%。

## 目录结构

```text
philosophy-db/
  docs/                 正文、总览、附录
  data/                 人物、流派、批判关系、时间线结构化数据
  scripts/              索引生成、校验、字数统计脚本
  README.md             项目说明与导航
  CONTRIBUTING.md       内容编写规范
```

## 阅读路径

1. 从 [`docs/00-overview`](docs/00-overview/README.md) 获取整体分期、流派谱系与使用说明。
2. 按 `01-ancient` 至 `14-political-phil` 顺序阅读思想史主线。
3. 使用 [`docs/15-cross-cutting`](docs/15-cross-cutting/README.md) 横向比较本体论、认识论、伦理学、政治哲学与美学问题。
4. 查阅 [`docs/appendix`](docs/appendix/README.md) 中的人名索引、术语词典、时间线与参考书目。

## 章节导航

| 目录 | 主题 | 目标字数 |
| --- | --- | ---: |
| [`00-overview`](docs/00-overview/README.md) | 总览、分期表、流派谱系图、使用说明 | 3,000 |
| [`01-ancient`](docs/01-ancient/README.md) | 古希腊罗马哲学 | 12,000 |
| [`02-medieval`](docs/02-medieval/README.md) | 教父哲学、经院哲学 | 8,000 |
| [`03-early-modern`](docs/03-early-modern/README.md) | 理性主义与经验主义 | 15,000 |
| [`04-enlightenment`](docs/04-enlightenment/README.md) | 启蒙运动 | 25,000 |
| [`05-german-idealism`](docs/05-german-idealism/README.md) | 德国唯心主义 | 15,000 |
| [`06-post-kantian`](docs/06-post-kantian/README.md) | 浪漫主义、唯意志论、存在主义先驱 | 12,000 |
| [`07-19th-century`](docs/07-19th-century/README.md) | 实证主义、功利主义、马克思主义 | 12,000 |
| [`08-phenomenology`](docs/08-phenomenology/README.md) | 现象学、存在主义、解释学 | 15,000 |
| [`09-analytic`](docs/09-analytic/README.md) | 分析哲学 | 15,000 |
| [`10-pragmatism`](docs/10-pragmatism/README.md) | 实用主义 | 6,000 |
| [`11-critical-theory`](docs/11-critical-theory/README.md) | 法兰克福学派与批判理论 | 8,000 |
| [`12-structuralism`](docs/12-structuralism/README.md) | 结构主义与后结构主义 | 8,000 |
| [`13-postmodern`](docs/13-postmodern/README.md) | 后现代主义 | 6,000 |
| [`14-political-phil`](docs/14-political-phil/README.md) | 当代政治哲学 | 8,000 |
| [`15-cross-cutting`](docs/15-cross-cutting/README.md) | 跨流派主题对照 | 6,000 |
| [`appendix`](docs/appendix/README.md) | 人名索引、术语词典、时间线、参考书目 | 4,000 |

## 数据文件

- [`data/philosophers.json`](data/philosophers.json)：人物数据，包括生卒年、流派归属、师承关系、代表作与核心概念。
- [`data/schools.json`](data/schools.json)：流派数据，包括时段、主张、代表人物、影响与批判关系。
- [`data/critiques.json`](data/critiques.json)：批判关系图数据，记录 `source`、`target`、批判类型、摘要与关键文本。
- [`data/timeline.json`](data/timeline.json)：哲学史事件时间线。

## 脚本

在 `philosophy-db` 目录下运行：

```bash
python3 scripts/validate.py
python3 scripts/word_count.py
python3 scripts/build_index.py
```

脚本约定：

- Markdown 中若需要强校验人物或流派引用，可使用 `[[philosopher:康德]]`、`[[school:德国唯心主义]]`、`[[work:纯粹理性批判]]` 等显式标记。
- `validate.py` 会校验 JSON 结构、批判关系端点、显式引用是否存在。
- `word_count.py` 会统计各章节中文字符数并与目标篇幅对照。
- `build_index.py` 会根据 `data/*.json` 生成索引与 Mermaid 关系图草稿。

## 当前进度

- [x] 初始化目录结构
- [x] 初始化数据文件 schema
- [x] 初始化脚本骨架
- [ ] 编写 `00-overview`
- [ ] 编写 `01-ancient` 至 `14-political-phil`
- [ ] 编写 `15-cross-cutting`
- [ ] 编写附录
- [ ] 达到 150,000 中文字正文目标

