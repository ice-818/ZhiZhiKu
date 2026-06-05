# 智知库服务端

智知库的核心服务端，提供 API 与 WebUI 功能。

## 安装

```bash
poetry install
poetry run chatchat init
poetry run chatchat start -a
```

## 品牌定制

如需修改产品名称、Logo 等对外展示信息，编辑 `chatchat/branding.py` 即可，无需改动业务逻辑代码。

## 上游项目

本模块基于 [Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) 改造，详见项目根目录 [NOTICE](../../NOTICE)。
