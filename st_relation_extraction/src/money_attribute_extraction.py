import enum
from collections import defaultdict
from typing import List, Tuple

import httpx
import pandas as pd
import streamlit as st

SPACES = "&nbsp;" * 10


def local_css(file_name):
    with open(file_name) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


def load_page() -> None:
    local_css("./src/style.css")
    prepare_layout()


def prepare_layout() -> None:
    st.title("📕 金额属性抽取")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.write("金额属性可以通过调用分析接口，具体体会该功能的作用。")

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")

    st.markdown("🍄 **示例文本: **")
    text_default = "合同上写明了借款是1万7千元。"
    st.markdown("```" + text_default + "```")
    res_default = "<div>合同上写明了<span class='highlight blue'>借款</span>是<span class='highlight red'>1万7千元</span>。</div>"
    st.markdown(res_default, unsafe_allow_html=True)
    st.markdown("")
    st.markdown("")
    st.markdown("")

    text_exam = """2013年6月4日，廖细妹丈夫刘德发，父母廖儒兴、胡秀芳，女儿刘芸珊、刘思燕以奇石卫生院对死者产后应急预案不到位，应急处置不当，应承担医疗损害责任为由诉至法院，要求奇石卫生院赔偿其丧葬费12000元、死亡赔偿金240000元、两名未成年人抚养费248000元、精神损害抚慰金50000元、被赡养人生活补助金50000元。"""

    st.markdown("🍄 **体验: **")
    text_input = st.text_area("请输入文本", text_exam, key=f"money_attr_text")

    if st.button("分析"):
        try:
            ping_msg = httpx.get(
                "http://192.168.108.197:9496/tres/v1/ping",
            ).json()

            if not ping_msg.get("message") == "pong":
                raise Exception("Server is not RUNING!")

            resp_json = httpx.post(
                "http://192.168.108.197:9496/tres/v1/attr/money",
                json={"item": {"text": text_input}},
            ).json()

            if not resp_json.get("text") or not resp_json.get("attrs"):
                raise Exception("API works FAILED!")

            if len(resp_json["attrs"]) == 0:
                st.write("该文本没有找到金额属性")
            else:

                md_table = "| # | 结果 |\n| ----- | ----- |\n"
                for i, attr_item in enumerate(resp_json["attrs"]):
                    md_table += f"| {i+1} | {reform_attr_res(attr_item)} |\n"
                st.markdown(md_table, unsafe_allow_html=True)

                # res_list = []
                # for i, attr_item in enumerate(resp_json["attrs"]):
                #     sub_list = []
                #     sub_list.append(i)
                #     sub_list.append(reform_attr_res(attr_item))

                #     res_list.append(sub_list)

                # df = pd.DataFrame(res_list, columns=["col1", "col2"])

        except:
            st.error("后端服务尚未启动，请联系**云嘉ASR基础研发部**")


def reform_attr_res(attr_item):
    ctx = attr_item.get("ctx")
    html_ctx = ctx

    insert_item = defaultdict(str)
    insert_item[0] = "<div>" + insert_item[0]
    insert_item[len(ctx)] = insert_item[len(ctx)] + "</div>"

    subj_bgn = attr_item.get("subj_bgn")
    subj_end = attr_item.get("subj_end")
    insert_item[subj_bgn] = insert_item[subj_bgn] + "<span class='highlight red'>"
    insert_item[subj_end] = "</span>" + insert_item[subj_end]

    obj_bgn = attr_item.get("obj_bgn")
    obj_end = attr_item.get("obj_end")
    insert_item[obj_bgn] = insert_item[obj_bgn] + "<span class='highlight blue'>"
    insert_item[obj_end] = "</span>" + insert_item[obj_end]

    # insert_item = sorted(insert_item, key=lambda x: x[0], reverse=True)

    for position, html_tag in sorted(insert_item.items(), reverse=True):
        html_ctx = html_ctx[:position] + html_tag + html_ctx[position:]
    return html_ctx
