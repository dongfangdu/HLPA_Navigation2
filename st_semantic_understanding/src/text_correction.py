import streamlit as st
import pandas as pd

def text_correction():
    st.title("文本纠错")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.markdown("文本纠错是判断一句话是否符合语言表达习惯，发掘`错字、同音字并进行改正`的能力")

    # ===============
    # 概述
    # ===============
    st.header("♟ 样例体验 ♟")
    st.warning("体验环境为测试环境，仅支持样例解析，暂不开放自定义输入")

    default_text = pd.DataFrame({
        "原文": ["被告一意向书为第三人提供担保的事实",
               "像今天这个情况不是我们乡的事情",
               "麻烦把这个证据交给第三任"],
    })

    default_res = pd.DataFrame({
        "错字": ["一", "乡", "任"],
        "纠正字": ["依", "想", "人"],
        "纠正结果": ["被告依意向书为第三人提供担保的事实",
                 "像今天这个情况不是我们想的事情",
                 "麻烦把这个证据交给第三人"],
    })

    st.markdown("🍄 待解析文本")
    st.table(default_text)

    if st.button("🍄 点击解析"):
        st.success("解析完成")
        st.table(default_res)

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("点击查看 接口文档"):
        st.write("未完成\n")

if __name__ == "__main__":
    text_correction()