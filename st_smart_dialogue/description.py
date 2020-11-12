import streamlit as st

def description():
    st.title("智能对话")
    st.header("♟ 概述 ♟")
    st.write("智能对话，主要服务于语音客服机器人的应用中，实现不间断的客服服务\n")
    st.markdown("该服务主要集成了")
    st.markdown("* ASR")
    st.markdown("* TTS")
    st.markdown("* 客服大脑")
    st.markdown("三项能力进行线上使用")

    st.header("♟ 功能清单 ♟")
    st.write("我们提供了几种不同场景的智能对话服务能力\n")
    st.write("便于体验，以下能力均以文本输入输出进行展示\n")

    st.markdown("* 12368司法服务")
    st.markdown("* 司法外呼")
    st.markdown("* ETC销售")
    st.markdown("* 物业咨询")
    st.markdown("* 诈骗预警")
    st.markdown("* 自学习")

    st.header("♟ 应用场景 ♟")

    st.subheader("🔹 智能客服12368")
    st.write("应用于湖州12368司法服务热线完整的智能语音客服服务")
