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
            }
        },
        mounted() {
            this.getFilms()
        }
    }
</script>

<style scoped>

</style>