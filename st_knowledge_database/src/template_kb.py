import streamlit as st
import pandas as pd

def template_kb():
    st.title("话术知识库")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.write("话术知识库是通过根据已构建的 问题-话术对 进行回复的能力")

    # ===============
    # 数据提供
    # ===============
    st.markdown("构建专属话术知识库，我们建议其提供的数据包括")
    st.markdown("* 标准问题")
    st.markdown("* 相似问题")
    st.markdown("* 问题对应的标准答案")

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")

    default_samples = pd.DataFrame(
        [["conn_layer", "我想联系法官", "可登录浙江移动微法院查询"],
         ["conn_layer", "负责我的法官怎么联系", "可登录浙江移动微法院查询"],
         ["ask_path", "如何到达浙高院", "通过地铁2号线沈塘桥站到达"]],
        columns = ["唯一id", "标准/相似问", "标准答案"]
    )

    default_query = "查下案子的负责人"

    default_res = "可登录浙江移动微法院查询"

    if st.checkbox("🍄 点击查看样例"):
        st.table(default_samples)

    if st.button("上传"):
        st.success("上传成功")

    if st.button("🍄 验证文本"):
        st.markdown("**问题**")
        st.markdown("```" + default_query + "```")
        st.success("解析完成")
        st.markdown("**回复话术**")
        st.markdown("```" + default_res + "```")

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("接口文档"):
        st.write("未完成\n")


if __name__ == "__main__":
    template_kb()