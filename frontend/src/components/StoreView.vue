<template>
  <!-- eslint-disable max-len -->
  <div class="container">
    <br><br>
    <div class="row">
      <form style="width: auto" action="javascript:void(0)">
        <div class="input-field col s3" style="margin: auto;">
          <input @input='searchList' id="search" type="text">
          <label class="label-icon left" for="search"><i class="material-icons">search</i> What are you looking for?</label>
        </div>
      </form>
    </div>
    <div class="row">
      <div class="col s6" style="width: 100%">
        <table class='striped' v-if="productList != null" style="border: inset 1px lightgreen">
          <thead class="light-green white-text">
            <tr>
              <th>NAME</th>
              <th>PRICE</th>
              <th>DESCRIPTION</th>
              <th>WEIGHT</th>
              <th>&nbsp;</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="product in productList" :key="product">
              <td>{{ product[1] }}</td>
              <td>{{ product[3] }} zł</td>
              <td>{{ product[2] }}</td>
              <td>{{ product[4] }} g</td>
              <td><button @click="addProductToBasket(product)" type="button" class="btn btn-floating green">ADD</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import _ from 'lodash';
import M from 'materialize-css';

export default {
  name: 'StoreView',
  computed: {
    console: () => console,
  },
  props: {
    activeCategoryName: String,
  },
  data() {
    return {
      productList: null,
      activeCategoryID: null,
    };
  },
  methods: {
    async getCategoryID() {
      await axios.get('http://127.0.0.1:5000/categories/'.concat(this.activeCategoryName.toString())).then((response) => {
        this.activeCategoryID = response.data;
      });
    },
    async getProductList() {
      await axios.get('http://127.0.0.1:5000/products').then((response) => {
        this.productList = response.data;
      }).catch((error) => {
        M.toast({ html: 'Connection error '.concat(error.message) });
      });
    },
    filterList() {
      /* eslint-disable */
      this.productList = _.filter(this.productList, (item) => item[5].toString() === this.activeCategoryID.toString());
      /* eslint-enable */
    },
    async searchList() {
      await this.getProductList();
      this.filterList();
      const string = document.getElementById('search').value;
      if (string === '') {
        return;
      }
      this.productList = _.filter(this.productList, (item) => {
        for (let i = 0; i < item.length; i += 1) {
          /* eslint-disable */
          if (item[i] == null) {
            i += 1;
            i -= 1;
          } else {
            if (item[i].toString().toLowerCase().indexOf(string.toString().toLowerCase()) > -1) {
              return true;
            }
          }
        }
        return false;
        /* eslint-enable */
      });
    },
    addProductToBasket(product) {
      for (let i = 0; i < this.$root.$data.basket.length; i += 1) {
        if (this.$root.$data.basket[i].thing === product) {
          return;
        }
      }
      this.$root.$data.basket.push({
        thing: product,
        quantity: 1,
      });
    },
  },
  async mounted() {
    await this.getProductList();
    await this.getCategoryID();
    this.filterList();
  },
  watch: {
    async activeCategoryName() {
      await this.getProductList();
      await this.getCategoryID();
      this.filterList();
    },
  },
};
</script>

<style scoped>

</style>
