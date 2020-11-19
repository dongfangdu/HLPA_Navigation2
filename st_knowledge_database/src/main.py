import streamlit as st
import description, template_kb, law_recommend

def run():
    mode_map = {0: "简介",
                1: "话术知识库",
                2: "法条推荐"}

    app_mode = st.sidebar.radio("请选择其中一个功能",
                                    ["简介", "话术知识库", "法条推荐"])

    if app_mode == mode_map.get(0):
        description.description()

    elif app_mode == mode_map.get(1):
        template_kb.template_kb()

    elif app_mode == mode_map.get(2):
        law_recommend.law_recommend()

if __name__ == "__main__":
    run()
