import { userService } from '../services';
// import { userServ } from '../plugins/addService';
const user = localStorage.getItem('busid');

export const state = () => ({
    products: []
    
})

export const mutations = {
    
    reset(state) {
        state.products = [];
        state.user = null;
    },
    addFailure(state) {
        state.products = [];
        state.user = null;
    },
    SET_PRODUCTS(state, products){
        state.products = products;
    },
    ADD_PRODUCTS(state, products){
        state.products.push({...products});
    }

}

export const actions = {
    addProduct({ dispatch, commit }, { form_data }) {
        this.$productService.addProduct(form_data)
            .then(res=> {
                   
                        dispatch('alert/success', 'Product added successfully.',{root:true});
                    setTimeout( function(){
                        dispatch('alert/clear');
                    },10);
                    commit('ADD_PRODUCTS', res.data);
                    
                },
                error => {
                    //commit('loginFailure', error);
                    dispatch('alert/error', error, { root: true });
                }
            );
    },
    displayProducts({ commit }) {
        this.$productService.showProducts()
        .then(res => {
            commit('SET_PRODUCTS', res);
            },
            error => {
                dispatch('alert/error', error, { root: true });
            }
        );
    }
   
}

export const getters = {
    allproducts(state){
        return state.products
    }
}

  