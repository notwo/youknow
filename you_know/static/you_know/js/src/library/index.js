"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const vue_1 = require("vue");
const app_vue_1 = __importDefault(require("./app.vue"));
const app = (0, vue_1.createApp)(app_vue_1.default);
app.mount('#app');
