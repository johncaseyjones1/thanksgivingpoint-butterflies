<template>
  <div>
    <ul>
        <li  v-for="species in allButterflies" :key="species.CommonName">
          <div @click="setSpeciesPrediction(species)">
            {{species.CommonName}}
          </div>
        </li>
      </ul>
  </div>
</template>

<script>
import request from 'superagent-bluebird-promise'

export default {
  data () {
    return {
      collectingData: false,
      allButterflies: null
    }
  },

  methods: {
    getAllButterflies() {
      this.collectingData = true;
      request
        .get('/api/butterfly_species')
        .then((res) => {
          this.allButterflies = JSON.parse(res.body.allButterflies)
        })
    }
  },

  created() {
    this.getAllButterflies()
  }
}
</script>
