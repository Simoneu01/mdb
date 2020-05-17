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
                <Cards/>
                <Cards/>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Footer from "./Footer";
    import SideNav from "./SideNav";
    import Cards from "./Cards";
    import NavBar from "./NavBar";
    export default {
        name: "Container",
        components: {NavBar, Cards, SideNav, Footer}
    }
</script>

<style scoped>

</style>