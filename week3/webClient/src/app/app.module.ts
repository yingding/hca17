/**
 * Created by yingding on 04.04.17.
 */
import { NgModule } from '@angular/core';
import { BrowserModule }  from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { AppComponentRoot } from './app.component.root';
import {routing} from './app.routes';
import {HomeComponent} from './home/home.component';
import {AboutComponent} from './about/about.component';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';
import {NavBarComponent} from './navbar.component';
import {ExampleComponent, BindingChildComponent, BindingParentComponent} from './examples';

/*
 * import submodules, all the exported components in submodule,
 * can be used directly, by calling the selectors.
 */
import {AppInputsModule} from './inputs';

@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        routing,
        HttpModule,
        AppInputsModule // app inputs sub modules
    ],
    declarations: [
        AppComponent,
        AppComponentRoot,
        HomeComponent,
        AboutComponent,
        NavBarComponent,
        ExampleComponent,
        BindingChildComponent,
        BindingParentComponent
    ],
    bootstrap: [ AppComponentRoot ]
})
export class AppModule { }
