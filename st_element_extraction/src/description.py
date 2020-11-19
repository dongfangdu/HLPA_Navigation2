import streamlit as st


def description():
    st.title("要素提取")
    st.header("♟ 概述 ♟")
    st.write("要素提取，一般简称为 NER，是一种在文本中寻找属于某类别属性的文字片段，如人名、地名、时间等")

    st.header("♟ 功能清单 ♟")
    st.write("我们提供了几种针对不同场景下要素提取能力，包括")

    st.markdown("* 公共要素提取")
    st.markdown("* 医疗要素提取")
    st.markdown("* 司法要素提取")
    st.markdown("* 热词发现")
    st.markdown("* 自学习")

    st.header("♟ 应用场景 ♟")

    st.subheader("🔹 视频点播")
    st.write("通过要素提取，可快速抽取文书、庭审、审讯、视频点播等场景下的关键信息")

    st.subheader("🔹 智能客服12368")
    st.write("抽取用户专命要素，助力智能客服判定对话流程，提升客户体验")

    st.subheader("🔹 类案推送")
    st.write("通过要素提取，构建业务场景的数据库、知识库和知识图谱")
