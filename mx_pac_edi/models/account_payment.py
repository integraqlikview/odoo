# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    mx_pac_edi_force_generate_cfdi = fields.Boolean(string='Generate CFDI')

    def mx_pac_edi_update_sat_status(self):
        return self.move_id.mx_pac_edi_update_sat_status()

    def action_mx_pac_edi_force_generate_cfdi(self):
        self.mx_pac_edi_force_generate_cfdi = True
        self.move_id._update_payments_edi_documents()
