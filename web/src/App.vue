<script setup>
import HomeworkList from "./component/HomeworkList.vue";
import {computed, ref} from "vue";

const homework = ref([]);

pywebview.api.listAllHomework().then(hw => {
    homework.value = hw;
});

</script>

<template>
  <v-app>
    <v-app-bar>
      <v-app-bar-nav-icon></v-app-bar-nav-icon>
      BJTU Homework Tracker
    </v-app-bar>
    <v-main>
      <v-container>
        <HomeworkList :homework="homework"></HomeworkList>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>

</style>