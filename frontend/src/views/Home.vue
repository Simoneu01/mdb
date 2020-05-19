<template>
    <div>
        <Cards :dati="recents"/>
        <Cards :dati="recents"/>
    </div>

</template>

<script>
    import Cards from "../components/Cards/Cards";
    export default {
        name: "Home",
        components: {Cards},
        data(){
            return {
                recents: [
                    {id: 1,src: "https://i.pinimg.com/236x/5a/ae/fc/5aaefce2692fc8f97a28f28395c51f26--rock-album-covers-bon-scott.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 2,src: "https://i.pinimg.com/236x/25/96/81/2596815592f58d1926132951747c228b--rolling-stones-album-covers-the-rolling-stones.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 3,src: "https://i.pinimg.com/236x/65/82/ad/6582ad1cf458b71f32a25a933717157f--neil-young-gold-rush.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 4,src: "https://i.pinimg.com/236x/5a/ae/fc/5aaefce2692fc8f97a28f28395c51f26--rock-album-covers-bon-scott.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 5,src: "https://i.pinimg.com/236x/25/96/81/2596815592f58d1926132951747c228b--rolling-stones-album-covers-the-rolling-stones.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 6,src: "https://i.pinimg.com/236x/65/82/ad/6582ad1cf458b71f32a25a933717157f--neil-young-gold-rush.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 7,src: "https://i.pinimg.com/236x/5a/ae/fc/5aaefce2692fc8f97a28f28395c51f26--rock-album-covers-bon-scott.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 8,src: "https://i.pinimg.com/236x/25/96/81/2596815592f58d1926132951747c228b--rolling-stones-album-covers-the-rolling-stones.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 9,src: "https://i.pinimg.com/236x/65/82/ad/6582ad1cf458b71f32a25a933717157f--neil-young-gold-rush.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 10,src: "https://i.pinimg.com/236x/5a/ae/fc/5aaefce2692fc8f97a28f28395c51f26--rock-album-covers-bon-scott.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 11,src: "https://i.pinimg.com/236x/25/96/81/2596815592f58d1926132951747c228b--rolling-stones-album-covers-the-rolling-stones.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 12,src: "https://i.pinimg.com/236x/65/82/ad/6582ad1cf458b71f32a25a933717157f--neil-young-gold-rush.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 13,src: "https://i.pinimg.com/236x/5a/ae/fc/5aaefce2692fc8f97a28f28395c51f26--rock-album-covers-bon-scott.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 14,src: "https://i.pinimg.com/236x/25/96/81/2596815592f58d1926132951747c228b--rolling-stones-album-covers-the-rolling-stones.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 15,src: "https://i.pinimg.com/236x/65/82/ad/6582ad1cf458b71f32a25a933717157f--neil-young-gold-rush.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 16,src: "https://i.pinimg.com/236x/5a/ae/fc/5aaefce2692fc8f97a28f28395c51f26--rock-album-covers-bon-scott.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 17,src: "https://i.pinimg.com/236x/25/96/81/2596815592f58d1926132951747c228b--rolling-stones-album-covers-the-rolling-stones.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"},
                    {id: 18,src: "https://i.pinimg.com/236x/65/82/ad/6582ad1cf458b71f32a25a933717157f--neil-young-gold-rush.jpg", title: "AC/DC Let There Be Rock", artist: "Simone Ungaro"}

                ]
            }
        }
    }
</script>

<style scoped>

</style>