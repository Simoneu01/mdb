<template>
        <div class="flex-center position-ref full-height">
            <div class="content">
                <div class="title">
                   404 Be right back.
                </div>
                <div>
                    <router-link to="/">
                        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Torna alla Home</button>
                    </router-link>
                </div>
            </div>
        </div>
</template>

<script>
    export default {
        name: "NotFound"
    }
</script>

<style scoped>
     html, body {
         background-color: #fff;
         color: #636b6f;
         font-family: 'Raleway', sans-serif;
         font-weight: 100;
         height: 100vh;
         margin: 0;
     }

    .full-height {
        height: 100vh;
    }

    .flex-center {
        align-items: center;
        display: flex;
        justify-content: center;
    }

    .position-ref {
        position: relative;
    }

    .content {
        text-align: center;
    }

    .title {
        font-size: 84px;
    }
</style>