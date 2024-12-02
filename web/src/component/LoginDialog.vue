<script setup>
import {ref} from "vue";
import {LoginStatus} from "../login";
const dialog = defineModel('dialog')

const selection = ref(null);
const loggingIn = ref(false);

async function login() {
  loggingIn.value = true;
  if(selection.value === 'MIS') {
    await pywebview.api.loginViaMis();
  }
  let i = setInterval(async () => {
    console.log(await pywebview.api.getLoginStatus());
    if(await pywebview.api.getLoginStatus() !== LoginStatus.LoggingIn) {
      loggingIn.value = false;
      clearInterval(i);
    }
  }, 200);
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
          <v-btn text="确定" variant="tonal" :disabled="loggingIn" @click="login"></v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </v-dialog>
</template>

<style scoped>

</style>