from odoo import models, fields,api

class Inherit(models.Model):
    _inherit = 'stock.picking'
    
    volume = fields.Float(string="Max volume (m3))")
