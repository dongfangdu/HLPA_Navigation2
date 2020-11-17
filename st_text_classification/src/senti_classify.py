# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd


def senti_classify():
    st.title("情感分类")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.write("情感分类是指根据文本所表达的含义和情感信息将文本划分成褒扬的或贬义的两种或几种类型\n")
    st.write("目前暂时把情感褒义或贬义两类，即正面或负面两类情绪\n")

    # ===============
    # 示例
    # ===============
    st.header("♟ 示例 ♟")

    default_sample1 = "前台客房服务态度非常好！早餐很丰富，房价很干净。再接再厉！"
    default_sample2 = "结果大失所望，灯光昏暗，空间极其狭小，床垫质量恶劣，房间还伴着一股霉味。"
    default_sample3 = "可利用文本分类实现情感分析，效果不是不行"
    default_res = pd.DataFrame({"文本": [default_sample1, default_sample2, default_sample3],
                                "情绪": ["正面", "负面", "正面"]})

    st.markdown("🍄 **输入文本: **")

    st.markdown("```" + default_sample1 + "```")
    st.markdown("```" + default_sample2 + "```")
    st.markdown("```" + default_sample3 + "```")
    if st.button("分析"):
        st.success("分析完成")
        st.table(default_res)


if __name__ == "__main__":
    senti_classify()
