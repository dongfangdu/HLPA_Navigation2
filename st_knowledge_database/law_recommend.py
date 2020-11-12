import streamlit as st
import pandas as pd

def law_recommend():
    st.title("法条推荐")

    # ================
    # 概述
    # ================
    st.header("♟ 概述 ♟")
    st.write("法条推荐是针对用户关于自身遇到的案情疑问进行相关法条推荐的能力\n")

    # ================
    # 样例体验
    # ================
    st.header("♟ 样例体验 ♟")

    default_text = "选民资格案件如何起诉?如何审理?"

    default_answer = "(1)、公民不服选举委员会对选民资格的申诉所做处理决定,可以在选举日的五日以前向选区所在地基层法院起诉。(2)、法院受理选民资格案件后,必须在选举日前审结。审理时,起诉人、选举委员会的代表和有关公民必须参加。法院的判决书,应当在选举日前送达选举委员会和起诉人,并通知有关公民。"

    if st.checkbox("🍄 点击查看文本"):
        st.markdown("```" + default_text + "```")

    if st.button("解析"):
        st.success("解析完成")
        st.markdown("```" + default_answer + "```")

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("接口文档"):
        st.write("服务通过 HTTP/POST 进行服务解析请求\n")

        option = st.selectbox("入参/出参", ("入参 JSON", "出参 JSON"))
        if option == "入参 JSON":
            st.json({"query": "选民资格案件如何起诉?如何审理?",
                     "qid": "111"})

            st.write('\n')
            st.table(pd.DataFrame({
                "属性": ["query", "qid"],
                "类型": ["String", "String"],
                "说明": ["待解析文本", "自定id"]
            }))

        elif option == "出参 JSON":
            st.json({"code": True,
                     "data": {"answer": "(1)、公民不服选举委员会对选民资格的申诉所做处理决定...",
                              "qid": "111"}
                     })

            st.write('\n')
            st.table(pd.DataFrame({
                "属性": ["code", "data"],
                "类型": ["Bool", "Dict[String]"],
                "说明": ["是否找到推荐法条", "返回法条"]
            }))


if __name__ == "__main__":
    law_recommend()