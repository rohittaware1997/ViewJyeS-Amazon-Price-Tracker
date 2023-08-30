<template>

  <p v-if="!card_details.length" style="font-size: 2em; margin: 400px; padding-left: 300px">
    No items to track
  </p>
  <div  class="graph-container" style="display: flex; flex-direction: column; align-items: center; flex-wrap: wrap">
    <div class="card-grid-container">
      <div v-for="(card, index) in card_details" :key="index" class="row-item">
        <div>
          <q-card style="border-radius: 15px;" class="my-card" flat bordered>
            <q-img style="width: 290px; height: 300px" :src="card.imageUrl"/>

            <q-card-section>
              <a :href="card.productLink" target="_blank">
                <q-btn
                  fab
                  color="primary"
                  icon="link"
                  class="absolute"
                  style="top: 0; right: 12px; transform: translateY(-50%);"
                  @click="enableRedirect"
                >
                </q-btn>
              </a>

              <div class="row no-wrap items-center">
                <div style="margin-top: 8px" class="col text-h6 ellipsis">
                  {{ card.productName }}
                </div>
              </div>

            </q-card-section>

            <q-card-section class="q-pt-none">
              <div class="text-subtitle1">
                Current Price: {{ card.currentPrice }}$
              </div>
              <div class="text-caption text-grey">
                ASIN: {{ card.asinServer }}
              </div>
            </q-card-section>

            <q-separator/>

            <q-card-actions align="evenly">
              <q-btn v-if="!card.notification_status" @click="popChange1(card.asinServer, index)" flat color="green">
                Disable Notification
              </q-btn>
              <q-btn v-if="card.notification_status" @click="popChange1(card.asinServer, index)" flat color="red">
                Enable Notification
              </q-btn>
              <q-btn @click="popChange2(card.asinServer)" flat color="red">
                Remove Tracking
              </q-btn>
            </q-card-actions>


          </q-card>
          <div style="width: 300px; height: 300px; margin-top: 50px;">
            <canvas :ref="'pieChart_' + index"></canvas>
          </div>
        </div>



        <q-dialog v-model="pop1" persistent transition-show="flip-down" transition-hide="flip-up">
          <q-card>
            <q-card-section class="row items-center">
              <q-avatar icon="notifications" color="primary" text-color="white"/>
              <span class="q-ml-sm">Are you sure you want to disable notification?</span>
            </q-card-section>

            <q-card-actions align="right">
              <q-btn flat label="Cancel" color="primary" v-close-popup/>
              <q-btn flat @click="toggleTracking()" label="Toggle Notification" color="primary" v-close-popup/>
            </q-card-actions>
          </q-card>
        </q-dialog>

        <q-dialog v-model="pop2" persistent transition-show="flip-down" transition-hide="flip-up" auto-close>
          <q-card>
            <q-card-section class="row items-center">
              <q-avatar icon="warning" color="primary" text-color="white"/>
              <span class="q-ml-sm">Are you sure want to remove this tracking</span>
            </q-card-section>

            <q-card-actions align="right">
              <q-btn flat label="Cancel" color="primary" v-close-popup/>
              <q-btn flat @click="removeTracking()" label="Remove Tracking" color="primary" v-close-popup/>
            </q-card-actions>
          </q-card>
        </q-dialog>

      </div>
    </div>
  </div>

</template>

<script>
import {onMounted, ref} from "vue";
import {useStore} from "vuex";
import axios from "axios";
import Chart from 'chart.js/auto';

