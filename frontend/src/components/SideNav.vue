<template>
    <div class="w-56 bg-black h-full flex-none">
        <div class="p-6">
            <router-link to="/">
                <img src="https://www.arizonachristian.edu/wp-content/uploads/2017/06/logo-placeholder.png" class="h-13">
            </router-link>
        </div>
        <div class="mx-2">
            <router-link v-for="page in pages" v-bind:key="page.id" :to="`/${page.id}`">
                <button @click="setID = page.id" :class="`opacity-75 hover:opacity-100 w-full font-semibold rounded px-3 py-2 flex items-center justify-started  ${setID === page.id ? 'bg-light text-white' : 'text-lightest'}`">
                    <font-awesome-icon class="mr-3" :icon="page.icon"/>
                    {{ page.name }}
                </button>
            </router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: "SideNav",
        data: function () {
            return {
                pages: [
                    {id: 'home', name: 'Home', icon: 'home'},
                    {id: 'film', name: 'Film', icon: 'film'},
                    {id: 'musica', name: 'Musica', icon: 'music'},
                    {id: 'libri', name: 'Libri', icon: 'book'}
                ],
                setID: this.$router,
            }
        }
    }
</script>

<style scoped>

</style>