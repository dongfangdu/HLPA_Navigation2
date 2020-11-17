# -*- coding: utf-8 -*-

"""
__author__ = Wangyd
__copyright__ = Copyright 2020
__version__ = 0.1
__status = Dev
"""

import os
import json
import requests
import numpy as np
from scipy.io import wavfile
import streamlit as st
from PIL import Image
from util.utils import *
from cfg.config import config

def home_page() -> None:
    image = Image.open(os.path.join(get_images_dir(), "logo_homepage.png"))
    st.image(image, use_column_width=True)
    st.header("声学处理服务")
    st.write("**声学处理**(acoustics processing)主要包含语音增强、声音转换、语音合成三个模块。")
    st.subheader("语音增强")
    st.write("* 旨在去除音频中的噪声，改善音质，提高ASR引擎识别率。")
    st.subheader("声音转换")
    st.write("* 旨在转换说话人声音。")
    st.subheader("语音合成")
    st.write("* 旨在将文本转换为音频。")


def speech_enh() -> None:
    image = Image.open(os.path.join(get_images_dir(), "logo_se.png"))
    st.image(image, use_column_width=True)
    st.write("**语音增强**是一种基于神经网络模型的**语音去噪**算法。模型在经过大量数据训练后，\
        能在保留音频有效信息的情况下，尽可能多的去除干扰噪声，从而改善音频质量。")
    st.header("Demo")
    # demo_in = open(os.path.join(get_enh_dir(), "demo/10.wav"), 'rb').read()
    st.write("* 去噪前")
    st.audio(os.path.join(get_enh_dir(), "demo/10.wav"), format="audio/wav")
    st.write("* 去噪后")
    # demo_out = open(os.path.join(get_enh_dir(), "demo/10_enh.wav"), 'rb').read()
    st.audio(os.path.join(get_enh_dir(), "demo/10_enh.wav"), format="audio/wav")

    st.header("Test")
    st.write("* 去噪前")
    uploaded_file = st.file_uploader(
                            "上传一个带噪音频",
                            type="wav",
                            )
    if uploaded_file is not None:
        bytes_in = uploaded_file.read()
        # with open("./audios/enh/uoloaded.wav", "wb") as f:
        #     f.write(bytes_in)
        st.audio(bytes_in, format="audio/wav")
        uploaded_wav = {"audio": bytes_in}
        ### return BytesIO
        res = requests.post(url=config.enh_url, files=uploaded_wav).content
        st.write("* 去噪后")
        st.audio(res, format="audio/wav") 

        ######## return an array
        # res = requests.post(url=config.enh_url, files=uploaded_wav).text
        # enh_wav = np.array(json.loads(res)["enh_wav"], dtype="int16")
        
        # enh_wav_path = os.path.join(get_enh_dir(), "test", uploaded_file.name)
        # wavfile.write(enh_wav_path, 16000, enh_wav)
        # st.write("* 去噪后")
        # st.audio(enh_wav_path, format="audio/wav")

def tts_zh() -> None:
    image = Image.open(os.path.join(get_images_dir(), "logo_tts.png"))
    st.image(image, use_column_width=True)
    st.write("**语音合成**是一种基于神经网络模型的**文本转语音**算法。模型在经过大量数据训练后，\
        能根据输入的中文字符合成对应的语音。")
    st.header("Test")
    st.write("* 输入文本")
    text_input = st.text_input("请输入一段中文文本", value="云嘉云计算有限公司，中文语音合成系统")
    if text_input is not None:
        text_tts = {"text": text_input}
        res = requests.post(url=config.tts_url, json=text_tts).content
        st.write("* 合成音频")
        st.audio(res, format="audio/wav")


def voice_conversion() -> None:
    image = Image.open(os.path.join(get_images_dir(), "logo_vc.png"))
    st.image(image, use_column_width=True)
    st.write("**声音转换**是一种基于神经网络模型的**变声**算法。模型在经过大量数据训练后，\
        能将**固定角色**的声音进行互相转换。")
    st.header("Demo")
    st.markdown("* 角色A")
    st.audio(os.path.join(get_vc_dir(), "demo/A/bej1f003_351.wav"), format="audio/wav")
    st.markdown("* 角色B")
    st.audio(os.path.join(get_vc_dir(), "demo/B/bej1m069_351.wav"), format="audio/wav")
    st.markdown("* A2B")
    st.audio(os.path.join(get_vc_dir(), "demo/A2B/bej1f003_351.wav"), format="audio/wav")
    st.markdown("* B2A")
    st.audio(os.path.join(get_vc_dir(), "demo/B2A/bej1m069_351.wav"), format="audio/wav")

    st.header("Test")
    st.write("* 角色B")
    uploaded_file = st.file_uploader(
                            "上传一个角色B的音频",
                            type="wav",
                            )
    if uploaded_file is not None:
        bytes_in = uploaded_file.read()
        # with open("./audios/enh/uoloaded.wav", "wb") as f:
        #     f.write(bytes_in)
        st.audio(bytes_in, format="audio/wav")
        uploaded_wav = {"audio": bytes_in}
        ### return bytes
        res = requests.post(url=config.vc_url, files=uploaded_wav).content
        st.write("* 变换后")
        st.audio(res, format="audio/wav") 




        
