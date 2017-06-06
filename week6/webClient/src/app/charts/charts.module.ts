import { NgModule } from '@angular/core';
import { BrowserModule }  from '@angular/platform-browser';
import { FormsModule} from '@angular/forms';
import { HttpModule} from '@angular/http';
import { MdButtonModule, MdCheckboxModule, MdInputModule } from '@angular/material';
import {ChartsRootComponent} from './charts.root.component';
import {ChartsService} from './charts.service';
import {LineChartComponent} from './line.chart.component';
import {ChartModule} from 'angular2-highcharts';
import {SpiderChartComponent} from './spider.chart.component';
import {PieChartComponent} from './pie.chart.component';
import {ColumnBarChartComponent} from './bar.drilldown.component';
import {ScatterPlotComponent} from './scatter.plot.component';
import {Scatter3DComponent} from './scatter.3d.component';

@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        MdInputModule,
        MdButtonModule,
        ChartModule.forRoot(
            require('highcharts'),
            require('highcharts-more'), // this will be needed for polar spider chart.
            require('highcharts/modules/exporting'), // needed for exporing
            require('highcharts/modules/offline-exporting'), // needed for exporting without export server
            require('highcharts/modules/data'), // needed for column bar drilldown
            require('highcharts/modules/drilldown'), // needed for column bar drilldown
            require('highcharts-3d') // needed for 3d scatter
        ) // get the module global highcharts
    ],
    exports: [
        ChartsRootComponent // the component in sub-module shall be exported
    ],
    declarations: [
        ChartsRootComponent,
        LineChartComponent,
        SpiderChartComponent,
        PieChartComponent,
        ColumnBarChartComponent,
        ScatterPlotComponent,
        Scatter3DComponent,
    ],
    providers: [
        ChartsService
    ],
    bootstrap: [ChartsRootComponent]
})
export class AppChartsModule {
}