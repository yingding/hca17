/**
 * Created by yingding on 04.04.17.
 */
import { Component } from '@angular/core';
import '../assets/css/styles.css';
@Component({
    selector: 'app',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent {
    onClick() {
        var message : string = "Your setup works fine!";
        alert(message);
    }
}
