# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
from datetime import date,datetime, timedelta
from odoo.addons import decimal_precision as dp
from odoo.tools import float_compare, pycompat, config
import logging
from odoo.exceptions import UserError, RedirectWarning, ValidationError,Warning
logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    ship_via = fields.Many2one(string='Ship Via',comodel_name='shipping.carrier')
    ship_to_street = fields.Char(string="Street")
    ship_to_street2 = fields.Char(string="Street 2")
    ship_to_city = fields.Char(string="City")
    ship_to_zip = fields.Char(string="Zip")
    ship_to_country_id = fields.Many2one('res.country', string="Country")
    ship_to_state_id = fields.Many2one('res.country.state', string="State", domain="[('country_id', '=?', ship_to_country_id)]")
    
    
    @api.onchange('sale_id')
    def onchange_sale_id(self):
        for each in self:
            if each.sale_id:
                each.ship_via= each.sale_id.ship_via.id
                each.ship_to_street = each.sale_id.street
                each.ship_to_street2 = each.sale_id.street2
                each.ship_to_city = each.sale_id.city
                each.ship_to_zip = each.sale_id.zip
                each.ship_to_state_id = each.sale_id.state_id.id
                each.ship_to_country_id = each.sale_id.country_id.id
                
                
                