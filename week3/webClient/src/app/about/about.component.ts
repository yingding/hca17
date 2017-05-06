
import {Component, OnInit, OnDestroy} from '@angular/core';

@Component({
    selector: 'about',
    templateUrl: './about.component.html'
})
export class AboutComponent implements OnInit, OnDestroy {
    public projectName: string;
    constructor() {
        this.projectName = 'Demo';
    }

    ngOnInit() { console.log('About::ngOnInit'); }
    ngOnDestroy() { console.log('About::ngOnDestroy'); }
}
