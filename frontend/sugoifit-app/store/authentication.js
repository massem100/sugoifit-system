import { userService } from '../services';
// import { userServ } from '../plugins/addService';
const user = localStorage.getItem('userid');
const initialState = user
    ? { status: { loggedIn: true }, user }
    : { status: {}, user: null };

export const state = () => ({
    initialState
    
})

export const mutations = {
    loginRequest(state, user) {
        state.status = { loggingIn: true };
        state.user = user;
    },
    loginSuccess(state, user) {
        state.status = { loggedIn: true };
        state.user = user;
    },
    loginFailure(state) {
        state.status = {};
        state.user = null;
    },
    logout(state) {
        state.status = {};
        state.user = null;
    },
    reset(state) {
        state.status = {};
        state.user = null;
    }

}

export const actions = {
    login({ dispatch, commit }, { form_data }) {
        commit('loginRequest', form_data.email);
        this.$userService.login(form_data)
            .then(
                res=> {
                   
                        dispatch('alert/success', 'User logged in successfully.',{root:true});
                    setTimeout( function(){
                        dispatch('alert/clear');
                    },10);
                    
                    commit('loginSuccess', res["0"].userid);
                    
                },
                error => {
                    commit('loginFailure', error);
                    dispatch('alert/error', error, { root: true });
                }
            );
    },
    logout({dispatch, commit }) {
        this.$userService.logout()
        .then(
            res => {
                commit('logout');
                setTimeout(function(){
                    $nuxt.$router.push('/auth/login');
                }, 1000);
            },
            error => {
                dispatch('alert/error', error, { root: true });
            }
        );
      
    },
    reset({dispatch, commit}) {
        this.$userService.resetLogin();
        commit('reset');
    }
}

export const getters = {}

  