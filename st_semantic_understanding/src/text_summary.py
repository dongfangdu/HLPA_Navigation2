import streamlit as st
import pandas as pd

def text_summary():
    st.title("文本摘要")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.markdown("文本摘要，是一种将较长的文本 `不失关键信息地进行精简` 的能力")

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")
    st.warning("体验环境为测试环境，仅支持样例解析，暂不开放自定义输入")

    default_text = "成都市软件和信息技术服务业近年来一直保持快速增长势头，稳居中西部城市之音，已成为我国西部'硅谷'。" \
                   "《xx年度成都市软件和信息技术服务产业发展报告》日前发布..."
    default_answer = "成都软件和信息技术服务业发展报告发布"

    st.markdown("🍄 待解析文本")
    st.markdown("```" + default_text + "```")

    if st.button("🍄 点击生成摘要"):
        st.success("解析完成")
        st.markdown("```" + default_answer + "```")

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("点击查看 接口文档"):
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