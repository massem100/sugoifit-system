export default async function authHeader({$axios,context }) {
    // return authorization header with jwt token
    try {
        let user = localStorage.getItem('userid');
        let token =  localStorage.getItem('token');
        
        if (user && token) {
            $axios.setHeader('Authorization', 'Bearer' +' '+ token);
        }
    } catch (error) {
        console.log(error);
        
    }
   
}