# -*- coding: utf-8 -*-
from odoo import http

# class GduPrueba3(http.Controller):
#     @http.route('/gdu_prueba3/gdu_prueba3/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gdu_prueba3/gdu_prueba3/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gdu_prueba3.listing', {
#             'root': '/gdu_prueba3/gdu_prueba3',
#             'objects': http.request.env['gdu_prueba3.gdu_prueba3'].search([]),
#         })

#     @http.route('/gdu_prueba3/gdu_prueba3/objects/<model("gdu_prueba3.gdu_prueba3"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gdu_prueba3.object', {
#             'object': obj
#         })