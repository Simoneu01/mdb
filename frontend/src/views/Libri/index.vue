<template>
    <div class="px-6 py-3">
        <!-- Titolo -->
        <div class="pl-2">
            <div class="flex items-center justify-between">
                <h1 class="text-2xl font-semibold text-white tracking-wider hover:underline">Libri</h1>
                <router-link to="libri/add">
                    <button class="bg-green hover:bg-greenest text-white font-bold py-2 px-4 rounded">Aggiungi Libri</button>
                </router-link>
            </div>
            <h2 class="text-lightest">Ultimi Libri aggiunti</h2>
        </div>
        <!-- Cards -->
        <div class="w-full flex flex-wrap">
            <router-link v-for="libro in libri" v-bind:key="libro.id" :to="`libri/${libro.id}`">
                <div class="p-2 w-48 relative">
                    <div class="absolute w-full h-full flex items-end justify-end p-8 opacity-0 hover:opacity-100">
                        <div class="bg-green rounded-full h-10 w-10 flex items-center justify-center">
                            <font-awesome-icon icon="eye"/>
                        </div>
                    </div>
                    <div class="bg-light w-full h-auto p-5 rounded-lg shadow-md">
                        <img :src="`${libro.e_src ? libro.e_src : libro.src}`"
                             alt="" class="h-auto w-full shadow mb-2">
                        <h1 class="text-sm font-semibold text-white tracking-wide">{{ libro.titolo }}</h1>
                        <h1 class="text-xs font-semibold text-lightest tracking-wide">{{ libro.pubblicazione }}</h1>
                        <h1 class="text-xs font-semibold text-lightest tracking-wide pb-5">{{ libro.scrittore }}</h1>
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
        name: "Libri",
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