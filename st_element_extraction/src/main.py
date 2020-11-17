import streamlit as st
import description, hotword_mining, judge_ner, medicine_ner, public_ner, self_learning

def run():
    mode_map = {0: "简介",
                1: "公共要素提取",
                2: "医疗要素提取",
                3: "文书要素提取",
                4: "热词发现",
                5: "要素提取自学习"}

    app_mode = st.sidebar.selectbox("要素提取",
                                    ["简介", "公共要素提取", "医疗要素提取", "文书要素提取", "热词发现", "要素提取自学习"])

    if app_mode == mode_map.get(0):
        description.description()

    elif app_mode == mode_map.get(1):
        public_ner.public_ner()

    elif app_mode == mode_map.get(2):
        medicine_ner.medicine_ner()

    elif app_mode == mode_map.get(3):
        judge_ner.judge_ner()

    elif app_mode == mode_map.get(4):
        hotword_mining.hotword_mining()

    elif app_mode == mode_map.get(5):
        self_learning.self_learning()

if __name__ == "__main__":
    run()