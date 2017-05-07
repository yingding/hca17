import { Injectable } from '@angular/core';
import { Subject }    from 'rxjs/Subject';


@Injectable()
export class RefreshSharedService {
    // Observable string sources
    private needUpdate = new Subject<boolean>();
    // a switch

    // Observable boolean streams
    needUpdate$ = this.needUpdate.asObservable();

    // Service message commands
    publishData(data: boolean) {
        this.needUpdate.next(data);
    }
}
