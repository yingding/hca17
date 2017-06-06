
import {Component} from '@angular/core';
import {} from 'AppInputsModule';

@Component({
    selector: 'example',
    template: `
<div>
    <!-- the input module is imported in appModule -->
    <inputs-root></inputs-root>
    <p>You are visiting {{componentName}}.</p>
    <binding-parent></binding-parent>
</div>`
})
export class ExampleComponent {
    public componentName: string;
    constructor() {
        this.componentName = 'Example Component';
    }
}
