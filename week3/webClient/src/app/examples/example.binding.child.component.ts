import { Component, Input, OnChanges, SimpleChange } from '@angular/core';
@Component({
    selector: 'child-component',
    template: `
    <h3>New Text is {{childText}}.</h3>
    <h3>New Number is {{childNumber}}</h3>
    <h4>Change log:</h4>
    <ul>
      <!-- use the ng2 structure directive to build a list of change-->
      <li *ngFor="let changeItem of changeLogList">{{changeItem}}</li>
    </ul>
  `
})
export class BindingChildComponent implements OnChanges {
    // Define the property, which can be bind from the parent component
    // with Input property
    @Input() childText: String;
    @Input() childNumber: number;
    @Input() clearLog: boolean;
    // String Array to stage the changes triggered from parent component
    changeLogList: string[] = [];
    // ngOnChanges
    ngOnChanges(changes: {[propKey: string]: SimpleChange}) {
        // show the changes structure in console
        console.log(changes);

        let log: string[] = [];
        let needClear: boolean = false;
        for (let propertyName in changes) {
            if (propertyName == "clearLog") {
                // set the clear flag
                needClear = true;

            } else {
                let changedProp = changes[propertyName];
                let to = JSON.stringify(changedProp.currentValue);
                if (changedProp.isFirstChange()) {
                    log.push(`Initial value of ${propertyName} set to ${to}`);
                } else {
                    let from = JSON.stringify(changedProp.previousValue);
                    log.push(`${propertyName} changed from ${from} to ${to}`);
                }
            }
        }
        // concat multiply changes in log to one string and push as a new log
        // to the global changeLogList
        if (!needClear) {
            this.changeLogList.push(log.join(', '));
        } else {
            //clear
            this.changeLogList = [];
        }
    }
}
