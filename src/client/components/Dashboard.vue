<template>
  <div class="main-container">
    <div class="column-div">
      <div class="heading">
        <p style="font-size: 26px; color: white;">Daily Stats</p>
      </div>
      <div class="daily-item item-1">
        <p><span style="color: #fe4600; font-size: 50px;">217</span></p>
        <p style="font-size: 18px;">butterflies in the Biosphere</p>
      </div>
      <div class="daily-item item-2">
        <p><span style="color: #fe4600; font-size: 50px;">89</span></p>
        <p style="font-size: 18px;">new butterflies this week</p>
      </div>
    </div>
    <div class="center-div">
      <div class="daily-notification">
        <div class="notification-text notification-item">
          <p style="font-size: 18px;">This butterfly has been spotted <span style="color: #fe4600">12</span> times this week. See if you can spot it!</p>
          <p>This species is Cethiosa-cyane.</p>
        </div>
        <div class="notification-item">
          <img class="notification-img" src="/static/photos/cethiosa-cyane.jpg" alt="">
        </div>
      </div>
      <div class="main-column">
        <div class="figure-1">

        </div>
        <div class="figure-1">

        </div>
      </div>
      <div class="main-column">
        <div class="figure-1">

        </div>
        <div class="figure-1">

        </div>
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
      observations: null,
      mostCommonSpecies: "",
      mostCommonSpeciesNum: 0,
      leastCommonSpecies: "",
      leastCommonSpeciesNum: 0,
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
          request
            .get('/api/observations/week')
            .then((res) => {
              this.observations = JSON.parse(res.body.observations)
              this.getMostCommonObservation()
              this.getLeastCommonObservation()
            })
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
    },
    getMostCommonObservation() {
        console.log("Doing most common")
        if(this.observations.length == 0)
          return "";
        var modeMap = {};
        var maxEl = this.observations[0], maxCount = 1;
        var ind;
        for (ind in this.observations) {
          var el = this.observations[ind].commonName
          console.log("el" + el)

          if (modeMap[el] == null)
            modeMap[el] = 1;
          else
            modeMap[el]++;

          if (modeMap[el] > maxCount) {
            maxEl = el
            maxCount = modeMap[el]
          }
        }
        console.log(modeMap);
        this.mostCommonSpecies = maxEl;
        this.mostCommonSpeciesNum = maxCount;
    },
    getLeastCommonObservation() {
        console.log("Doing least common")
        if(this.observations.length == 0)
          return "";
        var modeMap = {};
        var ind;
        for (ind in this.observations) {
          var el = this.observations[ind].commonName

          if (modeMap[el] == null){
            console.log('in the if');
            modeMap[el] = 1;
          }
          else
            modeMap[el]++;
        }

        console.log(modeMap);
        var [lowest] = Object.entries(modeMap).sort(([ ,v1], [ ,v2]) => v1 - v2);
        
        this.leastCommonSpecies = lowest[0];
        this.leastCommonSpeciesNum = lowest[1];
    }
  },

  created() {
    this.fetchData()
  }
}
</script>

<style scoped>
.main-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}
.column-div {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  height: 91.2vh;
  width:  25%;
  background-color: #606977;
  color: white;
}
.center-div {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-wrap: wrap;
  height: 91.2vh;
  width: 75%;
  background-image: linear-gradient(#eeeeed, #fff7ef);
}
.heading {
  padding-top: 30px;
}
.daily-item {
  padding: 20px;
  margin-bottom: 40px;
}
.item-1 {
  width: 70%;
  background-image: linear-gradient(to bottom right, #bbc0c7, #ffc5aa);
  border-radius: 20px;
}
.item-2 {
  width: 70%;
  background-image: linear-gradient(to bottom right, #ffc5aa, #b7c796);
  border-radius: 20px;
}
.main-column {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  flex-wrap: wrap;
  width: 50%;
}
.daily-notification {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  border-radius: 15px;
  background-color: white;
  margin: 20px 20px 20px 20px;
  padding: 15px;
}
.figure-1 {
  width: 90%;
  height: 200px;
  border-radius: 15px;
  margin: 10px;
  background-color: white;
}
.notification-text {
  padding: 10px;
}
.notification-img {
  width: 200px;
  border-radius: 15px;
}
.notification-item {
  padding: 0 40px 0 40px;
}
</style>
