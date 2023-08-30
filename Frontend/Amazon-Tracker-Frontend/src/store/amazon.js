const state = {
  email: null,
  full_name: "User Not Logged In",
  card_detail: [],
  chartData: [],
  trackToggle: false
};
const mutations = {
  setToggleNotification(state, index){
    state.card_detail[index].notification_status = !state.card_detail[index].notification_status
  },
  setEmail(state, email) {
    state.email = email;
  },
  setFullName(state, full_name) {
    state.full_name = full_name;
  },
  setCardDetail(state, card_detail) {
    state.card_detail.push(card_detail);
  },
  setCardEmpty(state, card_empty) {
    state.card_detail = card_empty
    state.chartData = []
  },
  removeCard(state, index) {
    state.card_detail.splice(index, 1);
  },
  setChartData(state, chartData){
    state.chartData.push(chartData);
  },
  setTrackToggle(state){
    state.trackToggle = !state.trackToggle;
  }
};
const actions = {
  updateChartData({commit}, chartData){
    commit("setChartData", chartData);
  },
  updateEmailId({commit}, email) {
    commit("setEmail", email);
  },
  updateFullName({commit}, full_name) {
    commit("setFullName", full_name);
  },
  updateCardDetail({commit}, card_detail) {
    commit("setCardDetail", card_detail);
  },
  updateCardEmpty({commit}, card_empty) {
    commit("setCardEmpty", card_empty)
  },
  removeCardIndex({commit}, index) {
    commit("removeCard", index)
  },
  toggleNotification({commit}, index){
    commit("setToggleNotification", index);
  },
  updateTrackToggle({commit}){
    commit("setTrackToggle")
  }
};
const getters = {
  getEmail(state) {
    return state.email;
  },
  getFullName(state) {
    return state.full_name;
  },
  getCardDetail(state) {
    return state.card_detail;
  },
  getChartData(state){
    return state.chartData;
  },
  getTrackToggle(state){
    return state.trackToggle;
  }
};


export default {
  namespaced: true,
  getters,
  mutations,
  actions,
  state
};
