<template>
        <!-- Cast -->
        <div class="w-full flex flex-wrap">
            <div v-for="cast in casts" v-bind:key="cast.id" class="rounded-lg p-2 w-48 relative">
                <div class="absolute w-full h-full flex items-end justify-end p-8 opacity-0 hover:opacity-100">
                    <div class="bg-green rounded-full h-10 w-10 flex items-center justify-center">
                        <font-awesome-icon icon="eye"/>
                    </div>
                </div>
                <img :src="cast.src" alt="" class="rounded-full h-auto w-full">
                <h1 class="text-center text-sm font-semibold text-white tracking-wide">{{ cast.nome }}</h1>
            </div>
        </div>
</template>

<script>
    export default {
        name: "Cast",
        props: {
            casts: Array
        }
    }
</script>

<style scoped>

</style>