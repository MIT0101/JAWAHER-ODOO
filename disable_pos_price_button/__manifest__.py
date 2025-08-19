{
    'name': "Disable POS Price Button",
    'version': '18.0.0.0',
    'category': 'Point of Sale',
    'summary': "Module used to disable the price button in POS",
    'description': """ 
      This module is used to disable the price button in POS.
      after installing this module, the price button will be disabled in the POS interface.
    """,
    "author": "@JAWAHER/M.Al-Mustafa",
    "website": "http://jawaher.co/",
    'depends': ['base', 'point_of_sale'],
    'data': [
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'disable_pos_price_button/static/src/app/store/pos_store.js',
        ],
    },
    'license': 'OPL-1',
    "auto_install": False,
    "installable": True,
}
