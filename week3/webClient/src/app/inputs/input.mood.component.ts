import { Component, Input } from '@angular/core';
import {MoodModel} from './mood.model';

@Component({
    selector: 'input-mood',
    template: `
    <h4>Moods History:</h4>
    <ul>
      <!-- use the ng2 structure directive to build a list of change-->
      <li *ngFor="let mood of moods">{{mood | json}}</li>
    </ul>
  `,
    styles: [``]
})
export class InputMoodComponent {
    // Define the property, which can be bind from the parent component
    // with Input property
    @Input() moods: MoodModel[];
}
