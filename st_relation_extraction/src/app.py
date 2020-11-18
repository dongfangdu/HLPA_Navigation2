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
from annotated_text import annotated_text


def main():
    # link_to_data, is_loaded_header = load_data_option()
    # df, player_list, exception = load_external_data(link_to_data)

    # if not exception:
    #     create_layout(df, player_list, is_loaded_header)
    # else:
    #     st.sidebar.text(str(exception))
    #     st.title("⭕️The data was not correctly loaded")
    #     preprocessing_tips()

    create_layout()


# def load_data_option() -> Tuple[str, st.delta_generator.DeltaGenerator]:
#     """ Prepare options for loading data"""
#     is_loaded_header = st.sidebar.subheader("⭕️ Data not loaded")
#     link_to_data = st.sidebar.text_input(
#         "Link to data",
#         "https://github.com/MaartenGr/boardgame/blob/master/files/matches.xlsx?raw=true",
#     )

#     return link_to_data, is_loaded_header


# @st.cache
# def load_external_data(link: str) -> Tuple[pd.DataFrame, List[str], Exception]:
#     """Load data from a link and preprocess it

#     Parameters:
#     -----------

#     link : str
#         Link to the data (should be hosted online)

#     Returns:
#     --------

#     df : pandas.core.frame.DataFrame | False
#         The data loaded and preprocessed.
#         If there is an issue loading/preprocessing then it
#         returns False instead.

#     player_list : list | False
#         List of players that have been in any board game match.
#         If there is an issue with loading/preprocessing the data
#         then it returns False instead.

#     exception : False | Exception
#         If there is something wrong with preprocessing,
#         return Exception, otherwise return False
#     """

#     exception = False
#     try:
#         df, player_list = preprocessing.prepare_data(link)
#         return df, player_list, exception
#     except Exception as exception:
#         return False, False, exception


def load_homepage() -> None:
    """"""
    image = Image.open("./images/logo.png")
    st.image(
        # "https://raw.githubusercontent.com/MaartenGr/boardgame/master/images/logo_small.jpg",
        image,
        use_column_width=True,
    )
    st.markdown("> 🔶关系属性抽取服务")
    st.write(
        "**关系抽取（Relation Extraction, RE）**是自然语言处理中信息抽取任务之一。该任务的定义是，给定标注了两个实体的句子，返回两个实体之间的语义关系。关系抽取任务得到的结果常用于问答系统和知识图谱等应用，是基础且重要的自然语言处理任务。"
    )
    st.write("**属性抽取（Entity Attribute Extraction, EAE）**是自然语言处理中信息抽取的任务之一。")
    st.markdown(
        "<div align='center'><br>"
        "<img src='https://img.shields.io/badge/MADE%20WITH-PYTHON%20-red?style=for-the-badge'"
        "alt='API stability' height='25'/>"
        "<img src='https://img.shields.io/badge/SERVED%20WITH-Fastapi-blue?style=for-the-badge'"
        "alt='API stability' height='25'/>"
        "<img src='https://img.shields.io/badge/DASHBOARDING%20WITH-Streamlit-green?style=for-the-badge'"
        "alt='API stability' height='25'/></div>",
        unsafe_allow_html=True,
    )
    for i in range(3):
        st.write(" ")
    st.header("📕 Dashboard应用说明")
    st.write("本应用是基于Streamlit开发的，用于展示部分NLP能力的基本使用方式。")
    st.write("现阶段开放下列功能：")
    st.subheader("♟ 金额属性抽取 ♟")
    st.markdown("* 给定一段文本，抽取出所有金额数，以及该金额数对应的类型属性。")
    st.write("比如：")
    st.write("输入文本： 合同上写明了借款是1万7千元。")
    st.write("可以解析获得：(1万7千元, 用于, 借款)")

    annotated_text(
        "合同上写明了",
        ("借款", "", "#8ef"),
        "是",
        ("1万7千元", "", "#faa"),
        "。",
    )
    # st.subheader("♟ Player Statistics ♟")
    # st.markdown(
    #     "* As you play with other people it would be interesting to see how they performed. "
    #     "This page allows you to see, per player, an overview of their performance across games."
    # )
    # st.markdown(
    #     "* This also includes a one-sample Wilcoxon signed-rank test to test if a player performs "
    #     "significantly better/worse than the average for one board game."
    # )
    # st.subheader("♟ Head to Head ♟")
    # st.markdown(
    #     "* I typically play two-player games with my wife and thought it would be nice to include a "
    #     "head to head page. This page describes who is the better of two players between and within games."
    # )
    # st.subheader("♟ Explore Games ♟")
    # st.markdown(
    #     "* This page serves to show statistics per game, like its distribution of scores, frequency of "
    #     "matches and best/worst players."
    # )


