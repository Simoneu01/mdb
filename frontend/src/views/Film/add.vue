<template>
    <div class="p-10 text-white film-add">
        <h1 class="text-4xl font-semibold tracking-wide mb-6">Aggiungi Film</h1>
        <form class="w-full h-full max-w-2xl">
            <div class="flex flex-wrap -mx-3 mb-6 ">
                <div class="w-full px-3">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-titolo">
                        Titolo
                    </label>
                    <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-titolo" type="text" placeholder="Doe">
                </div>
            </div>
            <div class="flex flex-wrap -mx-3 mb-2">
                <div class="w-full px-3 mb-6">
                    <label class="block uppercase tracking-wide font-bold mb-2" for="grid-city">
                        Trama
                    </label>
                    <textarea class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-city" type="text" placeholder="Albuquerque"></textarea>
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
                                placeholder: "Release date",
                                readonly: true
                            }'
                    />
                </div>
                <div class="flex flex-wrap px-3 mb-6">
                    <button class="bg-green hover:bg-greenest text-white font-bold py-2 px-10 rounded mr-5">Aggiungi</button>
                    <button class="bg-tmdb_secondary hover:bg-tmdb_primary text-white font-bold py-2 px-10 rounded">Fetch from TMDb</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
    import DatePicker from 'v-calendar/lib/components/date-picker.umd'

    export default {
        name: "add-film",
        data: function (){
            return {
                pubblicazione: null
            }
        },
        components: {DatePicker}
    }
</script>

<style scoped>

</style>