<template>
    <div class="p-10 text-white film-add">
        <h1 class="text-4xl font-semibold tracking-wide mb-6">Aggiungi Canzone</h1>
        <form class="w-full h-full max-w-2xl" method="post" @keydown.enter.prevent="">
            <div class="flex flex-wrap -mx-3 mb-6 ">
                <div class="w-full px-3">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-titolo">
                        Titolo
                    </label>
                    <input v-model="titolo" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-titolo" type="text" placeholder="Bad Romance">
                </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-2">
                <div class="w-full px-3 mb-6">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-plot">
                        Artista
                    </label>
                    <input v-model="artista" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-plot" type="text" placeholder="Lady Gaga">
                </div>

                <div class="w-full px-3 mb-6">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-pubblicazione">
                        Pubblicazione
                    </label>
                    <DatePicker
                            is-dark
                            id="grid-pubblicazione"
                            :max-date="new Date()"
                            v-model="pubblicazione"
                            :input-props='{
                                class: "w-full shadow appearance-none bg-gray-200 focus:bg-white focus:border-gray-500 border rounded py-2 px-3 text-gray-700 hover:border-blue-5",
                                placeholder: "26/08/2009",
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
                    <button v-on:click.prevent="postCanzone" class="bg-green hover:bg-greenest text-white font-bold py-2 px-10 rounded mr-5">Aggiungi</button>
                    <button v-on:click.prevent="fetchCanzone" class="bg-tmdb_secondary hover:bg-tmdb_primary text-white font-bold py-2 px-10 rounded">Fetch from Last.fm & Aggiungi</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
    import DatePicker from 'v-calendar/lib/components/date-picker.umd'
    import {APIService} from "../../APIService";
    import * as dayjs from 'dayjs'
    import {lastfmAPIService} from "../../lastfmAPIService";
    import swal from 'sweetalert';
    const apiService = new APIService();
    const lastfmService = new lastfmAPIService();

    export default {
        name: "add-song",
        data: function (){
            return {
                pubblicazione: null,
                titolo: '',
                artista: '',
                plot: '',
                data: {},
                file: '',
                canzone: {},
                datiArtista : null
            }
        },
        components: {
            DatePicker
        },
        methods:{
            postCanzone() {
                /*
                    Initialize the form data
                */
                let formData = new FormData();

                /*
                    Add the form data we need to submit
                */
                formData.append('titolo', this.titolo);
                formData.append('pubblicazione', dayjs(this.pubblicazione).format('YYYY-MM-DD'));
                //formData.append('plot', this.plot);
                if(this.nuovo.file){
                    formData.append('src', this.nuovo.file)
                }

                // Display the key/value pairs
                for (let pair of formData.entries()) {
                    console.log(pair[0]+ ', ' + pair[1]);
                }
                /*
                  Make the request to the POST /single-file URL
                */
                apiService.postCanzone(formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(() => {
                    swal({
                        title: "Ottimo!",
                        text: `Canzone ${this.titolo} aggiunta!`,
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
                this.file = this.$refs.file.files[0];
            },
            fetchCanzone(){
                lastfmService.searchTrack(this.titolo, this.artista)
                    .then(data => {
                        this.data = data.results.trackmatches.track[0]
                    })
                    .then(() => {
                        lastfmService.getArtistbyName(this.data.artist)
                            .then(ar =>{
                                let temp = ar
                                if(this.temp.mbid !== ''){
                                    console.log('mbid')
                                } else {
                                    this.datiArtista = temp.name
                                    console.log(this.datiArtista)
                                }
                            })
                    })
                    .then(()=>{
                        console.log(this.data)
                        if(this.data.mbid !== ''){
                            lastfmService.getTrack(this.data.mbid)
                                .then((canzone)=>{
                                    this.canzone = canzone.track
                                    console.log(this.canzone)
                                    apiService.postCanzone({
                                        "titolo": this.canzone.name,
                                        "pubblicazione": dayjs(this.canzone.wiki.published).format('YYYY-MM-DD'),
                                        "plot": this.canzone.wiki.content,
                                        "lastfm_id": this.canzone.mbid,
                                        "e_src": this.canzone.album.image[3]['#text'],
                                        "e_artista_id": this.canzone.artist.mbid
                                    }).then(() => {
                                        swal({
                                            title: "Ottimo!",
                                            text: `Libro ${this.canzone.name} aggiunto!`,
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
                            lastfmService.getTrackbyName(this.data.name, this.data.artist)
                                .then((canzone)=>{
                                    this.canzone = canzone.track
                                    console.log(this.canzone)
                                    apiService.postCanzone({
                                        "titolo": this.canzone.name,
                                        "pubblicazione": dayjs(this.canzone.wiki.published).format('YYYY-MM-DD'),
                                        "plot": this.canzone.wiki.content,
                                        "lastfm_id": this.canzone.name + this.canzone.duration,
                                        "e_src": this.canzone.album.image[3]['#text'],
                                        "e_artista_id": this.datiArtista
                                    }).then(() => {
                                        swal({
                                            title: "Ottimo!",
                                            text: `Libro ${this.canzone.name} aggiunto!`,
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
        }
    }
</script>

<style scoped>

</style>