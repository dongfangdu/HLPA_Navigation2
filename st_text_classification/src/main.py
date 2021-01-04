# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st

from parag_classify import parag_classify
from senti_classify import senti_classify


def homepage():
    # st.image("https://raw.githubusercontent.com/MaartenGr/boardgame/master/images/logo_small.jpg",
    #          use_column_width=True)
    st.title("文本分类功能服务")
    st.markdown(
        "文本分类在文本处理中是基础而且十分重要的一个模块，它的应用也非常广泛，比如：垃圾过滤，新闻分类等等。应用效果很大程序取决于实际场景的`数据模式`和`业务标注`。"
    )

    st.header("♟ 应用场景 ♟")
    st.subheader("🔹 文书段落分类")
    st.markdown("文书是一类书写结构规范的`应用类文本`，每块段落都有相对固定的描述和用途，段落分类有利于细化不同类别段落的信息提取。")

    st.subheader("🔹 情感分类")
    st.markdown("针对用户评论等信息，评估用户对某商品或某事件的好恶倾向。")


def create_layout():
    st.sidebar.title("菜单")
    app_mode = st.sidebar.radio("请选择其中一个功能", ["简介", "裁判文书段落分类", "情感分类"])
    if app_mode == "简介":
        homepage()
    elif app_mode == "裁判文书段落分类":
        parag_classify()
    elif app_mode == "情感分类":
        senti_classify()
    # elif app_mode == "接口文档":
    #     st.write("接口文档待写")


def main():
    create_layout()


if __name__ == "__main__":
    main()
