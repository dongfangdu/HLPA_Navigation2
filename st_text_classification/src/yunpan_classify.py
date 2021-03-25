# -*- coding: utf-8 -*- 

"""
# @Description: 
# @Author: AlexRainHao<yuanyuhaoyyh@gamil.com> 
# @Copyright 2021 - 2021 
# @Date: 2021-03-25 14:19:57 
# @Version: __Dev__ 
"""

import streamlit as st
import pandas as pd
import requests
import json

_URL = "http://192.168.108.197:9999"
_STATUS = _URL + "/status"
_PARSER = _URL + "/model/parse"
_MLIST = _URL + "/model/list"
_MPUT = _URL + "/model/put"
_MINFO = _URL + "/model/info"

_LAB_MAPPING = {"[cls]": "预警", "[unk]": "正常"}

def yunpan_classify():
    ''' pass '''

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.markdown("云盘预警，是针对云盘产品研发的`基于 NLP 学习`的智能文本敏感检测能力")
    st.markdown("该能力旨在弱化现有产品的 `词典强匹配` 方法，通过 `离线学习` 持续在客户本地进行模型优化")
    
    st.markdown("---")
    st.markdown("试用服务ip: `192.168.108.197:9999`, 各 API 见 `API 接口文档`")

    # ===============
    # 样例体验
    # ===============
    
    st.header("♟ 样例体验 ♟")
    st.warning("体验环境为测试环境，解析可能存在延迟")
    
    try:
        requests.get(_STATUS)
    except:
        st.error("服务未开启，请联系ASR基础研发部")
        
    default_sample = "尽管，法轮功，邪教组织宣称能让其信徒，功成圆满佛道神，通过，白日飞升，的方式进入所谓的，法轮世界，享受永不干涸的福泽，然而不幸的事实却是，一个接一个的，法轮功，骨干因为疾病等各种原因相继离世，甚至连，法轮功，邪教组织主李洪志的母亲也因病去世，命归黄泉，却从未见一个该邪教的信徒，白日飞升，功成圆满佛道神谎言就是谎言，纸包不住火，谎言在事实面前不堪一击。"
    
    text = st.text_area("🍄 请输入体验文本:", value = default_sample, key="yunpan_cls_sample_parser")
    
    if st.button("点击解析"):
        try:
            parser_res = requests.post(url = _PARSER, data = json.dumps({"text": text, "auto_split": True})).json()
            st.success("解析完成")
            
            sentences_res = parser_res["sentences"]
            for s in sentences_res:
                s["mapping"] = _LAB_MAPPING[s["intent"]]

            df = pd.DataFrame(
                sentences_res, columns=["order", "start","end", "text", "intent", "mapping", "prob"]
            )
            df.columns = ['序号', '开始', '结束', "文本", "类别", "备注", "置信度"]

            st.table(df)

        except:
            st.error("解析失败，请稍后重试")
            
    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("点击查看 接口文档"):
        st.write("服务通过 HTTP 进行服务解析请求\n")
        
        option = st.selectbox(
            "API 选择", (
                "服务状态", "文本解析", "在用模型信息", "模型列表", "更换模型", "错误码"
                )
            )
        
        # =====================
        if option == "服务状态":
            st.subheader("🍄 入参 GET")
            st.table(pd.DataFrame({
                "路由": ["/status"],
                "说明": ["服务是否存活"]
            }))
            
            st.subheader("🍄 反参 JSON")
            st.json(
                {
                    "statue": 200,
                    "message": "successfully"
                }
            )
            
        # =====================
        elif option == "文本解析":
            st.subheader("🍄 入参 POST/JSON")
            st.json({
                "text": "今天杭州的天气怎么样",
                "auto_split": True
            })
            st.write("\n")
            st.table(pd.DataFrame({
                "属性": ["text", "auto_split"],
                "类型": ["String", "Bool"],
                "说明": ["待解析文本", "是否采用长文本分割（建议采用)"]
            }))
            st.table(pd.DataFrame({
                "路由": ["/model/parse"],
                "说明": ["解析文本是否涉密"]
            }))
            
            st.subheader("🍄 反参 JSON")
            st.json({
                "task_id": "185693e61bc042a583f70a2944f516a3",
                "task_name": "rf",
                "sentences": [
                    {
                        "task_id": "185693e61bc042a583f70a2944f516a3",
                        "task_name": "rf",
                        "order": 0,
                        "sentence_id": "c3d3683dfd7347008c57d44cfb4052f3",
                        "start": 0,
                        "end": 200,
                        "time": "2021-03-25 15:07:34:511537",
                        "text": "从问题本身来讲，这根本就不是一个法学课题，而是一个政治学的课题，不可能在法学领域找到结论，从现实来讲，由于我国宪法规定了坚持中国共产党的领导，因此反对三权分立，宪政民主和司法独立，就成为我国每一个司法人员应尽的政治义务和宪法义务在不同政治体制下的司法机构，虽然名字都叫法院，但是西方三权分立下的司法机构与我国的司法机构在职能上是不完全一样的，甚至有很大差别。实行，定承办法官，定办理时限，定工作责任，",
                        "intent": "[cls]",
                        "prob": 0.88
                    },
                    {
                        "task_id": "185693e61bc042a583f70a2944f516a3",
                        "task_name": "rf",
                        "order": 1,
                        "sentence_id": "f0e0c87907324111b57a735fd56d5759",
                        "start": 200,
                        "end": 349,
                        "time": "2021-03-25 15:07:34:511569",
                        "text": "定包案领导，实行院长包案，的，四定一包，工作责任制，建立停偿案件台账，聚焦解决重难点问题为确保案件审执质量，吉林省高院拟制，驻吉军事单位停偿项目完成清退确认书，下发全省法院，明确要求经法院审判执行的停偿项目完成清退的，必须由案涉军事单位领导签字并盖章确认，确保了每一项涉案停偿工作都完成得干净彻底。",
                        "intent": "[unk]",
                        "prob": 0.6268904152144188
                    }
                ],
                "percentage": 0.500,
                "mean_prob": 0.627,
                "max_prob": 0.880,
                "min_prob": 0.373
            })
            
            st.write('\n外层属性')
            st.table(pd.DataFrame({
                "属性": ["task_name", "sentences", "percentage", "mean_prob", "max_prob", "min_prob"],
                "类型": ["String", "List", "Float", "Float", "Float", "Float"],
                "说明": ["在用模型名称", "单句解析结果", "涉密句占比", "平均涉密置信度", "最大涉密置信度", "最小涉密置信度"]
            }))
            st.write('\n内层属性')
            st.table(pd.DataFrame({
                "属性": ["order", "start", "end", "text", "intent", "prob"],
                "类型": ["Int", "Int", "Int", "String", "String", "Float"],
                "说明": ["序号", "单句在原上传文本的开始位置", "单句在原上传文本的结束位置", "分句文本", "分类结果([cls]为预警)", "所属分类结果置信度"]
            }))
        
        # =====================
        elif option == "在用模型信息":
            st.subheader("🍄 入参 GET")
            st.table(pd.DataFrame({
                "路由": ["/model/info"],
                "说明": ["在用模型信息"]
            }))
            
            st.subheader("🍄 反参 JSON")
            st.json(
                {
                    "task_name": "rf",
                    "model_path": "/home/admin/models/rf"
                }
            )
            st.write("\n")
            st.table(pd.DataFrame({
                "属性": ["task_name", "model_path"],
                "类型": ["String", "String"],
                "说明": ["模型名称", "模型路径"]
            }))
        
        # =====================
        elif option == "模型列表":
            st.subheader("🍄 入参 GET")
            st.table(pd.DataFrame({
                "路由": ["/model/list"],
                "说明": ["所有可用模型名称"]
            }))
            
            st.subheader("🍄 反参 JSON")
            st.json(
                {
                    "task_list": ["rf", "nb"],
                }
            )
            st.write("\n")
            st.table(pd.DataFrame({
                "属性": ["task_list"],
                "类型": ["List"],
                "说明": ["所有可用模型名称"]
            }))            

        # =====================
        elif option == "更换模型":
            st.subheader("🍄 入参 PUT/JSON")
            st.json({
                "task_name": "nb",
            })
            st.table(pd.DataFrame({
                "属性": ["task_name"],
                "类型": ["String"],
                "说明": ["模型名称"]
            }))
            st.table(pd.DataFrame({
                "路由": ["/model/put"],
                "说明": ["更换服务模型"]
            }))
            
            
            st.subheader("🍄 反参 JSON")
            {
                "statue": 200,
                "message": "successfully",
                "task_name": "nb",
                "model_path": "/home/admin/model/nb"
            }
            st.write("\n")
            st.table(pd.DataFrame({
                "属性": ["statue", "message", "task_name", "model_path"],
                "类型": ["Int", "String", "String", "String"],
                "说明": ["状态码", "状态信息", "替换后模型名称", "替换后模型路径"]
            })) 
            
        # =====================
        elif option == "错误码":
            st.table(pd.DataFrame({
                "错误码": [400, 500],
            }))
            
    # ===============
    # 部署文档
    # ===============
    st.header("♟ API 部署文档 ♟")
    if st.checkbox("点击查看 部署文档"):
        st.write("未完成\n")
        
    # ===============
    # 部署文档
    # ===============
    st.header("♟ API 未来功能♟")
    if st.checkbox("点击查看 未来功能♟"):
        st.markdown("* 接入敏感词汇模型")
        st.markdown("* 自定义上传数据进行训练的接口")
        st.markdown("* 状态码规整、日志规整")
        st.markdown("* 更多模型")
        
        
        
if __name__ == "__main__":
    yunpan_classify()