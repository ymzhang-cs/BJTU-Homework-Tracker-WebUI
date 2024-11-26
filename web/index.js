import App from "./src/App.vue";
import {createApp} from "vue";
import {createVuetify} from "vuetify";
import "vuetify/styles";
import "@mdi/font/css/materialdesignicons.css"

const vuetify = createVuetify({
    icons: {
        defaultSet: "mdi"
    }
});

createApp(App).use(vuetify).mount("#app")
