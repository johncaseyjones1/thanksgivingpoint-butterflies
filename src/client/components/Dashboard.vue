<template>
  <div id="screen">
    <div id="location_box">
      <div id="location_image"></div>
      <div id="location_text">
        <p>There are {{numFromAsia}} buterfly species from Asia!</p>
      </div>
    </div>
  </div>
</template>

<script>
import request from 'superagent-bluebird-promise'

export default {
  data () {
    return {
      allButterflies: null,
      numFromAsia: 0
    }
  },

  methods: {
    async fetchData() {
      request
        .get('/api/butterfly_species')
        .then((res) => {
          this.allButterflies = JSON.parse(res.body.allButterflies)
          this.calculateButterfliesFromAsia()
        })
    },
    calculateButterfliesFromAsia() {
      console.log("Doing Asia")
      var ind;
      for (ind in this.allButterflies) {
        if (this.allButterflies[ind].Location === "Asia") {
          this.numFromAsia += 1;
        }
      }
    }
  },

  created() {
    this.fetchData()
  }
}
</script>
