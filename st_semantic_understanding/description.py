import streamlit as st

def description():
    st.title("语义理解")
    st.header("♟ 概述 ♟")
    st.write("我们提供了几种在业务场景中丰富产品质量维度的语义理解工具，主要是对文本进行智能化处理\n")

    st.header("♟ 功能清单 ♟")
    st.write("以下提供的能力均在持续优化，也支持产品端的定制需求\n")
    st.write("主要包括")

    st.markdown("* 司法问答")
    st.markdown("* 文本纠错")
    st.markdown("* 敏感词过滤")

    st.header("♟ 应用场景 ♟")

    st.subheader("🔹 类案推送")
    st.write("对司法文书、审讯笔录、裁决资料进行自主提问，快速发掘目标信息")

    st.subheader("🔹 ASR 纠错")
    st.write("对 ASR 引擎的识别结果进行纠错，满足语言表达习惯")

    st.subheader("🔹 客服质检")
    st.write("检测敏感信息，包括黄暴、违法及特定场景下的文本，发掘敏感来源")


