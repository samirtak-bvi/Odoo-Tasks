from odoo import http
from odoo.http import request, route

class OwlPlayground(http.Controller):
    @http.route(['/owl_playground/playground'], type='http', auth='public')
    def show_playground(self):
        print('helllllllppppppp')
        """
        Renders the owl playground page
        """
        return request.render('owl_playground.playground')


# class CounterModel(http.Controller):
#     @http.route(['/counter'], type='http', auth='public')
#     def show_counter(self):
#         print('helllooo')

#         return request.render('my_module.Counter')


