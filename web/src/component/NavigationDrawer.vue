<script setup>
import {useDisplay} from "vuetify";
import {computed, onMounted, ref} from "vue";
import LoginDialog from "./LoginDialog.vue";

const hidden = defineModel('hidden', {type:Boolean, default: false});
const dialog = ref(false);
const items = [
  {title: '登录', onclick: () => dialog.value = true},
];
</script>

<template>
  <LoginDialog v-model:dialog="dialog"></LoginDialog>
  <v-navigation-drawer v-model="hidden" location="left" temporary>
    <v-list>
      <v-list-item
          v-for="(item, key) in items"
          :key="key"
          :title="item.title"
          @click="item.onclick"/>
    </v-list>
  </v-navigation-drawer>
</template>

<style scoped>

</style>