export const state= () => ({
    type: null

})

export const mutations = { 
    noncurrentasset(state, type){
        state.type = 'NCA';
    },
    currentasset(state, type){
        state.type = 'CA';
    },
    currentliab(state, type){
        state.type = 'Cliab';
    },
    longtermliab(state, type){
        state.type = 'LTliab';
    },
    revenue(state, type){
        state.type = 'REV';
    },
    expense(state, type){
        state.type = 'EXP';
    },
    equity(state, type){
        state.type = 'SE';
    },
}

export const actions =  { 
    noncurrentasset({commit}){
        commit('noncurrentasset');
    },
    currentasset({commit}){
        commit('currentasset');
    },
    currentliab({commit}){
        commit('currentliab');
    },
    longtermliab({commit}){
        commit('longtermliab');
    },
    revenue({commit}){
        commit('revenue');
    },
    expense({commit}){
        commit('expense');
    },
    equity({commit}){
        commit('equity');
    },
}

export const getters =  { 
    formType: state => {
        return state.type
    }

}