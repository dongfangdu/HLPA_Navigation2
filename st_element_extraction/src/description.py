import streamlit as st


def description():
    st.title("要素提取")
    st.header("♟ 概述 ♟")
    st.markdown("要素提取，一般简称为 NER，是一种在文本中寻找属于 `某类别属性` 的文字片段，如人名、地名、时间等")

    st.header("♟ 应用场景 ♟")

    st.subheader("🔹 视频点播")
    st.markdown("通过要素提取，可快速 `抽取文书、庭审、审讯、视频点播` 等场景下的关键信息")

    st.subheader("🔹 智能客服12368")
    st.markdown("抽取用户专名要素，助力 `智能客服` 判定对话流程，提升客户体验")

    st.subheader("🔹 类案推送")
    st.markdown("通过要素提取，构建业务场景的 `数据库、知识库和知识图谱`")
