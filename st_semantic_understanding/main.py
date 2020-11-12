import streamlit as st
import description, judge_mrc, text_correction, defraud
def run():
    mode_map = {0: "简介",
                1: "司法问答",
                2: "文本纠错",
                3: "敏感词过滤"}

    app_mode = st.sidebar.selectbox("语义理解",
                                    ["简介", "司法问答", "文本纠错", "敏感词过滤"])

    if app_mode == mode_map.get(0):
        description.description()

    elif app_mode == mode_map.get(1):
        judge_mrc.judge_mrc()

    elif app_mode == mode_map.get(2):
        text_correction.text_correction()

    elif app_mode == mode_map.get(3):
        defraud.defraud()

if __name__ == "__main__":
    run()