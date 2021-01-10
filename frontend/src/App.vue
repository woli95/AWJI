<template>
  <Navbar/>
  <StoreView v-if:="storeView === true" v-bind:activeCategoryName="whichView"/>
  <BasketModal v-bind:displayBasket="displayBasket"/>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import StoreView from '@/components/StoreView.vue';
import BasketModal from '@/components/BasketModal.vue';

import firebase from 'firebase';

const firebaseConfig = {
  apiKey: 'AIzaSyAmBPbn-RWTeSBg8T0Egd9ellloWnM7pTQ',
  authDomain: 'awji-e562b.firebaseapp.com',
  databaseURL: 'https://awji-e562b.firebaseio.com',
  projectId: 'awji-e562b',
  storageBucket: 'awji-e562b.appspot.com',
  messagingSenderId: '143315052356',
  appId: '1:143315052356:web:9cf1f8b5dc4121723ed911',
};

firebase.initializeApp(firebaseConfig);

export default {
  name: 'App',
  computed: {
    console: () => console,
  },
  data() {
    return {
      fb: firebase,
      basket: [],
      storeView: false,
      whichView: '',
      displayBasket: false,
    };
  },
  components: {
    Navbar, StoreView, BasketModal,
  },
};
</script>

<style>
</style>
