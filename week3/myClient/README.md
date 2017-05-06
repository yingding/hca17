# 0. About
This tutorial is designed for quickly building a web client with Angular2 and Typescript
* Angular2 can sometimes be written as Ng2. AngularJS refers to Angular1 with Javascript. Angular2 and AngularJS are different frameworks, please be care with the notions.

* more about Angular2 Quickstart can be found unter https://github.com/angular/quickstart/blob/master/README.md

# 1. Introduction
The following section shows how to use the tool chain relating to developing web-app with Angular2. The Ng2 Version used in this tutorial is 2.4.10. The Ng2 version is defined within the "dependencies" section/attribute in package.json file.

## 1.1 (Optional) Node Package Manager (NPM)

### console in os system
* open "terminal" in macosx, linux
* open "cmd" in windows

### Update NPM in the console
* Using <code>npm install -g npm</code> to update node package manager (npm) globally.
* Using <code>npm --verison</code> or <code>npm -v</code> to display the current npm version.

### About package.json file
* Using <code>npm init</code> to create an package.json file 
* While using <code>npm install xxx --save</code> or <code>npm install xxx --save-dev</code> with <code>save</code> or <code>save-dev</code> options, the lib dependency are automatically updated in package.json file.
* Dependencies are libs necessary for the application to run, dev dependencies are libs necessary to program the application, but not necessary for running the application.
* Using <code>npm install</code> to install all packages defined in package.json 

### Initializing package.json
* <code>npm init --force</code>
* <code>npm install typings --save-dev</code>
* <code>npm install angular --save</code>

### Run script in package.json
* <code>npm run script_name</code>

### Init a tsconfig.json file
* <code>tsc --init</code>
* Using <code>tsc -w</code> to start tsc build with watch flag

### TypeScript compiler and native JavaScript libs
* TypeScript compiler needs description files x.d.ts to recognize native JavaScript files.
* For the tsc to recognize '@angular/core', a typings.json file is needed to define d.ts files for angular2 js libs.

<!--
## Difference between let and var
* More details can be found under http://stackoverflow.com/questions/762011/let-keyword-vs-var-keyword
-->

# 2. How to start?
This sections shows how can you start this demo-app after you have cloned this repo.

## 2.1 Get ready
* Installing all node_modules with <code>npm install</code>

## 2.2 Debug Ng2 Application 
* Install Chrome on your system, since Ng2 debugging only works with chrome
* Install Chrome Addon "JetBrains IDE Support 2.0.9"
* Double check the setting "Host: 127.0.0.1" and "Port: 63342", otherwise debugger will not work.
* In IntelliJ IDE -> Menu -> Run -> Edit Configurations... -> + -> JavaScript Debugger, to add a JavaScript Debugger
### 2.2.1 Settings of JavaScript/Ng2 Debugger
* Name: wp-ng2-debugger (Choose what ever you want)
* URL: http://localhost:8080/ (URL information is defined in webpack.dev.js. If needed, please adapt the URL settings for debugger according to your webpack.dev.js definition.)
* Browser: Chrome (only works with chrome)

### 2.2.2 Try out the Debugger in IntelliJ IDEA IDE
* Starting your Web-App with `npm start` in the console, so that the webpack-dev-server runs.
* Set a break point in app.component.ts, for example before line 13 `var message ...`
* (Optional) you can set multiply break points in your code to examin the behaviour (If you set your break points before `onClick()` statements, what will happen? Nothing, because you just debugger an method declaration.)
* Run the wp-ng2-debugger in IntelliJ IDE Menu->Run->Debug...->Choose wp-ng2-debugger (If prompted to choose one), a tab in chrome is open and you will see "JetBrains IDE Support is debugging this browser" 
* Click now the "Button" on the Web-App website
* Now the debugger tab in IntelliJ for Typescript is activated.
* Click on the variables View (with the burger button)
* Using the "step to next line" button in the debugger to step through your codes.

