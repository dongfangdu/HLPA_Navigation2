import http.client
import json

import pandas as pd
import streamlit as st

from libs.common import get_config_dict


def jdoc_recommend():
    st.title("文书推荐")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.markdown("文书推荐，推荐已表征学习的`裁判文书库`下的相似文书")

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")

    st.warning("体验环境为测试环境，暂不支持近似近邻搜索，需要计算的时间较长，请耐心等待。")

    input_data = st.text_area(
        "待推荐文书",
        "北京市朝阳区人民法院\n民 事 判 决 书\n（2013）朝民初字第1812号\n原告大众汽车金融（中国）有限公司，住所地北京市朝阳区建国门外大街8号国际财源中心16层01、02、03、05、06、08单元及17层01、02、03、08单元。\n法定代表人傅海德，董事长。\n委托代理人李志华，女，1980年11月12日出生。\n委托代理人栗雯，男，1985年8月1日出生。\n被告王涛，男，1985年5月15日出生。\n被告李月兰，1958年10月31日出生。\n原告大众汽车金融（中国）有限公司（以下简称大众金融公司）与被告王涛、李月兰金融借款合同纠纷一案，本院受理后，依法由审判员王玲独任审判，公开开庭进行了审理。原告大众金融公司的委托代理人栗雯到庭参加了诉讼，被告王涛、李月兰经本院依法送达开庭传票无正当理由未出庭应诉。本案现已审理完毕。\n原告大众金融公司起诉称：2012年4月，王涛、李月兰为从大众金融公司指定经销商购买轿车一辆而向大众金融公司申请汽车贷款，并提交了贷款申请材料。2012年4月28日，王涛作为借款人、李月兰作为共同借款人与大众金融公司签订贷款合同和抵押合同。王涛、李月兰依借款合同向大众金融公司承担连带还款义务。2012年4月24日，王涛、李月兰为其购买的轿车办理了抵押登记，用于履行贷款合同的担保。2012年4月24日，大众金融公司按合同约定发放了汽车贷款38500元。按照双方在贷款合同中的约定，借款人应于2012年5月起至2014年4月，每月23日按时归还贷款本息。但王涛、李月兰自2012年5月起未按约定偿还贷款。大众金融公司多次催促王涛、李月兰履行还款义务，但其仍未履行。2012年8月3日，大众金融公司按照贷款合同上王涛、李月兰的地址发出《宣布贷款提前到期函》，宣布贷款提前到期，要求王涛、李月兰在7日内清偿提前到期贷款，但王涛、李月兰仍未履行还款义务。故大众金融公司诉至法院，要求王涛、李月兰偿还大众金融公司发放的贷款及相关费用共计39792.98元。其中包括截至贷款提前到期日（2012年8月3日）的本金人民币38500元（包括逾期本金4812.51元和提前到期本金33687.49元），应交罚息82.36元，其他费用1210.62元（其中包括催款函费用200元及违约金1010.62元）；要求王涛、李月兰连带支付自合同提前到期日次日起至大众金融公司全部债权实现之日所产生的相应罚息（按照中国人民银行有关金融机构计收逾期贷款的利率标准计算，即贷款合同载明的贷款利率水平上加收50%），并承担本案诉讼费用。\n原告大众金融公司向本院提交以下证据予以证明：1、贷款申请材料；2、《贷款合同》、《抵押合同》；3、机动车登记证书；4、催款函；5、宣布贷款提前到期函；6、中国工商银行代付费处理成功明细表。\n被告王涛未出庭，未答辩，未提交任何证据。\n被告李月兰未出庭，未答辩，未提交任何证据。\n经本院庭审审查，大众金融公司提交的证据材料具备真实性、合法性、关联性，本院予以确认。\n本院根据上述认证查明：2012年4月17日，大众金融公司作为贷款人与作为借款人的王涛、作为共同借款人的李月兰签订《贷款合同》，约定：合同项下贷款仅用于借款人向经销商支付购买一辆JETTA新伙伴轿车；贷款金额38500元；贷款期限24个月；第1至24期每期应付1604.17元；月还款日及结息日为每月与起息日相同的日历日；基本月利率0.91667%，除遇国家法律、法规要求，合同有效期内，贷款利率及计息方式保持不变；借款人应在银行开立帐户，并授权贷款人在每一还款日直接划扣应付款项；如果借款人在还款日因任何原因不能足额支付任何一期还款或其他应付款项，此未还款将被视为逾期付款，双方同意按期前欠本、期前欠息、罚息、当期欠本、当期欠息、其他费用及赔偿的顺序清偿；借款人不能按期支付其应付款时，贷款人将另收取出具催款函的费用每次100元及进行现场调查的费用300元；在借款人违约的情况下，贷款人有权采取如下救济手段：如借款人不能如期归还贷款，逾期宽限高的利率（逾期利率）为本合同约定基本月利率的150％，逾期利息自发生逾期之日起至全部款项清偿之日止，按日计算，计收复利；宣布合同终止及全部贷款提前到期，并收取提前到期本金3%的违约金，借款人对贷款人出具的“归还全部贷款函”应无条件放弃任何抗辩。任何以预付费邮寄或其他方式送达至借款人预留地址的文件、通知或信件均应被视为有效及合理送达，上述文件、通知或信件将自邮递发出时起48小时内视为已被借款人收到。与此同时大众金融公司作为抵押权人与抵押人王涛签订了抵押合同。\n合同签订后，大众金融公司发放了贷款。2012年4月28日，王涛为贷款所购车辆办理了以大众金融公司为抵押权人的抵押登记。王涛、李月兰自2012年5月后未按约定向大众金融公司偿还款项。2012年5月起，大众金融公司通过电话、信函等方式要求王涛、李月兰承担还款义务，两次向其二人发送催款函进行催款，并向王涛、李月兰的贷款合同上所确认的地址快递《宣布贷款提前到期函》。截至2012年8月3日，王涛、李月兰尚欠大众金融公司贷款本金38500元、罚息82.36元。\n上述事实，有大众金融公司提交的上述证据及当事人陈述意见佐证。\n本院认为：大众金融公司与王涛、李月兰签订的《贷款合同》是双方真实意思的体现，合同内容不违背法律、行政法规的强制性规定，合法有效。大众金融公司按照贷款合同的约定发放了贷款，履行了合同约定的义务。王涛作为借款人、李月兰作为共同借款人未按期偿还借款本息，已构成违约。大众金融公司催款未果发出宣布贷款提前到期的通知，是依据约定行使合同赋予贷款人的权利，王涛、李月兰有义务偿还全部贷款本金和利息。大众金融公司要求王涛、李月兰偿付截至2012年8月3日逾期本金、罚息及提前到期的贷款本金，并自2012年8月4日起按照中国人民银行有关金融机构计收逾期贷款的利率标准的上限计算前述款项的利息，符合合同约定、法律规定，应予以支持。大众金融公司曾向王涛、李月兰发出催款函，按照合同约定王涛、李月兰应承担催款函费用。关于大众金融公司主张的违约金，在双方合同中明确约定，合法有效，本院予以支持。王涛、李月兰经本院合法传唤，无正当理由拒不到庭应诉，不影响本院根据查明的事实依法作出判决。综上，依照《中华人民共和国合同法》第二百零六条、第二百零七条，《中华人民共和国民事诉讼法》第一百四十四条之规定，判决如下：\n一、被告王涛、李月兰于本判决生效之日共同偿还原告大众汽车金融（中国）有限公司截至二○一二年八月三日的借款本金三万八千五百元、罚息八十二元三角六分，并自二○一二年八月四日起至偿清前款应付款项之日止按照中国人民银行有关金融机构计收逾期贷款的利率标准的上限计算前述款项的利息；\n二、被告王涛、李月兰于本判决生效之日共同给付原告大众汽车金融（中国）有限公司催款函费用二百元；\n三、被告王涛、李月兰于本判决生效之日向原告大众汽车金融（中国）有限公司支付违约金一千零一十元六角二分。\n如果未按本判决指定的期间履行给付金钱义务，应当依照《中华人民共和国民事诉讼法》第二百五十三条之规定，加倍支付迟延履行期间的债务利息。\n案件受理费三百九十七元，由被告王涛、李月兰负担（于本判决生效之日起七日内交纳）。\n如不服本判决，可在判决书送达之日起十五日内，向本院递交上诉状，按对方当事人的人数提出副本，上诉于北京市第二中级人民法院。\n审判员　　王玲\n二〇一三年二月九日\n书记员　　赵鑫",
    )
    if st.button("点击推荐"):
        recommend_inter = get_config_dict()["RECOMMEND_inter"]
        host = recommend_inter["host"]
        port = recommend_inter["port"]
        path = recommend_inter["path"]
        httpHeaders = {"Content-Type": "application/json"}
        conn = http.client.HTTPConnection(host, port)
        data_dict = {"input_data": input_data}
        body = json.dumps(data_dict)
        url = "/%s" % path
        conn.request(method="POST", url=url, body=body, headers=httpHeaders)
        response = conn.getresponse()
        res = response.read()
        output_data = json.loads(res)["output_data"]
        output_data = list_2_DataFrame(output_data)
        st.write(output_data)


def list_2_DataFrame(input_data):
    df = pd.DataFrame(columns=("title", "score", "docContent"))
    for i in range(20):
        df.at[i, "title"] = input_data[i]["title"]
        df.at[i, "score"] = input_data[i]["score"]
        df.at[i, "docContent"] = input_data[i]["docContent"]
    return df
