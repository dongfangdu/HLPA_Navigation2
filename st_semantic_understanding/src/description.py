import streamlit as st

def description():
    st.title("语义理解")
    st.header("♟ 概述 ♟")
    st.markdown("我们提供了几种在业务场景中 `丰富产品质量维度` 的语义理解工具，主要是对文本进行智能化处理")
    st.markdown("以下提供的能力均在 `持续优化`，也支持 `产品端的定制需求`")

    st.header("♟ 应用场景 ♟")

    st.subheader("🔹 类案推送")
    st.write("对 `司法文书、审讯笔录、裁决资料` 进行自主提问，快速发掘目标信息")

    st.subheader("🔹 ASR 纠错")
    st.write("对 ASR 引擎的 `识别结果进行纠错`，满足语言表达习惯")

    st.subheader("🔹 客服质检")
    st.write("检测 `敏感词汇`，包括黄暴、违法及特定场景下的文本，发掘敏感来源")


