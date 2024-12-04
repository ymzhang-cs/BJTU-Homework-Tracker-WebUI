<script setup>
import {computed, ref} from "vue";
import HomeworkDetailDialog from "./HomeworkDetailDialog.vue";

const props = defineProps({
  courseName: {type: String, required: true},
  title: {type: String, required: true},
  submitStatus: {type: String, required: true},
  content: {type: String, default: null},
  createAt: {type: String, required: false, default: null},
  openAt: {type: String, required: false, default: null},
  dueAt: {type: String, required: false, default: null},
});

const majorItems = computed(() => [
  {title: '课程名称', value: props.courseName, present: true},
  {title: '作业标题', value: props.title, present: true},
  {title: '截止日期', value: props.dueAt, present: props.dueAt !== null},
]);

const items = computed(() => majorItems.value.concat([
  {title: '作业内容', value: props.content, present: props.content !== null && props.content.length > 0},
  {title: '提交人数', value: props.submitStatus, present: true},
  {title: '开放日期', value: props.openAt, present: props.openAt !== null},
  {title: '创建日期', value: props.createAt, present: props.createAt !== null},
]));

const detailPresent = ref(false);

</script>

<template>
  <v-card class="d-flex flex-column">
    <template v-for="(item, i) in majorItems">
      <template v-if="item.present" :key="i">
        <v-card-item
            :title="item.title"
            :subtitle="item.value">
        </v-card-item>
      </template>
    </template>
    <v-spacer/>
    <v-card-actions>
      <HomeworkDetailDialog :items="items" v-model:dialog="detailPresent"/>
      <v-spacer/>
      <v-btn
          icon="mdi-dots-horizontal"
          @click="detailPresent = !detailPresent"/>
    </v-card-actions>
  </v-card>
</template>

<style scoped>

</style>