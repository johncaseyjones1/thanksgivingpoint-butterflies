<template>
  <div id="main">
    <div class="header-div">
      <div class="header-text">Welcome Staff Member</div>
      <div>This is where the magic happens</div>
    </div>
    <div v-if="passwordCorrect">
      <div class="page-buttons">
        <button v-on:click="setPage('releases')" id="release-button" class="btn btn-outline-dark" @click="showReleases()">Releases</button>
        <button v-on:click="setPage('shipments')" id="shipment-button" class="btn btn-outline-dark" @click="showShipments()">Shipments</button>
        <button v-on:click="setPage('species')" id="species-data-button" class="btn btn-outline-dark" @click="showSpeciesData()">Species data</button>   
      </div>
      <Shipments v-show="shipments"/>
      <Releases v-show="releases"/>
      <SpeciesData v-show="species"/>
    </div>
    <div v-else>
      <div class="password-div">
        <h4>Password:</h4>
        <input class="form-control input-p" v-model="password" type="password">
        <button class="btn btn-dark" @click="checkPassword()">Submit</button>
      </div>
    </div>
  </div>
</template>



<script>
import Shipments from "./Shipments"
import Releases from "./Releases"
import SpeciesData from "./SpeciesData"
//import request from 'superagent-bluebird-promise'
//import axios from 'axios'

export default {
  data () {
    return {
      shipments: false,
      releases: false,
      species: false,
      passwordCorrect: false,
      password: ""
    }
  },

  components: {
    Shipments,
    Releases,
    SpeciesData
  },

  methods: {
    showShipments() {
      this.shipments = true;
      this.releases = false;
      this.species = false;
    },
    showReleases() {
      this.shipments = false;
      this.releases = true;
      this.species = false;
    },
    showSpeciesData() {
      this.shipments = false;
      this.releases = false;
      this.species = true;
    },
    setPage(page) {
      if (page == "releases") {
        document.getElementById("release-button").classList.add("active");
        document.getElementById("shipment-button").classList.remove("active");
        document.getElementById("species-data-button").classList.remove("active");
      }
      else if (page == "shipments") {
        document.getElementById("release-button").classList.remove("active");
        document.getElementById("shipment-button").classList.add("active");
        document.getElementById("species-data-button").classList.remove("active");
      }
      else {
        document.getElementById("release-button").classList.remove("active");
        document.getElementById("shipment-button").classList.remove("active");
        document.getElementById("species-data-button").classList.add("active");
      }
    },
    checkPassword() {
      if (this.password === "password") {
        this.passwordCorrect = true
      }
    }   
  },
  
  
}

</script>

<style scoped>
  .header-div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    height: 300px;
    background-color: #eeeeed;
    border-bottom: 30px solid #598400;
  }
  .header-text {
    font-size: 40px;
  }
  .page-buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    margin-top: 40px;
    margin-bottom: 40px;
  }
  .btn {
    margin-left: 20px;
    margin-right: 20px;
    width: 150px;
  }
  .password-div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 100px;
  }
  .input-p {
    background-color: white;
    border: 3px solid #598400;
    border-radius: 15px !important;
    width: 30%;
    margin-bottom: 20px;
  }

  @media only screen and (max-width: 600px) {
    .header-div {
      height: 200px;
    }
    .header-text {
      font-size: 22px;
      font-weight: bold;
    }
    .page-buttons {
      flex-direction: column;
    }
    .btn {
      margin-bottom: 20px;
    }
  }
</style>