# 智知库 (ZhiZhiKu)

**一款轻量化、全私有化、可离线部署的中文智能 RAG 问答系统**

智知库是基于大语言模型与 RAG 检索增强技术搭建的本地私有知识库对话系统，全程支持离线运行、数据本地存储，无需上传文件与对话数据至云端。项目主打低门槛部署、高自由度自定义、中文场景深度适配，适合个人学习、本地资料问答、企业内部私有文档智能检索等场景。

## 项目特色

- **100% 私有化部署**：所有文档、对话记录、向量数据均本地存储，无云端数据上传
- **全离线运行**：支持本地开源大模型，断网环境也可正常问答
- **中文场景优化**：针对中文文档分词、检索、问答逻辑专项优化
- **极低部署门槛**：支持 pip 安装与源码部署，新手零难度上手
- **高度可定制化**：界面名称、样式、功能模块、模型接口均可自由修改
- **轻量化高性能**：适配普通家用电脑与低配服务器

## 核心功能

- **通用智能对话**：多轮上下文对话、记忆留存、自定义角色设定
- **私有知识库问答**：文档上传、自动解析、智能分块、向量入库
- **多格式文档兼容**：PDF、Word、Excel、TXT、Markdown 等
- **混合检索优化**：关键词检索 + 向量语义检索双模式
- **多模型自由切换**：本地开源模型与云端 API 模型一键切换
- **可视化 Web 界面**：Streamlit 网页交互，多会话管理、历史记录查询

## 技术栈

- **核心框架**：LangChain
- **后端服务**：FastAPI
- **前端界面**：Streamlit
- **向量检索**：FAISS / Milvus / PGVector 等

## 快速部署

### 环境要求

- Python 3.10 ~ 3.11
- Windows / Linux / macOS

### 安装与启动

```bash
# 进入服务端目录
cd libs/chatchat-server

# 安装依赖（推荐使用 poetry）
poetry install

# 初始化项目（生成配置文件与示例知识库）
poetry run chatchat init

# 启动 API + WebUI
poetry run chatchat start -a
```

启动后浏览器访问 WebUI 地址（默认 `http://127.0.0.1:8501`）即可使用。

### 配置说明

初始化后，在项目数据目录（`CHATCHAT_ROOT`，默认为当前目录）下会生成以下配置文件：

- `basic_settings.yaml` — 服务端口、日志等基础配置
- `model_settings.yaml` — 模型平台与 LLM / Embedding 模型配置
- `kb_settings.yaml` — 知识库与检索参数
- `prompt_settings.yaml` — 提示词模板

按需修改 `model_settings.yaml` 中的模型平台地址与 API Key 后重启服务即可。

## 使用教程

1. 在「知识库管理」中创建知识库并上传文档
2. 等待系统自动完成解析与向量化
3. 在「RAG 对话」中选择对应知识库开始问答
4. 在「多功能对话」中使用 Agent 与工具能力

## 开源说明

本项目基于 [Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) 进行二次开发与品牌化改造，遵循 Apache License 2.0 协议。

- 原项目版权归 LangChain-Chatchat 团队所有
- 本仓库为个人学习与实践用途的定制版本

详见 [NOTICE](NOTICE) 文件。

## 致谢

感谢 [Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) 开源社区提供的优秀基础框架。
