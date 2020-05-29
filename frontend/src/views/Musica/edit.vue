<template>
    <div class="p-10 text-white film-add">
        <h1 v-if="canzone" class="text-4xl font-semibold tracking-wide mb-6">Modifica: {{canzone.titolo}}</h1>
        <form v-if="nuovo" class="w-full h-full max-w-2xl" @keydown.enter.prevent="">
            <div class="flex flex-wrap -mx-3 mb-6 ">
                <div class="w-full px-3">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-titolo">
                        Titolo
                    </label>
                    <input v-model="nuovo.titolo" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-titolo" type="text" placeholder="Fight Club">
                </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-2">
                <div class="w-full px-3 mb-6">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-plot">
                        Trama
                    </label>
                    <textarea v-model="nuovo.plot" rows="10" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-plot" type="text" placeholder="Un uomo di trent'anni è insofferente su tutto e la notte non riesce più a dormire. In cerca di qualche luogo dove scaricare la propria ansia si mette a frequentare quei corsi dove gruppi di malati gravi si riuniscono e confessano agli altri le rispettive situazioni. Mentre si lascia andare alla commozione e al pianto di fronte a quello che vede, l'uomo fa la conoscenza prima di Marla Singer poi di Tyler Durden. Lei è una ragazza a sua volta alla deriva, incapace di scelte o decisioni; lui è un tipo deciso e vigoroso con un'idea precisa in testa. Tyler fa saltare per aria l'appartamento dell'uomo e i due vanno a vivere insieme in una casa fatiscente. Deciso a coinvolgerlo nel suo progetto, Tyler lo fa entrare in un 'Fight Club', uno stanzone sotterraneo dove ci si riunisce per picchiarsi e in questo modo sentirsi di nuovo vivi"></textarea>
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
                                placeholder: "1999-10-15",
                                readonly: true
                            }'
                    />
                </div>

                <div class="w-full px-3 mb-6">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-file">
                        Copertina
                    </label>
                    <input type="file" id="grid-file" ref="file" v-on:change="handleFileUpload()"/>

                </div>
                <div class="flex flex-wrap px-3 mb-6">
                    <button v-on:click.prevent="patchCanzone" class="bg-green hover:bg-greenest text-white font-bold py-2 px-10 rounded mr-5">Aggiorna</button>
                    <button v-on:click.prevent="fetchCanzone" class="bg-tmdb_secondary hover:bg-tmdb_primary text-white font-bold py-2 px-10 rounded">Fetch from Last.fm & Aggiorna</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
    import DatePicker from 'v-calendar/lib/components/date-picker.umd'
    import {APIService} from "../../APIService";
    import * as dayjs from 'dayjs'
    const apiService = new APIService();
    import swal from 'sweetalert';
    import {lastfmAPIService} from "../../lastfmAPIService";
    const lastfmService = new lastfmAPIService();

    export default {
        name: "edit-film",
        data: function (){
            return {
                canzone: {},
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
            getCanzone(){
                this.canzone = null
                apiService.getCanzonenoCB(this.$route.params.id)
                    .then((canzone) => {
                        this.canzone = canzone
                        this.nuovo.titolo = canzone.titolo
                        this.nuovo.pubblicazione = new Date(canzone.pubblicazione)
                        this.nuovo.plot = canzone.plot
                    })
            },
            patchCanzone() {
                /*
                    Initialize the form data
                */
                let formData = new FormData();

                /*
                    Add the form data we need to submit
                */

                console.log(this.canzone.titolo !== this.nuovo.titolo)
                if(this.canzone.titolo !== this.nuovo.titolo){
                    formData.append('titolo', this.nuovo.titolo)
                }
                if(this.canzone.pubblicazione !== this.nuovo.pubblicazione){
                    formData.append('pubblicazione', dayjs(this.nuovo.pubblicazione).format('YYYY-MM-DD'));
                }
                if(this.canzone.plot !== this.nuovo.plot){
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
                apiService.patchCanzone(this.$route.params.id, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(() => {
                    swal({
                        title: "Ottimo!",
                        text: `Canzone ${this.nuovo.titolo} aggiornato!`,
                        icon: "success"
                    });
                    this.$router.push('/musica')
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
            fetchCanzone(){
                if(this.canzone.mbid !== ''){
                    lastfmService.getTrack(this.canzone.lastfm_id)
                        .then((canzone)=>{
                            this.data = canzone.track
                            apiService.patchCanzone(this.$route.params.id, {
                                "titolo": this.data.name,
                                "pubblicazione": dayjs(this.data.wiki.published).format('YYYY-MM-DD'),
                                "plot": this.data.wiki.content,
                                "e_src": this.data.album.image[3]['#text']
                            }).then(() => {
                                swal({
                                    title: "Ottimo!",
                                    text: `Canzone ${this.data.name} aggiornata!`,
                                    icon: "success"
                                });
                                this.$router.push('/musica')
                            }).catch((err) => {
                                console.log(err)
                                swal({
                                    title: "Attenzione!",
                                    text: "La canzone è già presente!",
                                    icon: "error"
                                });
                            })
                        })
                } else {
                    lastfmService.getTrackbyName(this.canzone.titolo, this.canzone.artista)
                        .then((canzone)=>{
                            this.data = canzone.track
                            apiService.patchCanzone(this.$route.params.id,{
                                "titolo": this.data.name,
                                "pubblicazione": dayjs(this.data.wiki.published).format('YYYY-MM-DD'),
                                "plot": this.data.wiki.content,
                                "e_src": this.data.album.image[3]['#text']
                            }).then(() => {
                                swal({
                                    title: "Ottimo!",
                                    text: `Canzone ${this.data.name} aggiornata!`,
                                    icon: "success"
                                });
                                this.$router.push('/musica')
                            }).catch((err) => {
                                console.log(err)
                                swal({
                                    title: "Attenzione!",
                                    text: "La canzone è già presente!",
                                    icon: "error"
                                });
                            })
                        })
                }
            }
        },
        async mounted() {
            await this.getCanzone()
        },
        beforeRouteEnter : (to, from, next) => {

            function isValid (id) {
                return apiService.getCanzone(id, (err) => {
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
                return apiService.getCanzone(id, (err) => {
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