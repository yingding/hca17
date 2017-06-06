/**
 * Created by yingding on 04.04.17.
 */
import { Component } from '@angular/core';
import '../assets/css/styles.css';
@Component({
    selector: 'my-app',
    templateUrl: './app.component.root.html',
    styleUrls: ['./app.component.root.scss']
})
export class AppComponentRoot {
    projectName : string = "DemoTemplate";

    onClick() {
        var message : string = "Your setup works fine!";
        alert(message);
    }
    // don't do things in the constructor, use onInit instead
    constructor() {}


}
