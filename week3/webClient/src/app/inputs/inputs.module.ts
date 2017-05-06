import { NgModule } from '@angular/core';
import { BrowserModule }  from '@angular/platform-browser';
import { FormsModule} from '@angular/forms';
import { HttpModule} from '@angular/http';
import { MdButtonModule, MdCheckboxModule, MdInputModule } from '@angular/material';
import { InputsRootComponent } from './inputs.root.component';
import { MoodsService} from './inputs.service';

@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        MdInputModule,
        MdButtonModule
    ],
    exports: [
        InputsRootComponent // the component in sub-module shall be exported
    ],
    declarations: [
        InputsRootComponent
    ],
    providers: [
        MoodsService
    ],
    bootstrap: [InputsRootComponent]
})
export class AppInputsModule {
}