<script setup>
const account = defineModel('account', {type: String, required: true});
const password = defineModel('password', {type: String, required: true});
</script>
<template>
  <v-col>
    <v-text-field label="账号" v-model="account"/>
    <v-text-field label="密码" v-model="password" type="password"/>
  </v-col>
</template>