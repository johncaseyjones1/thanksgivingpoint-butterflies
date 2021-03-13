<template>
  <div class="shipment-container">
    <div class="center-div">
      <table class="table">
        <thead class="thead-dark">
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Date</th>
            <th scope="col">Supplier</th>
            <th scope="col">Species</th>
            <th scope="col">Origin</th>
            <th scope="col">Qty</th>
            <th scope="col">Emerged early</th>
            <th scope="col">DOA</th>
            <th scope="col">Failed to emerge</th>
            <th scope="col">Parasitized</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="shipment in shipments" :key="shipment._id.$oid">
            <td>{{ shipment._id.$oid }}</td>
            <td>{{ shipment.formattedDate }}</td>
            <td>{{ shipment.Supplier }}</td>
            <td>{{ shipment.Species }}</td>
            <td>{{ shipment.Origin }}</td>
            <td>{{ shipment.Quantity }}</td>
            <td>{{ shipment.EmergedEarly }}</td>
            <td>{{ shipment.DOA }}</td>
            <td>{{ shipment.FTE }}</td>
            <td>{{ shipment.Parasite }}</td>
          </tr>
        </tbody>
      </table>
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
