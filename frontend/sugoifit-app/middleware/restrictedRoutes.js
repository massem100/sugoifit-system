export default async function ({context, app}){
    try {
        // redirect to login page if not logged in and trying to access a restricted page
    const { authorize } = to.meta;
    const currentUser = this.$userService.user;

    if (authorize) {
        if (!currentUser) {
            // not logged in so redirect to login page with the return url
            window.onNuxtReady(() => { window.$nuxt.$router.push('/auth/login')})
        }

        // check if route is restricted by role
        if (authorize.length && !authorize.includes(localStorage.getItem("user_role"))) {
            // role not authorised so redirect to home page
            window.onNuxtReady(() => { window.$nuxt.$router.push('/')})
        }
    }
    } catch (error) {
        console.log(error);
        
    }
    
}