/** @odoo-module **/
import rpc from 'web.rpc'
import publicWidget from "web.public.widget"
import core from 'web.core'

var Qweb = core.qweb

publicWidget.registry.CustomForm = publicWidget.Widget.extend({
    selector: '#wrapwrap',
    events: {
        'click #submit': function (e) {
            e.preventDefault();
            const element = this.$el
            var name = element.find('#name')[0]
            var job = element.find('#selector')[0]
            var query = element.find('#help')[0]
            var modal = element.find('#myModal')[0]
            var title = element.find('.modal-title')[0]
            var body = element.find('.modal-body')[0]
            var button = element.find('#button')[0]

            modal.style.display = 'block'
            this._rpc({
                route: '/register',
                params: { name: name.value, job: job.value, query: query.value }
            }).then((data) => {
                title.innerHTML = data.title
                body.innerHTML = data.msg
                if (data.btn) {
                    button.innerHTML = "Login"
                    console.log(button)
                    button.onclick = function () {
                        window.location = 'http://localhost:8069/web/login';
                        modal.style.display = 'none'

                    }
                }
                else {
                    button.onclick = function () {
                        name.innerHTML = ''
                        modal.innerHTML = ''
                        modal.style.display = 'none'
                    }
                }
            })


        },
        'click .close': function (e) {
            var modal = this.$el.find('#myModal')[0]
            modal.style.display = 'none'
        }
    }
})


// const btn = document.getElementById('submit').addEventListener("click", async function(event){
//     event.preventDefault()
//     console.log("Clicked")
//     console.log(rpc)
//     const a = await rpc.query({
//         model: 'customer.submission',
//         method: 'create',
//         args :[{'name': "Samir", 'job': "oashda", 'query': "asiydsgaiasuhdiashhsaohdaihidhsi"}] 
//     })
//     console.log(a)
//   });
