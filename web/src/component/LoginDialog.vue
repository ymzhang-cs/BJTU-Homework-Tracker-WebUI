<script setup>
import {reactive, ref} from "vue";
import {LoginStatus} from "../login";
import CoursePlatformLogin from "./CoursePlatformLogin.vue";
import CookiesLogin from "./CookiesLogin.vue";

const dialog = defineModel('dialog', {type: Boolean, default: false});
const loginStatus = defineModel('loginStatus', {type: Number, default: 0});


const loginMethod = ref(null);
const loggingIn = ref(false);
const cpCredential = reactive({
  account: '',
  password: ''
});
const cookiesCredential = ref('');


const loginMethods = [
  {
    title: "MIS",
    value: "mis",
    async login() {
      await pywebview.api.loginViaMis();
    }
  },
  {
    title: "Cookies",
    value: "cookies",
    async login() {
      await pywebview.api.loginViaCookies(cookiesCredential.value);
    }
  },
  {
    title: "课程平台",
    value: "cp",
    async login() {
      await pywebview.api.loginViaCoursePlatform(cpCredential.account, `pass:${cpCredential.password}`);
    }
  },
  {
    title: "课程平台(哈希密码)",
    value: "cp-hash",
    async login() {
      await pywebview.api.loginViaCoursePlatform(cpCredential.account, `hash:${cpCredential.password}`);
    }
  }
];

async function login() {
  loggingIn.value = true;
  loginStatus.value = LoginStatus.LoggingIn;

  const method = loginMethods.find((method) => method.value === loginMethod.value)
  if(method){
    await method.login();
  }

  // because pywebview cannot run js callbacks
  let i = setInterval(async () => {
    const status = await pywebview.api.getLoginStatus();
    loginStatus.value = Number(status);

    if(status === LoginStatus.LoggingIn) {
      return;
    }

    loggingIn.value = false;
    if(status === LoginStatus.LoggedIn) {
      dialog.value = false;
    }
    clearInterval(i);
  }, 200);
}


</script>

<template>
  <v-dialog v-model="dialog">
    <v-container>
      <v-card>
        <v-card-title>登录</v-card-title>
        <v-card-text>
          <v-select label="登录方式" :items="loginMethods" item-title="title" item-value="value"  v-model="loginMethod"/>
          <CoursePlatformLogin v-if="loginMethod === 'cp' || loginMethod === 'cp-hash'" v-model:account="cpCredential.account" v-model:password="cpCredential.password"/>
          <CookiesLogin v-else-if="loginMethod === 'cookies'" v-model:cookies="cookiesCredential"/>
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