import axios from 'axios';
const API_URL = 'https://www.googleapis.com/books/v1';

export class gbookAPIService{
    constructor(){
    }
    // API Books
    searchBook(name) {
        const url = `${API_URL}/volumes?q=${name}&printType=books`;
        return axios.get(url).then(response => response.data);
    }

    getBook(id){
        // https://www.googleapis.com/books/v1/volumes/lnGEEb7IqdsC
        const url = `${API_URL}/volumes/${id}`;
        return axios.get(url).then(response => response.data);
    }

    // https://books.google.com/books/content/images/frontcover/lnGEEb7IqdsC?fife=w500-h700
}