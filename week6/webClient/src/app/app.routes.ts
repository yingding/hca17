import {Routes, RouterModule} from '@angular/router';

import {HomeComponent} from './home';
import {AboutComponent} from './about';
import {ExampleComponent} from './examples';
import {ChartsRootComponent} from './charts';

export const routes: Routes = [
    {path: '', component: HomeComponent, pathMatch: 'full'},
    {path: 'example', component: ExampleComponent},
    {path: 'about', component: AboutComponent},
    {path: 'charts', component: ChartsRootComponent}
];

// add useHash is true to enable HashLocationStrategy
export const routing = RouterModule.forRoot(routes, {useHash: true});