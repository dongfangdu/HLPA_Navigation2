import streamlit as st
import pandas as pd

default_samples = ["您好，这里是杭州上城区人民法院，请问您是xxx吗？",
                   "",
                   "被告人xxx，您好。由杭州上城区人民法院做出的。原告xxx与您未还钱一案法律文书已发生法律效力。请问您是否已经履行",
                   "",
                   "您注意，逾期不履行，申请人周永强有权申请强制执行。对于规避执行的，根据情节轻重，予以罚款拘留；构成拒执罪的，依法追究刑事责任。请问您是否已经知晓",
                   "",
                   "好的再见",
                   ""]
default_answers = ["",
                   "对啊是我怎么了",
                   "",
                   "好像没有暂时没空",
                   "",
                   "好我知道了",
                   "",
                   "再见嘛"]

default_samples_2 = ["您好，这里是杭州上城区人民法院，请问您是xxx吗？",
                     "",
                     "被告人xxx，您好。由杭州上城区人民法院做出的。原告xxx与您未还钱一案法律文书已发生法律效力。请问您是否已经履行",
                     "",
                     "被告人xxx，您好。由杭州上城区人民法院做出的。原告xxx与您未还钱一案法律文书已发生法律效力。请问您是否已经履行",
                     "",
                     "好的再见",
                     ""]
default_answers_2 = ["",
                     "是我",
                     "",
                     "什么东西我听不清",
                     "",
                     "哦哦履行了已经弄了",
                     "",
                     "嗯"]

def tele_outbound():
    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.markdown(">**司法外呼**")
    st.markdown(">是方便法院提醒特定目标人相关案件的履行职责进度的一项能力")
    st.markdown(">能力对接工单系统，定时发送提醒电话或短信等")

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")

    if st.checkbox("🍄 点击查看样例对话 1"):
        chat1 = dict(Bot = default_samples,
                     User = default_answers)

        st.table(chat1)

    if st.checkbox("🍄 点击查看样例对话 2"):
        chat2 = dict(Bot = default_samples_2,
                     User = default_answers_2)

        st.table(chat2)

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("接口文档"):
        st.write("服务通过 HTTP/POST 进行服务解析请求\n")

        option = st.selectbox("入参/出参", ("入参 JSON", "出参 JSON"))
        if option == "入参 JSON":
            st.markdown("**访问地址**")
            st.write("在访问地址上，使用不同的 session_id 进行每个用户的对话流程管理")
            st.markdown("```" + "http//$ip:$port/conversations/$session_id/respond""```")

            st.json({"q": "对啊是我怎么了",
                     "customMessage": {}})

            st.write('\n')
            st.table(pd.DataFrame({
                "属性": ["sentence", "customMessage"],
                "类型": ["String", "Any"],
                "说明": ["用户文本", "自定传入信息"]
            }))

        elif option == "出参 JSON":
            st.json({"text": "被告人xxx，您好",
                     "recipient_id": "123",
                     })

            st.write('\n')
            st.table(pd.DataFrame({
                "属性": ["text", "recipient_id"],
                "类型": ["String", "String"],
                "说明": ["机器回话", "用户session_id"]
            }))

    # ===============
    # 定制需求
    # ===============
    st.header("♟ 定制需求 ♟")
    if st.checkbox("定制需求"):
        st.write("该能力持续优化中\n")
        st.write("同时也支持场景定制化")

if __name__ == '__main__':
    tele_outbound()