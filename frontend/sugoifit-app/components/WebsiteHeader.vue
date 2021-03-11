<template>
    <header class="header">
        <h6 class="title"><i class="fas fa-leaf"></i>Monique's Boutique</h6>
        <ul>
            <li>
                <nuxt-link to='/products'>All Products</nuxt-link>
            </li>
            <li>
                <nuxt-link to='/faq'>FAQ</nuxt-link>
            </li>
            <li>
                <nuxt-link to='/contact'>Contact</nuxt-link>
            </li>
            <li>
                <nuxt-link to='/placeorder'>Place an Order</nuxt-link>
            </li>
        </ul>

    </header>
</template>

<script>
export default {
    name: 'WebsiteHeader'
}
</script>

<style scoped>

.header{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    padding-bottom: 1rem;
}
.header .title{
    font-size: 2rem;
    color:black;
}
.header ul{
    list-style: none;
    display: flex;
}
.header a{
    display: inline-block;
    color: black;
    padding: 0.3rem 1rem;
    margin-right: 0.5rem;
}
</style>