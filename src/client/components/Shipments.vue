<template>
  <div class="shipment-container">
    <div class="center-div">
      <v-client-table v-model="shipments" :columns="columns" :options="options">
        <input type="number" slot="FTE" slot-scope="{row, update}" v-model="row.FTE" @input="update">
      </v-client-table>
    </div>
  </div>
</template>

<script>
import request from 'superagent-bluebird-promise'

export default {
  name: 'Shipments',
  data() {
    return {
      collectingData: false,
      shipments: [],
      columns: ["id","formattedDate","Supplier","Species","Origin","Quantity","EmergedEarly","DOA","FTE","W","Parasite"],
      options: {
        headings: {
          id: 'ID',
          formattedDate: 'Date',
          Supplier: 'Supplier',
          Species: 'Species',
          Origin: 'Origin',
          Quantity: 'Qty',
          EmergedEarly: 'Emerged early',
          DOA: 'DOA',
          FTE: 'FTE',
          W: 'Wings',
          Parasite: 'Parasite'
        },
        editableColumns:['FTE','Parasite']
      }
    }
  },

  methods: {
    getAllShipments() {
      this.collectingData = true;
      request
        .get('/api/shipment')
        .then((res) => {
          this.shipments = JSON.parse(res.body.allShipments)
          var ind
          for (ind in this.shipments) {
            this.shipments[ind].formattedDate = new Date(this.shipments[ind].Date.$date).toISOString()
            this.shipments[ind].id = this.shipments[ind]._id.$oid
          }
        })
    }
  },

  created() {
    this.getAllShipments()
  }
}

</script>

<style scoped>
.shipment-container {
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
