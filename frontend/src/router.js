import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Film from './views/Film/index.vue'
import Libri from "./views/Libri/index";
import Musica from "./views/Musica/index";
import Container from "./components/Container"
import {APIService} from './APIService';
const apiService = new APIService();

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            component: Container,
            children: [
                {
                    path: '',
                    component: Home,
                    alias: 'home'
                },
                // Film will be rendered inside Container's <router-view>
                // when /film is matched
                {
                    path: 'film',
                    component: Film
                },
                // Libri will be rendered inside Container's <router-view>
                // when /film is matched
                {
                    path: 'libri',
                    component: Libri
                },
                // Musica will be rendered inside Container's <router-view>
                // when /film is matched
                {
                    path: 'musica',
                    component: Musica
                },
                // Film add / view
                {
                    path: 'film/add',
                    component: () => import('./views/Film/add')
                },
                {
                    path: 'film/:id',
                    component: () => import('./views/Film/view'),
                    beforeEnter: (to, from, next) => {

                        function isValid (id) {
                            console.log("QUI")
                            return apiService.getFilm(id, (err) => {
                                if (err) {
                                    next({ name: 'not-found' });
                                } else {
                                    next();
                                }
                            })
                        }

                        isValid(to.params.id);
                    }
                },
                {
                    path: 'film/:id/edit',
                    component: () => import('./views/Film/edit'),
                    beforeEnter: (to, from, next) => {

                        function isValid (id) {
                            console.log("QUI")
                            return apiService.getFilm(id, (err) => {
                                if (err) {
                                    next({ name: 'not-found' });
                                } else {
                                    next();
                                }
                            })
                        }

                        isValid(to.params.id);
                    }
                },
                // Musica add / view
                {
                    path: 'musica/add',
                    component: () => import('./views/Musica/add')
                },
                {
                    path: 'musica/:id',
                    component: () => import('./views/Musica/view'),
                    beforeEnter: (to, from, next) => {

                        function isValid (id) {
                            return apiService.getCanzone(id, (err) => {
                                if (err) {
                                    next({ name: 'not-found' });
                                } else {
                                    next();
                                }
                            })
                        }

                        isValid(to.params.id);
                    }
                },
                // Libri add / view
                {
                    path: 'libri/add',
                    component: () => import('./views/Libri/add')
                },
                {
                    path: 'libri/:id',
                    component: () => import('./views/Libri/view'),
                    beforeEnter: (to, from, next) => {

                        function isValid (id) {
                            return apiService.getLibro(id, (err) => {
                                if (err) {
                                    next({ name: 'not-found' });
                                } else {
                                    next();
                                }
                            })
                        }

                        isValid(to.params.id);
                    }
                }
            ]
        },
        {
            path: '/404',
            component: () => import('./views/404'),
            name: '404'
        },
        {
            path: '*',
            component: () => import('./views/404'),
            name: 'not-found'
        }
    ]
})