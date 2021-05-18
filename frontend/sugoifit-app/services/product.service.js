
export class productService  {
    constructor ($axios) {
        this.$axios = $axios;
    }
    showProducts() {
        let busID = localStorage.getItem('busID');
        return this.$axios.get(`/api/${busID}/products`)
        .then(res => {
            return res.data;
        })
        /*let PATH_API = 'products';
        return this.$axios({
            url: `/api/${PATH_API}`,
            method: "GET",
            headers:{'Content-Type': 'application/json', },
        }).then(res =>{
            return res.data;
        })*/
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
            if (res.success["0"].message){
                this.alert_message = res.success["0"].message;   
            }
            return res.success;
        });
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