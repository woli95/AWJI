<template>
  <!-- eslint-disable max-len -->
  <br><br>
  <div class="container">
    <div class="row">
      <div class="col s4 grey lighten-4">
        <p>Update your information:</p>
        <form action="javascript:void(0)" style="width: 300px">
          <div class="input-field">
            <label for="cityPanel" class="active" ><p>Your's address city</p></label>
            <input id="cityPanel" type="text"/>
          </div>
          <div class="input-field">
            <label for="streetPanel" class="active"><p>Your's address street</p></label>
            <input id="streetPanel" type="text"/>
          </div>
          <div class="input-field">
            <label for="numberPanel" class="active"><p>Your's address number</p></label>
            <input id="numberPanel" type="text"/>
          </div>
          <div class="input-field">
            <label for="phonePanel" class="active"><p>Your's phone number</p></label>
            <input id="phonePanel" type="text"/>
          </div>
          <button @click="updateUserInfo" type="button" class="btn green">UPDATE</button>
        </form>
      </div>
      <div class="col s5">
        <button type="button" class="btn green" @click="showAllOrders">SHOW ALL ORDERS</button>
        <table v-if="this.clientOrders !== null">
          <thead>
            <tr>
              <th>Order date</th>
              <th>Status</th>
              <th>Order address</th>
              <th>Receiver</th>
              <th>Order ID</th>
              <th>&nbsp;</th>
            </tr>
          </thead>
          <tbody>
          <tr v-for="item in this.clientOrders" :key="item">
            <td>{{ item[0] }}</td>
            <td>{{ item[3] }}</td>
            <td>{{ item[1] }}</td>
            <td>{{ item[2] }}</td>
            <td>{{ item[4] }}</td>
            <td><button @click="showDetails(item[5])" type="button" class="btn green">details</button></td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div id="detailsModal" class="modal">
    <div class="modal-content center">
      <div class="row right">
        <a href="javascript:void(0)" @click="closeIt()"><i class="material-icons">close</i></a>
      </div>
      <table>
        <thead>
        <tr>
          <th>Product name</th>
          <th>Quantity</th>
          <th>Value per unit</th>
          <th>Total Value</th>
        </tr>
        </thead>
        <tbody v-if="this.detailItems != null">
        <tr v-for="item in this.detailItems" :key="item">
          <td>{{ item[0] }}</td>
          <td>{{ item[1] }}</td>
          <td>{{ item[2] }} zł.</td>
          <td>{{ item[2]*item[1] }} zł.</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import M from 'materialize-css';
import axios from 'axios';

export default {
  name: 'UserPanel',
  computed: {
    console: () => console,
  },
  data() {
    return {
      clientOrders: null,
      detailItems: null,
    };
  },
  methods: {
    async showAllOrders() {
      await axios.get('http://127.0.0.1:5000/clients/'.concat(this.$root.$data.fb.auth().currentUser.uid.toString()).concat('/orders')).then((response) => {
        this.clientOrders = response.data;
      }).catch((error) => {
        M.toast({ html: 'Connection error '.concat(error.message) });
      });
    },
    async updateUserInfo() {
      const city = document.getElementById('cityPanel').value;
      const street = document.getElementById('streetPanel').value;
      const number = document.getElementById('numberPanel').value;
      const phoneNum = document.getElementById('phonePanel').value;
      await axios.put('http://127.0.0.1:5000/clients/'.concat(this.$root.$data.fb.auth().currentUser.uid.toString()), {
        phone: phoneNum,
        address_city: city,
        address_street: street,
        address_number: number,
      }).then((response) => {
        if (response.data === 'OK') {
          M.toast({ html: 'Profile has been updated' });
        } else {
          M.toast({ html: 'Something gone wrong ' });
        }
      }).catch((error) => {
        M.toast({ html: 'Connection problem '.concat(error.message) });
      });
    },
    async fillCurrentInfo() {
      await axios.get('http://127.0.0.1:5000/clients/'.concat(this.$root.$data.fb.auth().currentUser.uid.toString())).then((response) => {
        this.console.log(response.data);
        [, document.getElementById('phonePanel').value, document.getElementById('cityPanel').value, document.getElementById('streetPanel').value, document.getElementById('numberPanel').value] = response.data;
      }).catch((error) => {
        M.toast({ html: 'Connection problem '.concat(error.message) });
      });
    },
    async showDetails(idCommission) {
      await axios.get('http://127.0.0.1:5000/orders/'.concat(idCommission.toString())).then((response) => {
        this.detailItems = response.data;
        const element = document.getElementById('detailsModal');
        M.AutoInit();
        const instance = M.Modal.getInstance(element);
        instance.open();
      }).catch((error) => {
        M.toast({ html: 'Connection error '.concat(error.message) });
      });
    },
    closeIt() {
      const element = document.getElementById('detailsModal');
      const instance = M.Modal.getInstance(element);
      instance.close();
      this.detailItems = null;
    },
  },
  mounted() {
    this.fillCurrentInfo();
  },
};
</script>

<style scoped>

</style>
