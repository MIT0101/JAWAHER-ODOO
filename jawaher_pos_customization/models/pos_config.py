from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    pos_show_product_sale_price = fields.Boolean(string="Show Product Price")
    pos_show_product_barcode_text = fields.Boolean(string="Show Product Barcode Text")
