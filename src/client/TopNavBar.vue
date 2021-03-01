<template>
    <div>
        <b-navbar 
            toggleable="lg"
            type="light"
            variant="light"
        >
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item active-class="active" class="nav-link" v-for="routes in links" 
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
                    name: 'ObservationInput',
                    path: '/observationInput',
                },
            ],
        }
    },
}

</script>