import streamlit as st
import description, case_query, tele_outbound, etc, property, self_learning

def run():
    mode_map = {0: "简介",
                1: "12368司法服务",
                2: "司法外呼",
                3: "ETC销售",
                4: "物业咨询",
                5: "自学习"}

    app_mode = st.sidebar.radio("请选择其中一个功能",
                                    ["简介", "12368司法服务", "司法外呼", "ETC销售", "物业咨询", "自学习"])

    if app_mode == mode_map.get(0):
        description.description()

    elif app_mode == mode_map.get(1):
        case_query.case_query()

    elif app_mode == mode_map.get(2):
        tele_outbound.tele_outbound()

    elif app_mode == mode_map.get(3):
        etc.etc()

    elif app_mode == mode_map.get(4):
        property.property()

    elif app_mode == mode_map.get(5):
        self_learning.self_learning()

if __name__ == "__main__":
    run()
