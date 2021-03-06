import streamlit as st
import pandas as pd
import requests
import json

URL = "http://192.168.106.170:9994"

def medicine_ner():
    st.title("医疗要素提取")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.markdown("医疗要素提取，是适用于病历场景下的要素提取能力")
    st.markdown("该能力是主要针对 `糖尿病` 临床指南背景，提供 `15 类` 要素供以提取使用")
    st.markdown("该能力是 `自学习/定制化（见自学习）` 的一种体现")

    # ===============
    # 字段
    # ===============
    st.header("♟ 要素字段 ♟")

    st.subheader("🍄 疾病相关")
    entity_df_1 = pd.DataFrame({"字段": ["Disease", "Symptom", "Test", "Method", "Test_Value"],
                                "要素": ["疾病名称", "病因", "临床表现", "检查方法", "检查指标值"],
                                "样例": ["I型糖尿病", "胰岛素抵抗", "头晕", "SPARC", ">11.3 mmol/L"]})
    st.table(entity_df_1)

    st.subheader("🍄 治疗相关")
    entity_df_2 = pd.DataFrame({"字段": ["Drug", "Frequency", "Amount", "Method", "Treatment", "Operation", "SideEff"],
                                "要素": ["药品名称", "用药频率", "用药剂量", "用药方法", "非药治疗", "手术", "不良反应"],
                                "样例": ["胰岛素", "一天两次", "500mg/d", "口服", "针灸", "代谢手术", "消化道不良反应"]})
    st.table(entity_df_2)

    st.subheader("🍄 常规实体")
    entity_df_3 = pd.DataFrame({"字段": ["部位", "程度", "持续时间"],
                                "要素": ["Anatomy", "Level", "Duration"],
                                "样例": ["胰岛细胞", "严重", "10周"]})
    st.table(entity_df_3)

    # ===============
    # 样例体验
    # ===============
    # st.header("♟ 样例体验 ♟")
    #
    # st.warning("体验环境为测试环境，仅支持样例解析，暂不开放自定义输入")
    #
    # default_sample = "在糖耐量受损( IGT)和 2型糖尿病的 ZDF 大鼠模型中,持续高血糖 10周后,大鼠 DRG 组织和坐骨神经氧化应激水平明显上升"
    # default_res = pd.DataFrame({
    #     "要素": ["糖耐量受损", "IGT", "2型糖尿病", "血糖", "10周", "DRG", "坐骨神经", "明显上升"],
    #     "标签": ["Disease", "Disease", "Disease", "Test", "Duration", "Anatomy", "Anatomy", "Test_Value"],
    #     "开始位置": [1, 8, 14, 34, 37, 45, 52, 62],
    #     "结束位置": [6, 11, 19, 36, 40, 48, 56, 66]
    # })
    #
    # st.markdown("🍄 **输入文本: **")
    #
    # st.markdown("```" + default_sample + "```")
    # if st.button("点击解析"):
    #     st.success("解析完成")
    #     st.table(default_res)
    
    st.header("♟ 样例体验 ♟")
    st.warning("体验环境为测试环境，建议文本长度在100字以内，解析可能存在延迟")

    try:
        requests.get(url=URL)
    except:
        st.error("服务未开启，请联系ASR基础研发部")

    default_sample = "在糖耐量受损( IGT)和 2型糖尿病的 ZDF 大鼠模型中,持续高血糖 10周后,大鼠 DRG 组织和坐骨神经氧化应激水平明显上升"

    text = st.text_area("🍄 请输入体验文本:", value = default_sample, key="medical_ner_sample_parser")

    if st.button("点击解析"):
        try:
            parser_res = requests.post(url = URL + "/parse", data = json.dumps({"q": text})).json()
            st.success("解析完成")
 
            entities = parser_res.get("entities")

            st.table(pd.DataFrame({"要素": [x["value"] for x in entities],
                                   "标签": [x["entity"] for x in entities],
                                   "开始位置": [x["start"] for x in entities],
                                   "结束位置": [x["end"] for x in entities]}))

        except:
            st.error("解析失败，请稍后重试")

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("点击查看 接口文档"):
        st.write("参考 公共类要素提取\n")

    # ===============
    # 部署文档
    # ===============
    st.header("♟ 部署文档 ♟")
    if st.checkbox("点击查看 部署文档"):
        st.write("参考 公共类要素提取\n")

if __name__ == "__main__":
    medicine_ner()