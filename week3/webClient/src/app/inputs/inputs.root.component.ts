import { Component } from '@angular/core';
import * as moment from 'moment';
// https://momentjs.com/docs/
// timestamp testing with https://www.epochconverter.com/
import {MoodModel} from './mood.model';
import {MoodsService} from './inputs.service';
import {Http, Response} from '@angular/http';

@Component({
    selector: 'inputs-root',
    templateUrl: './inputs.root.component.html',
    styles: [`
       md-input-container {
         background: #A796A7;
       }
    `]
})
export class InputsRootComponent {
    private packageName : string = "Input Module";
    private moods : MoodModel[] = [];
    private responseMessage : string = null;
    private responseMessageColor : string = null;


    constructor(private _moodService: MoodsService) {

    }

    private mood : string = "";
    cacheData() {
        // moment format can be found https://momentjs.com/docs/#/displaying/
        let now = moment().format('dddd, MMMM Do YYYY, h:mm:ss a');
        let nowTimeStamp = moment().utc().valueOf();
        let currentMood = new MoodModel(nowTimeStamp, this.mood.toUpperCase());
        console.log("currentDateString: ", now);
        console.log("currentUTCtimestamp: ", currentMood.timestamp);
        console.log("call service: ", currentMood.mood);
        this.moods.push(currentMood);
    }
    sendData() {
        this._moodService.sendMoods(this.moods).subscribe(
            response => this.handleResponse(response),
            error => this.handleResponse(error)
        );
    }

    handleResponse(response: Response) {
        if (response.ok) {
            this.responseMessage = response.text();
            this.responseMessageColor = 'lawngreen';
        } else {
            this.responseMessage = response.text();
            this.responseMessageColor = 'red';
        }
    }
}