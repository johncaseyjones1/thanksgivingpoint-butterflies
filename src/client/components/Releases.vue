<template>
  <div class="releases-container">
    <div class="center-div">
      <v-client-table v-model="releases" :columns="columns" :options="options">
      </v-client-table>
    </div>
  </div>   
</template>

<script>
import request from 'superagent-bluebird-promise'

export default {
  name: 'Releases',
  data() {
    return {
      collectingData: false,
      releases: [],
      columns: ["formattedDate","Species","Quantity"],
      options: {
        headings: {
          formattedDate: 'Date',
          species: 'Species',
          Sum: 'Qty'
        },
      }
    }
  },

  methods: {
    getAllReleases() {
      this.collectingData = true;
      request.get('/api/release')
        .then((res) => {
          this.releases = JSON.parse(res.body.allReleases)
          var ind
          for (ind in this.releases) {
            this.releases[ind].formattedDate = new Date(this.releases[ind].Date.$date).toDateString()
          }
        })
    }
  },

  created() {
    this.getAllReleases()
  }
}

</script>

<style scoped>
.releases-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 5px 0 5px;
}
.center-div {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}
</style>