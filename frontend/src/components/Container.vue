<template>
    <div class="container">
        <Body/>
        <Footer/>
    </div>
</template>

<script>
    import Body from "./Body"
    import Footer from "./Footer"

    export default {
        name: "Container",
        components: {
            Footer,
            Body
        }
    }
</script>

<style scoped>

</style>