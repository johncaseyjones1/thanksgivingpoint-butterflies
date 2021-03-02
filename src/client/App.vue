<template>
  <!-- <div class="app full-height">
    <div id="top_bar">
      <h1>{{ message }}</h1>
      <div id="router">
        <router-link class="router_item" :to="{ name: 'Dashboard' }">Dashboard</router-link>
        <router-link class="router_item" :to="{ name: 'Activities' }">Activities</router-link>
        <router-link class="router_item" :to="{ name: 'Gallery' }">Gallery</router-link>
        <router-link class="router_item" :to="{ name: 'ObservationInput' }">Observations</router-link>
      </div>
    </div> 

    <router-view />
  </div> -->

  <div id="app">
    <Navbar />
  </div>
</template>

<script>
import Navbar from './TopNavBar';

export default {
  data () {
    return {
      message: 'Butterflies!'
    }
  },
  components: {
    Navbar,
  }
}
</script>

<style>
  /* This style code will affect EVERY page on the website. Please don't change unless you're sure you want to*/

  * {
    font-family: 'Montserrat', sans-serif;
  }

  h1 {
    font-size: 5vh;
  }

  p {
    font-size: 14px;
  }

  .navbar-light {
    background-color: white !important;
  }

  .active {
    color: #fe4600 !important;
  }

  .shadow-box {
    box-shadow: 3px 3px 6px lightgray;
    border-radius: 10px;
    padding: 20px;
    background-color: white;
    margin-bottom: 30px;
  }



</style>
