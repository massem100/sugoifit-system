export default async function( {$axios, context}) {
    try {
        const csrf = await $axios.$get('http://localhost:8080/api/csrf')
        $axios.setHeader('X-CSRF-Token', csrf)
        console.log(csrf)
    }
    catch (error) {}
}