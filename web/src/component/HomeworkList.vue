<script setup>
import HomeworkCard from "./HomeworkCard.vue";

const props = defineProps({
  homework: {
    type: Array,
    required: true
  }
})
</script>
<template>
  <v-container class="homework-list d-flex flex-row flex-wrap justify-space-around">
    <HomeworkCard v-for="hw in props.homework"
                  class="homework-card ma-2 flex-grow-1"
                  :key="`{hw.courseName}-${hw.title}`"
                  :course-name="hw.courseName"
                  :title="hw.title"
                  :submit-status="hw.submitStatus"
                  :create-at="hw.createAt"
                  :open-at="hw.openAt"
                  :due-at="hw.dueAt">
    </HomeworkCard>
  </v-container>
</template>

<style scoped>
</style>