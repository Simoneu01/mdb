import axios from 'axios';
const API_URL = 'https://api.themoviedb.org';
import config from "./config"

export class tmdbAPIService{
    constructor(){
    }
    // API Film
    searchFilm(name) {
        const url = `${API_URL}/3/search/movie?api_key=${config.TMDb_API_KEY}&language=it-IT&query=${name}&page=1&include_adult=false`;
        return axios.get(url).then(response => response.data);
    }

    // API Film
    getFilm(id) {
        const url = `${API_URL}/3/movie/${id}?api_key=${config.TMDb_API_KEY}&language=it-IT`;
        return axios.get(url).then(response => response.data);
    }

    // API Cast Film
    getCastFilm(id){
        const url = `${API_URL}/3/movie/${id}/credits?api_key=${config.TMDb_API_KEY}`;
        return axios.get(url).then(response => response.data);
    }

}