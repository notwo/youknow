"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const vue_1 = __importDefault(require("vue"));
exports.default = vue_1.default.extend({
    methods: {
        onClick(event) {
            var _a;
            console.log((_a = event.target.parentElement) === null || _a === void 0 ? void 0 : _a.getElementsByTagName("input"));
        },
    },
});
const vue_2 = require("vue");
const App_vue_1 = __importDefault(require("./App.vue"));
const app = (0, vue_2.createApp)(App_vue_1.default);
app.mount('#app');
