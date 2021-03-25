import streamlit as st
import pandas as pd
import requests
import json

URL = "http://192.168.100.210:9999"

def public_ner():
    st.title("公共要素提取")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.markdown("公共要素提取，是适用于各场景下的要素提取能力")
    st.markdown("我们内置了`18 类`较为通用的要素供以提取使用")

    # ===============
    # 字段
    # ===============
    st.header("♟ 要素字段 ♟")
    schema_eng = ["Date", "PER", "ORG", "RESIDENT", "Money", "IDNumber", "MobilePhone", "BankCard",
                  "CarNumber", "CaseNum", "Age", "Gender", "Race", "Origin",
                  "Role", "Court", "TITLE", "EDU"]
    schema_zh = ["时间", "人名", "组织机构名", "地名", "金额", "身份证号", "手机号", "银行卡号", "车牌号",
                 "案件号", "年龄", "性别", "民族", "籍贯", "诉讼地位", "法院", "职业", "教育水平"]

    schema_dict = dict(zip(schema_eng, schema_zh))
    entity_df = pd.DataFrame({"字段": schema_eng,
                              "要素": schema_zh,
                              "样例": ["2020年1月", "小王", "社保局", "杭州市", "10元", "520520520520520520", "13600000000",
                                     "浙a12345", "6216610200016587010", "2020浙民事001号", "18岁", "男", "汉族",
                                     "浙江省杭州市余杭区", "原告", "浙江高院", "教师", "本科"]})
    st.table(entity_df)

    # ===============
    # 样例体验
    # ===============

    st.header("♟ 样例体验 ♟")
    st.warning("体验环境为测试环境，建议文本长度在100字以内，解析可能存在延迟")

    try:
        requests.get(url=URL)
    except:
        st.error("服务未开启，请联系ASR基础研发部")

    default_sample = "罪嫌疑人为郭磊昌，19岁，男，广西壮族腾王村十队人，汉族。罗翔，男，湖南耒阳人，北京大学法学院刑法学专业毕业，法学博士。"

    text = st.text_area("🍄 请输入体验文本:", value = default_sample, key="public_ner_sample_parser")

    if st.button("点击解析"):
        try:
            parser_res = requests.post(url = URL + "/parse", data = json.dumps({"q": text})).json()
            st.success("解析完成")

            entities = parser_res.get("entities")

            st.table(pd.DataFrame({"要素": [x["value"] for x in entities],
                                   "标签字段": [x["entity"] for x in entities],
                                   "标签含义": [schema_dict[x["entity"]] for x in entities],
                                   "开始位置": [x["start"] for x in entities],
                                   "结束位置": [x["end"] for x in entities]}))

        except:
            st.error("解析失败，请稍后重试")


    # ===============
    # API 接口文档
    # ===============

    st.header("♟ API 接口文档 ♟")
    if st.checkbox("点击查看 接口文档"):
        st.write("服务通过 HTTP/POST 进行服务解析请求\n")

        option = st.selectbox("入参/出参", ("入参 JSON", "出参 JSON"))
        if option == "入参 JSON":
            st.json({"q": "今天杭州的天气怎么样"})

            st.write('\n')
            st.table(pd.DataFrame({
                "属性": ["q"],
                "类型": ["String"],
                "说明": ["待解析文本"]
            }))

        elif option == "出参 JSON":
            st.json({"intent": {"name": None,
                                "confidence": 0.0},
                     "entities": [
                         {"start": 0,
                          "end": 2,
                          "value": "今天",
                          "entity": "Date",
                          "confidence": 1.0},
                         {"start": 2,
                          "end": 4,
                          "value": "杭州",
                          "entity": "RESIDENT",
                          "confidence": 1.0}
                     ],
                     "intent_ranking": [],
                     "text": "今天杭州的天气怎么样",
                     "project": "default",
                     "model": "model_20200710-015956"
                     })

            st.write('\n')
            st.markdown('仅需要返回结果的 `entities` 字段')
            st.table(pd.DataFrame({
                "属性": ["start", "end", "value", "entity", "confidence"],
                "类型": ["Int", "Int", "String", "String", "Float"],
                "说明": ["开始位置", "结束位置", "要素文本", "要素字段", "置信度"]
            }))

    # ===============
    # 部署文档
    # ===============
    st.header("♟ 部署文档 ♟")
    if st.checkbox("点击查看 部署文档"):
        st.write("服务通过 Docker 进行项目部署\n")

        st.header("🔹 目录结构")
        st.markdown("```\n"
                    "├── bin\n"
                    "│   ├── clean.sh\n"
                    "│   ├── docker-compose\n"
                    "│   ├── init.sh\n"
                    "│   ├── start.sh\n"
                    "│   └── stop.sh\n"
                    "├── conf\n"
                    "│   ├── compose\n"
                    "│   └── server_conf.ini\n"
                    "├── Dockerfile\n"
                    "├── images\n"
                    "│   └── yj-ner-server.tar\n"
                    "├── libs\n"
                    "├── logs\n"
                    "├── model\n"
                    "│   ├── AlbertModel\n"
                    "│   ├── BertModel\n"
                    "│   ├── CoreModel\n"
                    "│   └── NerModel\n"
                    "└── start_model.sh\n"
                    "```")

        st.header("🔹 服务启动")
        st.subheader("🍄 修改配置")
        st.markdown("```修改 conf/server_conf.ini```\n")
        st.table(pd.DataFrame({
            "字段": ["server_port"],
            "说明": ["外露端口"],
            "默认值": [9999]
        }))

        st.subheader("🍄 初始化镜像")
        st.markdown("```sh ./bin/init.sh```")

        st.subheader("🍄 启动服务")
        st.markdown("```sh ./bin/start.sh```")
        st.write("观察 logs 日志 server.log，若出现如下所示，表明启动成功")
        st.markdown("```\n"
                    "[2020-11-06 18:12] Start Albert Server...\n"
                    "[2020-11-06 18:12] Checking Bert Server Status...\n"
                    "[2020-11-06 18:12] Checking Bert Server Status...\n"
                    "[2020-11-06 18:12] Start Albert Server Successfully\n"
                    "[2020-11-06 18:12] Start NER Server...\n"
                    "[2020-11-06 18:12] Checking NER Status...\n"
                    "[2020-11-06 18:13] Checking NER Status...\n"
                    "[2020-11-06 18:14] Start NER Server Successfully\n"
                    "[2020-11-06 18:14] Waiting For Calling...\n"
                    "```")

        st.subheader("🍄 初始化镜像")
        st.markdown("```sh ./bin/init.sh```")

        st.subheader("🍄 停止服务")
        st.markdown("```sh ./bin/stop.sh```")

        st.subheader("🍄 清空镜像")
        st.markdown("```sh ./bin/clean.sh```")

    # ===============
    # 自定义热词词典
    # ===============
    st.header("♟ 热词词典 ♟")
    if st.checkbox("点击查看 热词词典"):
        st.markdown("该功能支持某些新词热词进行 `强制类别输出`，或者 `强制屏蔽`，如书记员名字等")

        st.markdown("```\n"
                    "cd ./NerModel/default/model_20200710-015956/tokenizer_spacy\n"
                    "并在该目录下增加自定义的 txt 文件")

        st.write("其中 txt 示例格式如下")
        st.markdown("```\n"
                    "杭州 LOC\n"
                    "世行 ORG\n"
                    "本科学历 EDU\n"
                    "程序猿 TITLE\n"
                    "一块 NOMEAN\n"
                    "```")

        st.write("支持的强制输出类别为")
        st.table(pd.DataFrame({
            "字段":["LOC", "PERSON", "ORG", "Date", "EDU", "TITLE"],
            "说明":["地点", "人名", "组织名", "时间", "教育水平", "职业"]
        }))
        st.write("支持的强制屏蔽类别为")
        st.table(pd.DataFrame({
            "字段": ["NOMEAN"],
            "说明": ["无意义"]
        }))


if __name__ == "__main__":
    public_ner()
