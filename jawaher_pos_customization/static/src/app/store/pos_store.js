/** @odoo-module **/
import {patch} from "@web/core/utils/patch";
import {PosStore} from "@point_of_sale/app/store/pos_store";

console.log("PosStore patching started...");

patch(PosStore.prototype, {
    cashierHasPriceControlRights() {
        const hasPriceControlOrigin = super.cashierHasPriceControlRights(...arguments);
        const isDisabled = this.isPriceChangeDisabled();
        const isRestrictedOld = this._super.config.restrict_price_control;
        const rtn = hasPriceControlOrigin && !isDisabled;
        console.log("Original hasPriceControlOrigin:", hasPriceControlOrigin);
        console.log("isRestrictedOld:", isRestrictedOld);
        console.log("isDisabled:", isDisabled);
        console.log("Final result:", rtn);
        console.log("Current Config:", this.config);
        return rtn;
    },

    isPriceChangeDisabled() {
        return this._super.config.disable_price_change_to_all_users;
    }

});
