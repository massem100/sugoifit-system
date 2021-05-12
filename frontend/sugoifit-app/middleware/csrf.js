export default async function ({ $axios, context }){
 try {

    const csrf = await $axios.$get(`/api/csrf`)
    $axios.setHeader('X-CSRF-Token', csrf);
    
 } catch (error){
     console.log(error)
 }
}
