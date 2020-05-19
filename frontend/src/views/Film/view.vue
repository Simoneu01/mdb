<template>
    <div class="film text-white">
        <div class="loading" v-if="loading">Loading...</div>
        <div v-if="error" class="error">
            {{ error }}
        </div>
        <transition name="slide">
            <!--
              giving the post container a unique key triggers transitions
              when the post id changes.
            -->
            <div v-if="film" class="content" :key="film.id">
                <h2>{{ film.titolo }}</h2>
                <p>{{ film.pubblicazione }}</p>
            </div>
        </transition>
    </div>
</template>

<script>
    import {APIService} from '../../APIService';
    const apiService = new APIService();

    export default {
        name: "film-details",
        data(){
            return {
                loading: false,
                film: null,
                error: null
            }
        },
        methods:{
            getFilm(){
                this.error = this.film = null
                this.loading = true
                apiService.getFilm(this.$route.params.id, (err, film) => {
                    if (err) {
                        this.error = err.toString()
                    } else {
                        this.film = film
                    }
                })
            }
        },
        watch: {
            '$route': 'getFilm'
        },
        mounted() {
            this.getFilm()
        },
        beforeRouteEnter : (to, from, next) => {

            function isValid (id) {
                return apiService.getFilm(id, (err) => {
                    if (err) {
                        next('/404');
                    } else {
                        next();
                    }
                })
            }

            isValid(to.params.id);
        },
        beforeRouteUpdate : (to, from, next) => {

            function isValid (id) {
                return apiService.getFilm(id, (err) => {
                    if (err) {
                        next('/404');
                    } else {
                        next();
                    }
                })
            }

            isValid(to.params.id);
        }
    }
</script>

<style scoped>
    .loading {
        position: absolute;
        top: 10px;
        right: 10px;
    }
    .error {
        color: red;
    }
    .content {
        transition: all .35s ease;
        position: absolute;
    }
    .slide-enter {
        opacity: 0;
        transform: translate(30px, 0);
    }
    .slide-leave-active {
        opacity: 0;
        transform: translate(-30px, 0);
    }
</style>