<template>
  <!-- eslint-disable max-len -->
  <nav class="light-green">
    <div class="nav-wrapper fixed-top">
      <ul class="left hide-on-med-and-down">
        <li @click="showStoreView('Music')"><a href="javascript:void(0)"><i class="material-icons left">library_music</i>Music</a></li>
        <li @click="showStoreView('Sport')"><a href="javascript:void(0)"><i class="material-icons left">fitness_center</i>Sport</a></li>
        <li @click="showStoreView('Tobacco')"><a href="javascript:void(0)"><i class="material-icons left">smoking_rooms</i>Tobacco</a></li>
        <li @click="showStoreView('Electronics')"><a href="javascript:void(0)"><i class="material-icons left">tablet_mac</i>Electronics</a></li>
        <li @click="showStoreView('Games')"><a href="javascript:void(0)"><i class="material-icons left">casino</i>Games</a></li>
        <li @click="showStoreView('Toys')"><a href="javascript:void(0)"><i class="material-icons left">toys</i>Toys</a></li>
      </ul>

      <ul class="right hide-on-med-and-down">
        <li><a href="javascript:void(0)" @click="this.callModal = 'login'" v-if:="this.$root.$data.fb.auth().currentUser == null">Sign In</a></li>
        <li><a href="javascript:void(0)" @click="this.callModal = 'register'" v-if:="this.$root.$data.fb.auth().currentUser == null">Sign Up</a></li>
        <li><a href="javascript:void(0)" @click="userPanelOnOff" v-if:="this.$root.$data.fb.auth().currentUser != null">{{ this.$root.$data.fb.auth().currentUser.email }}</a></li>
        <li><a href="javascript:void(0)" v-if:="this.$root.$data.fb.auth().currentUser != null && this.$root.$data.fb.auth().currentUser.email === 'admin@o2.pl'" @click='adminPanelOnOff' class='btn green'>Admin Panel</a></li>
        <li><a href="javascript:void(0)" @click="logOut" v-if:="this.$root.$data.fb.auth().currentUser != null">Logout</a></li>
        <li><a href="javascript:void(0)" @click="this.$root.$data.displayBasket = true"><i class="material-icons left">shopping_basket</i>{{ this.$root.$data.basket.length.toString() }}</a></li>
      </ul>
    </div>
  </nav><br><br>
  <AdminPanel v-if="adminPanelOn === true"/>
  <UserPanel v-if="userPanelOn === true"/>
  <LoginRegisterModals v-if:="this.$root.$data.fb.auth().currentUser == null" v-bind:whichModalToCall="this.$data.callModal"/>
</template>

<script>
import LoginRegisterModals from '@/components/LoginRegisterModals.vue';
import AdminPanel from '@/components/AdminPanel.vue';
import UserPanel from '@/components/UserPanel.vue';

export default {
  name: 'Navbar',
  computed: {
    console: () => console,
  },
  components: {
    LoginRegisterModals, AdminPanel, UserPanel,
  },
  data() {
    return {
      callModal: '',
      adminPanelOn: false,
      userPanelOn: false,
    };
  },
  methods: {
    logOut() {
      this.$root.$data.fb.auth().signOut();
      document.location.href = '/';
    },
    adminPanelOnOff() {
      if (this.adminPanelOn === true) {
        this.adminPanelOn = false;
      } else {
        this.adminPanelOn = true;
      }
    },
    userPanelOnOff() {
      if (this.userPanelOn === true) {
        this.userPanelOn = false;
      } else {
        this.userPanelOn = true;
      }
    },
    showStoreView(cat) {
      this.$root.$data.storeView = true;
      this.$root.$data.whichView = cat;
    },
  },
};
</script>

<style scoped>
nav {
  position: fixed;
  top:0;
}
</style>
