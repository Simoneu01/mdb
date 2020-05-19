<template>
    <!-- Two columns -->
    <div class="flex flex-col text-white">
        <div class="film flex mb-4">
            <div class="w-1/6 p-10">
                <img :src="film.src" alt="" class="flex-1 shadow mb-2">
                <h1 class="text-xl font-semibold tracking-wide">Titolo: {{film.titolo}}</h1>
            </div>
            <div class="w-5/6 p-10">
                <div class="text-5xl font-semibold tracking-wide">
                    {{film.titolo}}
                </div>
                <div>
                    CAST 1
                </div>
            </div>
        </div>
        <div class="p-10">
            <h1 class="text-4xl pl-2 font-semibold tracking-wide">CAST 2</h1>
            <Cast :casts="casts"/>
        </div>
    </div>

</template>

<script>
    import {APIService} from '../../APIService';
    import Cast from "../../components/Cast";
    const apiService = new APIService();

    export default {
        name: "film-details",
        components: {Cast},
        data(){
            return {
                film: null,
                casts: [
                    {id: 1, src: "https://pbs.twimg.com/profile_images/1055263632861343745/vIqzOHXj.jpg", nome: "Simone"},
                    {id: 2, src: "https://pbs.twimg.com/profile_images/1055263632861343745/vIqzOHXj.jpg", nome: "Simone"},
                    {id: 3, src: "https://pbs.twimg.com/profile_images/1055263632861343745/vIqzOHXj.jpg", nome: "Simone"},
                    {id: 4, src: "https://pbs.twimg.com/profile_images/1055263632861343745/vIqzOHXj.jpg", nome: "Simone"},
                    {id: 5, src: "https://pbs.twimg.com/profile_images/1055263632861343745/vIqzOHXj.jpg", nome: "Simone"}
                ]
            }
        },
        methods:{
            getFilm(){
                this.film = null
                apiService.getFilm(this.$route.params.id, (err, film) => {
                    if (err) {
                        console.log(err)
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

</style>