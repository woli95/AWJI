<template>
  <!-- eslint-disable max-len -->
  <div id="basketModal" class="modal">
    <div class="modal-content center">
      <div class="row">
        <a href="javascript:void(0)" @click="this.$root.$data.displayBasket = false"><i class="material-icons right">close</i></a>
      </div>
      <!-- eslint-disable -->
      <div v-if:="this.$root.$data.basket.length > 0">
        <div class="row">
          <p>Your current items: </p>
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>&nbsp;</th>
              </tr>
            </thead>
            <tbody>
            <tr v-for=" product in this.$root.$data.basket" :key="product">
              <td>{{ product.thing[1] }}</td>
              <td>{{ product.thing[3] }}</td>
              <td><input type="number" min="1" value="1" @change="changeQuantity($event, product)" style="width: 30px"></td>
              <td><button type="button" @click="removeFromBasket(product)" class="btn green lighten-2">Remove Item</button></td>
            </tr>
            </tbody>
          </table>
        </div>
        <div class="row">
          <p class="right"><b>Total value: </b>{{ this.calculateTotalValue().toString() }} zł</p>
        </div>
        <div class="row">
          <button v-if="proceeded === false" type="button" id="proceedButton" @click="proceed" class="btn right green">PROCEED</button>
        </div>
        <div v-if="proceeded === true" id="row">
          <div class="row"><p class="left">Please, enter necessary informations for delivery :</p></div>
          <form style="width: 50%;">
            <div class="input-field">
              <label for="receiverCommission" class="active">Receiver name or title</label>
              <input type="text" id="receiverCommission" required/>
            </div>
            <div class="input-field">
              <label for="phoneCommission" class="active">Enter your phone number</label>
              <input type="text" id="phoneCommission" required/>
            </div>
            <div v-if="this.$root.$data.fb.auth().currentUser === null" class="input-field">
              <label for="emailCommission" class="active">Enter your email</label>
              <input type="email" id="emailCommission" required/>
            </div>
            <div v-if="this.$root.$data.fb.auth().currentUser === null" class="input-field">
              <label for="passwordCommission" class="active">Enter your password</label>
              <input type="email" id="passwordCommission" required/>
            </div>
            <div class="input-field">
              <label for="addressCommission" class="active">Enter full address</label>
              <input type="text" id="addressCommission" required/>
            </div>
            <button type="button" @click="submitCommission" class="btn">SUBMIT</button>
          </form>
        </div>
      </div>
      <div v-else class="row">
        <p>YOUR BASKET IS EMPTY</p>
      </div>
      <!-- eslint-enable -->
    </div>
  </div>
</template>

<script>
import M from 'materialize-css';
import axios from 'axios';

export default {
  name: 'BasketModal',
  props: {
    displayBasket: Boolean,
  },
  data() {
    return {
      proceeded: false,
    };
  },
  computed: {
    console: () => console,
  },
  mounted() {
    M.AutoInit();
  },
  watch: {
    displayBasket() {
      const element = document.getElementById('basketModal');
      const instance = M.Modal.getInstance(element);
      if (this.displayBasket === true) {
        instance.open();
        this.proceeded = false;
      } else {
        instance.close();
        this.proceeded = false;
      }
    },
  },
  methods: {
    async proceed() {
      this.proceeded = true;
      if (this.$root.$data.fb.auth().currentUser != null) {
        const user = await axios.get('http://127.0.0.1:5000/clients/'.concat(this.$root.$data.fb.auth().currentUser.uid.toString())).catch((error) => {
          M.toast({ html: 'Connection error '.concat(error.message) });
        });
        let city;
        let street;
        let number;
        let strr = '';
        [, document.getElementById('phoneCommission').value, city, street, number] = user.data;
        if (city !== 'undefined') {
          strr = city;
        }
        if (street !== 'undefined') {
          strr += ' ';
          strr += street;
        }
        if (number !== 'undefinied') {
          strr += ' ';
          strr += number;
        }
        document.getElementById('addressCommission').value = strr;
      }
    },
    removeFromBasket(product) {
      for (let i = 0; i < this.$root.$data.basket.length; i += 1) {
        if (product === this.$root.$data.basket[i]) {
          this.$root.$data.basket.splice(i, 1);
          return;
        }
      }
    },
    async submitCommission() {
      const fulladdress = document.getElementById('addressCommission').value;
      const receiver = document.getElementById('receiverCommission').value;
      let isOK = false;
      if (this.$root.$data.fb.auth().currentUser === null) {
        const email = document.getElementById('emailCommission').value;
        const password = document.getElementById('passwordCommission').value;
        /* eslint-disable */
        await this.$root.$data.fb.auth().createUserWithEmailAndPassword(email, password).then(() => {
          const id = this.$root.$data.fb.auth().currentUser.uid;
          /* eslint-enable */
          axios.post('http://127.0.0.1:5000/clients/'.concat(id.toString()), {
            action: 'create',
          });
          M.toast({ html: 'Account has been created' });
          isOK = true;
        }).catch((error) => {
          M.toast({ html: 'Something gone wrong '.concat(error.message) });
        });
      } else {
        isOK = true;
      }
      if (isOK === false) {
        return;
      }
      await axios.post('http://127.0.0.1:5000/orders', {
        client_id: this.$root.$data.fb.auth().currentUser.uid.toString(),
        full_address: fulladdress,
        receiver_name: receiver,
        items: this.$root.$data.basket,
      }).then((response) => {
        if (response.data === 'OK') {
          M.toast({ html: 'Order has been created' });
          const element = document.getElementById('basketModal');
          const instance = M.Modal.getInstance(element);
          instance.close();
          this.proceeded = false;
          this.$root.$data.basket = [];
        } else {
          M.toast({ html: 'Something gone wrong' });
        }
      }).catch((error) => {
        M.toast({ html: 'Connection error '.concat(error.message) });
      });
      this.$root.$data.displayBasket = false;
    },
    changeQuantity(event, product) {
      /* eslint-disable no-param-reassign */
      product.quantity = event.target.value;
      /* eslint-enable no-param-reassign */
    },
    calculateTotalValue() {
      let sum = 0.0;
      for (let i = 0; i < this.$root.$data.basket.length; i += 1) {
        sum += this.$root.$data.basket[i].thing[3] * this.$root.$data.basket[i].quantity;
      }
      return sum;
    },
  },
};
</script>

<style scoped>

</style>
