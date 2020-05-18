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
                <CardsLibri :libri="libri"/>
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
    import CardsLibri from "../components/Cards/CardsLibri";
    const apiService = new APIService();

    export default {
        name: "Libri",
        components: {CardsLibri, NavBar, SideNav, Footer},
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
            }
        },
        mounted() {
            this.getLibri()
        }
    }
</script>

<style scoped>

</style>