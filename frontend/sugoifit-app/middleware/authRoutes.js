export default async function ({context, app}){
    try {
        // Redirects pages to login if user is not authenticated.
        let currentPathObject = window.$nuxt.$router.currentRoute;  
        let route_path = String(currentPathObject.path);
        // console.log(route_path);
        
        // Add routes to pages that are public, e.g the website for customers
        // there will pose a issue of specifying exact route when using params.. explore _slug
        const publicPages =  ['/auth/register', '/auth/login'];
        const authRequired = !publicPages.includes(route_path);
        const loggedIn =  localStorage.getItem('userid');
    
        if (authRequired && !loggedIn) {
            window.onNuxtReady(() => { window.$nuxt.$router.push('/auth/login')})
        }
                
    } catch (error) {
        console.log(error);
    
    }
}
