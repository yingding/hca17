import {Injectable} from '@angular/core';
import {MoodModel} from './mood.model';
import {Http, Response, Headers, RequestOptions} from '@angular/http';
import {Observable} from 'rxjs';

@Injectable()
export class MoodsService {
    API_URL : string = "api/moods/";
    // get the http provider as private variable
    constructor(private http: Http) {
    }
    getMoods(): void {

    }
    sendMoods(moods : MoodModel[]): Observable<Response> {
       // construct a request header, for json content
       let headers = new Headers({'Content-Type': 'application/json'});
       let options = new RequestOptions({headers: headers});

       return this.http.post(this.API_URL, moods, options);
    }
}