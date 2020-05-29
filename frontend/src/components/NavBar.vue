<template>
    <div class="w-full sticky top-0 py-4 px-6 flex items-center justify-between bg-black">
        <!-- Navigation Button -->
        <div class="flex items-center">
            <button class="focus:outline-none rounded-full bg-black w-8 h-8 mr-3 text-white opacity-75 hover:opacity-100">
                <font-awesome-icon @click="goBack" class="text-xl" icon="arrow-left"/>
            </button>
            <button class="focus:outline-none rounded-full bg-black w-8 h-8 text-white opacity-75 hover:opacity-100">
                <font-awesome-icon @click="goForward" class="text-xl" icon="arrow-right"/>
            </button>

        </div>
        <!-- Userprofile -->
        <div class="relative">
            <button @click="showDropdown = true" class="focus:outline-none bg-light rounded-full py-1 px-2 flex items-center text-white">
                <img src="https://pbs.twimg.com/profile_images/1055263632861343745/vIqzOHXj.jpg" class="rounded-full h-6 w-6 mr-2" alt="profile-pic.jpg">
                <p class="text-white font-semibold mr-3">{{nome}}</p>
                <font-awesome-icon v-if="showDropdown === false" icon="caret-down"/>
                <font-awesome-icon v-if="showDropdown === true" icon="caret-up"/>
            </button>
            <div v-if="showDropdown === true" class="absolute bg-light w-full rounded mt-1">
                <router-link to="/account">
                    <button @click="showDropdown = false" class="focus:outline-none w-full py-2 text-lightest hover text-white border-b border-light opacity-75 hover:opacity-100">Account</button>
                </router-link>
               <!-- <button @click="showDropdown = false" class="focus:outline-none w-full py-2 text-lightest hover text-white border-b border-white opacity-75 hover:opacity-100">Settings</button>
                <button @click="showDropdown = false" class="focus:outline-none w-full py-2 text-lightest hover text-white border-b border-light opacity-75 hover:opacity-100">Log Out</button>-->
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "NavBar",
        data: function () {
            return {
                showDropdown: false,
            }
        },
        computed:{
            nome(){
                return this.$store.getters.getName
            },
        },
        methods: {
            goBack(){
                this.$router.go(-1)
            },
            goForward(){
                this.$router.go(1)
            }
        }
    }
</script>

<style scoped>
div.sticky{
    z-index: 9999
}
</style>