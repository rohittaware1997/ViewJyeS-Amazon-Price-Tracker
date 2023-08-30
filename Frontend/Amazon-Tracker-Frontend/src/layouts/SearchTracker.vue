<template>
  <div class="search-container-grid">
    <div class="search-row row-1">
      <div class="search-row-item-1">
        <q-item-label>
          Amazon Link:
        </q-item-label>
      </div>
      <div class="search-row-item-2">
        <q-input rounded outlined v-model="text">
          <template v-slot:append>
            <q-avatar>
              <img src="../assets/amazon-logo.png">
            </q-avatar>
          </template>
        </q-input>
      </div>
      <div class="search-row-item-3">
        <q-btn :loading="loading[0]" color="primary" @click="simulateProgress(0)" style="width: 150px">
          Track
          <template v-slot:loading>
            <q-spinner-hourglass class="on-left" />
            Loading...
          </template>
        </q-btn>
      </div>
    </div>
    <div class="search-row row-2">
      <div class="search-row-item-1">
        <q-toggle
          v-model="priceDecrease"
          @click="changeToggle1"
          checked-icon="check"
          color="green"
          label="Notify when price decrease"
          unchecked-icon="clear"
        />
        <q-toggle
          v-model="everyHour"
          checked-icon="check"
          @click="changeToggle2"
          color="green"
          label="Notify every 12 hours"
          unchecked-icon="clear"
        />
      </div>
    </div>
  </div>

</template>

<script>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

export default {
  name: "SearchTracker",
  setup() {
    const loading = ref([
      false
    ]);
    const apiUrl = "http://34.203.234.126:5000/track";
    const router = useRouter();
    const priceDecrease = ref(true);
    const everyHour = ref(false);
    const store = useStore();

    const changeToggle1 = () =>{
        everyHour.value = !everyHour.value
    }
    const changeToggle2 = () =>{
        priceDecrease.value = !priceDecrease.value
    }
    function simulateProgress(number) {
      // we set loading state
      loading.value[number] = true;

      let toggleValue;

      if (everyHour.value)
        toggleValue = 1;
      else if (priceDecrease.value)
        toggleValue = 0;

      if (this.text !== "") {
        setTracker(this.text, toggleValue, store.getters["amazon/getEmail"]).then((data) => {
          console.log(data);
          store.dispatch("amazon/updateCardDetail", data);
          store.dispatch("amazon/updateTrackToggle");
          router.push("/account");
        }).catch((error) =>{
          alert(error);
          this.text = "";
        });
        // simulate a delay
        setTimeout(() => {
          // we're done, we reset loading state
          loading.value[number] = false;
        }, 3000);
      } else {
        loading.value[number] = false;
        alert("Enter a link");
      }
    }

    const setTracker = async (link, toggleValue, email) => {
      console.log("in tracker");
      try {
        const response = await axios.put(apiUrl, {
          link,
          toggleValue,
          email
        });
        return response.data;
      } catch (error) {
        const errMsg = error.response.data.error;
        console.error(errMsg);
        return Promise.reject(errMsg)
      }
    };

    return {
      text: ref(""),
      priceDecrease,
      everyHour,
      loading,
      store,
      simulateProgress,
      changeToggle1,
      changeToggle2
    };
  }
};
</script>

<style scoped>
.search-container-grid {
  display: flex;
  flex-direction: column;
}

.search-row {
  display: flex;
  justify-content: space-evenly;
  align-items: baseline;
}

.row-1 {
  padding-top: 100px;
}

.search-row-item-1 {
}

.search-row-item-2 {
  width: 80%;
}

.search-row-item-3 {
}
</style>
