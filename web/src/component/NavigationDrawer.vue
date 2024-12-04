<script setup>
import {useDisplay} from "vuetify";
import {computed, onMounted, ref} from "vue";
import LoginDialog from "./LoginDialog.vue";
import {LoginStatus} from "../login";

const hidden = defineModel('hidden', {type:Boolean, default: false});
const dialog = ref(false);

const loginStatus = ref(LoginStatus.NotLoggedIn);

pywebview.api.getLoginStatus().then(ls => {
  loginStatus.value = Number(ls);
});

const items = [
  {
    title: '登录',
    onclick() {
      dialog.value = true
    },
    display() {
      return loginStatus.value === LoginStatus.NotLoggedIn;
    }
  },
  {
    title: '登出',
    onclick() {
      pywebview.api.logout();
      loginStatus.value = LoginStatus.NotLoggedIn;
    },
    display() {
      return loginStatus.value === LoginStatus.LoggedIn;
    }
  }
];
</script>

<template>
  <LoginDialog v-model:dialog="dialog" v-model:login-status="loginStatus"></LoginDialog>
  <v-navigation-drawer v-model="hidden" location="left" temporary>
    <v-list>
      <template v-for="(item, key) in items" :key="key">
        <v-list-item
            v-if="item.display()"
            :title="item.title"
            @click="item.onclick"/>
      </template>
    </v-list>
  </v-navigation-drawer>
</template>

<style scoped>

</style>