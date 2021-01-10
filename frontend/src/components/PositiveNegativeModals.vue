<template>
  <!-- eslint-disable max-len -->
  <div id='positiveRegisterModal' class="modal">
    <div class="modal-content">
      <h3>Account created!</h3>
      <p>Click button to continue your yourney.</p>
      <a type="button" @click="closeModal('positiveRegisterModal')" class="btn">Continue</a>
    </div>
  </div>
  <div id='negativeRegisterModal' class="modal">
    <div class="modal-content">
      <h3>Unable to create account!</h3>
      <p>{{ whichModalToCall.message }}</p>
      <button type="button" @click="closeModal('negativeRegisterModal')" class="btn">Try again</button>
    </div>
  </div>
  <div id='positiveLoginModal' class="modal">
    <div class="modal-content">
      <h3>You are logged in!</h3>
      <a type="button" @click="closeModal('positiveLoginModal')" class="btn">OK</a>
    </div>
  </div>
  <div id='negativeLoginModal' class="modal">
    <div class="modal-content">
      <h3>Unable to login!</h3>
      <p>{{ whichModalToCall.message }}</p>
      <button type="button" @click="closeModal('negativeLoginModal')" class="btn">Try again</button>
    </div>
  </div>
</template>

<script>
import M from 'materialize-css';

export default {
  name: 'PositiveNegativeModals',
  computed: {
    console: () => console,
  },
  mounted() {
    M.AutoInit();
  },
  props: {
    whichModalToCall: Object,
  },
  watch: {
    whichModalToCall() {
      if (this.whichModalToCall.whichModal === 'positiveRegister') {
        const elemToOpen = document.getElementById('positiveRegisterModal');
        const instance = M.Modal.getInstance(elemToOpen);
        instance.open();
      } else if (this.whichModalToCall.whichModal === 'negativeRegister') {
        const elemToOpen = document.getElementById('negativeRegisterModal');
        const instance = M.Modal.getInstance(elemToOpen);
        instance.open();
      } else if (this.whichModalToCall.whichModal === 'positiveLogin') {
        const elemToOpen = document.getElementById('positiveLoginModal');
        const instance = M.Modal.getInstance(elemToOpen);
        instance.open();
      } else if (this.whichModalToCall.whichModal === 'negativeLoginModal') {
        const elemToOpen = document.getElementById('negativeLoginModal');
        const instance = M.Modal.getInstance(elemToOpen);
        instance.open();
      }
    },
  },
  methods: {
    closeModal(id) {
      const elementToClose = document.getElementById(id);
      const inst = M.Modal.getInstance(elementToClose);
      inst.close();
      document.location.href = '/';
    },
  },
};
</script>

<style scoped>

</style>
