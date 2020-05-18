<template>
    <div class="bg-dark h-screen">
        <div class="flex" style="height: 98vh">
            <!--  side nav -->
            <SideNav/>
            <!-- main content -->
            <div class="w-full h-full relative overflow-y-scroll">
                <!-- navbar -->
                <NavBar/>
                <!-- cards -->
                <CardsFilms :films="films"/>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import {APIService} from '../APIService';
    import Footer from "../components/Footer";
    import SideNav from "../components/SideNav";
    import NavBar from "../components/NavBar";
    import CardsFilms from "../components/Cards/CardsFilms";
    const apiService = new APIService();

    export default {
        name: "Film",
        components: {CardsFilms, NavBar, SideNav, Footer},
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