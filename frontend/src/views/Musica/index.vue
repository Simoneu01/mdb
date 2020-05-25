<template>
    <div class="px-6 py-3">
        <!-- Titolo -->
        <div class="pl-2">
            <div class="flex items-center justify-between">
                <h1 class="text-2xl font-semibold text-white tracking-wider hover:underline">Canzoni</h1>
                <router-link to="musica/add">
                    <button class="bg-green hover:bg-greenest text-white font-bold py-2 px-4 rounded">Aggiungi Canzone</button>
                </router-link>
            </div>
            <h2 class="text-lightest">Ultime Canzoni aggiunte</h2>
        </div>
        <!-- Cards -->
        <div class="w-full flex flex-wrap">
            <router-link v-for="canzone in canzoni" v-bind:key="canzone.id" :to="`musica/${canzone.id}`">
                <div class="p-2 w-48 relative">
                    <div class="absolute w-full h-full flex items-end justify-end p-8 opacity-0 hover:opacity-100">
                        <div class="bg-green rounded-full h-10 w-10 flex items-center justify-center">
                            <font-awesome-icon icon="eye"/>
                        </div>
                    </div>
                    <div class="bg-light w-full h-auto p-5 rounded-lg shadow-md">
                        <img :src="`${canzone.e_src ? canzone.e_src : canzone.src}`"
                             alt="" class="h-auto w-full shadow mb-2">
                        <h1 class="text-sm font-semibold text-white tracking-wide">{{ canzone.titolo }}</h1>
                        <h1 class="text-xs font-semibold text-lightest tracking-wide pb-5">{{ canzone.artista }}</h1>
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
        name: "Musica",
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
            },
            watchCanzoni(){
                setTimeout(this.getCanzoni, 1000)
            }
        },
        watch: {
            '$route': 'getCanzoni',
            libri: {
                handler: 'watchCanzoni'
            },
        },
        mounted() {
            this.getCanzoni()
        }
    }
</script>

<style scoped>

</style>