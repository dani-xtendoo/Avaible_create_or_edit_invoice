# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _
from odoo.http import request


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    def _is_authorized_user(self):

        if self.env.user != '':

            user_athorizhed= self.env.user

            return user_athorizhed
        return 'Dani'

    #logged_user = fields.Char(String="logged User", compute="_is_authorized_user()")

    logged_user = fields.Char("User ID",default=lambda self: self._uid, stored="False")