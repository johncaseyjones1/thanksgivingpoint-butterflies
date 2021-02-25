<template>
  <div class="app full-height">
    <div id="top_bar">
      <h1>{{ message }}</h1>
      <div id="router">
        <router-link class="router_item" :to="{ name: 'Dashboard' }">Dashboard</router-link>
        <router-link class="router_item" :to="{ name: 'Activities' }">Activities</router-link>
        <router-link class="router_item" :to="{ name: 'Gallery' }">Gallery</router-link>
        <router-link class="router_item" :to="{ name: 'ObservationInput' }">Observations</router-link>
      </div>
    </div>
    <router-view ></router-view>
  </div>
</template>

<script>
export default {
  data () {
    return {
      message: 'Butterflies!'
    }
  }
}
</script>

<style>
html {
  height: 100%;
}

body {
  display: flex;
  align-items: top;
  justify-content: start;
  height: 100%;
}

#top_bar {
  display: flex;
  flex-direction: row;
  align-items: center;
}

#router {
  display: flex;
  align-items: center;
  margin: 10%;
}

.router_item {
  margin: 10%;
  color:black;
  text-decoration: none;
}




</style>
