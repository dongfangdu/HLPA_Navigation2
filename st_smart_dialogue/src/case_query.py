import streamlit as st
import pandas as pd
import requests
import os.path as opt
from PIL import Image

IMAGE = opt.abspath(opt.join(__file__, opt.pardir, "case_query.png"))
SERVER_URL = "http://192.168.106.170:5005"
FORE_URL = "http://192.168.106.170:9995"

_default_samples = ["你好我想查下案子", "我的身份证是330501197804那个什么",
                    "是330501197804160037", "大概是去年的2月", "不是", "是的",
                    "我想查下我的承办法官是谁", "我那个案子现在到哪一步了",
                    "你说这个怎么样哎嘿跟你说话呢",
                    "你们这个有人工服务吗"]

default_samples = []
while _default_samples:
    default_samples.append("")
    default_samples.append(_default_samples.pop(0))
default_samples.append("")

_default_answer = [
    "欢迎体验智能语音服务,我们可以为您提供案件查询和其他服务，请问您需要什么帮助",
    "请告诉我您的身份证是多少",
    "身份证号码输入有误,请重新按键输入",
    "您好,请重新告诉我您去法院提出诉讼的大概日期",
    "查询到多个案子,照最新立案时间播报确认,"
    "请问案号是2019浙05执89号,当事人是袁建华,被执行人李春辉,董初升吗",
    "请问案号是2020浙民终525号,上述人是李春辉,董初升,被上诉人是袁建华吗",
    "请问您要查询什么信息",
    "您好,该案件的承办法官是谢芳,具体详情,您可登录移动微法院或浙江法院网查询,"
    "申请与您的承办法官线上进行沟通,请问还有什么需要帮您",
    "您好该案件的案件状态是已归档结案,请问还有什么需要帮您",
    "抱歉我没听清, 您需要查询什么信息呢",
    "好的我帮您转人工客服,您稍等"]

default_answer = []
while _default_answer:
    default_answer.append(_default_answer.pop(0))
    default_answer.append("")
default_answer.pop(-1)

def case_query():
    st.title("12368司法服务")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.markdown("**12368司法服务热线**，是便于用户根据自己的案子进行相关案件信息、进度查询的产品\n")
    st.markdown("目前已应用于湖州、杭州下城区等\n")

    # ===============
    # 流程图
    # ===============
    st.header("♟ 流程图 ♟")
    if st.checkbox("🍄 点击查看流程图"):
        image_1 = Image.open(IMAGE)
        st.image(image_1, caption="案件查询流程图", use_column_width = True)

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")
    if st.checkbox("🍄 点击查看样例对话"):
        chat1 = dict(User = default_samples, Bot = default_answer)
        st.table(chat1)

    # ===============
    # 交互体验
    # ===============
    st.header("♟ 交互体验 ♟")
    st.warning("体验环境为测试环境，解析可能存在延迟")
    st.warning("涉及身份证与日期请输入测试案例信息")

    try:
        requests.get(url = FORE_URL)
    except:
        st.error("服务未开启，请联系ASR基础研发部")

    href_url = FORE_URL
    st.markdown(f"[点击跳转至 **交互页面**]({href_url})")

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

            st.json({"q": "我想查下我一个案子"})

            st.write('\n')
            st.table(pd.DataFrame({
                "属性": ["sentence"],
                "类型": ["String"],
                "说明": ["用户文本"]
            }))

        elif option == "出参 JSON":

            st.json({"text": "请告诉我您的身份证",
                     "recipient_id": "123",
                     "customMessage": {}
                     })

            st.write('\n')
            st.table(pd.DataFrame({
                "属性": ["text", "recipient_id", "customMessage"],
                "类型": ["String", "String", "Any"],
                "说明": ["机器回话", "用户session_id", "自定义传出信息"]
            }))

    # ===============
    # 定制需求
    # ===============
    st.header("♟ 定制需求 ♟")
    if st.checkbox("点击查看 定制需求"):
        st.write("该能力持续优化中\n")
        st.write("同时也支持场景定制化")

if __name__ == "__main__":
    case_query()