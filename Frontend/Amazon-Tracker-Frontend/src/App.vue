<template>
    <AppDrawer></AppDrawer>
</template>

<script>
import {  defineComponent } from "vue";
import AppDrawer from "components/AppDrawer/AppDrawer.vue";


export default defineComponent({
  name: "App",
  components: { AppDrawer }
});
</script>
