
export class productService  {
    constructor ($axios) {
        this.$axios = $axios;
    }
    showProducts() {
        let busID = localStorage.getItem('busID');
        return this.$axios.get(`/api/${busID}/products`)
        .then(res => {
            let products = res.data;
            console.log('from service-product.js', products);
            return products;
           
        })
       
    }
    addProduct(form_data) {
        let busID = localStorage.getItem('busID');
        return this.$axios({
            url: `/api/${busID}/products`, data: form_data,
            method: "POST",
            headers:{'Content-Type': 'application/json', },
        }).then(res =>{
            return res.data;
        }).then (res => {
            if (res.message){
                this.alert_message = res.message;   
            }
            return res.success;
        });
    }
    deleteProduct(id){
        let busID = localStorage.getItem('busID'); 
        return this.$axios({
            url: `/api/${busID}/products/${id}`,
            method: "DELETE", 
            headers:{'Content-Type': 'application/json', },
        }).then(res => {
            return res.data;
        }).then(res => {
            if (res.message){
                return res.message
            }
        })
    }
    handleResponse(response) {
        return response.text().then(text => {
            const data = text && JSON.parse(text);
            if (!response.ok) {
                if (response.status === 401) {
                    // auto logout if 401 response returned from api
                    logout();
                    location.reload();
                }
    
                const error = (data && data.message) || response.statusText;
                return Promise.reject(error);
            }
    
            return data;
        });
    }
};