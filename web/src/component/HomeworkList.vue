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
  <div class="homework-list">
    <HomeworkCard v-for="hw in props.homework"
                  class="homework-card"
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
.homework-list {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-around;
}

.homework-card {
  flex-grow: 1;
  margin: 1rem;
}
</style>