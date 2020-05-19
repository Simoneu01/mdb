import axios from 'axios';
const API_URL = 'http://localhost:8000';
export class APIService{

    constructor(){
    }
    // API Film
    getFilms() {
        const url = `${API_URL}/api/film/`;
        return axios.get(url).then(response => response.data);
    }

    getFilm(pk, cb) {
        const url = `${API_URL}/api/film/${pk}`;
        axios.get(url)
            .then(response =>
                cb(null, response.data)
            )
            .catch(error =>
                cb(new Error(error.message))
            );
    }
    // API Canzoni
    getCanzoni() {
        const url = `${API_URL}/api/canzone/`;
        return axios.get(url).then(response => response.data);
    }

    getCanzone(pk) {
        const url = `${API_URL}/api/canzone/${pk}`;
        return axios.get(url).then(response => response.data);
    }

    // API Libri
    getLibri() {
        const url = `${API_URL}/api/libro/`;
        return axios.get(url).then(response => response.data);
    }

    getLibro(pk) {
        const url = `${API_URL}/api/libro/${pk}`;
        return axios.get(url).then(response => response.data);
    }

}