"""项目品牌与对外展示信息（换皮配置集中在此文件）。"""

# 中文产品名
PROJECT_NAME_CN = "智知库"

# 英文标识（用于包名、目录等）
PROJECT_NAME_EN = "ZhiZhiKu"

# 一句话描述（对外标语）
PROJECT_TAGLINE = "互联网企业私有知识库智能问答 —— PRD、接口文档、Runbook 问一句，有据可查"

# 项目使命（README / 关于页使用）
PROJECT_MISSION = (
    "面向互联网企业内部场景，在保障用户数据与商业机密安全的前提下，"
    "将 PRD、接口文档、运维手册、客服话术转化为可对话、可溯源的智能知识库，"
    "降低协作等待、重复答疑与知识传承成本。"
)

# 互联网企业核心痛点（简要版，用于关于页）
PAIN_POINTS_SUMMARY = [
    "文档散在飞书/Confluence/Git，研发产品到处找",
    "迭代快文档追不上，过期信息引发返工和客诉",
    "客服运营重复答疑，大促期间人力吃紧",
    "On-Call 找不到 Runbook，故障处理靠个人经验",
    "用户数据与商业机密不能用公有云 AI",
    "通用大模型易幻觉，不敢用于排查和对外答复",
    "人员流动大，业务知识随人走、新人上手慢",
]

# WebUI / API 标题
WEBUI_TITLE = f"{PROJECT_NAME_CN} WebUI"
API_TITLE = f"{PROJECT_NAME_CN} API Server"

# 品牌图片（位于 chatchat/img/ 目录）
ICON_FILENAME = "zhizhiku_icon.png"
LOGO_FILENAME = "logo-zhizhiku.png"


def about_text(version: str) -> str:
    pains = "\n".join(f"· {p}" for p in PAIN_POINTS_SUMMARY)
    return (
        f"欢迎使用 {PROJECT_NAME_CN} {version}！\n\n"
        f"{PROJECT_TAGLINE}\n\n"
        f"项目使命：{PROJECT_MISSION}\n\n"
        f"针对互联网企业痛点：\n{pains}"
    )


def startup_banner() -> str:
    return f"{PROJECT_NAME_CN} Configuration"
