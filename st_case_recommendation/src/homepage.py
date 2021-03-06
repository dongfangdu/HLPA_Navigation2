# -*- encoding: utf8 -*-

import streamlit as st


def description():
    st.title("类案推送")
    st.header("♟ 概述 ♟")
    # ******************
    # *****旧的概述
    # 在人工智能和法律结合的场景中，智能判决辅助作为智能司法引擎的重要组成部分，在人工智能背景下如何“准确定义类案”并“精准发现类案”是关键所在，对推动司法领域智慧化的建设有着极其重要的作用。另外，司法体制改革后，法官有了更大的自主判断权和自由裁量权，同时会产生裁判尺度不统一、类案不同判、量刑不规范等问题。而智能判决辅助技术通过发现案情相类似的裁判文书作为法官判案参考，以实现司法过程中类案类判的目标，维护司法公信力。因此，智能判决辅助的研究具有很高的意义和价值，极具应用前景。

    st.markdown("类案推送：通过智能表征学习，衡量裁判文书之间的相似性，基于隐语义特征推荐近似裁判文书。")

    st.header("♟ 应用场景 ♟")
    st.header("🔹 判决辅助")
    st.markdown("法官通过类案推送，快速找到同法院同类型的相似案件文书，可高效获取相似案件的量刑和法律依据。")

    st.header("🔹 同案不同判审查")
    st.markdown("法官通过类案推送，快速找到相似案情的案件，评估量刑是否有较大出入。")
