<script setup>
const dialog = defineModel('dialog', {type: Boolean});
const { items } = defineProps({ 'items': {type: Array}});
</script>

<template>
<v-dialog v-model="dialog">
  <v-card>
    <v-container>
    <template v-for="(item, index) in items" :key="index">
      <v-card-item v-if="item.present">
        <v-card-title>{{item.title}}</v-card-title>
        <v-card-text>{{item.value}}</v-card-text>
      </v-card-item>
    </template>
    <v-card-actions>
      <v-spacer/>
      <v-btn text="明白" @click="dialog = false" variant="tonal"/>
    </v-card-actions>
    </v-container>
  </v-card>
</v-dialog>
</template>

<style scoped>

</style>