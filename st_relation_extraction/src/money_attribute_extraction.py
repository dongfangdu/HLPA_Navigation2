from typing import List, Tuple

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from annotated_text import annotated_text

SPACES = "&nbsp;" * 10


def load_page() -> None:

    prepare_layout()
    # plot_distribution(selected_game_df)
    # plot_frequent_players(selected_game_df, player_list)
    # show_min_max_stats(selected_game_df, selected_game)
    # sidebar_activity_plot(selected_game_df)


def prepare_layout() -> None:
    """[summary]"""

    st.title("📕 金额属性抽取")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.write("金额属性可以通过调用分析接口，具体体会该功能的作用。")

    # annotated_text(
    #     "This ",
    #     ("is", "", "#8ef"),
    #     " some ",
    #     ("annotated", "", "#faa"),
    #     ("text", "", "#afa"),
    #     " for those of ",
    #     ("you", "", "#fea"),
    #     " who ",
    #     ("like", "", "#8ef"),
    #     " this sort of ",
    #     ("thing", "", "#afa"),
    # )

    # ===============
    # 示例
    # ===============
    st.header("♟ 示例 ♟")

    st.markdown("🍄 **示例文本: **")

    default_text = "合同上写明了借款是1万7千元。"
    st.markdown("```" + default_text + "```")

    st.markdown("🍄 **分析结果: **")
    annotated_text(
        "合同上写明了",
        ("借款", "", "#8ef"),
        "是",
        ("1万7千元", "", "#faa"),
        "。",
    )

    # ===============
    # 接口调用
    # ===============
    st.header("♟ 接口调用 ♟")

    st.markdown("🍄 **输入文本: **")

    text = st.text_area("待分析文本", default_text, key=f"money_attr_text")

    if st.button("分析"):
        pass
        print(text)

    else:
        st.write("请点击推荐")


def reform_attr_res():
    pass
