import { createStore } from 'vuex'

export default createStore({
    state: {
        profile: null
    },
    getters: {
        isAuthenticated: state => !!state.profile
    },
    mutations: {
    },
    actions: {
    },
    modules: {
    }
})