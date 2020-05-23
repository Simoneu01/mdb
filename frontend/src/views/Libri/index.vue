<template>
    <CardsLibri :libri="libri"/>
</template>

<script>
    import {APIService} from '../../APIService';
    import CardsLibri from "../../components/Cards/CardsLibri";
    const apiService = new APIService();

    export default {
        name: "Libri",
        components: {
            CardsLibri
        },
        data(){
            return {
                libri: []
            }
        },
        methods:{
            getLibri(){
                apiService.getLibri().then((data) => {
                    this.libri = data;
                });
            },
            watchLibri(){
                setTimeout(this.getLibri, 1000)
            }
        },
        watch: {
            '$route': 'getLibri',
            libri: {
                handler: 'watchLibri'
            },
        },
        mounted() {
            this.getLibri()
        }
    }
</script>

<style scoped>

</style>