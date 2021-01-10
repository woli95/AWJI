<template>
  <!-- eslint-disable max-len -->
  <div class="card">
    <div class="card-content">
      <h5>Admin panel</h5>
      <p>Choose database element which you want to moderate</p>
    </div>
    <div class="card-tabs">
      <ul class="tabs tabs-fixed-width">
        <li class="tab"><a href="javascript:void(0)" @click='showProductCard'>Products</a></li>
        <li class="tab"><a href="javascript:void(0)" @click='showClientCard'>Clients</a></li>
        <li class="tab"><a href="javascript:void(0)" @click='showOrderCard'>Orders</a></li>
      </ul>
    </div>
    <div class="card-content grey lighten-4">
      <div id="products" class="row">
        <div class="col s3" id="addProduct" style="border: 1px solid black;">
          <h5>Add new product to database</h5>
          <form style="width: auto" @submit="addProductToDatabase" action="javascript:void(0)">
            <div class="input-field">
              <input type="text" id="addProductName" required>
              <label for="addProductName" class="active">Enter product name</label>
            </div>
            <div class="input-field">
              <input type="text" id="addProductDescription">
              <label for="addProductDescription" class="active">Enter product description</label>
            </div>
            <div class="input-field">
              <input type="number" min="0.1" step="0.01" id="addProductUnitPrice" required>
              <label for="addProductUnitPrice" class="active">Enter product unit price</label>
            </div>
            <div class="input-field">
              <input type="number" min="1" step="1" id="addProductUnitWeight">
              <label for="addProductUnitWeight" class="active">Enter product unit weight</label>
            </div>
            <div class="input-field">
              <label for="addProductCategory" class="active">Category</label>
              <select v-model="selected1" id="addProductCategory" required>
                <option value="" disabled selected>Choose product category</option>
                <option>Music</option>
                <option>Sport</option>
                <option>Tobacco</option>
                <option>Electronics</option>
                <option>Games</option>
                <option>Toys</option>
              </select>
            </div>
            <div class="input-field">
              <button type="submit" class="btn btn-small center">ADD NEW PRODUCT</button>
            </div>
          </form>
          <br>
        </div>
        <div class="col s4" id="searchProduct" style="border: 1px solid black;">
          <h5>Search product for update</h5>
          <form action="javascript:void(0)" @submit='productFilter' style="width: auto">
            <div class="input-field">
              <label for="productFilter" class="active">Enter text to filter</label>
              <input type="text" id="productFilter"/>
            </div>
            <button type="submit" class="btn">FILTER</button>
          </form>
          <hr>
          <table v-if="productList != null" class="striped">
            <thead>
              <tr>
                <th>ID</th>
                <th>name</th>
                <th>unit price</th>
                <th>unit weight</th>
                <th>category</th>
                <th>&nbsp;</th>
                <th>&nbsp;</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in productList" :key="item">
                <td>{{ item[0] }}</td>
                <td>{{ item[1] }}</td>
                <td>{{ item[3] }}</td>
                <td>{{ item[4] }}</td>
                <td>{{ item[5] }}</td>
                <td><button type="button" class="btn btn-floating" @click="deleteProductByID(item[0])">X</button></td>
                <td><button type="button" class="btn btn-floating" @click="selectToUpdate(item)">U</button></td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="col s3" id="updateProduct" style="border: 1px solid black;">
          <h5>Update product in database</h5>
          <form style="width: auto" @submit="updateProductInDatabase" action="javascript:void(0)">
            <div class="input-field">
              <input type="text" id="updateProductId" disabled>
              <label for="addProductName" class="active">Enter product id</label>
            </div>
            <div class="input-field">
              <input type="text" id="updateProductName" required>
              <label for="addProductName" class="active">Enter product name</label>
            </div>
            <div class="input-field">
              <input type="text" id="updateProductDescription">
              <label for="addProductDescription" class="active">Enter product description</label>
            </div>
            <div class="input-field">
              <input type="number" id="updateProductUnitPrice" min="0.1" step="0.01" required>
              <label for="addProductUnitPrice" class="active">Enter product unit price</label>
            </div>
            <div class="input-field">
              <input type="number" id="updateProductUnitWeight" min="1" step="1">
              <label for="addProductUnitWeight" class="active">Enter product unit weight</label>
            </div>
            <div class="input-field">
              <label for="updateProductCategory" class="active">Category</label>
              <select v-model="selected2" id="updateProductCategory" required>
                <option disabled selected></option>
                <option>Music</option>
                <option>Sport</option>
                <option>Tobacco</option>
                <option>Electronics</option>
                <option>Games</option>
                <option>Toys</option>
              </select>
            </div>
            <button type="submit" class="btn btn-small center">UPDATE PRODUCT</button>
          </form>
          <br>
          <p><b>Categories:</b></p>
          <p>1: Music</p>
          <p>2: Sport</p>
          <p>3: Tobacco</p>
          <p>4: Electronics</p>
          <p>5: Games</p>
          <p>6: Toys</p>
        </div>
      </div>
      <div id="clients" class="row">
        <div class="col s9" id="searchClient" style="border:1px solid black;">
          <h5>Search client for update</h5>
          <form action="javascript:void(0)" @submit='clientFilter' style="width: auto">
            <div class="input-field">
              <label for="clientFilter">Enter text to filter</label>
              <input type="text" id="clientFilter" class="active"/>
            </div>
            <button type="submit" class="btn">FILTER</button>
          </form>
          <hr>
          <table v-if="clientList != null" class="striped">
            <thead>
              <tr>
                <th>ID</th>
                <th>phone</th>
                <th>city</th>
                <th>street</th>
                <th>street nr</th>
                <th style="width: 20px">&nbsp;</th>
                <th style="width: 20px">&nbsp;</th>
              </tr>
            </thead>
            <tbody>
            <tr v-for="item in clientList" :key="item">
              <td>{{ item[0] }}</td>
              <td>{{ item[1] }}</td>
              <td>{{ item[2] }}</td>
              <td>{{ item[3] }}</td>
              <td>{{ item[4] }}</td>
              <td style="width: 60px"><button type="button" class="btn btn-floating" @click="deleteClientByID(item[0])">X</button></td>
              <td style="width: 60px"><button type="button" class="btn btn-floating" @click="selectClientToUpdate(item)">U</button></td>
            </tr>
            </tbody>
          </table>
        </div>
        <div class="col s3" id="updateClient" style="border: 1px solid black;">
          <h5>Update client in database</h5>
          <form style="width: auto" @submit="updateClientInDatabase" action="javascript:void(0)">
            <div class="input-field">
              <input type="text" id="updateClientId" disabled>
              <label for="updateClientId" class="active">Client ID</label>
            </div>
            <div class="input-field">
              <input type="text" id="updateClientPhone" minlength="9" maxlength="9">
              <label for="updateClientPhone" class="active">Enter client phone</label>
            </div>
            <div class="input-field">
              <input type="text" id="updateClientCity">
              <label for="updateClientCity" class="active">Enter client address city</label>
            </div>
            <div class="input-field">
              <input type="text" id="updateClientStreet">
              <label for="updateClientStreet" class="active">Enter client address street</label>
            </div>
            <div class="input-field">
              <input type="text" id="updateClientStreetNr">
              <label for="updateClientStreetNr" class="active">Enter client address street number</label>
            </div>
            <button type="submit" class="btn btn-small center">UPDATE CLIENT</button>
          </form>
          <br>
        </div>
      </div>
      <div id="orders" class="row">
        <div class="col s9" id="searchCommission" style="border:1px solid black;">
          <h5>Search commission for update</h5>
          <form action="javascript:void(0)" @submit='commissionFilter' style="width: auto">
            <div class="input-field">
              <label for="commissionFilter">Enter text to filter</label>
              <input type="text" id="commissionFilter" class="active"/>
            </div>
            <button type="submit" class="btn">FILTER</button>
          </form>
          <hr>
          <table v-if="commissionList != null" class="striped">
            <thead>
            <tr>
              <th style="width: 20px;">ID</th>
              <th>client id</th>
              <th>current status</th>
              <th style="width: 20px;">&nbsp;</th>
              <th style="width: 20px;">&nbsp;</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in commissionList" :key="item">
              <td>{{ item[0] }}</td>
              <td>{{ item[1] }}</td>
              <td>{{ item[2] }}</td>
              <td style="width: 60px;"><button type="button" class="btn btn-floating" @click="showDetails(item[0])">I</button></td>
              <td style="width: 60px;"><button type="button" class="btn btn-floating" @click="deleteCommission(item[0])">X</button></td>
              <td style="width: 120px;"><button type="button" class="btn btn-floating" @click="openUpdateStatusModal(item[0])">CS</button>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
  <div id="detailsModal" class="modal">
    <div class="modal-content center">
      <div class="row right">
        <a href="javascript:void(0)" @click="closeIt('detailsModal')"><i class="material-icons">close</i></a>
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
  <div id="updateStatusModal" class="modal">
    <div class="modal-content center">
      <div class="container" style="height: 300px">
        <div class="row"/>
        <div class="divider"/>
        <label for="statusChoose" class="active">Choose status</label>
        <select id="statusChoose" v-model="selected3">
          <option disabled value=""></option>
          <option>Not approved</option>
          <option>Canceled</option>
          <option>Confirmed</option>
          <option>Completed</option>
        </select>
        <div class="row">
          <div class="col s6">
            <button type="button" @click="closeIt('updateStatusModal')" class="btn red">Cancel</button>
          </div>
          <div class="col s6">
            <button type="button" @click=changeStatusOfOrder(selected3) class="btn green">Submit</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import M from 'materialize-css';
