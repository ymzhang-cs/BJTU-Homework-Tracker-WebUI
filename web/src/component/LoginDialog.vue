<script setup>
import {reactive, ref} from "vue";
import {LoginStatus} from "../login";
import CoursePlatformLogin from "./CoursePlatformLogin.vue";
const dialog = defineModel('dialog')

const loginMethod = ref(null);
const loggingIn = ref(false);

const cpCredential = reactive({
  account: '',
  password: ''
});

async function login() {
  loggingIn.value = true;
  if(loginMethod.value === 'mis') {
    await pywebview.api.loginViaMis();
  }
  let i = setInterval(async () => {
    if(await pywebview.api.getLoginStatus() !== LoginStatus.LoggingIn) {
      loggingIn.value = false;
      clearInterval(i);
    }
  }, 200);
}

const loginMethods = [
  {
    "title": "MIS",
    "value": "mis",
  },
  {
    "title": "Cookies",
    "value": "cookie",
  },
  {
    "title": "课程平台",
    "value": "cp",
  },
  {
    "title": "课程平台(哈希密码)",
    "value": "cp-hash",
  }
];

</script>

<template>
  <v-dialog v-model="dialog">
    <v-container>
      <v-card>
        <v-card-title>登录</v-card-title>
        <v-card-text>
          <v-select label="登录方式" :items="loginMethods" item-title="title" item-value="value"  v-model="loginMethod"/>
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