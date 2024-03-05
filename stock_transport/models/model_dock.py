from odoo import fields, models


class ModelDock(models.Model):
    _name = "model.dock"
    _description = "Dock"

    name = fields.Char("Name", required=True)
    