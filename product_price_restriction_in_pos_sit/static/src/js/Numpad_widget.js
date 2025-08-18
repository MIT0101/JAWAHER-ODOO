/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { user } from "@web/core/user";


patch(PosStore.prototype, {

    async cashierHasPriceControlRights() {
        const hasGroup = await user.hasGroup('product_price_restriction_in_pos_sit.product_price_restriction_in_pos');
        if (hasGroup) {
            const button = document.querySelector('.numpad-price');
            if (button) {
                button.setAttribute('disabled', true);
                button.style.background = "#c7c7c7";
                button.style.color = "#a5a1a1";
                button.style.cursor = "not-allowed";
            }
        }

        // Call the original method
        return super.cashierHasPriceControlRights(...arguments);
    }
});
