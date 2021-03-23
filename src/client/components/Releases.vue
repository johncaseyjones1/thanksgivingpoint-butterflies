<template>
  <div class="releases-container">
    <div class="center-div">
      <button class="btn btn-dark add-release-btn" v-show="showTable" @click="showAddRelease()">Add new release</button>
      <button class="btn btn-dark add-release-btn" v-show="addRelease" @click="hideAddRelease()">Cancel</button>
      <v-client-table v-show="showTable" v-model="releases" :columns="columns" :options="options">
      </v-client-table>
    </div>
    <AddRelease v-show="addRelease"/>
  </div>   
</template>

<script>
import request from 'superagent-bluebird-promise'
import AddRelease from './AddRelease'

export default {
  name: 'Releases',
  data() {
    return {
      addRelease: false,
      showTable: true,
      collectingData: false,
      releases: [],
      columns: ["formattedDate","species","Sum"],
      options: {
        headings: {
          formattedDate: 'Date',
          species: 'Species',
          Sum: 'Qty'
        },
        orderBy: {column: "formattedDate", ascending: false}
      }
    }
  },

  components: {
    AddRelease
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
    },
    showAddRelease() {
      this.addRelease = true;
      this.showTable = false;
    },
    hideAddRelease() {
      this.addRelease = false;
      this.showTable = true;
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
  flex-direction: column;
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
.add-release-btn {
  margin-bottom: 30px;
}
</style>