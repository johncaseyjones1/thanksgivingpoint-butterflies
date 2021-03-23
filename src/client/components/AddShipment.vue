<template>
  <div class="add-shipment-container">
    <div class="center-div">
      <div class="heading">Add a new shipment</div>
      <div class="input-group mb-3">
        <div class="subheading">Date:</div>
        <v-date-picker color="orange" v-model="date" />
      </div>
      <div class="input-group mb-3">
        <div class="subheading">Supplier:</div>
        <select class="custom-select" v-model="supplier">
          <option>CRES</option>
          <option>LPS</option>
        </select>
      </div>
      <div class="column-div">
        <div class="input-group mb-3">
          <div class="subheading">Species:</div>
          <input type="text" class="form-control" v-model="searchText"/>
        </div>
        <div class="options" v-if="searchText.length > 0 && speciesList.length > 0 && !selected">
          <div v-for="option in speciesList" v-bind:key="option.Species">
            <button class="btn btn-outline-dark" @click="selectSpecies(option.Species)">{{ option.Species }}</button>
          </div>
        </div>
      </div>
      <div class="input-group mb-3">
        <div class="subheading">Origin:</div>
        <select class="custom-select" v-model="supplier">
          <option>BELIZE</option>
          <option>COLOMBIA</option>
          <option>COSTA RICA</option>
          <option>KENYA</option>
          <option>MALAYSIA</option>
          <option>PHILIPPINES</option>
          <option>THAILAND</option>
          <option>USA</option>
        </select>
      </div>
      <div class="input-group mb-3">
        <div class="subheading">Quantity:</div>
        <input type="text" class="form-control short-input" v-model="quantity"/>
      </div>
      <div class="input-group mb-3">
        <div class="subheading">Emerged early:</div>
        <input type="text" class="form-control short-input" v-model="emergedEarly"/>
      </div>
      <div class="input-group mb-3">
        <div class="subheading">Dead on arrival:</div>
        <input type="text" class="form-control short-input" v-model="deadOnArrival"/>
      </div>

      <div>
        <button class="btn" @click="submitShipment()"></button>
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
      searchText: "",
      selected: false,
      date: null,
      supplier: "",
      origin: "",
      quantity: "",
      emergedEarly: "",
      deadOnArrival: ""
    }
  },

  computed: {
    speciesList() {
      return this.allButterflies.filter(allButterflies => allButterflies.Species.toLowerCase().search(this.searchText.toLowerCase()) >= 0);
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
      this.searchText = species;
      this.selected = true;
    },

    async submitShipment() {
      request.post('/api/shipment/post')
        .type('json')
        .send({date: this.date,
              supplier: this.supplier,
              species: this.searchText,
              origin: this.origin,
              quantity: this.quantity,
              emergedEarly: this.emergedEarly,
              deadOnArrival: this.deadOnArrival})
        .then((res) => {
          this.message = res.body.message
      })
    }
  },

  watch: {
    searchText: function() {
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
.short-input {
  width: 30%;
}
input, select {
  background-color: white;
  border: none;
  border-radius: 15px !important;
}

@media only screen and (max-width: 600px) {
  .center-div {
    padding: 15px;
  }
}
</style>
