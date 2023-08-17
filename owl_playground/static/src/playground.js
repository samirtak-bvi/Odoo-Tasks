/** @odoo-module **/

// import { Component } from "@odoo/owl";

// export class Playground extends Component {
//     static template = "owl_playground.playground";
// }

// class Counter extends Component {
//     static template = "my_module.Counter";
// }

const { useState, Component } = owl;

class Counter extends Component {
  static template = xml`
    <button t-on-click="increment">
        Click Me! [<t t-esc="state.value"/>]
    </button>`;

  state = useState({ value: 0 });

  increment() {
    this.state.value++;
  }
}