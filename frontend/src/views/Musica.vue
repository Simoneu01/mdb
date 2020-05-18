<template>
    <div class="bg-dark h-screen">
        <div class="flex" style="height: 88vh">
            <!--  side nav -->
            <SideNav/>
            <!-- main content -->
            <div class="w-full h-full relative overflow-y-scroll">
                <!-- navbar -->
                <NavBar/>
                <!-- cards -->
                <CardsCanzoni :canzoni="canzoni"/>
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
    import CardsCanzoni from "../components/Cards/CardsCanzoni";
    const apiService = new APIService();

    export default {
        name: "Musica",
        components: {CardsCanzoni, NavBar, SideNav, Footer},
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