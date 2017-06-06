import {Component, OnInit, OnChanges} from '@angular/core';
import {MoodModel} from './mood.model';
import {MoodsService} from './inputs.service';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import { RefreshSharedService} from './inputs.shared.service';


@Component({
    selector: 'fetch-mood',
    template: `
    <h4>Moods in Database:</h4>
    <ul>
      <!-- use the ng2 structure directive to build a list of change-->
      
      <li *ngFor="let mood of moods | async">{{mood | json}}</li>
      
    </ul>
  `,
    styles: [``]
})
export class FetchMoodComponent implements OnInit, OnChanges{
    private moods : Observable<MoodModel[]>;
    private refresh: boolean ;
    constructor(private _moodsService : MoodsService, private _refreshSharedService: RefreshSharedService) {
        // subscribe the observable stream
        this._refreshSharedService.needUpdate$.subscribe(
            data => {
                console.log('Fetch Component received from sibling/parent: ' + data);
                this.refresh = data;
                // reload
                this.reload();
            });
    }

    ngOnInit(): void {
        this.reload()

    }

    // this method is nessary to receive the changes
    ngOnChanges(): void {
    }

    reload() :void {
        this.moods = this._moodsService.getMoods().catch(
            error => {
                console.log(error);
                // the observable of empty MoodModel[]
                return Observable.of<MoodModel[]>([]);
            }
        );
    }
}
