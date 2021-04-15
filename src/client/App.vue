<template>
  <div id="app">
    <Navbar />
  </div>
</template>

<script>
import Navbar from './TopNavBar';

export default {
  data () {
    return {
      message: 'Butterflies!'
    }
  },
  components: {
    Navbar,
  }
}
</script>

<style>
  /* This style code will affect EVERY page on the website. Please don't change unless you're sure you want to*/

  * {
    font-family: 'Montserrat', sans-serif;
  }
  h1 {
    font-size: 5vh;
  }
  p {
    font-size: 14px;
  }
  .navbar-light {
    background-color: white !important;
  }
  .logo-text {
    font-size: 16px;
  }
  .active-link {
    color: #fe4600 !important;
  }
  .shadow-box {
    box-shadow: 3px 3px 6px lightgray;
    border-radius: 10px;
    padding: 20px;
    background-color: white;
    margin-bottom: 30px;
  }

</style>
