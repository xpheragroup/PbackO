from odoo import api, fields, models

class Cycle(models.Model):

    _name = 'overwrite_mrp.cycle'
    _description = 'Cylce defined by the client'

    name = fields.Integer(string='Ciclo')