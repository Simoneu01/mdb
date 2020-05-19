<template>
    <div class="px-6 py-3">
        <!-- Titolo -->
        <div class="flex items-center justify-between">
            <h1 class="pl-2 text-2xl font-semibold text-white tracking-wider hover:underline">Ultimi Aggiunti</h1>
            <h2 class="pr-8 pt-4 text-lightest uppercase tracking-wider hover:underline mb-3">Vedi Tutti</h2>
        </div>
        <!-- Cards -->
        <div class="w-full flex flex-wrap">
            <div v-for="recent in dati" v-bind:key="recent.id" class="p-2 w-48 relative">
                <div class="absolute w-full h-full flex items-end justify-end p-8 opacity-0 hover:opacity-100">
                    <div class="bg-green rounded-full h-10 w-10 flex items-center justify-center">
                        <font-awesome-icon icon="eye"/>
                    </div>
                </div>
                <div class="bg-light w-full h-auto p-5 rounded-lg shadow-md">
                    <img :src="recent.src" alt="" class="h-auto w-full shadow mb-2">
                    <h1 class="text-sm font-semibold text-white tracking-wide">{{ recent.title }}</h1>
                    <h1 class="text-xs font-semibold text-lightest tracking-wide pb-5">{{ recent.artist }}</h1>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    export default {
        name: "Cards",
            props: {
                dati: Array
            }
    }
</script>

<style scoped>

</style>