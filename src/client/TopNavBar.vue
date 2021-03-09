<template>
  <div>
    <b-navbar toggleable="lg" type="light" variant="light">
      <b-navbar-brand class="logo-text">
        <img src="/static/icons/logo.png" alt="logo" height="40px">
        Thanksgiving Point
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item exact-active-class="active" class="nav-link" v-for="routes in links" 
            :key="routes.id" :to="routes.path" >
            {{ routes.name }} 
          </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'Navbar',
  data() {
    return {
      links: [
        {
          id: 0,
          name: 'Dashboard',
          path: '/',
        },
        {
          id: 1,
          name: 'Activities',
          path: '/activities',
        },
        {
          id: 2,
          name: 'Gallery',
          path: '/gallery',
        },
        {
          id: 3,
          name: 'Observations',
          path: '/observationInput',
        },
        {
          id: 4,
          name: 'Staff',
          path: '/staff/dashboard',
        },
      ],
    }
  },
}

</script>