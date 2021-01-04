# -*- coding: utf-8 -*-
import json
import re

import pandas as pd
import requests
import streamlit as st


def parag_classify():
    st.title("裁判文书段落分类")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.write("裁判文书段落分类是指根据判决书文本的结构以及所表达的含义和情感信息将判决书的段落进行分类\n")

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")
    st.warning("体验环境为测试环境")

    text_exam = "原告杨晓琴，女，汉族，43岁，东胜区人，个体户，现住东胜区。被告戴永强，男，蒙古族，47岁，东胜区人，个体户，现住东胜区。被告杜胜利，女，蒙古族，47岁，东胜区人，个体户，现住东胜区。原告杨晓琴诉被告戴永强、杜胜利民间借贷纠纷一案，本院于2013年1月5日立案受理后，依法由代理审判员于洋独任适用简易程序公开开庭进行了审理。原告杨晓琴、被告戴永强、杜胜利到庭参加诉讼。本案现已审理终结。原告诉称：2009年3月30日被告戴永强向原告借款40万元，并打下借条一支，双方约定借款月利率3.5%，被告杜胜利为连带担保责任人在借款协议中签字。但从2011年3月30日后，被告再未给付借款本金及利息，经原告多次催要未果，故诉至法院要求被告戴永强偿还原告借款本金40万元及利息22万元（从2011年3月30日到2013年1月30日），共计62万元，月利率按2.5%计算；判令被告戴永强给付从起诉之日起到结案给付之日止的利息，月利率按2.5%计算；被告杜胜利对上述借款本金及利息承担连带还款责任，诉讼费用及相关费用由二被告承担。被告戴永强辩称：不同意原告的诉讼请求，40万元的利息从一开始借款就应该按银行贷款利率计算，现在40万元我们给原告抵顶一个价值2万元的茶台，本金现在剩余38万元。"

    text_input = st.text_area("请输入文本", text_exam, key=f"parag_classify")

    # default_sample = "原告杨晓琴，女，汉族，43岁，东胜区人，个体户，现住东胜区。被告戴永强，男，蒙古族，47岁，东胜区人，个体户，现住东胜区。被告杜胜利，女，蒙古族，47岁，东胜区人，个体户，现住东胜区。原告杨晓琴诉被告戴永强、杜胜利民间借贷纠纷一案，本院于2013年1月5日立案受理后，依法由代理审判员于洋独任适用简易程序公开开庭进行了审理。原告杨晓琴、被告戴永强、杜胜利到庭参加诉讼。本案现已审理终结。原告诉称：2009年3月30日被告戴永强向原告借款40万元，并打下借条一支，双方约定借款月利率3.5%，被告杜胜利为连带担保责任人在借款协议中签字。但从2011年3月30日后，被告再未给付借款本金及利息，经原告多次催要未果，故诉至法院要求被告戴永强偿还原告借款本金40万元及利息22万元（从2011年3月30日到2013年1月30日），共计62万元，月利率按2.5%计算；判令被告戴永强给付从起诉之日起到结案给付之日止的利息，月利率按2.5%计算；被告杜胜利对上述借款本金及利息承担连带还款责任，诉讼费用及相关费用由二被告承担。被告戴永强辩称：不同意原告的诉讼请求，40万元的利息从一开始借款就应该按银行贷款利率计算，现在40万元我们给原告抵顶一个价值2万元的茶台，本金现在剩余38万元。"
    # default_sample1 = "内蒙古鄂尔多斯市东胜区人民法院"
    # default_sample2 = "民事判决书"
    # default_sample3 = "（2013）东法民初字第37号。"
    # default_sample4 = "原告杨晓琴，女，汉族，43岁，东胜区人，个体户，现住东胜区。"
    # default_sample5 = "被告戴永强，男，蒙古族，47岁，东胜区人，个体户，现住东胜区。"
    # default_sample6 = "被告杜胜利，女，蒙古族，47岁，东胜区人，个体户，现住东胜区。"
    # default_sample7 = "原告杨晓琴诉被告戴永强、杜胜利民间借贷纠纷一案，本院于2013年1月5日立案受理后，依法由代理审判员于洋独任适用简易程序公开开庭进行了审理。原告杨晓琴、被告戴永强、杜胜利到庭参加诉讼。本案现已审理终结。"
    # default_sample8 = "原告诉称：2009年3月30日被告戴永强向原告借款40万元，并打下借条一支，双方约定借款月利率3.5%，被告杜胜利为连带担保责任人在借款协议中签字。但从2011年3月30日后，被告再未给付借款本金及利息，经原告多次催要未果，故诉至法院要求被告戴永强偿还原告借款本金40万元及利息22万元（从2011年3月30日到2013年1月30日），共计62万元，月利率按2.5%计算；判令被告戴永强给付从起诉之日起到结案给付之日止的利息，月利率按2.5%计算；被告杜胜利对上述借款本金及利息承担连带还款责任，诉讼费用及相关费用由二被告承担。"
    # default_sample9 = "被告戴永强辩称：不同意原告的诉讼请求，40万元的利息从一开始借款就应该按银行贷款利率计算，现在40万元我们给原告抵顶一个价值2万元的茶台，本金现在剩余38万元。"

    # default_res = pd.DataFrame(
    #     {
    #         "文本段落": [
    #             default_sample1,
    #             default_sample2,
    #             default_sample3,
    #             default_sample4,
    #             default_sample5,
    #             default_sample6,
    #             default_sample7,
    #             default_sample8,
    #             default_sample9,
    #         ],
    #         "类别": [
    #             "标题",
    #             "文书编号",
    #             "当事人信息",
    #             "审理过程",
    #             "原告主张",
    #             "被告答辩",
    #             "举证质证",
    #             "审理事实",
    #             "判决理由",
    #         ],
    #     }
    # )

    # st.markdown("```" + default_sample + "```")
    if st.button("分析"):
        st.success("分析完成")
        st.table(do_text_clsf(text_input))


