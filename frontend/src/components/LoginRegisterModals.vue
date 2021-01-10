<template>
  <!-- eslint-disable max-len -->
  <div id="loginModal" class="modal">
    <div class="modal-content center">
      <form id="loginForm">
        <div class="input-field">
          <i class="material-icons prefix">person</i>
          <input type="email" id="loginEmail">
          <label for="loginEmail">Email</label>
        </div>
        <br>
        <div class="input-field">
          <i class="material-icons prefix">lock</i>
          <input type="password" id="loginPassword">
          <label for="loginPassword">Password</label>
        </div>
        <input type="button" @click="loginUser" value="Login" class="btn btn-large">
      </form>
    </div>
  </div>
  <div id="registerModal" class="modal">
    <div class="modal-content center">
      <form action="javascript:void(0)" @submit="registerUser" id="registerForm">
        <div class="input-field">
          <i class="material-icons prefix">lock</i>
          <input type="email" id="registerEmail" required>
          <label for="registerEmail">Email</label>
        </div>
        <br>
        <div class="input-field">
          <i class="material-icons prefix">lock</i>
          <input type="password" id="registerPassword" required minlength="6">
          <label for="registerPassword">Password</label>
        </div>
        <button type="submit" class="btn btn-large">Register</button>
      </form>
    </div>
  </div>
  <PositiveNegativeModals v-bind:whichModalToCall="callPositiveOrNegativeLogin"/>
</template>

<script>
import M from 'materialize-css';
import axios from 'axios';
import PositiveNegativeModals from '@/components/PositiveNegativeModals.vue';

export default {
  name: 'LoginRegisterModals',
  computed: {
    console: () => console,
  },
  components: {
    PositiveNegativeModals,
  },
  data() {
    return {
      callPositiveOrNegativeLogin: {
        whichModal: '',
        message: '',
      },
    };
  },
  props: {
    whichModalToCall: String,
  },
  watch: {
    whichModalToCall() {
      if (this.whichModalToCall === 'login') {
        const elemToOpen = document.getElementById('loginModal');
        const elemToClose = document.getElementById('registerModal');
        const instance = M.Modal.getInstance(elemToOpen);
        const instance2 = M.Modal.getInstance(elemToClose);
        instance.open();
        instance2.close();
      } else if (this.whichModalToCall === 'register') {
        const elemToOpen = document.getElementById('registerModal');
        const elemToClose = document.getElementById('loginModal');
        const instance = M.Modal.getInstance(elemToOpen);
        const instance2 = M.Modal.getInstance(elemToClose);
        instance.open();
        instance2.close();
      }
    },
  },
  mounted() {
    M.AutoInit();
  },
  methods: {
    async registerUser() {
      const e = document.getElementById('registerEmail').value;
      const p = document.getElementById('registerPassword').value;
      if (p) {
        await this.$root.$data.fb.auth().createUserWithEmailAndPassword(e, p).then(async () => {
          const id = this.$root.$data.fb.auth().currentUser.uid;
          await axios.post('http://127.0.0.1:5000/clients/'.concat(id.toString()), {
            action: 'create',
          }).then(() => {
            this.$data.callPositiveOrNegativeLogin = {
              whichModal: 'positiveRegister',
              message: 'Account created. You are logged in',
            };
          });
        }).catch((error) => {
          this.$data.callPositiveOrNegativeLogin = {
            whichModal: 'negativeRegister',
            message: error.message,
          };
        });
      }
    },
    async loginUser() {
      const email = document.getElementById('loginEmail').value;
      const password = document.getElementById('loginPassword').value;
      await this.$root.$data.fb.auth().signInWithEmailAndPassword(email, password).then(() => {
        this.$data.callPositiveOrNegativeLogin = {
          whichModal: 'positiveLogin',
          message: 'You are logged in',
        };
      }).catch((error) => {
        this.$data.callPositiveOrNegativeLogin = {
          whichModal: 'negativeLogin',
          message: error.message,
        };
      });
    },
  },
};
</script>

<style scoped>
.modal {
  width: 400px;
}
</style>
