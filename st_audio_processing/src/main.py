# -*- coding: utf-8 -*-

"""
__author__ = Wangyd
__copyright__ = Copyright 2020
__version__ = 0.1
__status = Dev
"""

import os

import streamlit as st

from mode import home_page, speech_enh, tts_zh, voice_conversion
from util.utils import get_doc_dir


def creat_layout() -> None:
    st.sidebar.title("功能清单")
    select_mode = st.sidebar.radio(
        "请选择其中一个功能",
        (
            "简介",
            "语音增强",
            "语音合成",
            "声音转换",
            # "接口文档",
            # "使用文档",
        ),
    )
    if select_mode == "简介":
        home_page()
    elif select_mode == "语音增强":
        speech_enh()
    elif select_mode == "语音合成":
        tts_zh()
    elif select_mode == "声音转换":
        voice_conversion()
    # elif select_mode == "接口文档":
    #     doc_I = open(os.path.join(get_doc_dir(), "接口文档.md"), "r").read()
    #     st.write(doc_I)
    # elif select_mode == "使用文档":
    #     doc_U = open(os.path.join(get_doc_dir(), "使用文档.md"), "r").read()
    #     st.write(doc_U)


def main():
    creat_layout()


if __name__ == "__main__":
    main()
