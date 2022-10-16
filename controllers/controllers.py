# -*- coding: utf-8 -*-
# from odoo import http


# class GestionIcs(http.Controller):
#     @http.route('/gestion_ics/gestion_ics/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_ics/gestion_ics/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_ics.listing', {
#             'root': '/gestion_ics/gestion_ics',
#             'objects': http.request.env['gestion_ics.gestion_ics'].search([]),
#         })

#     @http.route('/gestion_ics/gestion_ics/objects/<model("gestion_ics.gestion_ics"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_ics.object', {
#             'object': obj
#         })
