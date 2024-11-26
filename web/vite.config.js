import {defineConfig} from "vite";
import vuePlugin from "@vitejs/plugin-vue";
import vuetify from "vite-plugin-vuetify";

export default defineConfig({
    base: './',
    plugins: [vuePlugin(), vuetify()]
})