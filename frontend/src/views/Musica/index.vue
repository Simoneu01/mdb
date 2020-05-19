<template>
    <CardsCanzoni :canzoni="canzoni"/>
</template>

<script>
    import {APIService} from '../../APIService';
    import CardsCanzoni from "../../components/Cards/CardsCanzoni";
    const apiService = new APIService();

    export default {
        name: "Musica",
        components: {CardsCanzoni},
        data(){
            return {
                canzoni: []
            }
        },
        methods:{
            getCanzoni(){
                apiService.getCanzoni().then((data) => {
                    this.canzoni = data;
                });
            }
        },
        mounted() {
            this.getCanzoni()
        }
    }
</script>

<style scoped>

</style>