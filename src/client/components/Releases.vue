<template>
  <div class="releases-container">
    <div class="center-div">
      <div class="buttons" v-show="showTable">
        <button class="btn btn-outline-success option-btn" @click="showAddRelease()">Add new release</button>
        <button class="btn btn-outline-success option-btn" @click="download()">Download release data</button>
      </div>
      <button class="btn btn-dark add-release-btn" v-show="addRelease" @click="hideAddRelease()">Cancel</button>
      <v-client-table v-show="showTable" v-model="releases" :columns="columns" :options="options">
        <div slot="Delete" slot-scope="{row}">
          <span>
            <button type="button" class="btn btn-outline-dark btn-sm" @click="deleteRelease(row)">Delete</button>
          </span>  
        </div> 
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
      editMessage: "",
      releases: [],
      columns: ["formattedDate","Species","Quantity","Delete"],
      options: {
        headings: {
          formattedDate: 'Date',
          species: 'Species',
          Quantity: 'Qty'
        },
        customSorting: {
          formattedDate: function (ascending) {
            return function (a, b) {
              var dateA = a.Date.$date;
              var dateB = b.Date.$date;

              if (ascending)
                return dateA >= dateB ? 1 : -1;

              return dateA <= dateB ? 1 : -1;
            }
          }
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
            this.releases[ind].id = this.releases[ind]._id.$oid
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
    },
    deleteRelease(row) {
      console.log("delete " + row)
      console.log(row._id)
      request.post('/api/release/delete')
        .type('json')
        .send({
              _id: row._id.$oid,
              })
        .then((res) => {
          this.editMessage = res.body.message
          console.log(this.editMessage)
          const index = this.releases.findIndex(item => item.id === row.id);

          if (index !== undefined) this.releases.splice(index, 1);

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
.buttons {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 30px;
  margin-right: 20px;
}
.option-btn {
  margin-right: 20px;
}
.add-release-btn {
  margin-bottom: 30px;
}
</style>