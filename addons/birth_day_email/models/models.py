# -*- coding: utf-8 -*-

from odoo import models, fields

class HrEmployeeCustom(models.Model):
     _inherit = 'hr.employee'
     _name = 'hr.employee.custom'

     def send_birthday_messages(self):
          today = fields.Date.today()
          today_day_month = today.strftime('%d-%m')

          birthday_message_sent = fields.Boolean(
               string='Birthday Message Sent',
               help="Indicates whether a birthday message has been sent to this employee."
          )


          employees = self.search([
               ('birthday', 'like', today_day_month),
               ('birthday_message_sent', '=', False)
               ])

          for employee in employees:
               self.send_birthday_email(employee)

     def send_birthday_email(self, employee):

          mail_template = self.env.ref('birth_day_email.bdayemail')  # Replace with your actual email template
          if mail_template:
               mail_template.send_mail(employee.id, force_send=True)
               employee.write({'birthday_message_sent': True})
