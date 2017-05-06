import { Component } from '@angular/core';
import * as moment from 'moment';
import {MoodModel} from './mood.model';
// https://momentjs.com/docs/
// timestamp testing with https://www.epochconverter.com/

@Component({
    selector: 'inputs-root',
    templateUrl: './inputs.root.component.html',
    styles: [``]
})
export class InputsRootComponent {
    private packageName : string = "Input Module";

    private mood : string = "";
    sendData() {
        // moment format can be found https://momentjs.com/docs/#/displaying/
        let now = moment().format('dddd, MMMM Do YYYY, h:mm:ss a');
        let nowTimeStamp = moment().utc().valueOf();
        let currentMood = new MoodModel(nowTimeStamp, this.mood);
        console.log("currentDateString: ", now);
        console.log("currentUTCtimestamp: ", currentMood.timestamp);
        console.log("call service: ", currentMood.mood);

    }
}