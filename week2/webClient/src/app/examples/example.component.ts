
import {Component} from '@angular/core';

@Component({
    selector: 'example',
    template: `
<div>
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
