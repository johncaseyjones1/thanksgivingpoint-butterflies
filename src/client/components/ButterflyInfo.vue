<template>
  <div class="butterfly-container">
    <div class="heading">
      <h2 class="heading-text">I'm {{this.article}} {{this.butterfly.commonName}} butterfly!</h2>
    </div>
    <div class="photo-column">
      <img :src="this.butterfly.imagePath" alt="Butterfly Image" class="image"/>
      <div class="name-container">
        <h6>Scientific name: <em>{{this.butterfly.scientificName}}</em></h6>
        <h6>Common name: <em>{{this.butterfly.commonName}}</em></h6>
      </div>
    </div>
    <div class="details-column">
      <div class="details-container">
        <h6>Location: <em>{{this.butterfly.location}}</em></h6>
        <h6>Primary color: <em>{{this.butterfly.primaryColor}}</em></h6>
        <h6>Secondary color: <em>{{this.butterfly.secondaryColor}}</em></h6>
        <h6>Pattern: <em>{{this.butterfly.pattern}}</em></h6>
        <h6>Size: <em>{{this.butterfly.size}}</em></h6>
        <h6>Wing shape: <em>{{this.butterfly.wingShape}}</em></h6>
        <h6>Eyespot: <em>{{this.eyespot}}</em></h6>
        <h6>Caterpillar host plants: <em>{{this.butterfly.caterpillarHostPlants}}</em></h6>
        <h6>Sexually dimorphic: <em>{{this.butterfly.sexuallyDimorphic}}</em></h6>
        <h6>Quick fact: <em>{{this.butterfly.quickFact}}</em></h6>
      </div>
    </div>
  </div>
</template>

<script>
//import request from 'superagent-bluebird-promise'

export default {
  data() {
    return {
      collectingData: false,
      butterfly: null
    }
  },
  computed: {
    article() {
      var vowelRegex = '^[aieouAIEOU].*';
      var matched = this.butterfly.commonName.match(vowelRegex);
      if (matched) {
        return "an";
      }
      return "a";
    },
    eyespot() {
      if (this.butterfly.eyespot == "N") {
        return "No";
      }
      return "Yes";
    }
  },
  methods: {

  },
  created() {
    this.butterfly = this.$route.params
  }
}
</script>

<style scoped>
.butterfly-container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-wrap: wrap;
  background-color: #eeeeed;
  height: 100%;
  min-height: 91.2vh;
  width: 100%;
  padding: 40px;
}
.heading {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100px;
  background-color: #eeeeed;
}
.heading-text {
  padding-bottom: 10px;
  border-bottom: 5px solid #fe4600;
}
.photo-column {
  width: 50%;
  height: 100%;
}
.details-column {
  width: 50%;
  height: 100%;
}
.image {
  width: 100%;
  border-radius: 5px;
}
.name-container {
  border-radius: 5px;
  background-color: white;
  padding: 20px;
  margin-top: 20px;
}
.details-container {
  border-radius: 5px;
  background-color: white;
  padding: 20px;
  margin: 0 20px 0 20px;
}
</style>
