<template>
        <div class="p-10 text-white film-add w-full h-full max-w-2xl">
            <h1 class="text-4xl font-semibold tracking-wide mb-6">Modifica Account</h1>
                <div class="flex flex-wrap -mx-3 mb-6 ">
                    <div class="w-full px-3">
                        <label class="block uppercase tracking-wide font-bold mb-2" for="grid-titolo">
                            Nome Account
                        </label>
                        <input v-model="nome" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-titolo" type="text" placeholder="Simone Ungaro">
                    </div>
                </div>
        </div>

</template>

<script>
    export default {
        name: "Account",
        computed: {
            nome:{
                get () {
                    return this.$store.getters.getName
                },
                set (value) {
                    this.$store.commit('changeName', value)
                }
            }
        }
    }
</script>

<style scoped>

</style>