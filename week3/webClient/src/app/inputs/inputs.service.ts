import {Injectable} from '@angular/core';
import {MoodModel} from './mood.model';
import {Http, Response, Headers, RequestOptions} from '@angular/http';
import {Observable} from 'rxjs';
import 'rxjs/add/operator/map';
// import he map operator

@Injectable()
export class MoodsService {
    API_URL_GET : string = "api/moods/get/";
    API_URL_POST: string = "api/moods/post/";
    // get the http provider as private variable
    constructor(private http: Http) {
    }
    getMoods(): Observable<MoodModel[]> {
        let headers = new Headers({'Content-Type': 'application/json'});
        let options = new RequestOptions({headers: headers});
        let body = {
            seed:  "seedToChange"
        };
        // the wrapper object from the responsebody has the property name moods, which is an Array
        return this.http.post(this.API_URL_GET, body, options).map(
            response => response.json().moods as MoodModel[]
        );
    }

    sendMoods(moods : MoodModel[]): Observable<Response> {
       // construct a request header, for json content
       let headers = new Headers({'Content-Type': 'application/json'});
       let options = new RequestOptions({headers: headers});
       let body = {
            seed:  "seedToChange",
            moods: moods
       };
       return this.http.post(this.API_URL_POST, body, options);
    }
}