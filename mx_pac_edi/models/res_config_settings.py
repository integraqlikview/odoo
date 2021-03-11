# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # == PAC web-services ==
    mx_pac_edi_pac = fields.Selection(
        related='company_id.mx_pac_edi_pac', readonly=False,
        string='MX PAC*')
    mx_pac_edi_pac_test_env = fields.Boolean(
        related='company_id.mx_pac_edi_pac_test_env', readonly=False,
        string='MX PAC test environment*')
    mx_pac_edi_pac_username = fields.Char(
        related='company_id.mx_pac_edi_pac_username', readonly=False,
        string='MX PAC username*')
    mx_pac_edi_pac_password = fields.Char(
        related='company_id.mx_pac_edi_pac_password', readonly=False,
        string='MX PAC password*')
    mx_pac_edi_certificate_ids = fields.Many2many(
        related='company_id.mx_pac_edi_certificate_ids', readonly=False,
        string='MX Certificates*')

    # == CFDI EDI ==
    mx_pac_edi_fiscal_regime = fields.Selection(
        related='company_id.mx_pac_edi_fiscal_regime', readonly=False,
        string="Fiscal Regime",
        help="It is used to fill Mexican XML CFDI required field "
        "Comprobante.Emisor.RegimenFiscal.")
