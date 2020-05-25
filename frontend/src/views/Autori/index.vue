<template>
    <div class="px-6 py-3">
        <!-- Titolo -->
        <div class="pl-2">
            <div class="flex items-center justify-between">
                <h1 class="text-2xl font-semibold text-white tracking-wider hover:underline">Autori</h1>
                <router-link to="autori/add">
                    <button class="bg-green hover:bg-greenest text-white font-bold py-2 px-4 rounded">Aggiungi Autore</button>
                </router-link>
            </div>
            <h2 class="text-lightest">Ultimi Autori aggiunti</h2>
        </div>
        <!-- Cards -->
        <div class="w-full flex flex-wrap">
            <router-link v-for="autore in autori" v-bind:key="autore.id" :to="`autore/${autore.id}`">
                <div class="p-2 w-48 relative">
                    <div class="absolute w-full h-full flex items-end justify-end p-8 opacity-0 hover:opacity-100">
                        <div class="bg-green rounded-full h-10 w-10 flex items-center justify-center">
                            <font-awesome-icon icon="eye"/>
                        </div>
                    </div>
                    <div class="bg-light w-full h-auto p-5 rounded-lg shadow-md">
                        <img :src="`${autore.e_src ? autore.e_src : autore.src}`"
                             alt="" class="h-auto w-full shadow mb-2">
                        <h1 class="text-sm font-semibold text-white tracking-wide">{{ autore.titolo }}</h1>
                        <h1 class="text-xs font-semibold text-lightest tracking-wide">{{ autore.pubblicazione }}</h1>
                        <h1 class="text-xs font-semibold text-lightest tracking-wide pb-5">{{ autore.scrittore }}</h1>
                    </div>
                </div>
            </router-link>
        </div>
    </div>
</template>

<script>
    import {APIService} from '../../APIService';
    const apiService = new APIService();

    export default {
        name: "Scrittori",
        data(){
            return {
                autori: []
            }
        },
        methods:{
            getLibri(){
                apiService.getLibri().then((data) => {
                    this.autori = data;
                });
            },
            watchLibri(){
                setTimeout(this.getLibri, 1000)
            }
        },
        watch: {
            '$route': 'getLibri',
            libri: {
                handler: 'watchLibri'
            },
        },
        mounted() {
            this.getLibri()
        }
    }
</script>

<style scoped>

</style>