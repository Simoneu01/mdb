import axios from 'axios';
const API_URL = 'http://ws.audioscrobbler.com/2.0/';
const lastFM_APIKEY = process.env.lastFM_APIKEY;

export class lastfmAPIService{
    constructor(){
    }
    // API Film
    searchFilm(name) {
        const url = `${API_URL}/2.0/?method=track.search&track=${name}&api_key=${lastFM_APIKEY}&format=json`;
        return axios.get(url).then(response => response.data);
    }

}