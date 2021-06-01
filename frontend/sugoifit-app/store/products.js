import { userService, productService } from '../services';
// import { userServ } from '../plugins/addService';
const user = localStorage.getItem('busID');

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
    }, 

    DELETE_PRODUCTS(state, id){
        let products = state.products;
        const index = products.indexOf((x) => x.id == id);
        products.splice(index, 1);

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
    deleteProduct({dispatch, commit}, id){
        this.$productService.deleteProduct(id)
        .then(res=>{
            dispatch('alert/info', 'Product Deleted', {root:true});
            setTimeout( function(){
                dispatch('alert/clear', {root:true});
            },10);
            commit('DELETE_PRODUCTS', res.data);
        })

    },
    displayProducts({ commit }) {
        this.$productService.showProducts()
        .then(res => {
            console.log('from store', res);
            commit('SET_PRODUCTS', res);
           
            },
            error => {
                dispatch('alert/error', error, { root: true });
            }
        );
    }
   
}

export const getters = {
    allProducts(state){
        return state.products
    }
}

  