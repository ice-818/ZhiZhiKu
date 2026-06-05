"""项目品牌与对外展示信息（换皮配置集中在此文件）。"""

# 中文产品名
PROJECT_NAME_CN = "智知库"

# 英文标识（用于包名、目录等）
PROJECT_NAME_EN = "ZhiZhiKu"

# 一句话描述
PROJECT_TAGLINE = "私有知识库智能问答系统"

# WebUI / API 标题
WEBUI_TITLE = f"{PROJECT_NAME_CN} WebUI"
API_TITLE = f"{PROJECT_NAME_CN} API Server"

# 品牌图片（位于 chatchat/img/ 目录）
ICON_FILENAME = "zhizhiku_icon.png"
LOGO_FILENAME = "logo-zhizhiku.png"

# 关于页文案
def about_text(version: str) -> str:
    return f"欢迎使用 {PROJECT_NAME_CN} {version}！\n{PROJECT_TAGLINE}"

# 控制台启动横幅
def startup_banner() -> str:
    return f"{PROJECT_NAME_CN} Configuration"
