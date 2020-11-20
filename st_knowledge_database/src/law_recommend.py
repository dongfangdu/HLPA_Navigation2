import streamlit as st
import pandas as pd
import requests
import json

URL = "http://192.168.106.170:54321/"

def law_recommend():
    st.title("法条推荐")

    # ================
    # 概述
    # ================
    st.header("♟ 概述 ♟")
    st.markdown("法条推荐是针对用户关于自身遇到的 `案情描述或疑问` 进行相关 `法条推荐` 的能力\n")

    # ================
    # 样例体验
    # ================
    st.header("♟ 样例体验 ♟")
    st.warning("可以简要描述自己的问题")

    default_text = "选民资格案件如何起诉?如何审理?"

    text = st.text_area("🍄 请输入体验文本:", value = default_text, key="law_recommend_sample")

    if st.button("点击解析"):
        try:
            requests.get(url = URL + "ping")
        except:
            st.error("服务未开启，请联系ASR基础研发部")

        try:
            parser_res = requests.post(url = URL + "queryRegex", data = json.dumps({"query": text})).json()
            st.success("解析完成")

            st.json(parser_res)
        except:
            st.error("解析失败，请稍后重试")
    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("点击查看 接口文档"):
        st.write("服务通过 HTTP/POST 进行服务解析请求\n")

        option = st.selectbox("入参/出参", ("入参 JSON", "出参 JSON"))
        if option == "入参 JSON":
            st.json({"query": "选民资格案件如何起诉?如何审理?"})

            st.write('\n')
            st.table(pd.DataFrame({
                "属性": ["query"],
                "类型": ["String"],
                "说明": ["待解析文本"]
            }))

        elif option == "出参 JSON":
            st.json({"code": True,
                     "answer": "(1)、公民不服选举委员会对选民资格的申诉所做处理决定..."})

            st.write('\n')
            st.table(pd.DataFrame({
                "属性": ["code", "data"],
                "类型": ["Bool", "String"],
                "说明": ["是否找到推荐法条", "返回法条"]
            }))


if __name__ == "__main__":
    law_recommend()