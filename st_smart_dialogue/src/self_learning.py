import streamlit as st
import pandas as pd
from PIL import Image

def self_learning():
    st.title("自学习")

    # ================
    # 概述
    # ================
    st.header("♟ 概述 ♟")
    st.write("我们提供了智能对话的自学习能力，方便快速搭建不同场景的较简单案例\n")
    st.write("对于复杂的对话流程，我们建议进行定制化")

    # ================
    # 能力优势
    # ================
    st.header("♟ 能力优势 ♟")

    st.write("传统的对话管理方法，通过嵌套if-else进行")
    st.write("这种方法泛化性不高，对话流程设计门槛高，人力维护成本大")
    st.write("___")

    st.write("\n")
    st.write("我们的对话管理能力具备灵活的自学习能力，主要具备以下优势")
    st.markdown("* 工程框架完整，搭建方式简捷")
    st.markdown("* 多模支撑、小样本学习、自学习能力")
    st.markdown("* 提供全链路智能对话建设服务，标准化对接、多种系统协议支持，满足不同场景不同部署方式诉求")

    # ================
    # 自学习流程
    # ================
    st.header("♟ 自学习流程 ♟")

    st.markdown("对于需要进行自学习的客户，我们建议其提供的数据包括")
    st.markdown("* 意图标准句")
    st.markdown("* 要素标准词")
    st.markdown("* 话术集合")
    st.markdown("* 意图-话术执行对")

    st.table(pd.DataFrame({
        "属性": ["Intent_T", "Entity_T", "Template", "Action"],
        "类型": ["List[Dict]", "List[Dict]", "List[Dict]", "List[Tuple[Intent,Template]]"],
        "说明": ["意图标准句", "要素标准词", "话术集合", "意图-话术执行对"],
        "是否必须": ["是", "否", "是", "是"],
        "样例": [[{"intent": "weather", "text": ["查下天气", "天气如何"]}],
               [{"entity": "loc", "text": ["北京", "成都"]}],
               [{"idx": "T1", "text": ["你好", "不知道"]}],
               [("weather", "T1"), ("order", "T2")]]
    }))

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")

    default_samples_1 = pd.DataFrame({"intent": ["weather", "clock", "others"],
                                      "text": [["查下天气", "天气如何"],
                                               ["帮我设个明早7点的闹铃",
                                                "2小时候叫醒我"],
                                               ["的阿当的啊当"]]})
    default_samples_2 = pd.DataFrame({"entity": ["loc", "time"],
                                      "text": [["北京", "成都"],
                                               ["7点", "上午"]]})
    default_samples_3 = pd.DataFrame({"idx": ["T1", "T2", "T3"],
                                      "template": [["{loc}的天气良好", "{loc}温度为20摄氏度"],
                                                   ["已完成{time}的闹铃设置", "将在{time}唤醒您"],
                                                   ["抱歉我没听懂"]]})
    default_samples_4 = pd.DataFrame({"action": [("weather", "T1"),
                                                 ("order", "T2"),
                                                 ("others", "T3")]})

    default_query = "我想问下明早的天气如何"
    default_answer = "杭州的天气良好"

    if st.checkbox("🍄 上传文本"):
        st.table(default_samples_1)
        st.table(default_samples_2)
        st.table(default_samples_3)
        st.table(default_samples_4)

    if st.button("上传"):
        st.success("上传成功")
        st.success("训练完成")

    if st.button("🍄 验证文本"):
        st.success("解析完成")
        st.markdown("```" + default_query + "```")
        st.markdown("```" + default_answer + "```")

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("接口文档"):
        st.write("未完成\n")

    # ===============
    # 定制需求
    # ===============
    st.header("♟ 定制需求 ♟")
    if st.checkbox("定制需求"):
        st.write("对于复杂的对话场景\n")
        st.write("我们支持场景定制化")

if __name__ == "__main__":
    self_learning()