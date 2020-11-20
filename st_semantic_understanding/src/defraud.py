import streamlit as st
import pandas as pd
import requests
import json

URL = "http://192.168.106.170:9997/v1/api/"

def defraud():
    st.title("敏感词过滤")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.markdown("敏感词过滤是一项检测给定文本中是否 `存在敏感词` 的能力")

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")
    st.warning("体验环境为测试环境，建议文本长度在100字以内")

    default_sample = "在线出售雷管炸药各种炸药配方大全"

    # if st.checkbox("🍄 点击查看文本"):
    #     st.markdown("```" + default_text + "```")
    text = st.text_area("🍄 请输入体验文本:", value = default_sample, key="defraud_sample")

    if st.button("点击解析"):
        try:
            requests.get(url = URL + "ping")
        except:
            st.error("服务未开启，请联系ASR基础研发部")

        try:
            parser_res = requests.post(url = URL + "defraudParse", data = json.dumps({"sentence": text})).json()
            st.success("解析完成")

            st.table(pd.DataFrame.from_dict(parser_res.get("defraud")))

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
            st.json({"sentence": "在线出售雷管炸药各种炸药配方大全"})

            st.write('\n')
            st.table(pd.DataFrame({
                "属性": ["sentence"],
                "类型": ["String"],
                "说明": ["待解析文本"]
            }))

        elif option == "出参 JSON":
            st.json({"sentence": "在线出售雷管炸药各种炸药配方大全",
                     "defraud": [
                         {"word": 2,
                          "start": 6,
                          "end": "出售雷管"},
                         {"word": 6,
                          "start": 8,
                          "end": "炸药"},
                         {"word": 8,
                          "start": 16,
                          "end": "各种炸药配方大全"}
                     ]})

            st.write('\n')
            st.write('仅需要返回结果的 defraud 字段')
            st.table(pd.DataFrame({
                "属性": ["word", "start", "end"],
                "类型": ["String", "Int", "Int"],
                "说明": ["敏感词", "开始位置", "结束位置"]
            }))

    # ===============
    # 自定义热词词典
    # ===============
    st.header("♟ 热词词典 ♟")
    if st.checkbox("点击查看 热词词典"):
        st.write("该能力支持动态增删敏感词供模型使用")

        st.markdown("```\n"
                    "在指定预料库中添加自定义的 txt 文件")

        st.write("其中 txt 示例格式如下")
        st.markdown("```\n"
                    "硝酸甘油炸弹制作\n"
                    "TNT炸弹的制作\n"
                    "```")


if __name__ == "__main__":
    defraud()