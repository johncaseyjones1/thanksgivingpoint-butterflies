<template>
  <div class="main-container">
    <div class="column-div">
      <div class="heading">
        <p style="font-size: 26px; color: white;">Daily Stats</p>
      </div>
      <div class="daily-item item-1">
        <p><span style="color: #fe4600; font-size: 50px;">{{totalReleasedThisWeek}}</span></p>
        <p style="font-size: 18px;">new butterflies this week</p>
      </div>
      <div class="daily-item item-2">
        <p><span style="color: #fe4600; font-size: 50px;">{{totalButterfliesFlying}}</span></p>
        <p style="font-size: 18px;">butterflies in the Biosphere</p>
      </div>
      <div class="daily-item item-3">
        <p><span style="color: #fe4600; font-size: 50px;">{{totalSpeciesFlying}}</span></p>
        <p style="font-size: 18px;">different species in the Biosphere</p>
      </div>
    </div>
    <div class="center-div">
      <div class="daily-notification">
        <div class="notification-text notification-item">
          <p style="font-size: 18px;">The {{mostCommonSpecies.CommonName}} butterfly has been spotted <span style="color: #fe4600">{{mostCommonSpeciesNum}}</span> times this week. See if you can spot it!</p>
        </div>
        <div class="notification-item">
          <img class="notification-img" v-bind:src="mostCommonSpecies.ImagePath" alt="">
        </div>
      </div>
      <div class="main-column">
        <div class="figure-1">
          <img class="notification-img" src="/static/graphs/worldMap.svg" alt="">
        </div>
        <div class="figure-1">
          <h5>{{numFromSouthAmerica}} of the butterfliy species in the Biosphere come from South America!
             {{numFromAsia}} come from Asia, {{numFromAfrica}} come from Africa,
              {{numFromNorthAmerica}} come from North America. Right now, {{numFromAustralia}}
               species come from Australia and {{numFromEurope}} come from Europe.</h5>
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
      releasesInWeek: null,
      numFromAsia: 0,
      numFromAfrica: 0,
      numFromNorthAmerica: 0,
      numFromSouthAmerica: 0,
      numFromEurope: 0,
      numFromAustralia: 0,
      pathToMap: "",
      stillFlying: null,
      totalButterfliesFlying: 0,
      totalSpeciesFlying: 0,
      totalReleasedThisWeek: 0,
    }
  },

  methods: {
    async fetchData() {
      request
        .get('/api/butterfly_species')
        .then((res) => {
          this.allButterflies = JSON.parse(res.body.allButterflies)
          this.calculateButterfliesFromAsia()
          this.calculateButterfliesFromAustralia()
          this.calculateButterfliesFromAfrica()
          this.calculateButterfliesFromNorthAmerica()
          this.calculateButterfliesFromSouthAmerica()
          this.calculateButterfliesFromEurope()
          request
            .get('/api/observations/week')
            .then((res) => {
              this.observations = JSON.parse(res.body.observations)
              this.getMostCommonObservation()
              this.getLeastCommonObservation()
              request
              .get('/api/location')
              .then((res) => {
                this.pathToMap = res.body.pathToMap
                request
                .get('/api/longevity/stillflying')
                .then((res) => {
                  this.stillFlying = JSON.parse(res.body.stillFlying)
                  this.getButterfliesStillFlying()
                  this.getNumberOfSpecies()
                  request
                  .post('/api/release/inrange')
                  .type('json')
                  .send({'numDays': 7})
                  .then((res) => {
                    this.releasesInWeek = JSON.parse(res.body.releasesInRange)
                    this.getButterfliesAddedThisWeek()
                  })
                })
              })
            })
        })
    },
    calculateButterfliesFromAsia() {
      var ind;
      for (ind in this.allButterflies) {
        if (this.allButterflies[ind].Location === "Asia") {
          this.numFromAsia += 1;
        }
      }
    },
    calculateButterfliesFromAustralia() {
      var ind;
      for (ind in this.allButterflies) {
        if (this.allButterflies[ind].Location === "Australia") {
          this.numFromAustralia += 1;
        }
      }
    },
    calculateButterfliesFromAfrica() {
      var ind;
      for (ind in this.allButterflies) {
        if (this.allButterflies[ind].Location === "Africa") {
          this.numFromAfrica += 1;
        }
      }
    },
    calculateButterfliesFromNorthAmerica() {
      var ind;
      for (ind in this.allButterflies) {
        if (this.allButterflies[ind].Location === "North America") {
          this.numFromNorthAmerica += 1;
        }
      }
    },
    calculateButterfliesFromSouthAmerica() {
      var ind;
      for (ind in this.allButterflies) {
        if (this.allButterflies[ind].Location === "South America") {
          this.numFromSouthAmerica += 1;
        }
      }
    },
    calculateButterfliesFromEurope() {
      var ind;
      for (ind in this.allButterflies) {
        if (this.allButterflies[ind].Location === "Europe") {
          this.numFromEurope += 1;
        }
      }
    },
    getButterfliesStillFlying() {
      var index = 0
      for (index in this.stillFlying) {
        this.totalButterfliesFlying += Number(this.stillFlying[index].Quantity)
      }
    },
    getButterfliesAddedThisWeek() {
      var index = 0
      for (index in this.releasesInWeek) {
        this.totalReleasedThisWeek += Number(this.releasesInWeek[index].Quantity)
      }
    },
    getNumberOfSpecies() {
      var modeMap = {};
      var maxEl = this.stillFlying[0].Species, maxCount = 1;
      var ind;
      for (ind in this.stillFlying) {
        var el = this.stillFlying[ind].Species
        console.log("el " + el)

        if (modeMap[el] == null)
          modeMap[el] = 1;
        else
          modeMap[el]++;

        if (modeMap[el] > maxCount) {
          maxEl = el
          maxCount = modeMap[el]
        }
      }
      console.log("length of map: " + Object.keys(modeMap).length)
      this.totalSpeciesFlying = Object.keys(modeMap).length
      maxEl
    },
    getMostCommonObservation() {
        if(this.observations.length == 0)
          return "";
        var modeMap = {};
        var maxEl = this.observations[0].commonName, maxCount = 1;
        var ind;
        for (ind in this.observations) {
          var el = this.observations[ind].commonName
          console.log("el " + el)

          if (modeMap[el] == null)
            modeMap[el] = 1;
          else
            modeMap[el]++;

          if (modeMap[el] > maxCount) {
            maxEl = el
            maxCount = modeMap[el]
          }
        }
        this.mostCommonSpecies = this.allButterflies.find(t=>t.CommonName === maxEl);
        this.mostCommonSpeciesNum = maxCount;
    },
    getLeastCommonObservation() {
        if(this.observations.length == 0)
          return "";
        var modeMap = {};
        var ind;
        for (ind in this.observations) {
          var el = this.observations[ind].commonName

          if (modeMap[el] == null){
            modeMap[el] = 1;
          }
          else
            modeMap[el]++;
        }

        console.log(modeMap);
        var [lowest] = Object.entries(modeMap).sort(([ ,v1], [ ,v2]) => v1 - v2);
        
        this.leastCommonSpecies = lowest[0];
        
        this.leastCommonSpecies = this.allButterflies.find(t=>t.CommonName === lowest[0]);
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
  margin-bottom: 20px;
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
.item-3 {
  width: 70%;
  background-image: linear-gradient(to bottom right, #b7c796, #bbc0c7);
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

@media only screen and (max-width: 600px) {
  .main-container {
    flex-direction: column;
  }
  .column-div {
    width: 100%;
    height: 740px;
  }
  .center-div {
    width: 100%;
    height: auto;
    flex-direction: column;
    justify-content: flex-start;
  }
  .daily-notification {
    flex-direction: column;
    margin: 0;
    margin-bottom: 30px;
    border-radius: 0;
    padding: 30px 0 30px 0;
  }
  .notification-img {
    width: 300px;
  }
  .main-column {
    width: 100%;
  }
}
</style>
