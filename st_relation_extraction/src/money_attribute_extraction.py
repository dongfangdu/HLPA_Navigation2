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
    st.write("本页可以通过调用分析接口，具体体会该功能的作用。")

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

    text = "合同上写明了借款是1万7千元。"
    annotated_text(
        "合同上写明了",
        ("借款", "", "#8ef"),
        "是",
        ("1万7千元", "", "#faa"),
        "。",
    )

    # st.markdown("There are several things you see on this page:".format(SPACES))
    # st.markdown(
    #     "{}🔹 On the **left** you can see how often the selected game was played "
    #     "in the last year. ".format(SPACES)
    # )
    # st.markdown(
    #     "{}🔹 You can see the **distribution** of scores for the selected game. ".format(
    #         SPACES
    #     )
    # )
    # st.markdown("{}🔹 The **frequency** of matches for each player. ".format(SPACES))
    # st.markdown(
    #     "{}🔹 The **top** and **bottom** players for the selected game.".format(SPACES)
    # )

    # # Prepare ordered selection of games
    # games = list(df.Game.unique())
    # games.sort()

    # # Select game and possibly a version of it
    # selected_game = st.selectbox("Select a game to explore.", games)
    # selected_game_df = df.loc[(df.Game == selected_game), :]
    # versions = list(selected_game_df.Version.unique())
    # versions.sort()
    # if len(versions) > 1:
    #     version = st.selectbox("Select a game to explore.", versions)
    #     selected_game_df = selected_game_df.loc[selected_game_df.Version == version, :]

    # return selected_game_df, selected_game
