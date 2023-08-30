<template>

  <div class="container" id="content">
    <form @submit.prevent>
      <h2 class="mb-3">SignUp</h2>
      <div class="input">
        <label for="email">Full Name</label>
        <input
          class="form-control"
          type="text"
          v-model="fullName"
          placeholder="User Name"
        />
      </div>
      <div class="input">
        <label for="email">Email address</label>
        <input
          class="form-control"
          type="text"
          v-model="email"
          placeholder="email@adress.com"
        />
      </div>
      <div class="input">
        <label for="password">Password</label>
        <input
          class="form-control"
          type="password"
          v-model="password"
          placeholder="password123"
        />
      </div>
      <q-item to="/">
        <q-item-label> Already an user? Login Here!!</q-item-label>
      </q-item>
      <p v-if="errMsg">{{ errMsg }}</p>
      <button @click="registerUser" class="mt-4 btn-pers" id="login_button">
        Register
      </button>
    </form>
  </div>
</template>

<script>
import { ref } from "vue";
import { getAuth, createUserWithEmailAndPassword, GoogleAuthProvider, signInWithPopup } from "firebase/auth" ;
import { useRouter } from "vue-router";
import axios from "axios";
import {  useStore } from "vuex";

export default {
  name: "RegisterLayout",
  setup() {
    const email = ref("");
    const password = ref("");
    const fullName = ref("");
    const router = useRouter();
    const auth = getAuth();
    const errMsg = ref();
    const apiUrl = "http://34.203.234.126:5000/register";
    const store = useStore();
    const registerUser = () => {
      console.log("kaha hoo")
      createUserWithEmailAndPassword(auth, email.value, password.value)
        .then((data) => {
         console.log(data);
          console.log("Successfully registered!");
          store.dispatch('amazon/updateFullName',fullName.value)
          store.dispatch('amazon/updateEmailId',email.value)
          registerUserInDB(email.value, fullName.value);
          router.push("/search");
        }).catch((error) => {
        console.log(error.code);
        alert(error.message);
      });
    };

    const registerUserInDB = async (email, fullName) => {
      console.log("in the db function");
      try {
        const response = await axios.put(apiUrl, {
          email,
          fullName
        });
        console.log(response.data); // logs the response from the server
      } catch (error) {
        console.error(error);
      }
    };
    return {
      registerUser,
      email,
      password,
      errMsg,
      fullName
    };
  }
};
</script>

<style scoped>

</style>