Note: For further issues with debugging with IntelliJ IDEA Utimate and Webpack, please refer https://manuel-rauber.com/2016/09/30/how-to-debug-angular-2-with-webstorm/

# Hacking Arround the Codes
* Now copy the app.component.ts to app.component.root.ts
* Change the name of the component to "AppComponentRoot", import "AppComponentRoot" in app.module.ts, add the AppComponentRoot component in the module declarations, bootstrap from the AppComponentRoot
* Copy the app.component.html and app.component.css file and rename to app.component.root.html and app.component.root.css files, update the css and html linking in app.component.root.ts
* start the webpack-dev-server with `npm start` in the console
* remove all codes in the app.component.root.html and commented out the background css style in `assets/css/styles.css`
* ... (demo the changes)


Note: if the webpack-dev-server is running and the code changes, the code changes can be viewed immediately in the browser.
 
# Home Work:
* working on the presentation 1
* finish reading the following sections 3-6 about Angular2
* **Important**: get familiar with the RxJS Examples in https://angular.io/docs/ts/latest/guide/server-communication.html , we will need these knowledge in the next session to have server and client exchange data
 
# 3. Angular2

## 3.1 Bindings 
### Property Binding
* Component Property Binding with square brackets []

### Event Binding
* Template Event Binding with parenthesis ()

### Input Decoration
* Input property with Input Decoration `@Input()`
* More about Input property can be found unter https://angular.io/docs/ts/latest/cookbook/component-communication.html#!#parent-to-child-on-changes

## Binding a component property to Angular Template
* More details about two-way binding can be found under https://angular.io/docs/ts/latest/guide/template-syntax.html
* Examples of using model bindings in form can be found under https://angular.io/docs/ts/latest/guide/forms.html
* **Note:** For two-way binding in Angular2@2.4.10, <code>import {FormsModule} from '@angular/forms';</code> is needed in your AngularModule.

## Asterisk (*) appearing before directive names
* The * is a bit of syntactic sugar that makes it easier to read and write directives that modify HTML layout with the help of templates. NgFor, NgIf, and NgSwitch all add and remove element subtrees that are wrapped in `<template>` tags.
* More about this can be found unter https://angular.io/docs/ts/latest/guide/template-syntax.html#!#star-template

## Directives
One of the defining features of a single page application is its manipulation of the DOM tree. Instead of serving a whole new page every time a user navigates, whole sections of the DOM appear and disappear according to the application state.

There are three kinds of Angular directives:
1. Components or Component Directives
2. Attribute directives 
3. Structural directives

### Components or Component Directives
The Component is really a directive with a template. It's the most common of the three directives and we write lots of them as we build our application.

### Attribute Directive
An attribute directive only changes the behavior or appearance of an element. An attribute element modifies an existing element.

For example: <pre><code>&lt;div [ngStyle]="{'background-color': element.color}"&gt;&lt;/div&gt;</code></pre>

### Structural Directive
A structural directive shows or hides an element. A structural directive changes the Document Object Model (DOM) by adding or removing an element entirely.

For example: <pre><code>&lt;div *ngIf="isAvailabe"&gt;{{element.title}} is available!&lt;/div&gt;</code></pre>

### Reactive extensions library (rxjs / RxJS)
A reactive Extension allows us to get data from a security source.

* Added in package.json
* Imported in systemjs.config.js
* More infos about RxJS can be found under https://angular.io/docs/ts/latest/guide/server-communication.html
* **Note**: Using either the .toPromise() or .map() methods from RxJS to asynchronously parse the result of the HTTP request.

