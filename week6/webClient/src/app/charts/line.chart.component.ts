import { Component } from '@angular/core';


@Component({
    selector: 'line-chart',
    template:`    
    <chart [options]="options"></chart>
   `, 
   styles: [``]
})
export class LineChartComponent {
    private ComponentName : string = "Line Chart";
    options : Object;
    constructor() {
        this.options = {
            title : { text : 'simple line chart'},
            credits: {
                enabled: false
            },
            series: [
                {
                  data: [29.9, 71.5, 106.4, 129.2, 50, 76, 13],
                },
                {
                    data: [50, 76, 13, 29.9, 71.5, 106.4, 129.2, 111],
                }
            ]
        }
    }
}