import streamlit as st

def description():
    st.title("智能对话")
    st.header("♟ 概述 ♟")
    st.write("智能对话，主要服务于 `语音客服机器人` 的应用中，实现不间断的客服服务\n")
    st.markdown("该服务主要集成了")
    st.markdown("* 语音识别 (ASR)")
    st.markdown("* 语音合成 (TTS)")
    st.markdown("* 客服大脑")
    st.markdown("* 工单系统")
    st.markdown("* 外呼系统")
    st.markdown("五项能力进行线上使用\n")
    st.markdown("为便于展示，这里只展示 `客服大脑的文本端` 的交互\n")
    st.markdown("由于不同业务特殊性，智能对话能力支持 `自学习` 以及 `产品端的定制需求`")


    st.header("♟ 应用场景 ♟")
    st.subheader("🔹 智能客服12368")
    st.write("应用于湖州12368司法服务热线完整的智能语音客服服务")
