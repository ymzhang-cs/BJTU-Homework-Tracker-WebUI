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
  <div class="homework-list d-flex flex-row flex-wrap justify-space-around">
    <HomeworkCard v-for="hw in props.homework"
                  class="homework-card ma-2 flex-grow-1"
                  :course-name="hw.courseName"
                  :title="hw.title"
                  :submit-status="hw.submitStatus"
                  :create-at="hw.createAt"
                  :open-at="hw.openAt"
                  :due-at="hw.dueAt">
    </HomeworkCard>
  </div>
</template>

<style scoped>
</style>