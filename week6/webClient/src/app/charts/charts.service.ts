import {Injectable} from '@angular/core';
import {Http, Response, Headers, RequestOptions} from '@angular/http';
import {Observable} from 'rxjs';
import 'rxjs/add/operator/map';
// import he map operator

@Injectable()
export class ChartsService {
    API_URL_GET : string = "api/moods/get/";
    API_URL_POST: string = "api/moods/post/";
    // get the http provider as private variable
    constructor(private http: Http) {
    }

}