import streamlit as st
import pandas as pd

def text_correction():
    st.title("文本纠错")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.write("文本纠错是判断一句话是否符合语言表达习惯，发掘错字并进行改正的能力")

    # ===============
    # 概述
    # ===============
    st.header("♟ 样例体验 ♟")

    default_text = pd.DataFrame({
        "原文": ["被告一意向书为第三人提供担保的事实",
               "像今天这个情况不是我们乡的事情",
               "麻烦把这个证据交给第三任"],
    })

    default_res = pd.DataFrame({
        "纠正结果": ["被告依意向书为第三人提供担保的事实",
               "像今天这个情况不是我们想的事情",
               "麻烦把这个证据交给第三人"],
    })

    if st.checkbox("🍄 点击查看文本"):
        st.table(default_text)

    if st.button("解析"):
        st.success("解析完成")
        st.table(default_res)

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("接口文档"):
        st.write("未完成\n")

if __name__ == "__main__":
    text_correction()