from odoo import models, fields,api

class Inherit(models.Model):
    _inherit = 'stock.picking'
    shipping_volume = fields.Float(compute="_compute_volume" ,string="Volume for shipping")
    shipping_weight = fields.Float(compute="_compute_weight" ,string="Weight for shipping")

    @api.depends('product_id.weight', 'product_id.volume','move_line_ids.quantity')
    def _compute_weight(self):
        for record in self:
            current_weight = 0
            for move_id in record.move_ids:
                current_weight = current_weight + move_id.product_qty*move_id.product_id.weight
            print('asdkfjsadlfjskfdjsdkfjdkfjlksddkasjfdksfjkdsjfksdjfksdjfksdjfkjdkfjkdjfkjdfj')
            print(current_weight)
            record.shipping_weight= current_weight


    @api.depends('product_id.weight', 'product_id.volume','move_line_ids.quantity')
    def _compute_volume(self):
        for record in self:
            current_volume = 0
            for move_id in record.move_ids:
                current_volume = current_volume + move_id.product_qty*move_id.product_id.volume
            print('asdkfjsadlfjskfdjsdkfjdkfjlksddkasjfdksfjkdsjfksdjfksdjfksdjfkjdkfjkdjfkjdfj')
            print(current_volume)
            record.shipping_volume= current_volume