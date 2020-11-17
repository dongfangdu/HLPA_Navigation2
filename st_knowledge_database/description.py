import streamlit as st

def description():
    st.title("知识库")
    st.header("♟ 概述 ♟")
    st.write("知识库主要用于构建话术、问答类的业务场景")

    st.header("♟ 功能清单 ♟")
    st.write("以下提供的能力是作为产品支撑能力展示，也支持定制需求\n")
    st.write("包括")

    st.markdown("* 话术知识库")
    st.markdown("* 法条推荐")

    st.header("♟ 应用场景 ♟")

    st.subheader("🔹 客服质检")
    st.write("构建问题-话术回复的知识库，丰富语音质检内容")

    st.subheader("🔹 智能客服12368")
    st.write("对用户提问进行知识库匹配搜索推荐，定位用户意图")
