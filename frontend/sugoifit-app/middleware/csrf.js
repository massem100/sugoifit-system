export default async function ({ $axios, context }){
 try{
     const csrf = await $axios.$get('/api/csrf')
     $axios.setHeader('X-CSRF-Token', csrf)
     console.log(csrf);
 } catch (error){
     console.log('There is an error.. fix me')
 }
}



