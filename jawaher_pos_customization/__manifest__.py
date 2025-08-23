{
    'name': "Jawaher POS Customization",
    'version': '18.0.0.0',
    'category': 'Point of Sale',
    'summary': "Module contains customization for Point of Sale in Odoo",
    'description': """ 
        ## Features
        - Show Product Sale Price on POS product screen.
        - Show Product Barcode Text on POS product screen.
        
        ## Enabling the Features
        Features can be enabled from the POS configuration settings:
        1. Activate single company before starting.
        2. Go to Point of Sale > Press on edit action on your sale point (3 dots on sale point card).
        3. Click on  "More settings: Configurations > Settings" link.
        4. Enable "Show Product Sale Price" and/or "Show Product Barcode Text" options (check the boxes).
        5. Save the changes.
        After enabling the features, refresh the POS page to see the changes.
    """,
    "author": "@JAWAHER/M.Al-Mustafa",
    "website": "http://jawaher.co/",
    'depends': ['base', 'product', 'point_of_sale'],
    'data': [
        'views/pos_config.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'jawaher_pos_customization/static/src/app/generic_components/product_card/product_card.js',
            'jawaher_pos_customization/static/src/app/generic_components/product_card/product_card.xml',
            'jawaher_pos_customization/static/src/app/screens/product_screen/product_screen.xml',

        ],
    },
    'license': 'OPL-1',
    "auto_install": False,
    "installable": True,
}
