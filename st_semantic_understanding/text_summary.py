import streamlit as st
import pandas as pd

def text_summary():
    st.title("文本摘要")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.write("文本摘要，是一种将较长的文本进行精简的能力\n")

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")

    default_text = "成都市软件和信息技术服务业近年来一直保持快速增长势头，稳居中西部城市之音，已成为我国西部'硅谷'。" \
                   "《xx年度成都市软件和信息技术服务产业发展报告》日前发布..."
    default_answer = "成都软件和信息技术服务业发展报告发布"

    if st.checkbox("🍄 点击查看文本"):
        st.markdown("**文本**")
        st.markdown("```" + default_text + "```")

    if st.button("解析"):
        st.success("解析完成")
        st.markdown("**摘要**")
        st.markdown("```" + default_answer + "```")

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("接口文档"):
        st.write("未完成\n")

    # ===============
    # 定制需求
    # ===============
    st.header("♟ 定制需求 ♟")
    if st.checkbox("定制需求"):
        st.write("该能力持续优化中\n")
        st.write("同时也支持场景定制化")

if __name__ == "__main__":
    text_summary()