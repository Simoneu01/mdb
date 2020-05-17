<template>
    <div class="px-6 py-3">
        <!-- Titolo -->
        <div class="flex items-center justify-between">
            <h1 class="pl-2 text-2xl font-semibold text-white tracking-wider hover:underline">Ultimi Aggiunti</h1>
            <h2 class="pr-8 pt-4 text-lightest uppercase tracking-wider hover:underline mb-3">Vedi Tutti</h2>
        </div>
        <!-- Cards -->
        <div class="w-full flex flex-wrap">
            <div v-for="recent in recents" v-bind:key="recent" class="p-2 w-48 relative">
                <div class="absolute w-full h-full flex items-end justify-end p-8 opacity-0 hover:opacity-100">
                    <div class="bg-green rounded-full h-10 w-10 flex items-center justify-center">
                        <font-awesome-icon icon="edit"/>
                    </div>
                </div>
                <div class="bg-light w-full h-auto p-5 rounded-lg shadow-md">
                    <img :src="recent.src" alt="" class="h-auto w-full shadow mb-2">
                    <h1 class="text-sm font-semibold text-white tracking-wide">{{ recent.title }}</h1>
                    <h1 class="text-xs font-semibold text-lightest tracking-wide pb-5">{{ recent.artist }}</h1>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    export default {
        name: "Cards",
        data: function () {
            return {
                recents: [
                    {src: "https://i.pinimg.com/236x/5a/ae/fc/5aaefce2692fc8f97a28f28395c51f26--rock-album-covers-bon-scott.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/25/96/81/2596815592f58d1926132951747c228b--rolling-stones-album-covers-the-rolling-stones.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/65/82/ad/6582ad1cf458b71f32a25a933717157f--neil-young-gold-rush.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/5a/ae/fc/5aaefce2692fc8f97a28f28395c51f26--rock-album-covers-bon-scott.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/25/96/81/2596815592f58d1926132951747c228b--rolling-stones-album-covers-the-rolling-stones.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/65/82/ad/6582ad1cf458b71f32a25a933717157f--neil-young-gold-rush.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/5a/ae/fc/5aaefce2692fc8f97a28f28395c51f26--rock-album-covers-bon-scott.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/25/96/81/2596815592f58d1926132951747c228b--rolling-stones-album-covers-the-rolling-stones.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/65/82/ad/6582ad1cf458b71f32a25a933717157f--neil-young-gold-rush.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/5a/ae/fc/5aaefce2692fc8f97a28f28395c51f26--rock-album-covers-bon-scott.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/25/96/81/2596815592f58d1926132951747c228b--rolling-stones-album-covers-the-rolling-stones.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/65/82/ad/6582ad1cf458b71f32a25a933717157f--neil-young-gold-rush.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/5a/ae/fc/5aaefce2692fc8f97a28f28395c51f26--rock-album-covers-bon-scott.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/25/96/81/2596815592f58d1926132951747c228b--rolling-stones-album-covers-the-rolling-stones.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/65/82/ad/6582ad1cf458b71f32a25a933717157f--neil-young-gold-rush.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/5a/ae/fc/5aaefce2692fc8f97a28f28395c51f26--rock-album-covers-bon-scott.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/25/96/81/2596815592f58d1926132951747c228b--rolling-stones-album-covers-the-rolling-stones.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {src: "https://i.pinimg.com/236x/65/82/ad/6582ad1cf458b71f32a25a933717157f--neil-young-gold-rush.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"}

                ]
            }
        }
    }
</script>

<style scoped>

</style>