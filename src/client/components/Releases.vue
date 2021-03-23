<template>
  <div class="releases-container">
    <div class="center-div">
      <table class="table">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Date</th>
            <th scope="col">Species</th>
            <th scope="col">Qty</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="release in releases" :key="release.releaseID">
            <td>{{ release.Date.$date }}</td>
            <td>{{ release.species }}</td>
            <td>{{ release.Sum }}</td>
          </tr>
        </tbody>
      </table>
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
    }
  },

  methods: {
    getAllReleases() {
      this.collectingData = true;
      request.get('/api/release')
        .then((res) => {
          this.releases = JSON.parse(res.body.allReleases)
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