<script setup>
import HomeworkList from "./component/HomeworkList.vue";
import {computed, ref} from "vue";
import NavigationDrawer from "./component/NavigationDrawer.vue";

const homework = ref([]);
const homeworkAvailable = ref(false);

pywebview.api.listAllHomework().then(hw => {
    homeworkAvailable.value = true;
    homework.value = hw;
});

const drawerHidden = ref(false);

</script>

<template>
  <v-app>
    <v-app-bar>
      <v-app-bar-nav-icon @click="drawerHidden = !drawerHidden"></v-app-bar-nav-icon>
      <v-app-bar-title>BJTU Homework Tracker</v-app-bar-title>
    </v-app-bar>
    <NavigationDrawer v-model:hidden="drawerHidden"></NavigationDrawer>
    <v-main>
      <v-container>
        <VProgressCircular v-if="!homeworkAvailable" indeterminate></VProgressCircular>
        <HomeworkList v-else :homework="homework"></HomeworkList>
      </v-container>
    </v-main>
  </v-app>
</template>

<style>
html {
  scrollbar-width: none;
}
</style>