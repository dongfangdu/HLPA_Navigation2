<template>
  <div id="app">
    <div class="allWapper">
      <!-- logo -->
      <div class="systemLogo">
        <img src="../static/HLPAN.png" />
      </div>
      <!-- 顶部tabs -->
      <!-- <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane class="temp" label="要素提取" name="element_extraction">
      <iframe v-if="ifArr.element_extraction" class="ifa" scrolling=auto src="http://192.168.100.210:8503/" frameborder="0"></iframe>
    </el-tab-pane>
    <el-tab-pane class="temp"  label="类案推荐" name="case_recommendation">
       <iframe v-if="ifArr.case_recommendation"   class="ifa" scrolling=auto src="" frameborder="0"></iframe>
    </el-tab-pane>
    <el-tab-pane class="temp"  label="文本分类" name="text_classification">
       <iframe v-if="ifArr.text_classification"  class="ifa" scrolling=auto src="" frameborder="0"></iframe>
    </el-tab-pane>
    <el-tab-pane class="temp"  label="关系提取" name="relation_extraction">
       <iframe v-if="ifArr.relation_extraction"  class="ifa" scrolling=auto src="" frameborder="0"></iframe>
    </el-tab-pane>
    <el-tab-pane class="temp"  label="语义理解" name="semantic_understanding">
       <iframe v-if="ifArr.semantic_understanding"  class="ifa" scrolling=auto src="" frameborder="0"></iframe>
    </el-tab-pane>
    <el-tab-pane class="temp"  label="声学处理" name="audio_processing">
       <iframe v-if="ifArr.audio_processing"  class="ifa" scrolling=auto src="" frameborder="0"></iframe>
    </el-tab-pane>
    <el-tab-pane class="temp"  label="ASR优化" name="asr_optimazation">
       <iframe v-if="ifArr.asr_optimazation"  class="ifa" scrolling=auto src="" frameborder="0"></iframe>
    </el-tab-pane>
    <el-tab-pane class="temp"  label="智能对话" name="smart_dialogue">
       <iframe v-if="ifArr.smart_dialogue"  class="ifa" scrolling=auto src="" frameborder="0"></iframe>
    </el-tab-pane>
    <el-tab-pane class="temp"  label="知识库" name="knowledge_database">
       <iframe v-if="ifArr.knowledge_database"  class="ifa" scrolling=auto src="" frameborder="0"></iframe>
    </el-tab-pane>
  </el-tabs> -->

      <div class="menu">
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
        >
          <!-- <el-submenu index="2">
            <template slot="title">我的工作台</template>
            <el-menu-item index="2-1">选项1</el-menu-item>
            <el-menu-item index="2-2">选项2</el-menu-item>
            <el-menu-item index="2-3">选项3</el-menu-item>
            <el-submenu index="2-4">
              <template slot="title">选项4</template>
              <el-menu-item index="2-4-1">选项1</el-menu-item>
              <el-menu-item index="2-4-2">选项2</el-menu-item>
              <el-menu-item index="2-4-3">选项3</el-menu-item>
            </el-submenu>
          </el-submenu> -->
          <el-menu-item index="st_element_extraction_choice">要素提取</el-menu-item>
          <el-menu-item index="st_case_recommendation_choice">类案推荐</el-menu-item>
          <el-menu-item index="st_text_classification_choice">文本分类</el-menu-item>
          <el-menu-item index="st_relation_extraction_choice">关系提取</el-menu-item>
          <el-menu-item index="st_semantic_understanding_choice">语义理解</el-menu-item>
          <el-menu-item index="st_audio_processing_choice">声学处理</el-menu-item>
          <el-menu-item index="st_asr_optimization_choice">ASR优化</el-menu-item>
          <el-menu-item index="st_smart_dialogue_choice">智能对话</el-menu-item>
          <el-menu-item index="st_knowledge_database_choice">知识库</el-menu-item>

          <!-- <el-submenu index="1">
            <template slot="title">要素提取</template>
            <el-menu-item index="1-1">通用要素</el-menu-item>
            <el-menu-item index="1-2">医疗要素</el-menu-item>
            <el-menu-item index="1-3">司法要素</el-menu-item>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">类案推荐</template>
            <el-menu-item index="2-1">文书推荐</el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">文本分类</template>
            <el-menu-item index="3-1">文书段落分类</el-menu-item>
            <el-menu-item index="3-2">情感分类</el-menu-item>
          </el-submenu>
          <el-submenu index="4">
            <template slot="title">关系提取</template>
            <el-menu-item index="4-1">金额属性提取</el-menu-item>
          </el-submenu>
          <el-submenu index="5">
            <template slot="title">语义理解</template>
            <el-menu-item index="5-1">文书QA</el-menu-item>
            <el-menu-item index="5-2">文本纠错</el-menu-item>
            <el-menu-item index="5-3">敏感词过滤</el-menu-item>
          </el-submenu>
          <el-submenu index="6">
            <template slot="title">声学处理</template>
            <el-menu-item index="6-1">去噪</el-menu-item>
            <el-menu-item index="6-2">变声</el-menu-item>
            <el-menu-item index="6-3">合成</el-menu-item>
          </el-submenu>
          <el-submenu index="7">
            <template slot="title">ASR优化</template>
            <el-menu-item index="7-1">口音优化</el-menu-item>
            <el-menu-item index="7-2">领域优化</el-menu-item>
          </el-submenu>
          <el-submenu index="8">
            <template slot="title">智能对话</template>
            <el-menu-item index="8-1">12368</el-menu-item>
            <el-menu-item index="8-2">ETC</el-menu-item>
            <el-menu-item index="8-3">外呼</el-menu-item>
            <el-menu-item index="8-4">物业</el-menu-item>
            <el-menu-item index="8-5">诈骗预警</el-menu-item>
            <el-menu-item index="8-6">自学习</el-menu-item>
          </el-submenu>
          <el-submenu index="9">
            <template slot="title">知识库</template>
            <el-menu-item index="9-1">话术知识库</el-menu-item>
            <el-menu-item index="9-2">法条推荐</el-menu-item>
          </el-submenu> -->
          <!-- <el-menu-item index="4"
            ><a href="https://www.ele.me" target="_blank"
              >订单管理</a
            ></el-menu-item
          > -->
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
      menuName: "st_asr_optimization_choice",
      activeName: "element_extraction",
      //   linkUrls: {
      //     ST_ASR_OPTIMIZATION: "http://st_asr_optimization:8502",
      //     ST_AUDIO_PROCESSING: "http://st_audio_processing:8502",
      //     ST_CASE_RECOMMENDATION: "http://st_case_recommendation:8502",
      //     ST_ELEMENT_EXTRACTION: "http://st_element_extraction:8502",
      //     ST_KNOWLEDGE_DATABASE: "http://st_knowledge_database:8502",
      //     ST_RELATION_EXTRACTION: "http://st_relation_extraction:8502",
      //     ST_SEMANTIC_UNDERSTANDING: "http://st_semantic_understanding:8502",
      //     ST_SMART_DIALOGUE: "http://st_smart_dialogue:8502",
      //     ST_TEXT_CLASSIFICATION: "http://st_text_classification:8502",
      //   },
      //   deployHost: Config.VUE_APP_DEPLOY_HOST,
      //   deployPort: Config.VUE_APP_DEPLOY_PORT,
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

      ifArr: {
        element_extraction: true,
        case_recommendation: false,
        text_classification: false,
        relation_extraction: false,
        semantic_understanding: false,
        audio_processing: false,
        asr_optimazation: false,
        text_classification: false,
        knowledge_database: false,
      },
    };
  },
  methods: {
    handleClick(tab, event) {
      let flagName = tab.name;
      this.ifArr[flagName] = true;
    },
    handleSelect(key, keyPath) {
      this.menuName = key;
      console.log("process.env.VUE_APP_OTHER_IP");
      //   console.log(this.deployHost);
      //   console.log(this.deployPort);
      console.log(this.deployUrl);
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
