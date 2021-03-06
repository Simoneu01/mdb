import axios from 'axios';
import config from "./config";
const API_URL = 'http://ws.audioscrobbler.com/';

export class lastfmAPIService{
    constructor(){
    }
    // API Search Track
    searchTrack(track,artist) {
        const url = `${API_URL}2.0/?method=track.search&track=${track}&artist=${artist}&api_key=${config.lastFM_APIKEY}&format=json`;
        return axios.get(url).then(response => response.data);
    }

    // API GET Track
    getTrack(id) {
        const url = `${API_URL}2.0/?method=track.getInfo&api_key=${config.lastFM_APIKEY}&mbid=${id}&format=json`;
        return axios.get(url).then(response => response.data);
    }

    getTrackbyName(track,artist) {
        const url = `${API_URL}2.0/?method=track.getInfo&api_key=${config.lastFM_APIKEY}&artist=${artist}&track=${track}&format=json`;
        return axios.get(url).then(response => response.data);
    }

    getArtistbyName(artist){
        // /2.0/?method=artist.getinfo&artist=Cher&api_key=YOUR_API_KEY&format=json
        const url = `${API_URL}2.0/?method=artist.getTopAlbums&api_key=${config.lastFM_APIKEY}&artist=${artist}&format=json`;
        return axios.get(url).then(response => response.data);
    }

    getArtist(id){
        // /2.0/?method=artist.getinfo&artist=Cher&api_key=YOUR_API_KEY&format=json
        const url = `${API_URL}2.0/?method=artist.getTopAlbums&api_key=${config.lastFM_APIKEY}&mbid=${id}&format=json`;
        return axios.get(url).then(response => response.data);
    }

}