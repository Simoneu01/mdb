<template>
    <!-- Two columns -->
    <div class="flex flex-col text-white">
        <div class="libro flex mb-4">
            <div class="w-1/6 p-10">
                <img :src="`${libro.e_src ? libro.e_src : libro.src}`" alt="" class="flex-1 shadow mb-2">
                <h1 class="text-xl font-semibold tracking-wide">Pubblicazione: {{libro.pubblicazione}}</h1>
            </div>
            <div class="w-5/6 p-10">
                <div class="text-5xl font-semibold tracking-wide">
                    {{libro.titolo}}
                </div>
                <div v-html="libro.plot">

                </div>
            </div>
            <div class="w-6/6 p-10">
                <div class="inline-flex">
                    <router-link :to="`${libro.id}/edit`">
                        <button class="bg-green hover:bg-greenest text-white font-bold py-2 px-5 rounded mr-2">Edit</button>
                    </router-link>
                    <button v-on:click.prevent="deleteLibro" class="bg-red-600 hover:bg-red-800 text-white font-bold py-2 px-5 rounded mr-2">Delete</button>
                </div>
            </div>
        </div>
        <div v-if="autore" class="p-10">
            <h1 class="text-4xl pl-2 font-semibold tracking-wide">Autore</h1>
            <!-- Autore -->
            <div class="w-full flex flex-wrap">
                <div v-bind:key="autore.id" class="rounded-lg p-2 w-48 relative">
                    <div class="absolute w-full h-full flex items-end justify-end p-8 opacity-0 hover:opacity-100">
                        <div class="bg-green rounded-full h-10 w-10 flex items-center justify-center">
                            <font-awesome-icon icon="eye"/>
                        </div>
                    </div>
                    <img :src="autore.src" alt="" class="rounded-full h-auto w-full">
                    <h1 class="text-center text-sm font-semibold text-white tracking-wide">{{ autore.nome }}</h1>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    import {APIService} from '../../APIService';
    import swal from 'sweetalert';
    const apiService = new APIService();

    export default {
        name: "libri-details",
        data(){
            return {
                libro: null,
                autore: {
                    id: 1,
                    src: "https://pbs.twimg.com/profile_images/1055263632861343745/vIqzOHXj.jpg",
                    nome: "Simone"
                }
            }
        },
        methods:{
            getLibro(){
                this.libro = null
                apiService.getLibro(this.$route.params.id, (err, libro) => {
                    if (err) {
                        console.log(err)
                    } else {
                        this.libro = libro
                    }
                })
            },
            deleteLibro(){
                swal({
                    title: "Sei sicuro?",
                    text: "Una volta eliminato, non sarai in grado di ripristinare il libro ma dovrai riaggiungerlo!!",
                    icon: "warning",
                    buttons: true,
                    dangerMode: true,
                })
                    .then((willDelete) => {
                        if (willDelete) {
                            swal("Poof! Il Libro è stato eliminato!!", {
                                icon: "success",
                            });
                            apiService.deleteLibro(this.$route.params.id)
                            this.$router.push('/libri')
                        } else {
                            swal("Il tuo libro è salvo!!");
                        }
                    });

            }
        },
        watch: {
            '$route': 'getFilm'
        },
        mounted() {
            this.getLibro()
        },
        beforeRouteEnter : (to, from, next) => {

            function isValid (id) {
                return apiService.getLibro(id, (err) => {
                    if (err) {
                        next('/404');
                    } else {
                        next();
                    }
                })
            }

            isValid(to.params.id);
        },
        beforeRouteUpdate : (to, from, next) => {

            function isValid (id) {
                return apiService.getLibro(id, (err) => {
                    if (err) {
                        next('/404');
                    } else {
                        next();
                    }
                })
            }

            isValid(to.params.id);
        }
    }
</script>

<style scoped>

</style>