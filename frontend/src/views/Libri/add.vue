<template>
    <div class="p-10 text-white film-add">
        <h1 class="text-4xl font-semibold tracking-wide mb-6">Aggiungi Libro</h1>
        <form class="w-full h-full max-w-2xl" @keydown.enter.prevent="">
            <div class="flex flex-wrap -mx-3 mb-6 ">
                <div class="w-full px-3">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-titolo">
                        Titolo
                    </label>
                    <input v-model="titolo" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-titolo" type="text" placeholder="La fattoria degli animali">
                </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-2">
                <div class="w-full px-3 mb-6">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-plot">
                        Trama
                    </label>
                    <textarea v-model="plot" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-plot" type="text" placeholder="Plottt"></textarea>
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
                    <button v-on:click.prevent="postLibro" class="bg-green hover:bg-greenest text-white font-bold py-2 px-10 rounded mr-5">Aggiungi</button>
                    <button v-on:click.prevent="fetchLibro" class="bg-tmdb_secondary hover:bg-tmdb_primary text-white font-bold py-2 px-10 rounded">Fetch from Google Books & Aggiungi</button>
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
    import swal from 'sweetalert';
    const apiService = new APIService();
    const gbooksService = new gbookAPIService();

    export default {
        name: "add-libro",
        data: function (){
            return {
                pubblicazione: null,
                titolo: '',
                plot: '',
                data: {},
                file: '',
                libro: {}
            }
        },
        components: {
            DatePicker
        },
        methods:{
            postLibro() {
                /*
                    Initialize the form data
                */
                let formData = new FormData();

                /*
                    Add the form data we need to submit
                */
                formData.append('titolo', this.titolo);
                formData.append('pubblicazione', dayjs(this.pubblicazione).format('YYYY-MM-DD'));
                formData.append('plot', this.plot);
                formData.append('src', this.file);

                // Display the key/value pairs
                for (let pair of formData.entries()) {
                    console.log(pair[0]+ ', ' + pair[1]);
                }
                /*
                  Make the request to the POST /single-file URL
                */
                apiService.postLibro(formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(() => {
                    swal({
                        title: "Ottimo!",
                        text: `Libro ${this.titolo} aggiunto!`,
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
            fetchLibro(){
                gbooksService.searchBook(this.titolo)
                    .then(data => {
                        this.data = data.items[0]
                    })
                    .then(()=>{
                        gbooksService.getBook(this.data.id)
                            .then((libro)=>{
                                this.libro = libro.volumeInfo
                                apiService.postLibro({
                                    "titolo": this.libro.title,
                                    "pubblicazione": this.libro.publishedDate,
                                    "plot": this.libro.description,
                                    "gbooks_id": this.data.id,
                                    // https://books.google.com/books/content/images/frontcover/lnGEEb7IqdsC?fife=w500-h700
                                    "e_src": "https://books.google.com/books/content/images/frontcover/"+this.data.id+"?fife=w500-h700"
                                }).then(() => {
                                    swal({
                                        title: "Ottimo!",
                                        text: `Libro ${this.titolo} aggiunto!`,
                                        icon: "success"
                                    });
                                    this.$router.push('/libri')
                                }).catch((err) => {
                                    console.log(err)
                                    swal({
                                        title: "Attenzione!",
                                        text: "Il Libro è già presente!",
                                        icon: "error"
                                    });
                                })
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
        }
    }
</script>

<style scoped>

</style>