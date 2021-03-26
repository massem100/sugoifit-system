export default async function ({ axios, context }){
 try{
     let path = csrf;
     const csrf = await $axios.$get(`/api/${path}`)
     $axios.setHeader('X-CSRF-Token', csrf)
     console.log(csrf);
 } catch (error){
     console.log('There is an error.. fix me')
 }
}

