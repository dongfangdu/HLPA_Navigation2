import streamlit as st
import pandas as pd


def judge_ner():
    st.title("司法要素提取")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.markdown("司法要素提取，是适用于 `裁判文书场景` 下的关键信息提取能力")
    st.markdown("该能力提供")
    st.markdown("* 案情 `共 11 类`要素")
    st.markdown("* 案由 `共 9 类`要素")

    # ===============
    # 字段
    # ===============
    st.header("♟ 要素字段 ♟")

    st.subheader("🍄 案情相关")
    entity_df_1 = pd.DataFrame(
        {
            "字段": [
                "relaInfo_court",
                "relaInfo_caseType",
                "relaInfo_reason",
                "relaInfo_trialRound",
                "relaInfo_trialDate",
                "relaInfo_appellor",
                "relaInfo_docType",
                "relaInfo_processType",
                "plaintiff",
                "defendant",
                "agent",
            ],
            "要素": [
                "审判法院",
                "案件类型",
                "案由类型",
                "审判程序",
                "审判日期",
                "当事人",
                "文书类型",
                "程序类型",
                "原告/上诉人",
                "被告/被上诉人",
                "委托代理人",
            ],
            "样例": [
                "北京市朝阳区人民法院",
                "民事案件",
                "金融借款合同纠纷",
                "一审",
                "2013-02-09",
                "大众汽车金融有限公司，王涛，李月兰",
                "判决书",
                "普通程序",
                "大众汽车金融有限公司",
                "王涛 李月兰",
                "李志华 栗雯",
            ],
        }
    )
    st.table(entity_df_1)

    st.subheader("🍄 案由相关")
    entity_df_2 = pd.DataFrame(
        {
            "字段": [
                "mortgage",
                "pledge",
                "daily_rate",
                "monthly_rate",
                "annual_rate",
                "appeal_amount",
                "affirm_amount",
                "judge_amount",
                "delay_pay",
            ],
            "要素": ["抵押物", "质押物", "日利率", "月利率", "年利率", "诉请金额", "认定金额", "判决金额", "滞纳金"],
            "样例": [
                "房产",
                "汽车",
                "0.916%",
                "0.916%",
                "0.916%",
                "5000元",
                "5000元",
                "5000元",
                "5000元",
            ],
        }
    )
    st.table(entity_df_2)

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")
    st.warning("体验环境为测试环境，仅支持样例解析，暂不开放自定义输入")

    default_sample = (
        "\n北京市朝阳区人民法院\n民 事 判 决 书\n（2013）朝民初字第1812号\n原告大众汽车金融（中国）有限公司，\n......\n"
        "如不服本判决，可在判决书送达之日起十五日内，向本院递交上诉状，按对方当事人的人数提出副本，"
        "上诉于北京市第二中级人民法院。\n审判员　　王玲\n二〇一三年二月九日\n书记员　　赵鑫"
    )
    default_res = pd.DataFrame(
        {
            "要素": [
                "北京市朝阳区人民法院",
                "民事案件",
                "金融借款合同纠纷",
                "一审",
                "2013-02-09",
                "大众汽车金融有限公司，王涛，李月兰",
                "判决书",
                "普通程序",
                "大众汽车金融有限公司",
                "王涛 李月兰",
                "李志华 栗雯",
                "汽车",
                "0.91667%",
                "39792.98",
                "68500",
                "38500",
            ],
            "标签": [
                "relaInfo_court",
                "relaInfo_caseType",
                "relaInfo_reason",
                "relaInfo_trialRound",
                "relaInfo_trialDate",
                "relaInfo_appellor",
                "relaInfo_docType",
                "relaInfo_processType",
                "plaintiff",
                "defendant",
                "agent",
                "mortgage",
                "monthly_rate",
                "appeal_amount",
                "affirm_amount",
                "judge_amount",
            ],
        }
    )

    st.markdown("🍄 **输入文本: **")
    st.markdown("```" + default_sample + "```")
    if st.button("点击解析"):
        st.success("解析完成")
        st.table(default_res)

    # ===============
    # API 接口文档
    # ===============
    st.header("♟ API 接口文档 ♟")
    if st.checkbox("点击查看 接口文档"):
        st.write("未完成\n")


if __name__ == "__main__":
    judge_ner()