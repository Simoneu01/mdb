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
                <router-view></router-view>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import NavBar from "./NavBar";
    import SideNav from "./SideNav";
    import Footer from "./Footer";

    export default {
        name: "Container",
        components: {NavBar, SideNav, Footer},
    }
</script>

<style scoped>

</style>