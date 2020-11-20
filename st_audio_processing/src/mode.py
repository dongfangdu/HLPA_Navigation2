# -*- coding: utf-8 -*-

"""
__author__ = Wangyd
__copyright__ = Copyright 2020
__version__ = 0.1
__status = Dev
"""

import json
import os

import numpy as np
import requests
import streamlit as st
from PIL import Image
from scipy.io import wavfile

from cfg.config import config
from util.utils import *


def home_page() -> None:
    # image = Image.open(os.path.join(get_images_dir(), "logo_homepage.png"))
    # st.image(image, use_column_width=True)
    st.title("声学处理服务")
    st.header("♟ 概述 ♟")

    st.write("**声学处理**(acoustics processing)主要包含语音增强、声音转换、语音合成三个模块。")

    st.header("♟ 应用场景 ♟")

    st.subheader("ASR引擎优化")

    st.subheader("数据增强")

    st.subheader("语音交互")


def speech_enh() -> None:
    # image = Image.open(os.path.join(get_images_dir(), "logo_se.png"))
    # st.image(image, use_column_width=True)

    st.title("📕 语音增强")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.write(
        "**语音增强**是一种基于神经网络模型的**语音去噪**算法。模型在经过大量数据训练后，\
        能在保留音频有效信息的情况下，尽可能多的去除干扰噪声，从而改善音频质量。"
    )
    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")

    st.markdown("🍄 **示例文本: **")

    # demo_in = open(os.path.join(get_enh_dir(), "demo/10.wav"), 'rb').read()
    st.write("* 去噪前")
    st.audio(os.path.join(get_enh_dir(), "demo/10.wav"), format="audio/wav")
    st.write("* 去噪后")
    # demo_out = open(os.path.join(get_enh_dir(), "demo/10_enh.wav"), 'rb').read()
    st.audio(os.path.join(get_enh_dir(), "demo/10_enh.wav"), format="audio/wav")

    st.markdown("🍄 **体验: **")
    st.write("* 去噪前")
    # uploaded_file = st.file_uploader(
    #     "上传一个带噪音频",
    #     type="wav",
    # )
    uploaded_file = st.file_uploader(
        "上传一个带噪音频(\
                下载地址：\
                192.168.100.210:\
                /home/user/wangyd/speech_enh_serving/test_data/noisy_data)",
        type="wav",
    )
    if uploaded_file is not None:
        bytes_in = uploaded_file.read()
        # with open("./audios/enh/uoloaded.wav", "wb") as f:
        #     f.write(bytes_in)
        st.audio(bytes_in, format="audio/wav")
        uploaded_wav = {"audio": bytes_in}
        ### return BytesIO
        try:
            res = requests.post(url=config.enh_url, files=uploaded_wav).content
            st.write("* 去噪后")
            st.audio(res, format="audio/wav")
        except:
            st.error("后端服务尚未启动，请联系**云嘉ASR基础研发部**")

        ######## return an array
        # res = requests.post(url=config.enh_url, files=uploaded_wav).text
        # enh_wav = np.array(json.loads(res)["enh_wav"], dtype="int16")

        # enh_wav_path = os.path.join(get_enh_dir(), "test", uploaded_file.name)
        # wavfile.write(enh_wav_path, 16000, enh_wav)
        # st.write("* 去噪后")
        # st.audio(enh_wav_path, format="audio/wav")
    else:
        st.error("请上传音频")


def tts_zh() -> None:
    # image = Image.open(os.path.join(get_images_dir(), "logo_tts.png"))
    # st.image(image, use_column_width=True)

    st.title("📕 语音合成")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.write(
        "**语音合成**是一种基于神经网络模型的**文本转语音**算法。模型在经过大量数据训练后，\
        能根据输入的中文字符合成对应的语音。"
    )

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")

    st.markdown("🍄 **体验: **")

    st.write("* 输入文本")

    text_default = "云嘉云计算有限公司，中文语音合成系统"
    text_input = st.text_input("请输入一段中文文本", value=text_default)
    if st.button("合成"):
        if text_input is not None:
            try:
                text_tts = {"text": text_input}
                res = requests.post(url=config.tts_url, json=text_tts).content
                st.write("* 合成音频")
                st.audio(res, format="audio/wav")
            except:
                st.error("后端服务尚未启动，请联系**云嘉ASR基础研发部**")
        else:
            st.error("请输入文本")


def voice_conversion() -> None:
    # image = Image.open(os.path.join(get_images_dir(), "logo_vc.png"))
    # st.image(image, use_column_width=True)

    st.title("📕 声音转换")

    # ===============
    # 概述
    # ===============
    st.header("♟ 概述 ♟")
    st.write(
        "**声音转换**是一种基于神经网络模型的**变声**算法。模型在经过大量数据训练后，\
        能将**固定角色**的声音进行互相转换。"
    )

    # ===============
    # 样例体验
    # ===============
    st.header("♟ 样例体验 ♟")

    st.markdown("🍄 **示例: **")
    st.markdown("* 角色A")
    st.audio(os.path.join(get_vc_dir(), "demo/A/bej1f003_351.wav"), format="audio/wav")
    st.markdown("* 角色B")
    st.audio(os.path.join(get_vc_dir(), "demo/B/bej1m069_351.wav"), format="audio/wav")
    st.markdown("* A2B")
    st.audio(
        os.path.join(get_vc_dir(), "demo/A2B/bej1f003_351.wav"), format="audio/wav"
    )
    st.markdown("* B2A")
    st.audio(
        os.path.join(get_vc_dir(), "demo/B2A/bej1m069_351.wav"), format="audio/wav"
    )

    st.markdown("🍄 **体验: **")
    st.write("* 角色B")
    uploaded_file = st.file_uploader(
        "上传一个角色B的音频",
        type="wav",
    )
    if st.button("转换"):
        if uploaded_file is not None:

            bytes_in = uploaded_file.read()
            # with open("./audios/enh/uoloaded.wav", "wb") as f:
            #     f.write(bytes_in)
            st.audio(bytes_in, format="audio/wav")
            uploaded_wav = {"audio": bytes_in}
            ### return bytes
            try:
                res = requests.post(url=config.vc_url, files=uploaded_wav).content
                st.write("* 变换后")
                st.audio(res, format="audio/wav")
            except:
                st.error("后端服务尚未启动，请联系**云嘉ASR基础研发部**")
        else:
            st.error("请上传音频")
