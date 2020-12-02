import streamlit as st
import description, judge_mrc, text_correction, defraud, text_summary
def run():
    mode_map = {0: "简介",
                1: "司法问答",
                2: "文本纠错",
                3: "敏感词过滤",
                4: "文本摘要"}

    app_mode = st.sidebar.radio("请选择其中一个功能",
                                ["简介", "司法问答", "文本纠错", "敏感词过滤", "文本摘要"])

    if app_mode == mode_map.get(0):
        description.description()

    elif app_mode == mode_map.get(1):
        judge_mrc.judge_mrc()

    elif app_mode == mode_map.get(2):
        text_correction.text_correction()

    elif app_mode == mode_map.get(3):
        defraud.defraud()

    elif app_mode == mode_map.get(4):
        text_summary.text_summary()

if __name__ == "__main__":
    run()
