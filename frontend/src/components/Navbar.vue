<template>
    <b-navbar>
        <template slot="brand">
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                <img
                        src="https://arizonachristian.edu/wp-content/uploads/2017/06/logo-placeholder.png"
                        alt="Lightweight UI components for Vue.js based on Bulma"
                >
            </b-navbar-item>
        </template>
        <template slot="start">
            <b-navbar-item href="#">
                Home
            </b-navbar-item>
            <b-navbar-dropdown label="Contenuti">
                <b-navbar-item href="#">
                    Film
                </b-navbar-item>
                <b-navbar-item href="#">
                    Musica
                </b-navbar-item>
                <b-navbar-item href="#">
                    Libri
                </b-navbar-item>
            </b-navbar-dropdown>
        </template>
        <template slot="end">
                <figure class="image is-32x32">
                    <img class="is-rounded" src="https://bulma.io/images/placeholders/32x32.png">
                </figure>
        </template>
    </b-navbar>
</template>

<script>
    export default {
        name: "Navbar"
    }
</script>

<style scoped>

</style>