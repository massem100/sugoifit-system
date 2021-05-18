export const state = () => ({
    type: null,
    message: null
})

export const mutations = {
    success(state, message) {
        state.type = 'alert-success';
        state.message = message;
    },
    info (state, message) {
        state. type = 'alert-info';
        state.message = message;
    },
    warning(state, message) {
        state.type = 'alert-warning';
        state.message = message;
    },
    error(state, message) {
        state.type = 'alert-danger';
        state.message = message;
    },
    clear(state) {
        state.type = null;
        state.message = null;
    }
}

export const actions = {
    success({ commit }, message) {
        commit('success', message);
    },

    info({commit}, message){
        commit('info', message)
    },
    warning({commit}, message){
        commit('warning', message)
    },
    error({ commit }, message) {
        commit('error', message);
    },
    clear({ commit }) {
        commit('clear');
    }
}

export const getters = {}
