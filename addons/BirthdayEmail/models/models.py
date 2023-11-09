# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrEmployeeBirthday(models.Model):
     #_inherit = 'hr.employee'
     _name = 'hr.employee.custom'
     _description = 'Birthday Messages'

     category_ids = fields.Many2many('employee.custom',string='Tags')

     birthday_message_sent = fields.Boolean(
          string='birthday_message_sent',
          help="Indicates whether a birthday message has been sent to this employee."
     )
     birthday = fields.Date(string='birthday')
     name = fields.Char(string="Name", required=True)

     @api.model
     def find_birthdays(self):
          today = fields.Date.today()
          today_day_month = today.strftime('%d-%m')


          employees = self.search([
               ('birthday', 'like', today_day_month),
               ('birthday_message_sent', '=', False)
               ])

          for employee in employees:
               self.send_birthday_email(employee)
          # reset to False for next birthday
          for employee in employees:
               employee.write({'birthday_message_sent': False})

     def send_birthday_email(self, employee):
          mail_template = self.ref('birth_day_email.bdayemail')
          if mail_template:
               mail_template.send_mail(employee.id, force_send=True, email_values={
                'email_from': employee.company_id.email,
                'email_to': employee.work_email,
                'object': employee,
            })
               employee.write({'birthday_message_sent': True})
