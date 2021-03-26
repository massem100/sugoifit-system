

export default async function ({ $axios, context }){
 try {
    
    const csrf = await $axios.$get(`/api/csrf`)
    $axios.setHeader('X-CSRF-Token', csrf)
    // $axios.defaults.headers.common['X-CSRFTOKEN'] = csrf;
    console.log(csrf);
 } catch (error){
     console.log(error)
 }
}
