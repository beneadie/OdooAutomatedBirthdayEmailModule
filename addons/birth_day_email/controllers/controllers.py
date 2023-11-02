# -*- coding: utf-8 -*-
# from odoo import http


# class BirthDayEmail(http.Controller):
#     @http.route('/birth_day_email/birth_day_email', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/birth_day_email/birth_day_email/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('birth_day_email.listing', {
#             'root': '/birth_day_email/birth_day_email',
#             'objects': http.request.env['birth_day_email.birth_day_email'].search([]),
#         })

#     @http.route('/birth_day_email/birth_day_email/objects/<model("birth_day_email.birth_day_email"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('birth_day_email.object', {
#             'object': obj
#         })
