import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Film from './views/Film.vue'
import Libri from "./views/Libri";
import Musica from "./views/Musica";

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            alias: '/home',
            name: 'Home',
            component: Home
        },
        {
            path: '/film',
            name: 'Film',
            component: Film
        },
        {
            path: '/musica',
            name: 'Musica',
            component: Musica
        },
        {
            path: '/libri',
            name: 'Libri',
            component: Libri
        }
    ]
})