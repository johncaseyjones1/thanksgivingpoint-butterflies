<template>
  <div>
    <div class="header-div">
      <h2>Butterfly Gallery</h2>
      <div class="search-item">
        <input type="text" class="search-bar" placeholder="Search for a butterfly" v-model="searchText"/>
        <button class="search-button">
          <i class="fa fa-search" aria-hidden="true"></i>
        </button>
      </div>
    </div>
    <v-flex d-flex>
      <v-layout wrap>
        <v-card v-for="species in butterflies" :key="species.CommonName" v-on:click="$router.push({ name: 'SpeciesPage', params: { id: species.CommonName } })"
          class="mx-auto" 
          width="300px"  
          hover="true">
          <v-img v-bind:src="species.ImagePath"
            height="200px"
            width="300px">
          </v-img>
          <v-card-title style="font-size:1em">{{species.CommonName}}</v-card-title>
        </v-card>
      </v-layout>
    </v-flex>
    
  </div>
</template>

<script>
import request from 'superagent-bluebird-promise'

export default {
  data () {
    return {
      collectingData: false,
      allButterflies: [],
      searchText: ""
    }
  },

  computed: {
    butterflies() {
      return this.allButterflies.filter(species => species.CommonName.toLowerCase().search(this.searchText.toLowerCase()) >= 0);
    }
  },

  methods: {
    popupButterfly(species) {
      this.currentSpecies = species;
    },
    getAllButterflies() {
      this.collectingData = true;
      request
        .get('/api/butterfly_species')
        .then((res) => {
          this.allButterflies = JSON.parse(res.body.allButterflies)
        })
    }
  },

  created() {
    this.getAllButterflies()
  }
}
</script>
<style scoped>
.header-div {
  background-color: #eeeeed;
  flex-direction: column;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
  margin-bottom: 40px;
}
.search-item {
  margin-top: 40px;
  background-color: white;
  width: 1000px;
  height: 44px;
  border-radius: 5px;
  display: flex;
  flex-direction: row;
  align-items: center;
}
.search-bar {
  all: unset;
  font-size: 16px;
  color: black;
  height: 100%;
  width: 100%;
  padding: 6px 10px;
}
.search-button {
  all: unset;
  cursor: pointer;
  width: 44px;
  height: 44px;
}
.v-card{
  margin-bottom: 20px;
}

@media only screen and (max-width: 600px) {
  .header-div {
    height: 200px;
  }
  .search-item {
    margin: 0;
    width: 80%;
  }
}
</style>