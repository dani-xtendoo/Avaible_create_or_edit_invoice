# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _
from odoo.http import request


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    #logged_user = fields.Char(String="logged User", compute="_is_authorized_user()")

    logged_user = fields.Char("User ID", default=lambda self: self.env.user.name, stored="False")