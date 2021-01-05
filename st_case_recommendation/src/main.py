# -*- coding: utf-8 -*-


import streamlit as st

import case_recommend
import homepage


def create_layout():
    st.sidebar.title("菜单")
    app_mode = st.sidebar.radio("请选择其中一个功能", ["简介", "文书推荐"])
    if app_mode == "简介":
        homepage.description()
    elif app_mode == "文书推荐":
        case_recommend.jdoc_recommend()
    # elif app_mode == "接口文档":
    #     st.write("接口文档待写")
    #     # body = " ".join(open("files/instructions.md", 'r').readlines())
    #     # st.markdown(body, unsafe_allow_html=True)


def main():
    create_layout()


if __name__ == "__main__":
    main()