def create_layout(
    # df: pd.DataFrame,
    # player_list: List[str],
    # is_loaded_header: st.delta_generator.DeltaGenerator,
) -> None:

    # is_loaded_header.subheader("✔️Data is loaded")
    st.sidebar.title("菜单")
    app_mode = st.sidebar.selectbox(
        "请选择其中一个功能",
        [
            "简介",
            "金额属性抽取",
            "使用文档",
            "接口文档",
            # "Data Exploration",
            # "Player Statistics",
            # "Game Statistics",
            # "Head to Head",
        ],
    )
    if app_mode == "简介":
        load_homepage()
        # preprocessing_tips()
    elif app_mode == "使用文档":
        body = " ".join(open("files/instructions.md", "r").readlines())
        st.markdown(body, unsafe_allow_html=True)
    elif app_mode == "接口文档":
        body = " ".join(
            codecs.open("files/openapi.md", "r", encoding="utf8").readlines()
        )
        st.markdown(body, unsafe_allow_html=True)
    elif app_mode == "金额属性抽取":
        money_attribute_extraction.load_page()
    # elif app_mode == "Data Exploration":
    #     generalstats.load_page(df)
    # elif app_mode == "Player Statistics":
    #     playerstats.load_page(df, player_list)
    # elif app_mode == "Game Statistics":
    #     exploregames.load_page(df, player_list)
    # elif app_mode == "Head to Head":
    #     headtohead.load_page(df, player_list)


# def preprocessing_tips() -> None:
#     """ Description of how to process the data and in which format. """
#     st.header("🎲 Tips for preparing your data")
#     st.write("Make sure your dataset is in a xlsx (excel) format.")
#     st.write(
#         "Make sure it has the structure as seen below with the exact same column names"
#         ", same structure for scoring points, same structure for players that participated, and "
#         "make sure to use the same date format. Any changes to this structure will break the "
#         "application. "
#     )

#     example_df = pd.DataFrame(
#         [
#             [
#                 "2018-11-18",
#                 "Peter+Mike",
#                 "Qwixx",
#                 "Peter77+Mike77",
#                 "Peter+Mike",
#                 "Normal",
#             ],
#             [
#                 "2018-11-18",
#                 "Chris+Mike",
#                 "Qwixx",
#                 "Chris42+Mike99",
#                 "Mike",
#                 "Big Points",
#             ],
#             ["2018-11-22", "Mike+Chris", "Jaipur", "Mike84+Chris91", "Chris", "Normal"],
#             [
#                 "2018-11-30",
#                 "Peter+Chris+Mike",
#                 "Kingdomino",
#                 "Chris43+Mike37+Peter35",
#                 "Chris",
#                 "5x5",
#             ],
#         ],
#         columns=["Date", "Players", "Game", "Scores", "Winner", "Version"],
#     )
#     st.write(example_df)

#     st.write("An example of the data can be found here:")
#     st.write("https://github.com/MaartenGr/boardgame/blob/dev/files/matches.xlsx")


if __name__ == "__main__":
    main()
