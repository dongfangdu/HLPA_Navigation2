import streamlit as st

def description():
    st.title("知识库")
    st.header("♟ 概述 ♟")
    st.markdown("知识库主要用于 `构建话术、问答类` 的业务场景")
    st.markdown("提供的能力是作为产品支撑能力展示，也支持定制需求")

    st.header("♟ 应用场景 ♟")

    st.subheader("🔹 客服质检")
    st.markdown("构建 `问题-话术回复` 的知识库，丰富语音质检内容")

    st.subheader("🔹 智能客服12368")
    st.markdown("对用户提问进行知识库匹配 `搜索推荐`，定位用户意图")
