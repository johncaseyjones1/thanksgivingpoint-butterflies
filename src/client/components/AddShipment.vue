<template>
  <div class="add-shipment-container">
    <div class="center-div">
      <div class="heading">Add a new shipment</div>
      <div class="input-group mb-3">
        <div class="subheading">Date:</div>
        <v-date-picker color="orange" is-inline v-model="date" />
      </div>
      <div class="column-div">
        <div class="input-group mb-3">
          <div class="subheading">Supplier:</div>
          <input type="text" class="form-control" v-model="supplier"/>
        </div>
        <div class="options" v-if="supplier.length > 0 && supplierList.length > 0 && !selected">
          <div v-for="supplier in supplierList" v-bind:key="supplier">
            <button class="btn btn-outline-dark" @click="selectSupplier(supplier)">{{ supplier }}</button>
          </div>
        </div>
      </div>
      <div class="column-div">
        <div class="input-group mb-3">
          <div class="subheading">Species:</div>
          <input type="text" class="form-control" v-model="speciesName"/>
        </div>
        <div class="options" v-if="speciesName.length > 0 && speciesList.length > 0 && !selected">
          <div v-for="option in speciesList" v-bind:key="option.Species">
            <button class="btn btn-outline-dark" @click="selectSpecies(option.Species)">{{ option.Species }}</button>
          </div>
        </div>
      </div>
      <div class="column-div">
        <div class="input-group mb-3">
          <div class="subheading">Origin:</div>
          <input type="text" class="form-control" v-model="origin"/>
        </div>
        <div class="options" v-if="origin.length > 0 && origin.length > 0 && !selected">
          <div v-for="origin in originList" v-bind:key="origin">
            <button class="btn btn-outline-dark" @click="selectOrigin(origin)">{{ origin }}</button>
          </div>
        </div>
      </div>
      <div class="input-group mb-3">
        <div class="subheading">Quantity:</div>
        <input type="text" class="form-control" v-model="quantity"/>
      </div>
      <div class="input-group mb-3">
        <div class="subheading">Emerged early:</div>
        <input type="text" class="form-control" v-model="emergedEarly"/>
      </div>
      <div class="input-group mb-3">
        <div class="subheading">Dead on arrival:</div>
        <input type="text" class="form-control" v-model="deadOnArrival"/>
      </div>

      <div class="row-div">
        <div class="button-div"> 
          <button class="btn btn-dark" @click="submitShipment()">Submit</button>
        </div>

        <b-alert
          :show="dismissCountDown"
          dismissible
          variant="success"
          @dismissed="dismissCountDown=0"
          @dismiss-count-down="countDownChanged"
        >
          <p>Shipment added succesfully!</p>
        </b-alert>
      </div>
    </div>
  </div>  
</template>

<script>
import request from 'superagent-bluebird-promise'

export default {
  name: 'AddShipment',
  data() {
    return {
      allButterflies: "",
      speciesName: "",
      selected: false,
      date: null,
      supplier: "",
      origin: "",
      quantity: "",
      emergedEarly: "",
      deadOnArrival: "",
      dismissSecs: 3,
      dismissCountDown: 0,
    }
  },

  computed: {
    speciesList() {
      return this.allButterflies.filter(allButterflies => allButterflies.Species.toLowerCase().search(this.speciesName.toLowerCase()) >= 0);
    },
    supplierList() {
      return null; //Get list of suppliers
    },
    originList() {
      return null; //Get list of origins
    }
  },

  methods: {
    getAllButterflies() {
      request
        .get('/api/butterfly_species')
        .then((res) => {
          this.allButterflies = JSON.parse(res.body.allButterflies)
        })
    },

    selectSpecies(species) {
      this.speciesName = species;
      this.selected = true;
    },

    selectSupplier(supplier) {
      this.supplier = supplier;
    },

    selectOrigin(origin) {
      this.origin = origin;
    },

    async submitShipment() {
      request.post('/api/shipment/post')
        .type('json')
        .send({date: this.date,
              supplier: this.supplier,
              species: this.speciesName,
              origin: this.origin,
              quantity: this.quantity,
              emergedEarly: this.emergedEarly,
              deadOnArrival: this.deadOnArrival})
        .then((res) => {
          this.message = res.body.message
          this.dismissCountDown = this.dismissSecs
          this.date = new Date()
          this.supplier = ""
          this.origin = ""
          this.quantity = ""
          this.emergedEarly = ""
          this.deadOnArrival = ""
          this.speciesName = ""
      })
    }
  },

  watch: {
    speciesName: function() {
      this.selected = false;
    }
  },

  created() {
    this.getAllButterflies()
    this.date = new Date()
  }
}

</script>

<style scoped>
.add-shipment-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 5px 0 5px;
  width: 100%;
  margin-bottom: 40px;
}
.center-div {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  background-color: #eeeeed;
  border: 3px solid #eeeeed;
  border-radius: 10px;
  width: 80%;
  padding: 40px;
}
.heading {
  font-size: 24px;
  margin-bottom: 30px;
}
.subheading {
  padding: 15px 15px 0 0;
  width: 15%;
  text-align: right;
}
.input-group {
  margin: 10px 0 10px 0;
}
.row-div {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  flex-wrap: wrap;
  width: 100%;
}
.column-div {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  flex-wrap: wrap;
  width: 100%;
}
input, select {
  background-color: white;
  border: none;
  border-radius: 15px !important;
}
.button-div {
  margin-top: 20px;
  margin-right: 40px;
}

@media only screen and (max-width: 600px) {
  .center-div {
    padding: 15px;
  }
}
</style>
