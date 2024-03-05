from odoo import models, fields,api

class Inherit(models.Model):
    _inherit = 'stock.picking.batch'

    dock = fields.Many2one('model.dock',string="Dock")

    vehicle = fields.Many2one("fleet.vehicle","Vehicle",plceholder="Opel GJ45XC1234")

    category = fields.Many2one("fleet.vehicle.model.category",String="Category")

    category_weight = fields.Float(compute="_compute_weight",string="Weight",store=True)
    category_volume = fields.Float(compute="_compute_volume",string="Volume",store=True)

    