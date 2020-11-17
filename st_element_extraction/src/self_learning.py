import streamlit as st
import pandas as pd
from PIL import Image

def self_learning():
    st.title("自学习")

    # ================
    # 概述
    # ================
    st.header("♟ 概述 ♟")
    st.write("我们提供了要素提取的自学习能力，方便在不同场景进行专名识别\n")

    # ================
    # 能力优势
    # ================
    st.header("♟ 能力优势 ♟")
    st.write("针对中文的传统要素提取模型存在一定的不足，主要包括以下几点")
    st.markdown("* 对个性化专名支持度低，训练需要收集有效且大量标注数据")
    st.markdown("* 需要专业人士进行模型设计到实现的全程参与，参与门槛较高")
    st.markdown("* 基于神经网络下的时间复杂度高导致应用的实时性不令人满意")
    st.markdown("* 整套预测系统对非预期结果的可控性低，难以实时调整")
    st.markdown("* 模型的泛化性和鲁棒性难以保证")

    st.write("\n")
    st.write("___")
    st.write("我们的要素提取能力具备灵活的自学习能力，主要具备以下优势")
    st.markdown("* 提供数据简单")
    st.markdown("* 多模型自我调整训练择优")
    st.markdown("* 在线模型学习、验证和上线")
    st.markdown("* 配置简易")

    # ================
    # 自学习流程
    # ================
    st.header("♟ 自学习流程 ♟")

    st.subheader("🍄 主要流程")
    st.markdown("```用户上传训练数据，并启动自学习服务，能力将输出模型并可进行验证和使用```")
    image_1 = Image.open('./img/self_learning_main.png')
    st.image(image_1, caption = "自学习主要流程")

    st.subheader("🍄 自学习架构")
    st.markdown("```自学习框架各子能力均可进行自由配置，但我们简易使用默认配置```")
    image_2 = Image.open("./img/self_learning.png")
    st.image(image_2, caption = "自学习架构")

    # ===============
    # 数据提供
    # ===============
    st.markdown("对于需要进行要素提取自学习的客户，我们建议其提供的数据包括")
    st.markdown("* 定义的要素类别")
    st.markdown("* 各类别下的典型词词典")
    st.markdown("* 包含词典词的典型句，每个词至少在2句话中出现")

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")

    default_samples = pd.DataFrame(
        [["fruit", "苹果", "我今天买了1斤苹果"],
         ["fruit", "苹果", "苹果上市的时间到了"],
         ["fruit", "香蕉", "这香蕉多少钱"],
         ["fruit", "香蕉", "香蕉味的酸奶"],
         ["fruit", "橘子", "电影中橘子象征死亡"],
         ["fruit", "橘子", "橘子颜色的猫"]],
        columns = ["要素类别", "典型词", "典型句"]
    )

    default_query = "火龙果真好吃"

    default_res = pd.DataFrame({"要素": ["火龙果"],
                                "标签": ["fruit"],
                                "开始位置": [0],
                                "结束位置": [3]})

    if st.checkbox("🍄 上传文本"):
        st.table(default_samples)

    if st.button("上传"):
        st.success("上传成功")
        st.success("训练完成")

    if st.button("🍄 验证文本"):
        st.success("解析完成")
        st.markdown("```" + default_query + "```")
        st.table(default_res)

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("接口文档"):
        st.write("未完成\n")

if __name__ == "__main__":
    self_learning()