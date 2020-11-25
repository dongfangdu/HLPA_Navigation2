import streamlit as st
import pandas as pd

def tele_outbound():
    st.title("司法外呼")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.markdown("司法外呼, 是方便法院提醒特定目标人相关案件的履行职责进度的一项能力\n")
    st.markdown("能力对接工单系统，定时发送提醒电话或短信等")

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")
    st.warning("体验环境为测试环境，仅支持样例解析，暂不开放自定义输入")

    if st.checkbox("🍄 点击查看样例对话 1"):
        st.markdown("|Bot|User|\n"
                    "|---|---|\n"
                    "|您好，这里是杭州上城区人民法院，请问您是xxx吗？||\n"
                    "||对啊是我怎么了|\n"
                    "|被告人xxx，您好。由杭州上城区人民法院做出的。<br>原告xxx与您未还钱一案法律文书已发生法律效力。<br>请问您是否已经履行||\n"
                    "||好像没有暂时没空|\n"
                    "|您注意，逾期不履行，申请人xxx有权申请强制执行。<br>对于规避执行的，根据情节轻重，予以罚款拘留；<br>构成拒执罪的，依法追究刑事责任。请问您是否已经知晓||\n"
                    "||好我知道了|\n"
                    "|好的再见||\n"
                    "||再见嘛|\n", unsafe_allow_html = True)

    if st.checkbox("🍄 点击查看样例对话 2"):
        st.markdown("|Bot|User|\n"
                    "|---|---|\n"
                    "|您好，这里是杭州上城区人民法院，请问您是xxx吗？||\n"
                    "||是我|\n"
                    "|被告人xxx，您好。由杭州上城区人民法院做出的。<br>原告xxx与您未还钱一案法律文书已发生法律效力。<br>请问您是否已经履行||\n"
                    "||什么东西我听不清|\n"
                    "|被告人xxx，您好。由杭州上城区人民法院做出的。<br>原告xxx与您未还钱一案法律文书已发生法律效力。<br>请问您是否已经履行||\n"
                    "||哦哦履行了已经弄了|\n"
                    "|好的再见||\n"
                    "||嗯|\n", unsafe_allow_html=True)
    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("点击查看 接口文档"):
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
                "说明": ["用户文本", "自定外呼当事人信息"]
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
    if st.checkbox("点击查看 定制需求"):
        st.write("客服大脑能力支持场景定制化")

if __name__ == '__main__':
    tele_outbound()