<template>
    <div class="p-10 text-white libro-add">
        <h1 v-if="libro" class="text-4xl font-semibold tracking-wide mb-6">Modifica {{libro.titolo}}</h1>
        <form class="w-full h-full max-w-2xl" @keydown.enter.prevent="">
            <div class="flex flex-wrap -mx-3 mb-6 ">
                <div class="w-full px-3">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-titolo">
                        Titolo
                    </label>
                    <input v-model="nuovo.titolo" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-titolo" type="text" placeholder="La fattoria degli animali">
                </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-2">
                <div class="w-full px-3 mb-6">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-plot">
                        Trama (HTML SUPPORTATO)
                    </label>
                    <textarea v-model="nuovo.plot" rows="10" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-plot" type="text" placeholder="Plottt"></textarea>
                </div>

                <div class="w-full px-3 mb-6">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-pubblicazione">
                        Pubblicazione
                    </label>
                    <DatePicker
                            is-dark
                            id="grid-pubblicazione"
                            :max-date="new Date()"
                            v-model="nuovo.pubblicazione"
                            :input-props='{
                                class: "w-full shadow appearance-none bg-gray-200 focus:bg-white focus:border-gray-500 border rounded py-2 px-3 text-gray-700 hover:border-blue-5",
                                placeholder: "15/10/1999",
                                readonly: true
                            }'
                    />
                </div>
                <div class="w-full px-3 mb-6">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-file">
                        Copertina
                    </label>
                    <input id="grid-file" type="file" ref="file" v-on:change="handleFileUpload()"/>
                </div>
                <div class="flex flex-wrap px-3 mb-6">
                    <button v-on:click.prevent="patchLibro" class="bg-green hover:bg-greenest text-white font-bold py-2 px-10 rounded mr-5">Modifica</button>
                    <button v-on:click.prevent="fetchLibro" class="bg-tmdb_secondary hover:bg-tmdb_primary text-white font-bold py-2 px-10 rounded">Fetch from Google Books & Aggiorna</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
    import DatePicker from 'v-calendar/lib/components/date-picker.umd'
    import {APIService} from "../../APIService";
    import * as dayjs from 'dayjs'
    import {gbookAPIService} from "../../gbookAPIService";
    const apiService = new APIService();
    const gbooksService = new gbookAPIService();
    import swal from 'sweetalert';

    export default {
        name: "edit-libro",
        data: function (){
            return {
                libro: {},
                nuovo: {
                    titolo: null,
                    pubblicazione: null,
                    plot: null,
                    file: null
                },
                data: {}
            }
        },
        components: {
            DatePicker
        },
        methods:{
            getLibro(){
                this.libro = null
                apiService.getLibronoCB(this.$route.params.id)
                    .then((libro) => {
                        this.libro = libro
                        this.nuovo.titolo = libro.titolo
                        this.nuovo.pubblicazione = new Date(libro.pubblicazione)
                        this.nuovo.plot = libro.plot
                    })
            },
            patchLibro() {
                /*
                    Initialize the form data
                */
                let formData = new FormData();

                /*
                    Add the form data we need to submit
                */

                console.log(this.libro.titolo !== this.nuovo.titolo)
                if(this.libro.titolo !== this.nuovo.titolo){
                    formData.append('titolo', this.nuovo.titolo)
                }
                if(this.libro.pubblicazione !== this.nuovo.pubblicazione){
                    formData.append('pubblicazione', dayjs(this.nuovo.pubblicazione).format('YYYY-MM-DD'));
                }
                if(this.libro.plot !== this.nuovo.plot){
                    formData.append('plot', this.nuovo.plot)
                }
                if(this.nuovo.file){
                    formData.append('src', this.nuovo.file)
                }

                /*
                  Make the request to the POST /single-file URL
                */

                for (let pair of formData.entries()) {
                    console.log(pair[0]+ ', ' + pair[1]);
                }
                apiService.patchLibro(this.$route.params.id, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(() => {
                    swal({
                        title: "Ottimo!",
                        text: `Libro ${this.nuovo.titolo} aggiornato!`,
                        icon: "success"
                    });
                    this.$router.push('/libri')
                }).catch((err) => {
                    console.log(err)
                    swal({
                        title: "Attenzione!",
                        text: "Errore! Non hai compilato tutti i campi!",
                        icon: "error"
                    });
                })
            },
            handleFileUpload(){
                this.nuovo.file = this.$refs.file.files[0];
            },
            fetchLibro(){
                gbooksService.getBook(this.libro.gbooks_id)
                .then(data => {
                    console.log(data.volumeInfo)
                    this.data = data.volumeInfo
                })
                .then(() => {
                    apiService.patchLibro(this.$route.params.id,{
                        "titolo": this.data.title,
                        "pubblicazione": dayjs(this.data.publishedDate).format('YYYY-MM-DD'),
                        "plot": this.data.description,
                        "e_src": "https://books.google.com/books/content/images/frontcover/"+this.libro.gbooks_id+"?fife=w500-h700"
                    }).then(() => {
                        swal({
                            title: "Ottimo!",
                            text: `Libro ${this.data.title} aggiornato!`,
                            icon: "success"
                        });
                        this.$router.push('/libri')
                    }).catch((err) => {
                        console.log(err)
                        swal({
                            title: "Attenzione!",
                            text: "Il Film è già presente!",
                            icon: "error"
                        });
                    })
                })
                .catch((err) => {
                    console.log(err)
                    swal({
                        title: "Oops!!",
                        text: "Qualcosa è andato storto\n" + err.message,
                        icon: "error"
                    });
                })
            }
        },
        async mounted() {
            await this.getLibro()
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