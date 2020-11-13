import streamlit as st
import pandas as pd

default_samples = ["您好，这里是麓湖物业服务中心，请问有什么可以帮您",
                   "",
                   "先生，很抱歉，我们的专车服务已经取消了，但是麓湖范围内出行是有大巴车的，您可以到蓝花屿附近站点乘坐大巴车到白玉台组团。",
                   "",
                   "在2019年10月份取消的，我们在组团公告栏及业主群都有发相关温馨提示，可能您没有注意到，还请谅解。",
                   "",
                   "是这样的，专车是公司考虑到客户前期在麓湖出行多有不便所提供的温暖服务，后期随着周边配套的不断完善、地铁开通、网约车的普及，客户对专车服务的需求频次越来越低，所以我们取消了专车服务，但是开通了大巴车供业主麓湖范围内的出行。",
                   "",
                   "各个已交付组团附近都有固定的站点，你只需要根据时刻表在站上乘坐即可。",
                   "",
                   "不客气的，还有其他需要帮您的吗？",
                   "",
                   "好的，祝您生活愉快，再见！"]
default_answers = ["",
                   "我要叫个车，从蓝花屿到白玉台",
                   "",
                   "客户：啥子时候取消的，我咋个不晓得呢",
                   "",
                   "为啥子要取消呢",
                   "",
                   "那好的，我知道了。大巴车怎么乘坐呢？",
                   "",
                   "客户：那行，我明白了，谢谢",
                   "",
                   "没有了",
                   ""]

def property():
    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.markdown(">**物业咨询**")
    st.markdown(">是某物业为其设置的专车服务智能客服功能")

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")

    if st.checkbox("🍄 点击查看样例对话 1"):
        chat1 = dict(Bot=default_samples,
                     User=default_answers)

        st.table(chat1)

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("接口文档"):
        st.markdown("见 **12368司法服务热线**")

    # ===============
    # 定制需求
    # ===============
    st.header("♟ 定制需求 ♟")
    if st.checkbox("定制需求"):
        st.write("该能力持续优化中\n")
        st.write("同时也支持场景定制化")

if __name__ == '__main__':
    property()