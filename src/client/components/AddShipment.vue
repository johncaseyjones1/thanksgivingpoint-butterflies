<template>
  <div class="add-shipment-container">
    <div class="center-div">
      <div>
        Date:

      </div>
      <div class="row-div">
        Supplier:
        <select class="custom-select" v-model="supplier">
          <option>CRES</option>
          <option>LPS</option>
        </select>
      </div>
      <div class="input-group mb-3">
        Species:
        <input type="text" class="form-control" v-model="searchText"/>
        <div class="options" v-if="searchText.length > 0 && speciesList.length > 0">
          <div v-for="option in speciesList" v-bind:key="option.Species">
            <button @click="selectSpecies(option.Species)">{{ option.Species }}</button>
          </div>
        </div>
      </div>
      <div>
        Origin:
      </div>
      <div>
        Quantity:
      </div>
      <div>
        Emerged early:
      </div>
      <div>
        Dead on arrival:
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
      supplier: "",
      allButterflies: "",
      searchText: ""
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
    }
  },

  created() {
    this.getAllButterflies()
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
.row-div {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  flex-wrap: wrap;
  width: 100%;
}
</style>