export default {
  name: "AccountLayout",
  data() {
    return {};
  },
  mounted() {
    let tog = this.store.getters["amazon/getTrackToggle"]
    console.log(tog);
    if (tog == true) {
      console.log("ideal");
      let d = this.store.getters["amazon/getChartData"];
      if (d.length > 0) {
        this.demoFunction(false);
      }
      this.getData(tog);
    } else {
      this.demoFunction(tog);
    }
  },
  setup() {
    let finalChartData = ref([]);
    const redirectFlag = ref(false);
    const store = useStore();
    let card_details = ref([]);
    const apiRemove = "http://34.203.234.126:5000/remove";
    const apiToggle = "http://34.203.234.126:5000/toggleNotification";
    let ASIN = ref("");
    let pop1 = ref(false);
    let pop2 = ref(false);
    let ind = ref(0);
    let chartInstances = ref([]);

    let toggleStatus = ref(true);

    onMounted(() => {
      loadCardData();
    });

    function loadCardData() {
      console.log("in the load card")
      card_details.value = (store.getters["amazon/getCardDetail"]);
    }

    const enableRedirect = () => {
      redirectFlag.value = true;
    };

    const popChange1 = (asin, index) => {
      ASIN.value = asin
      pop1.value = true
      ind.value = index;
    };

    const popChange2 = (asin, index) => {
      ASIN.value = asin
      pop2.value = true
      ind.value = index;
    };
    const removeTracking = () => {
      //  get the asin from store.
      let asin = ASIN.value
      removeFromDB(asin).then((status) => {
        console.log(status);
      });
      const index = card_details.value.findIndex(item => item.asinServer === asin);
      store.dispatch("amazon/removeCardIndex", index);
      pop2.value = false;
    };

    const toggleTracking = () => {

      let asin = ASIN.value
      toggleFromDB(asin).then((status) => {
        console.log(status);
      });
      console.log(ind.value)
      store.dispatch("amazon/toggleNotification", ind.value);
      pop1.value = false;
    };

    const removeFromDB = async (asin) => {
      try {
        const response = await axios.put(apiRemove, {
          asin
        });
        return response.data;
      } catch (error) {
        console.error(error);
      }
    };

    const toggleFromDB = async (asin) => {
      try {
        const response = await axios.put(apiToggle, {
          asin
        });
        return response.data;
      } catch (error) {
        console.error(error);
      }
    };
    return {
      enableRedirect,
      redirectFlag,
      ind,
      card_details,
      pop1,
      pop2,
      store,
      chartInstances,
      removeTracking,
      popChange1,
      popChange2,
      ASIN,
      toggleTracking,
      toggleStatus,
      finalChartData
    };
  },
  methods: {
    async getData(tog) {
      console.log("in this even called")
      axios.get('http://34.203.234.126:5001/add')
        .then((response) => {
          console.log('Data:', response.data);
          let chartData = response.data;
          let demo = chartData.map(str => JSON.parse(str));
          this.store.dispatch("amazon/updateChartData", demo[0]);
          this.demoFunction(tog);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
    demoFunction(tog) {
      console.log("in the demo function");
      this.finalChartData = this.store.getters["amazon/getChartData"];
      console.log(this.finalChartData);
      if (tog) {
        console.log("inside tog");
        this.store.dispatch("amazon/updateTrackToggle");
        let dd = this.store.getters["amazon/getChartData"];
        let index = dd.length - 1;
        console.log(index);
        setTimeout(() => {

          const ctx = this.$refs[`pieChart_${index}`][0].getContext('2d');
          console.log("whats my index", index);
          this.chartInstances[index] = new Chart(ctx, {
            type: 'pie',
            data: {
              labels: ['Positive', 'Negative'],
              datasets: [
                {
                  data: [this.finalChartData[index][1], this.finalChartData[index][0]],
                  backgroundColor: ['#29AB87', '#ff726f'],
                },
              ],
            },
          });
        }, 200);
      } else {
        setTimeout(() => {
          this.finalChartData.forEach((card, index) => {
            const ctx = this.$refs[`pieChart_${index}`][0].getContext('2d');
            console.log("whats my index", index);
            // check if a chart instance already exists for this canvas
            if (this.chartInstances[index]) {
              // if it does, destroy the existing instance
              this.chartInstances[index].destroy();
            }

            // create a new chart instance and add it to the chartInstances array
            this.chartInstances[index] = new Chart(ctx, {
              type: 'pie',
              data: {
                labels: ['Positive', 'Negative'],
                datasets: [
                  {
                    data: [this.finalChartData[index][1], this.finalChartData[index][0]],
                    backgroundColor: ['#29AB87', '#ff726f'],
                  },
                ],
              },
            });
          });
        }, 200);
      }
    }
  }
};
</script>

<style scoped>
.my-card {
  width: 100%;
  max-width: 300px;
}

.card-grid-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-flow: wrap;
}

.row-item {
  width: 300px;
  margin: 80px  20px 20px 20px;
}

</style>
