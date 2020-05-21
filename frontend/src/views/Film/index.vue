<template>
    <CardsFilms :films="films"/>
</template>

<script>
    import {APIService} from '../../APIService';
    import CardsFilms from "../../components/Cards/CardsFilms";
    const apiService = new APIService();

    export default {
        name: "Film",
        components: {CardsFilms},
        data(){
            return {
                films: []
            }
        },
        methods:{
            getFilms(){
                apiService.getFilms().then((data) => {
                    this.films = data;
                });
            },
            watchFilms(){
                setTimeout(this.getFilms, 1000)
            }
        },
        watch: {
            '$route': 'getFilms',
            films: {
                handler: 'watchFilms'
            },
        },
        mounted() {
            this.getFilms()
        }
    }
</script>

<style scoped>

</style>