import { Component } from '@angular/core';
import * as moment from 'moment';
import {MoodModel} from './mood.model';
import {MoodsService} from './inputs.service';
// https://momentjs.com/docs/
// timestamp testing with https://www.epochconverter.com/

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
        this._moodService.sendMoods(this.moods);
    }
}