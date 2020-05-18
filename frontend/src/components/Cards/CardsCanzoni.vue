<template>
    <div class="px-6 py-3">
        <!-- Titolo -->
        <div class="pl-2">
            <h1 class="text-2xl font-semibold text-white tracking-wider hover:underline">Canzoni</h1>
            <h2 class="text-lightest">Ultime Canzoni aggiunte</h2>
        </div>
        <!-- Cards -->
        <div class="w-full flex flex-wrap">
            <div v-for="canzone in canzoni" v-bind:key="canzone.id" class="p-2 w-48 relative">
                <div class="absolute w-full h-full flex items-end justify-end p-8 opacity-0 hover:opacity-100">
                    <div class="bg-green rounded-full h-10 w-10 flex items-center justify-center">
                        <font-awesome-icon @click="showModal" icon="edit"/>
                        <Modal
                                v-show="isModalVisible"
                                @close="closeModal"
                        />
                    </div>
                </div>
                <div class="bg-light w-full h-auto p-5 rounded-lg shadow-md">
                    <img :src="canzone.src" alt="" class="h-auto w-full shadow mb-2">
                    <h1 class="text-sm font-semibold text-white tracking-wide">{{ canzone.titolo }}</h1>
                    <h1 class="text-xs font-semibold text-lightest tracking-wide pb-5">{{ canzone.artista }}</h1>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    import Modal from "../Modal";
    export default {
        name: "Cards",
        props: {
            canzoni: Array
        },
        components: {Modal},
        data () {
            return {
                isModalVisible: false
            }
        },
        methods: {
            showModal() {
                this.isModalVisible = true;
            },
            closeModal() {
                this.isModalVisible = false;
            }
        },
    }
</script>

<style scoped>

</style>