def do_text_clsf(text):

    url = "http://192.168.100.210:5650/sents_cls"

    HANZI_PUNT_STOPS = "！？｡。"

    text = re.sub("({}+)".format("|".join(list(HANZI_PUNT_STOPS))), r"\1\n", text)
    lines = [t for t in re.split("\s+", text) if t.strip()]

    # print(len(lines))

    # sents = [text_1, text_2]
    sents = lines
    request_data = {"sentences": sents}
    res = requests.post(url, json=request_data)
    # print(json.loads(res.text))
    # print("耗时：{}".format(end_time-start_time))

    req_res = json.loads(res.text)
    clsf_res = req_res.get("result")

    cat_list = [r.get("category") for r in clsf_res]

    cat_label_tmp = "当事人信息"
    cat_relabel = []

    for c in cat_list:
        if c == "其它":
            cat_relabel.append(cat_label_tmp)
        else:
            cat_label_tmp = c
            cat_relabel.append(cat_label_tmp)
    # print(len(cat_list))
    # print(len(cat_relabel))
    # print(cat_relabel)

    reform_res = [[lines[0], cat_relabel[0]]]
    for sent, cat in list(zip(lines, cat_relabel))[1:]:
        if reform_res[-1][1] == cat:
            reform_res[-1][0] += sent
        else:
            reform_res.append([sent, cat])

    label_dict = {
        "首句": "审理过程",
        "诉称": "原告诉称",
        "辩称": "被告辩称",
        "查明": "事实查明",
        "认为": "法院认为",
    }

    show_res = []
    for sent, cat in reform_res:
        show_res.append((sent, (label_dict.get(cat) or cat)))

    df_res = pd.DataFrame(
        {
            "文本段落": [sent for sent, cat in show_res],
            "类别": [cat for sent, cat in show_res],
        }
    )
    return df_res


if __name__ == "__main__":
    parag_classify()
