import sys

import streamlit as st
import streamlit_antd_components as sac

from chatchat import __version__
from chatchat.branding import (
    ICON_FILENAME,
    LOGO_FILENAME,
    PROJECT_NAME_CN,
    WEBUI_TITLE,
    about_text,
)
from chatchat.server.utils import api_address
from chatchat.webui_pages.dialogue.dialogue import dialogue_page
from chatchat.webui_pages.kb_chat import kb_chat
from chatchat.webui_pages.mcp import mcp_management_page
from chatchat.webui_pages.knowledge_base.knowledge_base import knowledge_base_page
from chatchat.webui_pages.utils import *

api = ApiRequest(base_url=api_address())

if __name__ == "__main__":
    is_lite = "lite" in sys.argv  # TODO: remove lite mode

    st.set_page_config(
        WEBUI_TITLE,
        get_img_base64(ICON_FILENAME),
        initial_sidebar_state="expanded",
        menu_items={
            "About": about_text(__version__),
        },
        layout="centered",
    )

    st.markdown(
        """
        <style>
        [data-testid="stSidebarUserContent"] {
            padding-top: 20px;
        }
        .block-container {
            padding-top: 25px;
        }
        [data-testid="stBottomBlockContainer"] {
            padding-bottom: 20px;
        }
        """,
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.image(get_img_base64(LOGO_FILENAME), use_column_width=True)
        st.caption(
            f"""<p align="right">{PROJECT_NAME_CN} · v{__version__}</p>""",
            unsafe_allow_html=True,
        )

        selected_page = sac.menu(
            [
                sac.MenuItem("多功能对话", icon="chat"),
                sac.MenuItem("RAG 对话", icon="database"),
                sac.MenuItem("知识库管理", icon="hdd-stack"),
                sac.MenuItem("MCP 管理", icon="hdd-stack"),
            ],
            key="selected_page",
            open_index=0,
        )

        sac.divider()

    if selected_page == "知识库管理":
        knowledge_base_page(api=api, is_lite=is_lite)
    elif selected_page == "RAG 对话":
        kb_chat(api=api)
    elif selected_page == "MCP 管理":
        mcp_management_page(api=api)
    else:
        dialogue_page(api=api, is_lite=is_lite)
