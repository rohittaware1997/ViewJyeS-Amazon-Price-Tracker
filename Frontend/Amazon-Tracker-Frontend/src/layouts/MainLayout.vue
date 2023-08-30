<template>
  <div class="container-column">
    <div class="row-item-1">
      <p style="font-size: 3em"> Login to get Trackin !!</p>
    </div>
    <div class="row-item-2" style="padding-bottom: 50px">
      <q-btn to="/" style="font-size: 1.5em; margin-bottom: 40px; width: 250px" outline rounded color="green" label="Login"/>
      <q-separator ></q-separator>
    </div>

  </div>
</template>

<script>
import {defineComponent, ref} from "vue";
import {computed} from 'vue'
import {useQuasar} from "quasar";

export default defineComponent({
  name: "MainLayout",
  components: {},
  setup() {
    const $q = useQuasar();

    return {
      standard: ref(2),
      min: ref(),
      max: ref(),
      val: ref(0),
      layout: computed(() => {
        return $q.screen.lt.sm ? 'dense' : ($q.screen.lt.md ? 'comfortable' : 'loose')
      })
    };
  }
});
</script>

<style scoped>
.container-column {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
