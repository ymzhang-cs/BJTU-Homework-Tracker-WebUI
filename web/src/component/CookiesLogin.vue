<script setup>
const cookies = defineModel('cookies', {type: String, required: true});
</script>

<template>
  <v-container>
    <v-text-field label="JSESSIONID" v-model="cookies"/>
  </v-container>
</template>

<style scoped>

</style>