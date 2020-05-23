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

    getFilmnoCB(pk) {
        const url = `${API_URL}/api/film/${pk}`;
        return axios.get(url).then(response => response.data)
    }

    postFilm(data, config) {
        const url = `${API_URL}/api/film/`;
        return axios.post(url, data, config)
            .then(res => res.data)
    }

    patchFilm(pk, data, config) {
        const url = `${API_URL}/api/film/${pk}/`;

        return axios.patch(url, data, config)
            .then(res => res.data)
    }

    deleteFilm(pk) {
        const url = `${API_URL}/api/film/${pk}`;
        axios.delete(url)
            .then(res => console.log(res))
            .catch(err => console.log(err, err.response));
    }

    // API Canzoni
    getCanzoni() {
        const url = `${API_URL}/api/canzone/`;
        return axios.get(url).then(response => response.data);
    }

    getCanzone(pk, cb) {
        const url = `${API_URL}/api/canzone/${pk}`;
        axios.get(url)
            .then(response =>
                cb(null, response.data)
            )
            .catch(error =>
                cb(new Error(error.message))
            );
    }

    postCanzone(data, config) {
        const url = `${API_URL}/api/canzone/`;
        console.log(data)
        return axios.post(url, data, config)
            .then(res => res.data)
    }

    deleteCanzone(pk) {
        const url = `${API_URL}/api/canzone/${pk}`;
        axios.delete(url)
            .then(res => console.log(res))
            .catch(err => console.log(err, err.response));
    }


    // API Libri
    getLibri() {
        const url = `${API_URL}/api/libro/`;
        return axios.get(url).then(response => response.data);
    }


    getLibro(pk, cb) {
        const url = `${API_URL}/api/libro/${pk}`;
        axios.get(url)
            .then(response =>
                cb(null, response.data)
            )
            .catch(error =>
                cb(new Error(error.message))
            );
    }

    postLibro(data, config) {
        const url = `${API_URL}/api/libro/`;
        console.log(data)
        return axios.post(url, data, config)
            .then(res => res.data)
    }

    deleteLibro(pk) {
        const url = `${API_URL}/api/libro/${pk}`;
        axios.delete(url)
            .then(res => console.log(res))
            .catch(err => console.log(err, err.response));
    }
}