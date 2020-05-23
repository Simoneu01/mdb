<template>
    <!-- Two columns -->
    <div class="flex flex-col text-white">
        <div v-if="film" class="film flex mb-4">
            <div class="w-1/6 p-10">
                <img :src="`${film.e_src ? film.e_src : film.src}`" alt="" class="flex-1 shadow mb-2">
                <h1 class="text-xl font-semibold tracking-wide">Uscita: {{film.pubblicazione}}</h1>
            </div>
            <div class="w-5/6 p-10">
                <div class="text-5xl font-semibold tracking-wide">
                    {{film.titolo}}
                </div>
                <div>
                    {{film.plot}}
                </div>
            </div>
            <div class="w-6/6 p-10">
                <div class="inline-flex">
                    <router-link :to="`${film.id}/edit`">
                        <button class="bg-green hover:bg-greenest text-white font-bold py-2 px-5 rounded mr-2">Edit</button>
                    </router-link>
                    <button v-on:click.prevent="deleteFilm" class="bg-red-600 hover:bg-red-800 text-white font-bold py-2 px-5 rounded mr-2">Delete</button>
                </div>
            </div>
        </div>
        <div v-if="casts" class="p-10">
            <h1 class="text-4xl pl-2 font-semibold tracking-wide">CAST</h1>
            <Cast :casts="casts"/>
        </div>
    </div>

</template>

<script>
    import {APIService} from '../../APIService';
    import Cast from "../../components/Cast";
    import swal from 'sweetalert';
    import {tmdbAPIService} from "../../tmdbAPIService,js";
    const tmdbService = new tmdbAPIService();
    const apiService = new APIService();

    export default {
        name: "film-details",
        components: {Cast},
        data(){
            return {
                film: {},
                casts: null
            }
        },
        methods:{
            async getFilm(){
                this.film = null
                await apiService.getFilm(this.$route.params.id, (err, film) => {
                    if (err) {
                        console.log(err)
                    } else {
                        this.film = film
                        console.log(this.film.e_src)
                        if(this.film.e_src !== null){
                            this.getCastFilm()
                        }
                    }
                })
            },
            getCastFilm(){
                this.casts = []
                tmdbService.getCastFilm(this.film.tmdb_id)
                    .then(data => {
                        for (let i = 0; i < 8; i++) {
                            this.casts.push(data.cast[i])
                        }
                })
            },
            deleteFilm(){
                swal({
                    title: "Sei sicuro?",
                    text: "Una volta eliminato, non sarai in grado di ripristinare il film ma dovrai riaggiungerlo!!",
                    icon: "warning",
                    buttons: true,
                    dangerMode: true,
                })
                    .then((willDelete) => {
                        if (willDelete) {
                            swal("Poof! Il Film è stato eliminato!!", {
                                icon: "success",
                            });
                            apiService.deleteFilm(this.$route.params.id)
                            this.$router.push('/film')
                        } else {
                            swal("Il tuo film è salvo!!");
                        }
                    });

            },
        },
        watch: {
            '$route': 'getFilm'
        },
        async mounted() {
            await this.getFilm()
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

</style>