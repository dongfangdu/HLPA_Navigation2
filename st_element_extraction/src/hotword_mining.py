import streamlit as st
import pandas as pd

def hotword_mining():
    st.title("热词发现")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.write("热词发现，是从批量文本中，尝试发现高频重要的词组\n")
    st.write("可快速定位出现在用户语句中的潜在关键词\n")

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")

    default_sample = ["是由古时期食肉类进化而来。在第三纪早期，古食肉类中的猫形类有数个分支：其中一支是古猎豹，贯穿各地质时期而进化为现今的猎豹；一支是犬齿高度特化的古剑齿虎类；一支是与古剑齿虎类相似的伪剑齿虎类；最后一支是古猫类。古剑齿虎类和伪剑齿虎类分别在第三纪早期和晚期灭绝，古猫类得以幸存。其中，类虎古猫就是现今的虎的祖先。后来，古猫类又分化为三支：真猫类、恐猫类和真剑齿虎类。其后二者均在第四纪冰河期灭绝，只有真猫类幸存下来，并分化成猫族和豹族两大类群而延续至21世纪，现今的虎，就是豹族成员之一。 [4]",
                      "...",
                      "虎强壮高大，毛色从北而南呈黄色到红色渐变，有深色条纹。不同于狮子吻长所以脸廓狭长的特点，老虎吻部较短，显得头大而圆。"]

    default_res = pd.DataFrame(
        [["化石", 300, 0.021172],
         ["中国", 500, 0.013029],
         ["形态", 200, 0.003257],
         ["发现", 300, 0.013029],
         ["亚洲", 200, 0.004885],
         ["个体", 400, 0.006514],
         ["剑齿虎", 100, 0.009771],
         ["人类", 200, 0.004885],
         ["华南", 200, 0.003257],
         ["华南虎", 100, 0.004885],
         ["古时期", 100, 0.0016286]],
        columns = ["热词", "词频", "热度"]
    )

    st.markdown("🍄 **输入文本: **")

    for id in range(len(default_sample)):
        st.markdown("```" + default_sample[id] + "```")

    if st.button("解析"):
        st.success("解析完成")
        st.table(default_res)

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("接口文档"):
        st.write("服务通过 HTTP/POST 进行服务解析请求\n")

        option = st.selectbox("入参/出参", ("入参 JSON", "出参 JSON"))
        if option == "入参 JSON":
            st.json({"q": "['今天杭州的天气怎么样', '今天天气不错']"})

            st.write('\n')
            st.table(pd.DataFrame({
                "属性": ["q"],
                "类型": ["List[String]"],
                "说明": ["待解析文本列表"]
            }))

        elif option == "出参 JSON":
            st.json({"Content": [
                {"id": 0,
                 "word": "今天",
                 "count": 2,
                 "freq": 0.02584},
                {"id": 1,
                 "word": "天气",
                 "count": 2,
                 "freq": 0.02584},
                {"id": 2,
                 "word": "杭州",
                 "count": 1,
                 "freq": 0.01561}
            ],
            })

            st.write('\n')
            st.table(pd.DataFrame({
                "属性": ["id", "word", "count", "freq"],
                "类型": ["Int", "String", "Int", "Float"],
                "说明": ["序号", "热词", "词频", "热度"]
            }))

    # ===============
    # 部署文档
    # ===============
    st.header("♟ 部署文档 ♟")
    if st.checkbox("部署文档"):
        st.write("未完成\n")

if __name__ == "__main__":
    hotword_mining()