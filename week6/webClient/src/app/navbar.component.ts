import {Component} from '@angular/core';

@Component({
    selector: 'navbar',
    // Example of using a inline Style
    template: `
    <nav class="sidebar" [ngClass]="{sidebarePushRight: isActive}">
      <ul class="list-group">
        <li>
          <a class="list-group-item" routerLink="" routerLinkActive="active" [routerLinkActiveOptions]="{exact: true}">Home</a>
        </li>
        <li>
          <a class="list-group-item" routerLink="example" routerLinkActive="active">Examples</a>
        </li>
        <li>
          <a class="list-group-item" routerLink="about" routerLinkActive="active">About</a>
         </li>
         <li>
          <a class="list-group-item" routerLink="charts" routerLinkActive="active">Charts</a>
         </li>
      </ul>
    </nav>
  `,
  styleUrls: ['./navbar.component.scss']
  //   styles: [`
  //   nav ul {
  //     list-style-type: none;
  //     margin: 1em 0;
  //     padding: 0 1em;
  //     border-top: 1px solid #069;
  //     border-bottom: 1px solid #069;
  //   }
  //   nav li {
  //     display: inline-block;
  //     padding: 0;
  //   }
  //   nav a {
  //     color: #069;
  //     text-decoration: none;
  //     padding: 0.5em;
  //     display: inline-block;
  //   }
  //   nav .active {
  //     background-color: #069;
  //     color: #fff;
  //   }
  // `]
})
export class NavBarComponent {}