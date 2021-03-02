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

  h1 {
    font-size: 5vh;
  }

  body {
    font-size: 2vh;
  }




</style>
