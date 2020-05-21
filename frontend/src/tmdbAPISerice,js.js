import axios from 'axios';
const API_URL = 'https://api.themoviedb.org';
import TMDb_API_KEY from '../config'

export class tmdbAPIService{
    constructor(){
    }
    // API Film
    searchFilm(name) {
        const url = `${API_URL}/3/search/movie?api_key=${TMDb_API_KEY}&language=it-IT&query=${name}&page=1&include_adult=false`;
        return axios.get(url).then(response => response.data);
    }

}