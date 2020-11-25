import pandas as pd
import streamlit as st
from PIL import Image


def self_learning():
    st.title("要素提取自学习")

    # ================
    # 概述
    # ================
    st.header("♟ 概述 ♟")
    st.markdown("我们提供了要素提取的自学习能力，方便在 `不同场景` 进行 `专名识别` \n")
    st.write("同时我部门也支持各场景的定制化\n")


    # ================
    # 能力优势
    # ================
    st.header("♟ 能力优势 ♟")
    st.markdown("针对中文的 `传统要素提取模型` 存在一定的不足，主要包括以下几点")
    st.markdown("* 个性化专名支持度低，需大量标注数据")
    st.markdown("* 需专业人士参与，门槛较高")
    st.markdown("* 应用实时性较低，非预期结果的可控性低")
    st.markdown("* 模型的泛化性难以保证")

    st.write("\n")
    st.write("___")
    st.markdown("我司的要素提取能力具备灵活的自学习能力，主要具备以下优势")
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
    image_1 = Image.open("./img/self_learning_main.png")
    st.image(image_1, caption="自学习主要流程", width = 200)

    st.subheader("🍄 自学习架构")
    st.markdown("```自学习框架各子能力均可进行自由配置，但我们简易使用默认配置```")
    image_2 = Image.open("./img/self_learning.png")
    st.image(image_2, caption="自学习架构", width = 700)

    # ===============
    # 数据提供
    # ===============
    st.subheader("🍄 数据提供")
    st.markdown("对于需要进行要素提取自学习的客户，我们建议其提供的数据包括")
    st.markdown("* 定义的要素类别")
    st.markdown("* 各类别下的典型词词典")
    st.markdown("* 包含词典词的典型句，每个词至少在2句话中出现")

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")
    st.warning("体验环境仅支持样例解析，暂不开放自定义输入，请上传训练文本再进行模型验证")

    default_samples = pd.DataFrame(
        [
            ["fruit", "苹果", "我今天买了1斤苹果"],
            ["fruit", "苹果", "苹果上市的时间到了"],
            ["fruit", "香蕉", "这香蕉多少钱"],
            ["fruit", "香蕉", "香蕉味的酸奶"],
            ["fruit", "橘子", "电影中橘子象征死亡"],
            ["fruit", "橘子", "橘子颜色的猫"],
        ],
        columns=["要素类别", "典型词", "典型句"],
    )

    default_query = "火龙果真好吃"

    default_res = pd.DataFrame(
        {"要素": ["火龙果"], "标签": ["fruit"], "开始位置": [0], "结束位置": [3]}
    )

    if st.checkbox("点击查看上传文本"):
        st.table(default_samples)

    if st.button("🍄 点击上传训练文本"):
        st.success("上传成功")
        st.success("训练完成")

    if st.button("🍄 点击验证模型"):
        st.success("解析完成")
        st.markdown("验证文本: ")
        st.markdown("```" + default_query + "```")
        st.table(default_res)

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("点击查看 接口文档"):
        st.write("未完成\n")


if __name__ == "__main__":
    self_learning()
