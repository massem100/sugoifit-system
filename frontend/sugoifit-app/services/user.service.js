// import config from 'config';
// import axios from 'axios'
export class userService  {
    constructor ($axios) {
        this.$axios = $axios;
      }
    
        
        
    login(form_data){
        let PATH_API = 'auth/login';
        return this.$axios(
            {url: `/api/${PATH_API}`,data: form_data,
            method: "POST",
            headers:{'Content-Type': 'application/json', },
            }).then(res =>{
                return res.data;
            }).then (res => {
                if (res.success["0"].message){
                    this.alert_message = res.success["0"].message;
                    let userid = res.success["0"].userid;
                    let jwt_token = res.success["0"].token;
                    let user_role = res.success["0"].user_role["0"].role_name;
                    console.log(res.success["0"].user_role);
                    let busID = res.success["0"].busID;
                    localStorage.setItem("token", jwt_token);
                    localStorage.setItem("userid", userid);
                    localStorage.setItem("user_role",user_role);

                    localStorage.setItem("busID", busID);
                    console.info("Token generated and added to localStorage.");    
                }
                return res.success;
            });
        }
    logout() {
        // remove user from local storage to log user out
        let PATH_API = 'auth/logout';
        return this.$axios.get(`/api/${PATH_API}`, {
            headers: {
            'contentType': 'application/json',
            }
            })
            .then(res => {
                return res.data;
            }).then(res => {
                return res;
            });
        
        
    };
    resetLogin(){
        localStorage.removeItem('userid');
        localStorage.removeItem('token');
        localStorage.removeItem('busID');
        localStorage.removeItem('user_role');
    };

    async nca_show(){
        this.$store.dispatch('transaction_forms/noncurrentasset', {root:true});
        const submit = await this.$refs['nca_modal'].show();
          
    };
      async ca_show()  {
        this.$store.dispatch('transaction_forms/currentasset', {root:true});
        const submit = await this.$refs['ca_modal'].show();
      };
      async cliab_show()  {
        this.$store.dispatch('transaction_forms/currentliab');
        const submit = await this.$refs['cliab_modal'].show();
      };
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