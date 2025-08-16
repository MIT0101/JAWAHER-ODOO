/** @odoo-module **/

import {patch} from "@web/core/utils/patch";
import {ProductCard} from "@point_of_sale/app/generic_components/product_card/product_card";

// Patch ProductCard to add new prop
patch(ProductCard, {
    props: {
        ...ProductCard.props,   // keep existing props
        salePrice: {type: Number | String, optional: true},
        barcodeText: {type: Boolean | String, optional: true},
    },
});