# -*- coding: utf-8 -*-
from odoo import http


class PosTraining(http.Controller):
    @http.route('/pos_training/pos_training', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/pos_training/pos_training/objects', auth='public')
    def list(self, **kw):
        return http.request.render('pos_training.listing', {
            'root': '/pos_training/pos_training',
            'objects': http.request.env['pos_training.pos_training'].search([]),
        })

    @http.route('/pos_training/pos_training/objects/<model("pos_training.pos_training"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('pos_training.object', {
            'object': obj
        })
