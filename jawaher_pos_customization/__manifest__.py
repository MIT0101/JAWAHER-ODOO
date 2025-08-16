{
    'name': "Jwawaher POS Customization",
    'version': '18.0.0.0',
    'category': 'Point of Sale',
    'summary': "Module contains customization for Point of Sale in Odoo",
    'description': """ 

        Show Product Sale Price on POS in odoo,
        Show Product Barcode Text on POS in odoo,
        
        Those options can be enabled|disabled for each company in POS configuration.

    """,
    "author": "@JAWAHER/M.Al-Mustafa",
    "website": "http://jawaher.co/",
    'depends': ['base', 'point_of_sale'],
    'data': [
        'views/pos_config.xml',
    ],
    'assets': {
    },
    'license': 'OPL-1',
    "auto_install": False,
    "installable": True,
}
