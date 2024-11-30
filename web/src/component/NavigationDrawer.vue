<script setup>
import {useDisplay} from "vuetify";
import {computed, onMounted, ref} from "vue";

const hidden = defineModel('hidden', {type:Boolean, default: false});
const items = [
  {title: '通过MIS登录', onclick: () => pywebview.api.loginViaMis()}
];
</script>

<template>
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