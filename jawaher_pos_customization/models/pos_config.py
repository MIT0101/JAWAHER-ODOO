from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    show_product_sale_price = fields.Boolean(string="Show Product Price")
    show_product_barcode_text = fields.Boolean(string="Show Product Barcode Text")
