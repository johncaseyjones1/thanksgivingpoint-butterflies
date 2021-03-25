<template>
  <div class="main-container">
    <div class="column-div">
      <div class="heading">
        Daily Stats
      </div>
      <div>

      </div>
    </div>
    <div class="center-div">
      <div class="daily-notification">
        Can you spot this rare butterfly?
      </div>
      <div class="main-column">
        <div class="figure-1">
          place holder
        </div>
        <div class="figure-1">
          place holder
        </div>
      </div>
      <div class="main-column">
        <div class="figure-1">
          place holder
        </div>
        <div class="figure-1">
          place holder
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
  height: 91vh;
  width:  25%;
  background-color: #eeeeed;
}
.center-div {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  height: 91vh;
  width: 75%;
}
.heading {
  padding-top: 30px;
}
.main-column {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  flex-wrap: wrap;
  width: 50%;
  height: 100%;
}
.daily-notification {
  width: 100%;
  border-radius: 15px;
  background-color: #fff7ef;
  margin: 0 20px 20px 20px;
  padding: 15px;
}
.figure-1 {
  width: 80%;
  height: 200px;
  border-radius: 15px;
  margin: 10px;
  background-color: #fff7ef;
}
</style>
