import { NgModule } from '@angular/core';
import { BrowserModule }  from '@angular/platform-browser';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';
import {InputsRootComponent} from './inputs.root.component';

@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule
    ],
    exports: [
        InputsRootComponent // the component in sub-module shall be exported
    ],
    declarations: [
        InputsRootComponent
    ],
    bootstrap: [InputsRootComponent]
})
export class AppInputsModule {

}