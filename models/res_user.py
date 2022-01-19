# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)
class ResUser(models.Model):
    _inherit = ['res.users']
    #uno = fields.Char(string="uno")