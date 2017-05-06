
import {Component} from '@angular/core';
import {} from 'AppInputsModule';

@Component({
    selector: 'example',
    template: `
<div>
    <p>You are visiting {{componentName}}.</p>
    <binding-parent></binding-parent>
</div>
<!-- the input module is imported in appModule -->
<inputs-root></inputs-root>`
})
export class ExampleComponent {
    public componentName: string;
    constructor() {
        this.componentName = 'Example Component';
    }
}
