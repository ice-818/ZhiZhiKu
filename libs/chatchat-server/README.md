# 智知库服务端

面向**互联网企业内部场景**的私有化 RAG 问答服务端，覆盖 PRD、API 文档、On-Call Runbook、客服话术等资料的智能检索与问答。

## 解决的互联网痛点

| 痛点 | 智知库的应对 |
|------|-------------|
| 文档散在飞书 / Confluence / Git，协作靠 @ 人 | 按业务线建库，语义 + 关键词检索 |
| 双周发版，文档过期引发联调返工、客服口径错误 | 按版本 / 迭代维护知识库，更新即入库 |
| 客服 / 运营重复答疑，大促人力不足 | FAQ、活动规则、话术库统一问答 |
| 告警时 Runbook 难找，MTTR 拉长 | SRE 手册、故障预案、复盘报告可语义检索 |
| 用户数据与商业机密禁止上传公有云 AI | 内网私有化部署，支持离线运行 |
| 通用 AI 易幻觉，不敢用于排查和对外答复 | 基于内部文档 RAG 作答，引用可溯源 |
| 人员流动大，业务知识随人走 | 降低 Wiki 使用门槛，沉淀可传承资产 |

## 典型互联网场景

- 产品与需求问答（PRD、MRD、交互说明）
- 研发与接口文档（API、微服务、库表设计）
- On-Call 与 SRE（Runbook、故障预案、复盘）
- 客服与运营支持（活动规则、会员权益、话术库）
- 研发规范（代码规范、发布流程、环境说明）

## 推荐试点

1. 客服 / 运营 FAQ 库（见效快）
2. 核心接口 / 微服务文档库（联调高频）
3. On-Call Runbook 库（故障场景价值直观）

## 安装

```bash
poetry install
poetry run chatchat init
poetry run chatchat start -a
```

## 品牌定制

编辑 `chatchat/branding.py` 可修改产品名称、标语与关于页文案。

## 上游项目

基于 [Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) 改造，详见 [NOTICE](../../NOTICE)。