import axios from 'axios';
import _ from 'lodash/';

export default {
  name: 'AdminPanel',
  computed: {
    console: () => console,
  },
  data() {
    return {
      productList: null,
      clientList: null,
      commissionList: null,
      detailItems: null,
      selected1: '',
      selected2: '',
      productIDToStatusUpdate: null,
      selected3: '',
    };
  },
  methods: {
    showProductCard() {
      document.getElementById('products').style.display = 'block';
      document.getElementById('clients').style.display = 'none';
      document.getElementById('orders').style.display = 'none';
    },
    showClientCard() {
      document.getElementById('products').style.display = 'none';
      document.getElementById('clients').style.display = 'block';
      document.getElementById('orders').style.display = 'none';
    },
    showOrderCard() {
      document.getElementById('products').style.display = 'none';
      document.getElementById('clients').style.display = 'none';
      document.getElementById('orders').style.display = 'block';
    },
    async addProductToDatabase() {
      const pName = document.getElementById('addProductName');
      const pDesc = document.getElementById('addProductDescription');
      const pPrice = document.getElementById('addProductUnitPrice');
      const pWeight = document.getElementById('addProductUnitWeight');
      const pCat = this.selected1;
      await axios.post('http://127.0.0.1:5000/products', {
        name: pName.value,
        description: pDesc.value,
        unit_price: pPrice.value,
        unit_weight: pWeight.value,
        category_name: pCat,
      }).then((response) => {
        if (response.data === 'OK') {
          M.toast({ html: 'Product was added' });
          pName.value = '';
          pDesc.value = '';
          pPrice.value = '';
          pWeight.value = '';
          this.getProductList();
        } else {
          M.toast({ html: 'Something gone wrong' });
        }
      }).catch((error) => {
        M.toast({ html: 'Connection error '.concat(error.message) });
      });
    },
    async getProductList() {
      await axios.get('http://127.0.0.1:5000/products').then((response) => {
        this.productList = response.data;
      }).catch((error) => {
        M.toast({ html: 'Connection error '.concat(error.message) });
      });
    },
    async getClientList() {
      await axios.get('http://127.0.0.1:5000/clients').then((response) => {
        this.clientList = response.data;
      }).catch((error) => {
        M.toast({ html: 'Connection error '.concat(error.message) });
      });
    },
    async getCommissionList() {
      await axios.get('http://127.0.0.1:5000/orders').then((response) => {
        this.commissionList = response.data;
      }).catch((error) => {
        M.toast({ html: 'Connection error '.concat(error.message) });
      });
    },
    async deleteProductByID(id) {
      const url = 'http://127.0.0.1:5000/products/'.concat(id.toString());
      await axios.post(url, {
        action: 'delete',
      }).then((response) => {
        if (response.data === 'OK') {
          M.toast({ html: 'Product has been deleted' });
          this.getProductList();
        } else {
          M.toast({ html: 'Something gone wrong' });
        }
      }).catch((error) => {
        M.toast({ html: 'Connection error '.concat(error.message) });
      });
    },
    async deleteClientByID(id) {
      const url = 'http://127.0.0.1:5000/clients/'.concat(id.toString());
      await axios.post(url, {
        action: 'delete',
      }).then((response) => {
        if (response.data === 'OK') {
          M.toast({ html: 'Client has been deleted' });
          this.clientList = this.getClientList();
        } else {
          M.toast({ html: 'Something gone wrong' });
        }
      }).catch((error) => {
        M.toast({ html: 'Connection error '.concat(error.message) });
      });
    },
    async deleteCommission(id) {
      await axios.post('http://127.0.0.1:5000/orders/'.concat(id.toString()), {
        action: 'delete',
      }).then((response) => {
        if (response.data === 'OK') {
          M.toast({ html: 'Order has been deleted' });
          this.commissionList = this.getCommissionList();
        } else {
          M.toast({ html: 'Something gone wrong' });
        }
      }).catch((error) => {
        M.toast({ html: 'Connection error '.concat(error.message) });
      });
    },
    async productFilter() {
      const filterString = document.getElementById('productFilter').value;
      await this.getProductList();
      if (filterString === '') {
        return;
      }
      this.productList = _.filter(this.productList, (item) => {
        for (let i = 0; i < item.length; i += 1) {
          if (item[i].toString().toLowerCase().indexOf(filterString.toLowerCase()) > -1) {
            return true;
          }
        }
        return false;
      });
    },
    async clientFilter() {
      const filterString = document.getElementById('clientFilter').value;
      await this.getClientList();
      if (filterString === '') {
        return;
      }
      this.clientList = _.filter(this.clientList, (item) => {
        for (let i = 0; i < item.length; i += 1) {
          if (item[i] != null) {
            if (item[i].toString().toLowerCase().indexOf(filterString.toLowerCase()) > -1) {
              return true;
            }
          }
        }
        return false;
      });
    },
    async commissionFilter() {
      const filterString = document.getElementById('commissionFilter').value;
      await this.getCommissionList();
      if (filterString === '') {
        return;
      }
      this.commissionList = _.filter(this.commissionList, (item) => {
        for (let i = 0; i < item.length; i += 1) {
          if (item[i] != null) {
            if (item[i].toString().toLowerCase().indexOf(filterString.toLowerCase()) > -1) {
              return true;
            }
          }
        }
        return false;
      });
    },
    selectToUpdate(item) {
      let cos = '';
      [document.getElementById('updateProductId').value, document.getElementById('updateProductName').value, document.getElementById('updateProductDescription').value, document.getElementById('updateProductUnitPrice').value, document.getElementById('updateProductUnitWeight').value, cos] = item;
      if (cos === 1) {
        this.selected2 = 'Music';
      } else if (cos === 2) {
        this.selected2 = 'Sport';
      } else if (cos === 3) {
        this.selected2 = 'Tobacco';
      } else if (cos === 4) {
        this.selected2 = 'Electronics';
      } else if (cos === 5) {
        this.selected2 = 'Games';
      } else if (cos === 6) {
        this.selected2 = 'Toys';
      }
    },
    selectClientToUpdate(item) {
      [document.getElementById('updateClientId').value, document.getElementById('updateClientPhone').value, document.getElementById('updateClientCity').value, document.getElementById('updateClientStreet').value, document.getElementById('updateClientStreetNr').value] = item;
    },
    async updateProductInDatabase() {
      const pId = document.getElementById('updateProductId');
      const url = 'http://127.0.0.1:5000/products/'.concat(pId.value.toString());
      const pName = document.getElementById('updateProductName');
      const pDesc = document.getElementById('updateProductDescription');
      const pPrice = document.getElementById('updateProductUnitPrice');
      const pWeight = document.getElementById('updateProductUnitWeight');
      await axios.put(url, {
        name: pName.value,
        description: pDesc.value,
        unit_price: pPrice.value,
        unit_weight: pWeight.value,
        category_name: this.selected2,
      }).then((response) => {
        if (response.data === 'OK') {
          M.toast({ html: 'Product was updated' });
          this.getProductList();
          pName.value = '';
          pDesc.value = '';
          pPrice.value = '';
          pWeight.value = '';
          this.selected2 = '';
        } else {
          M.toast({ html: 'Something gone wrong' });
        }
      }).catch((error) => {
        M.toast({ html: 'Connection error '.concat(error.message) });
      });
    },
    async updateClientInDatabase() {
      const cId = document.getElementById('updateClientId');
      const url = 'http://127.0.0.1:5000/clients/'.concat(cId.value.toString());
      const cPhone = document.getElementById('updateClientPhone');
      const cCity = document.getElementById('updateClientCity');
      const cAddress = document.getElementById('updateClientStreet');
      const cAddressNr = document.getElementById('updateClientStreetNr');
      await axios.put(url, {
        phone: cPhone.value,
        address_city: cCity.value,
        address_street: cAddress.value,
        address_number: cAddressNr.value,
      }).then((response) => {
        if (response.data === 'OK') {
          M.toast({ html: 'Client has been updated' });
          this.getClientList();
          cId.value = '';
          cPhone.value = '';
          cCity.value = '';
          cAddress.value = '';
          cAddressNr.value = '';
        } else {
          M.toast({ html: 'Something gone wrong' });
        }
      }).catch((error) => {
        M.toast({ html: 'Connection error '.concat(error.message) });
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
    closeIt(elementId) {
      const element = document.getElementById(elementId);
      const instance = M.Modal.getInstance(element);
      instance.close();
      this.detailItems = null;
    },
    async openUpdateStatusModal(id) {
      this.productIDToStatusUpdate = id;
      const elems = document.querySelectorAll('.modal');
      M.Modal.init(elems);
      const elem = document.getElementById('updateStatusModal');
      const inst = M.Modal.getInstance(elem);
      inst.open();
    },
    async changeStatusOfOrder(st) {
      await axios.put('http://127.0.0.1:5000'.concat('/orders/', this.productIDToStatusUpdate), {
        status: st,
      }).then((response) => {
        if (response.data === 'OK') {
          M.toast({ html: 'Status changed' });
          this.closeIt('updateStatusModal');
          this.getCommissionList();
        } else if (response.data === 'Backward try') {
          M.toast({ html: 'Cannot update backward status' });
        } else if (response.data === 'Values are the same') {
          M.toast({ html: 'Nothing to change, this status is equal to old one' });
        }
      });
    },
  },
  mounted() {
    document.getElementById('products').style.display = 'none';
    document.getElementById('clients').style.display = 'none';
    document.getElementById('orders').style.display = 'none';
    M.AutoInit();
    this.getProductList();
    this.getClientList();
    this.getCommissionList();
  },
};
</script>

<style scoped>
table ,tr td{}
tbody {
  display:block;
  height: 500px;
  overflow:auto;
}
thead, tbody tr {
  display:table;
  width:100%;
  table-layout:fixed;
}
thead {
  width: calc( 100% - 1em );
}
table {
  width: auto;
}
table td {
  overflow: hidden;
}
input[type=number]::-webkit-outer-spin-button,
input[type=number]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
input[type=number] {
  -moz-appearance:textfield;
}
</style>
