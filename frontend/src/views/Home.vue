<template>
    <div>
        <!-- FILMS -->
        <div class="px-6 py-3">
            <!-- Titolo -->
            <router-link to="/film">
                <div class="flex items-center justify-between">
                    <h1 class="pl-2 text-2xl font-semibold text-white tracking-wider hover:underline">Ultimi Films Aggiunti</h1>
                    <h2 class="pr-8 pt-4 text-lightest uppercase tracking-wider hover:underline mb-3">Vedi Tutti</h2>
                </div>
            </router-link>
            <!-- Cards -->
            <div class="w-full flex flex-wrap">
                <router-link v-for="film in films" v-bind:key="film.id" :to="`film/${film.id}`">
                    <div class="p-2 w-48 relative">
                        <div class="absolute w-full h-full flex items-end justify-end p-8 opacity-0 hover:opacity-100">
                            <div class="bg-green rounded-full h-10 w-10 flex items-center justify-center">
                                <font-awesome-icon icon="eye"/>
                            </div>
                        </div>
                        <div class="bg-light w-full h-auto p-5 rounded-lg shadow-md">
                            <img :src="`${film.e_src ? film.e_src : film.src}`"
                                 alt="" class="h-auto w-full shadow mb-2">
                            <h1 class="text-sm font-semibold text-white tracking-wide">{{ film.titolo }}</h1>
                            <h1 class="text-xs font-semibold text-lightest tracking-wide pb-5">{{ film.pubblicazione }}</h1>
                        </div>
                    </div>
                </router-link>
            </div>
        </div>
        <!-- LIBRI -->
        <div class="px-6 py-3">
            <!-- Titolo -->
            <router-link to="/libri">
                <div class="flex items-center justify-between">
                    <h1 class="pl-2 text-2xl font-semibold text-white tracking-wider hover:underline">Ultimi Libri Aggiunti</h1>
                    <h2 class="pr-8 pt-4 text-lightest uppercase tracking-wider hover:underline mb-3">Vedi Tutti</h2>
                </div>
            </router-link>
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
        <!-- MUSICA -->
        <div class="px-6 py-3">
            <!-- Titolo -->
            <router-link to="/musica">
                <div class="flex items-center justify-between">
                    <h1 class="pl-2 text-2xl font-semibold text-white tracking-wider hover:underline">Ultime Canzoni Aggiunte</h1>
                    <h2 class="pr-8 pt-4 text-lightest uppercase tracking-wider hover:underline mb-3">Vedi Tutti</h2>
                </div>
            </router-link>
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
    </div>
</template>

<script>
    import {APIService} from '../APIService';
    const apiService = new APIService();

    export default {
        name: "Home",
        data(){
            return {
                canzoni: null,
                films: null,
                libri: null
            }
        },
        methods: {
            getCanzoni(){
                apiService.getCanzoni().then((data) => {
                    this.canzoni = data.slice(-9).reverse();
                });
            },
            getFilms(){
                apiService.getFilms().then((data) => {
                    this.films = data.slice(-9).reverse();
                });
            },
            getLibri(){
                apiService.getLibri().then((data) => {
                    this.libri = data.slice(-9).reverse();
                });
            },
        },
        mounted() {
            this.getLibri()
            this.getCanzoni()
            this.getFilms()
        }
    }
</script>

<style scoped>

</style>