export default async function authHeader({$axios,context }) {
    // return authorization header with jwt token
    try {
        let user = await localStorage.getItem('userid');
        let token =  await localStorage.getItem('token');
        
        if (user && token) {
            $axios.setHeader('Authorization', 'Bearer' +' '+ token);
        }
    } catch (error) {
        console.log(error);
        
    }
   
}