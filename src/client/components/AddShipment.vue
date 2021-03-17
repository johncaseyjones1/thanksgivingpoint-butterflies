<template>
  <div class="add-shipment-container">
    <div class="center-div">
      <div>
        Date:
      </div>
      <div>
        Supplier:
      </div>
      <div>
        Species:
      </div>
      <div>
        Origin:
      </div>
      <div>
        Quantity:
      </div>
      <div>
        Emerged early:
      </div>
      <div>
        Dead on arrival:
      </div>
    </div>
  </div>  
</template>

<script>

export default {
  name: 'AddShipment',
  data() {
    return {

    }
  },

  methods: {

  }
}

</script>

<style scoped>
.add-shipment-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 5px 0 5px;
  width: 100%;
}
.center-div {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  background-color: #eeeeed;
  border: 3px solid #eeeeed;
  border-radius: 10px;
  width: 80%;
}
</style>
