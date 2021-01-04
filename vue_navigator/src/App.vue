<template>
  <div id="app">
    <div class="allWapper">
      <!-- logo -->
      <div class="systemLogo">
        <img src="../static/HLPAN.png" />
      </div>

      <div class="menu">
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
        >
          <el-menu-item index="st_element_extraction_choice">要素提取</el-menu-item>
          <el-menu-item index="st_case_recommendation_choice">类案推荐</el-menu-item>
          <el-menu-item index="st_text_classification_choice">文本分类</el-menu-item>
          <el-menu-item index="st_relation_extraction_choice">信息抽取</el-menu-item>
          <el-menu-item index="st_semantic_understanding_choice">语义理解</el-menu-item>
          <el-menu-item index="st_audio_processing_choice">声学处理</el-menu-item>
          <el-menu-item index="st_asr_optimization_choice">ASR优化</el-menu-item>
          <el-menu-item index="st_smart_dialogue_choice">智能对话</el-menu-item>
          <el-menu-item index="st_knowledge_database_choice">知识库</el-menu-item>

        </el-menu>
      </div>
      <div class="iframe">
        <iframe
          v-if="menuName == 'st_asr_optimization_choice'"
          class="ifa"
          scrolling="auto"
          :src="linkUrls.ST_ASR_OPTIMIZATION"
          frameborder="0"
        ></iframe>
        <iframe
          v-if="menuName == 'st_audio_processing_choice'"
          class="ifa"
          scrolling="auto"
          :src="linkUrls.ST_AUDIO_PROCESSING"
          frameborder="0"
        ></iframe>
        <iframe
          v-if="menuName == 'st_case_recommendation_choice'"
          class="ifa"
          scrolling="auto"
          :src="linkUrls.ST_CASE_RECOMMENDATION"
          frameborder="0"
        ></iframe>
        <iframe
          v-if="menuName == 'st_element_extraction_choice'"
          class="ifa"
          scrolling="auto"
          :src="linkUrls.ST_ELEMENT_EXTRACTION"
          frameborder="0"
        ></iframe>
        <iframe
          v-if="menuName == 'st_knowledge_database_choice'"
          class="ifa"
          scrolling="auto"
          :src="linkUrls.ST_KNOWLEDGE_DATABASE"
          frameborder="0"
        ></iframe>
        <iframe
          v-if="menuName == 'st_relation_extraction_choice'"
          class="ifa"
          scrolling="auto"
          :src="linkUrls.ST_RELATION_EXTRACTION"
          frameborder="0"
        ></iframe>
        <iframe
          v-if="menuName == 'st_semantic_understanding_choice'"
          class="ifa"
          scrolling="auto"
          :src="linkUrls.ST_SEMANTIC_UNDERSTANDING"
          frameborder="0"
        ></iframe>
        <iframe
          v-if="menuName == 'st_smart_dialogue_choice'"
          class="ifa"
          scrolling="auto"
          :src="linkUrls.ST_SMART_DIALOGUE"
          frameborder="0"
        ></iframe>
        <iframe
          v-if="menuName == 'st_text_classification_choice'"
          class="ifa"
          scrolling="auto"
          :src="linkUrls.ST_TEXT_CLASSIFICATION"
          frameborder="0"
        ></iframe>
      </div>
    </div>
    <!-- </div> -->
    <!-- <router-view/> -->
  </div>
</template>

<script>
import Config from "./config";

export default {
  name: "App",
  data() {
    return {
      activeIndex: "st_element_extraction_choice",
      menuName: "st_element_extraction_choice",

      deployUrl: Config.VUE_APP_DEPLOY_URL,
      linkUrls: {
        ST_ASR_OPTIMIZATION: Config.VUE_APP_DEPLOY_URL + "/asr-optimization/",
        ST_AUDIO_PROCESSING: Config.VUE_APP_DEPLOY_URL + "/audio-processing/",
        ST_CASE_RECOMMENDATION:
          Config.VUE_APP_DEPLOY_URL + "/case-recommendation/",
        ST_ELEMENT_EXTRACTION:
          Config.VUE_APP_DEPLOY_URL + "/element-extraction/",
        ST_KNOWLEDGE_DATABASE:
          Config.VUE_APP_DEPLOY_URL + "/knowledge-database/",
        ST_RELATION_EXTRACTION:
          Config.VUE_APP_DEPLOY_URL + "/relation-extraction/",
        ST_SEMANTIC_UNDERSTANDING:
          Config.VUE_APP_DEPLOY_URL + "/semantic-understanding/",
        ST_SMART_DIALOGUE: Config.VUE_APP_DEPLOY_URL + "/smart-dialogue/",
        ST_TEXT_CLASSIFICATION:
          Config.VUE_APP_DEPLOY_URL + "/text-classification/",
      },
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      this.menuName = key;
    },
  },
};
</script>

<style>
body {
  margin: 0;
  padding: 5px;
}
.ifa {
  width: 100%;
  height: 100%;
}
.el-tabs__content {
  border: 1px solid red;
  border-top: none;
  position: absolute;
  top: 62px;
  left: 0;
  bottom: 0;
  right: 0;
  /* width:100%;
     height:80%;
     */
}
.allWapper {
  display: flex;
  border-bottom: 1px solid #e4e7ed;
}
.el-tabs__header {
  margin-bottom: 0px;
}
.el-tabs__header .el-tabs__item {
  margin: 8px 0;
  font-size: 16px;
  padding-left: 29px;
}
.temp {
  width: 100%;
  height: 100%;
}
.systemLogo {
  width: 200px;
  height: 53px;
  margin-right: 35px;
}
.systemLogo img {
  width: 100%;
}
.menu {
  width: 100%;
  height: 60px;
  position: absolute;
  left: 220px;
  top: 15px;
}
.iframe {
  width: 100%;
  height: 100%;
  position: absolute;
  left: 0;
  top: 100px;
}
</style>
