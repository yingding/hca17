import { Component } from '@angular/core';
import {InputMoodComponent} from './input.mood.component';
import {FetchMoodComponent} from './input.fetch.component';

@Component({
    selector: 'inputs-root',
    templateUrl: './inputs.root.component.html',
    styles: [``]
})
export class InputsRootComponent {
    private packageName : string = "Input Module";
    constructor() {
    }
}