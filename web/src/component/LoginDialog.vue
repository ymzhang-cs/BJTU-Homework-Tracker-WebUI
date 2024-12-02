<script setup>
import {ref} from "vue";

const dialog = defineModel('dialog')

const selection = ref(null);

function login() {
  if(selection.value === 'MIS') {
    pywebview.api.loginViaMis();
  }
}

</script>

<template>
  <v-dialog v-model="dialog">
    <v-container>
      <v-card>
        <v-card-title>登录</v-card-title>
        <v-card-text>
          <v-select label="登录方式" :items="['MIS']" v-model="selection"/>
        </v-card-text>
        <v-card-actions>
          <v-spacer/>
          <v-btn text="确定" variant="tonal" @click="login"></v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </v-dialog>
</template>

<style scoped>

</style>