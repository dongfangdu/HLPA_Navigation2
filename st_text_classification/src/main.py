# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
from parag_classify import parag_classify
from senti_classify import senti_classify


def homepage():
    st.image("https://raw.githubusercontent.com/MaartenGr/boardgame/master/images/logo_small.jpg",
             use_column_width=True)
    st.title("文本分类功能服务")
    st.markdown("文本分类在文本处理中是很重要的一个模块，它的应用也非常广泛，比如：垃圾过滤，新闻分类，词性标注等等。它和其他的分类没有本质的区别，核心方法为首先提取分类数据的特征，然后选择最优的匹配，从而分类。该功能目前主要有：文本段落分类和情感分类。")


def create_layout():
    st.sidebar.title("菜单")
    app_mode = st.sidebar.selectbox("请选择其中一个功能", ["首页", "文本段落分类", "情感分类", "接口文档"])
    if app_mode == '首页':
        homepage()
    elif app_mode == '文本段落分类':
        parag_classify()
    elif app_mode == '情感分类':
        senti_classify()
    elif app_mode == "接口文档":
        st.write("接口文档待写")


def main():
    create_layout()


if __name__ == "__main__":
    main()
