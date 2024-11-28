<script setup>
import {computed, ref} from "vue";

const props = defineProps({
  courseName: {type: String, required: true},
  title: {type: String, required: true},
  submitStatus: {type: String, required: true},
  createAt: {type: String, required: false, default: null},
  openAt: {type: String, required: false, default: null},
  dueAt: {type: String, required: false, default: null},
});

const items = computed(() => [
  {title: '课程名称', value: props.courseName, present: true},
  {title: '作业标题', value: props.title, present: true},
  {title: '提交人数', value: props.submitStatus, present: true},
  {title: '创建日期', value: props.createAt, present: props.createAt !== null},
  {title: '开放日期', value: props.openAt, present: props.openAt !== null},
  {title: '截止日期', value: props.dueAt, present: props.dueAt !== null},
]);

</script>

<template>
  <v-card>
    <template v-for="(item, i) in items">
      <v-card-item
          v-if="item.present"
          :key="i"
          :title="item.title"
          :subtitle="item.value">
      </v-card-item>
    </template>
  </v-card>
</template>

<style scoped>

</style>