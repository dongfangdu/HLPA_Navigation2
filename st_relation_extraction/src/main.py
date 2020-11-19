# -*- encoding: utf8 -*-

"""
__author__ = Jocky Hawk
__copyright__ = Copyright 2020
__version__ = 0.1
__status = Dev
"""


import codecs
from typing import List, Tuple

import pandas as pd

# Custom packages
# import preprocessing
import streamlit as st
from PIL import Image

import money_attribute_extraction


def main():

    create_layout()


def load_homepage() -> None:

    st.title("关系属性抽取")
    st.header("♟ 概述 ♟")
    st.write(
        "**关系抽取（Relation Extraction, RE）**是自然语言处理中信息抽取任务之一。该任务的定义是，给定标注了两个实体的句子，返回两个实体之间的语义关系。关系抽取任务得到的结果常用于问答系统和知识图谱等应用，是基础且重要的自然语言处理任务。"
    )
    st.write("**属性抽取（Entity Attribute Extraction, EAE）**是自然语言处理中信息抽取的任务之一。")

    st.header("♟ 应用场景 ♟")
    st.subheader("♟ 金额属性抽取 ♟")
    st.markdown("* 给定一段文本，抽取出所有金额数，以及该金额数对应的类型属性。")


def create_layout() -> None:

    st.sidebar.title("功能清单")
    app_mode = st.sidebar.radio(
        "请选择其中一个功能",
        [
            "简介",
            "金额属性抽取",
        ],
    )
    if app_mode == "简介":
        load_homepage()
    elif app_mode == "金额属性抽取":
        money_attribute_extraction.load_page()


if __name__ == "__main__":
    main()
