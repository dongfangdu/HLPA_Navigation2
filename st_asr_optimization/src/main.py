# -*- coding: utf-8 -*-
import streamlit as st


def homepage():
    # st.image(
    #     "https://raw.githubusercontent.com/MaartenGr/boardgame/master/images/logo_small.jpg",
    #     use_column_width=True,
    # )
    st.title("引擎识别效果优化服务")
    st.markdown(
        "语音识别算法目前虽已日趋完善，但语音识别系统的性能受多方面影响，如口语化，方言，短词，语速，音量，噪声等。在不同的应用场景中，往往遇到各种各样的问题影响引擎的最终识别结果。如何因地制宜，差异性地解决这些问题造成的不良影响，提升引擎的识别准确率，是优化声学模型的一项重要准则。引擎识别效果优化主要从声学模型优化和语音模型优化两个方面进行。"
    )


def acoustic_model():
    st.title("声学模型优化")
    st.markdown(
        "我们采用有监督学习和无监督学习结合的方法，即自学习系统。自学习系统是一套自动优化声学模型识别率的工具，其减少优化声学模型过程中不必要的成本消耗，提升方法的可复用性。"
    )
    st.markdown(
        "首先，自学习系统通过语音增强扩充标注数据以及通过非线性回归和 LDA算法预测识别音频的识别率来挑选数据，以此扩充训练数据，减少人工标注成本，其中语音增强算法通过音量增强、语音去噪及语音转换等多种方法来抑制背景噪声，改善音频质量，以及减少口音对语音识别结果的影响，从而提高了语音识别结果的准确率。"
    )
    st.markdown(
        "其次，自学习系统采用docker配置，可以一键启动、停止、删除、重启，启动后系统会自动训练，只需配以相关参数即可，该系统以声学模型基础模型为起点进行训练，亦可自定义基础模型，从而使训练得到的声学模型的识别率在特定用户场景下相比基础模型有显著提升。"
    )
    st.markdown(
        "最后，自学习系统会自动将自动训练生成的模型进行测试，并自动将测试结果录入数据库以及生成测试报告。本系统已经应用于带有四川方言的普通话的声学模型优化当中，声学模型识别率已从基础模型识别率的83%提升到优化后的89%，优化效果显著。"
    )


def voice_model():
    st.title("语言模型优化")
    st.markdown(
        "语言模型采用N-gram模型，统计语言模型就是计算一个句子的概率值大小，整句的概率就是各个词出现概率的乘积，概率值越大表明该句子越合理。N-gram是典型的统计语言模型，它做出了一种假设，当前词的出现只与前面N-1个词相关，而与其它任何词都不相关，整句的概率就是各个词出现概率的乘积。"
    )
    st.markdown("我们针对不同地域的语言文本，复制大量该地域的语言文本，训练N-gram语言模型，加大该地域的语言识别概率值，以提升引擎识别效果。")


def create_layout():
    st.sidebar.title("菜单")
    app_mode = st.sidebar.radio("请选择其中一个功能", ["简介", "声学模型优化", "语言模型优化"])
    if app_mode == "简介":
        homepage()
    elif app_mode == "声学模型优化":
        acoustic_model()
    elif app_mode == "语言模型优化":
        voice_model()


def main():
    create_layout()


if __name__ == "__main__":
    main()
