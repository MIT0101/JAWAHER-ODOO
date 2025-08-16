from odoo import fields, models, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_show_product_sale_price = fields.Boolean(related='pos_config_id.pos_show_product_sale_price', readonly=False)
    pos_show_product_barcode_text = fields.Boolean(related='pos_config_id.pos_show_product_barcode_text', readonly=False)
