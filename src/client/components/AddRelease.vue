<template>
  <div class="add-release-container">
    <div class="center-div">
      <div class="heading">Add a new release</div>
      <div class="input-group mb-3">
        <div class="subheading">Date:</div>
        <v-date-picker color="orange" is-inline v-model="date" />
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
        <div class="subheading">Quantity:</div>
        <input type="text" class="form-control short-input" v-model="quantity"/>
      </div>

      <div>
        <div class="button-div"> 
          <button class="btn btn-dark" @click="submitRelease()">Submit</button>
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
  name: 'AddRelease',
  data() {
    return {
        allButterflies: "",
        searchText: "",
        selected: false,
        date: null,
        quantity: "",
        dismissSecs: 3,
        dismissCountDown: 0,
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

    async submitRelease() {
      request.post('/api/release/post')
        .type('json')
        .send({date: this.date,
              species: this.searchText,
              quantity: this.quantity})
        .then((res) => {
          this.message = res.body.message
          this.dismissCountDown = this.dismissSecs
          this.searchText = ""
          this.quantity = ""
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
.add-release-container {
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
.short-input {
  width: 30%;
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