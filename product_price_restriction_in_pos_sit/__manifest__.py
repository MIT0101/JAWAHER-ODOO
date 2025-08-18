# -*- coding: utf-8 -*-
{
    'name': 'Product Price Restriction In POS',
    'summary': 'Product Price Restriction In POS',
    'description': """
         module is designed to enforce strict access controls over price adjustments in your Odoo Point of Sale system.
""",
    'depends': ["base", "point_of_sale"],
    'data': [
        'security/security_groups.xml',
    ],
    'category': 'Point of Sale',
    "version": "18.0.1.0.0",
    'license': u'OPL-1',
    'author': 'Silent Infotech Pvt. Ltd. , Updated by @JAWAHER/M.Al-Mustafa',
    'website': 'https://silentinfotech.com',
    "price": 20.00,
    "currency": "USD",
    "images": ['static/description/banner.gif'],
    'assets': {
        'point_of_sale._assets_pos': [
            'product_price_restriction_in_pos_sit/static/src/js/**/*',
            'product_price_restriction_in_pos_sit/static/src/xml/systray.xml',
        ],
    },
}
