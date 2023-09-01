/** @odoo-module **/

import { Component, useState, useRef, useSubEnv, onPatched, xmlrpc } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { ActionSwiper } from "@web/core/action_swiper/action_swiper";
import { useService } from "@web/core/utils/hooks";
import { Domain } from "@web/core/domain";
import { getDefaultConfig } from "@web/views/view";

class A extends Component {
    setup() {
        console.log("HELLO")
    }
}

class B extends Component {
    setup() {
        console.log("OLLEH")
    }
}

class Button extends Component {
    setup() {
        this.bt = useRef("bt");
    }
    yo() {
        console.log(this.bt)
    }
}

class None extends Component {
    setup() {

        this.btn = useRef("btnel");
        this.inp = useRef("inpData");
        this.options = useState(['Done', 'Not Done'])
        this.todo = useState({ todoList: [{ id: 1, description: 'Buy Something', done: this.options[0] }, { id: 2, description: 'Buy Other Thing', done: this.options[1] }] })
    }
    status(e, item) {

        // console.log(e)

        if (item.done == this.options[0]) {
            e.target.className = "btn btn-danger"
            item.done = this.options[1];
        }
        else {
            e.target.className = "btn btn-success"
            item.done = this.options[0];
        }
        console.log(item)
        console.log(e)
    }

    add() {

        if (this.inp.el.value!=""){
        this.todo.todoList.push({
            id: this.todo.todoList.length + 1,
            description: this.inp.el.value,
            done: this.options[1]
        })  
    }

        
    }

    delete(item) {
        let arr = this.todo.todoList;
        let index = arr.indexOf(item);
        if (index > -1) {
            arr.splice(index, 1);
        }
        console.log(this.todo.todoList)
    }

    pointer(e){
        console.log(e);
        e.target.style.cursor = 'pointer';
    }
}

class Root extends Component {
    select = useRef("selection");
    setup() {
        this.count = useState({ num: 0, bool: false, component: None, selection: "" })
        this.action = useService("action");
    }

    selector() {
        if (this.count.selection == "A") {
            console.log(this.env._t);
            this.count.component = A
        }

        if (this.count.selection == "B") {
            this.count.component = B
        }

        if (this.count.selection == "") {
            this.count.component = None
        }
    }
    increment() {
        this.count.num++;
    }
    openOrders(title, domain) {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: title,
            res_model: "estate.property",
            domain: [['postcode', '=', '123'], ['estate', '=', '352']],
            // domain: domain,
            views: [
                [false, "kanban"],
                [false, "form"],
            ],
        });
    }

    openLast7DaysOrders() {
        const domain = "[('postcode', '=', '123'), ('estate', '=', '352')]"
        // "[('date_availabilty','<=', (context_today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d'))]";

        this.openOrders(this.env._t("Last 7 days orders", domain));
        console.log(new Domain(domain).toList())
    }
}

Root.components = { A, B, None, Button };
Root.template = "estate.clientaction";
A.template = "A";
B.template = "B";
Button.template = "ButtonCom";
None.template = "None";
None.components = { Button };

registry.category("actions").add("estate.dashboard", Root);
