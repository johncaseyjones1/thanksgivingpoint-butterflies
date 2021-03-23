<template>
  <div id="screen">
    <div id="location_box">
      <div id="location_image"></div>
      <div id="location_text">
        <p>There are {{numFromAsia}} buterfly species from Asia!</p>
      </div>
    </div>

    <div id="observation_box">
      <div id="observation_box_text">
        <p>The {{mostCommonSpecies}} buterfly has been seen {{mostCommonSpeciesNum}} times by guests this week!</p>
        <p>The {{leastCommonSpecies}} buterfly has only been seen {{leastCommonSpeciesNum}} times! See if you can spot it!</p>
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
