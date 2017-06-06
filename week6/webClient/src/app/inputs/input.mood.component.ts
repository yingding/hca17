import { Component, Input } from '@angular/core';
import {MoodModel} from './mood.model';
import * as moment from 'moment';
import {MoodsService} from './inputs.service';
import {RefreshSharedService} from './inputs.shared.service';
import {Response} from '@angular/http';
// https://momentjs.com/docs/
// timestamp testing with https://www.epochconverter.com/

@Component({
    selector: 'input-mood',
    template: `
    <md-input-container>
      <!-- use # to make ng2 referable to this input element -->
      <input #moodInput mdInput [(ngModel)]="mood" (keydown.enter)="cacheData(moodInput)" placeholder="Enter your mood">
    </md-input-container>
    <button md-raised-button (click)="sendData()">Submit</button>
    <!-- print out the input history -->
    <span *ngIf="responseMessage!=null" [style.background-color]="responseMessageColor">{{responseMessage}}</span>
    
    <!-- print out the input history -->
    <h4>Moods History:</h4>
    <ul>
      <!-- use the ng2 structure directive to build a list of change-->
      <li *ngFor="let mood of moods">{{mood | json}}</li>
    </ul>
  `,
    styles: [`
       md-input-container {
         background: #A796A7;
       }
    `]
})
export class InputMoodComponent {
    private moods : MoodModel[] = [];
    private responseMessage : string = null;
    private responseMessageColor : string = null;
    private refresh : boolean = false;

    constructor(private _moodService: MoodsService, private _refreshSharedService: RefreshSharedService) {
    }

    private mood : string = "";
    cacheData(inputElement : HTMLInputElement) {
        // moment format can be found https://momentjs.com/docs/#/displaying/
        let now = moment().format('dddd, MMMM Do YYYY, h:mm:ss a');
        let nowTimeStamp = moment().utc().valueOf();
        let currentMood = new MoodModel(nowTimeStamp, this.mood.toUpperCase());
        console.log("currentDateString: ", now);
        console.log("currentUTCtimestamp: ", currentMood.timestamp);
        console.log("call service: ", currentMood.mood);
        this.moods.push(currentMood);
        inputElement.value = null; // clean the value
    }
    sendData() {
        this._moodService.sendMoods(this.moods).subscribe(
            response => this.handleResponse(response),
            error => this.handleResponse(error)
        );
        // refresh is true
        this.refresh = !this.refresh; //switch
        this._refreshSharedService.publishData(this.refresh);
    }

    handleResponse(response: Response) {
        if (response.ok) {
            this.responseMessage = response.text();
            this.responseMessageColor = 'lawngreen';
            this.moods = []; // clear the moods
        } else {
            this.responseMessage = response.text();
            this.responseMessageColor = 'red';
        }
    }
}
