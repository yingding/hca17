import { Component } from '@angular/core';
@Component({
    selector: 'binding-parent',
    template: `    
    <h2>Parent to Child Component Binding Example</h2>
    <button (click)="newNumber()">increase a number</button>
    <input type="text" [(ngModel)]="textToChange">
    <button (click)="toClearLog()">Clear Log</button>
    <!-- use the selector defined in BindingChildComponent -->
    <child-component [childText]="textToChange" [childNumber]="numberToChange" [clearLog]="clearLog"></child-component>`,
    styles: [``]
})
export class BindingParentComponent {
    textToChange : string = "init text";
    numberToChange : number = 1;
    clearLog : boolean = true;

    newNumber() {
        this.numberToChange++;
    }
    toClearLog() {
        // just switch to make changes happend
        this.clearLog = !this.clearLog;
    }
}
