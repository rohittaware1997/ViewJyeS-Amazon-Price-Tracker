import {onMounted, ref, defineComponent} from "vue";
import {getAuth, onAuthStateChanged, signOut} from "firebase/auth";
import {useRouter} from "vue-router";
import {mapGetters, useStore} from "vuex";


export default defineComponent({
  name: "AppDrawer",
  computed: {
    ...mapGetters('amazon', ['getFullName'])
  },
  setup() {
    const isLoggedIn = ref(false);
    let auth;
    const router = useRouter();
    const store = useStore();

    onMounted(() => {
      auth = getAuth();
      onAuthStateChanged(auth, (user) => {
          if (user) {
            isLoggedIn.value = true;
          } else {
            isLoggedIn.value = false;
          }
        }
      );
    });
    const handleSignOut = () => {
      signOut(auth).then(() => {
        store.dispatch('amazon/updateCardEmpty', [])
        store.dispatch('amazon/updateFullName', "User Not Logged In")
        router.push("/");
      });
    };
    return {
      isLoggedIn,
      handleSignOut,
      drawer: ref(false)
    };
  }
});