For example:
```javascript
var data;
{"price": 20,"meta": "from-the-server","data": [] }

var source = getDataFromUrlOrOtherAsyncSource();
source
.filter(item => item.price > 50.60) // filter the item
    .map(item => item.data) // map item to item.data
    .subscribe( items => this.data = items // save the item.data list to data 
    );
```
* An Observable is a stream of events that we can process with array-like operators. With `toPromise()`, an Observable can be converted to a promise. A single result in the form of a promise is easy for the calling component to consume. But requests aren't always "one and done". We may start one request, then cancel it, and make a different request before the server has responded to the first request. Such a request-cancel-new-request sequence is difficult to implement with Promise. It is easy with Observalbes.  


### Cold Observable

After the http.get is called, the request is not sent out instantaneously. This means, http.get does not send the request automatically. The observable is cold which means the request won't go out until the observable is subscribed by another component.
    
### Testing HTTP Request
* http://httpbin.org/ provides some free API, which allows you to test HTTP Request and Response.

### Working with ngIf or ngSwitch
Both the ngSwitch and ngIf directives add elements to the DOM subtree only if there conditions are met. If the coditions are false, the element is not rendered in HTML at all.

# 4. Angular2 Component Lifecycle

  1. OnChanges:           Event hook called when a data-bound input property value changes
  2. OnInit:              Event hook called when the data-bound property are initialized
  3. DoCheck:             Event hook for manual checks
  4. AfterContentInit:    Event hook after content is initialized
  5. AfterContentChecked: Event hook after content is checked
  6. AfterViewInit:       Event hook after view is initialized
  7. AfterViewChecked:    Event hook after view is checked
  8. OnDestroy:           Event hook after component is disposed.

In the lifecycle of a component, the OnChanges is called first time to get the initial value of all the properties of the component class. Once the properties are set to their initial values, Oninit is called. DoCheck is than called, allowing doing a manually check of any further things...

## Component Lifecycle Hooks

Hook | Purpose | Components | Directives
--- | --- | --- | --- 
ngOnInit | Initialize the directive/component after Angular initializes the data-bound input properties. | yes | yes 
ngOnChanges | Respond after Angular sets a data-bound input property. The method receives a changes object of current and previous values. | yes | yes
ngDoCheck | Detect and act upon changes that Angular can or won't detect on its own. Called every change detection run. | yes | yes
ngOnDestroy | Cleanup just before Angular destroys the directive/component. Unsubscribe observables and detach event handlers to avoid memory leaks.| yes | yes
ngAfterContentInit | After Angular projects external content into its view.	| yes | no
ngAfterContentChecked | After Angular checks the bindings of the external content that it projected into its view. | yes | no
ngAfterViewInit	| After Angular creates the component's view(s). | yes | no
ngAfterViewChecked | After Angular checks the bindings of the component's view(s). | yes | no

# 5. Angular2 Dependency Injection
In software engineering, dependency injection is a software design pattern that implements inversion of control for resolving dependencies. A dependency is an object that can be used (a service). An injection is the passing of a dependency to a dependent object (a client) that would use it.

## 5.1 Type of Dependency Injection
* Add providers to the "root module" so that the same instance of a service is available everywhere.
* Register provider at a component level in the `providers` property of the `@Component` metadata.

## 5.2 Injector
* An injector maintains a container of service instances that it created.
* An injector can create a new service instance from a provider.
* Register provider with injectors.

Note: Registering at a component level means you get a new instance of the service with each new instance of that component.

# 6. Angular2 Modules
Modules are executed within their own scope, not in the global scope; this means that variables, functions, classes, etc. declared in a module are not visible outside the module unless they are explicitly exported using one of the export forms. Conversely, to consume a variable, function, class, interface, etc. exported from a different module, it has to be imported using one of the import forms.

Modules are declarative; the relationships between modules are specified in terms of imports and exports at the file level.

Modules import one another using a module loader. At runtime the module loader is responsible for locating and executing all dependencies of a module before executing it. Well-known modules loaders used in JavaScript are the CommonJS module loader for Node.js and require.js for Web applications.

## Import Module
* Import all members from a file as a specific variable name `import * as YourModuleIdentifier from 'path/module'`, the ModuleIdentifier can be different as the module name.


