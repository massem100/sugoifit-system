<template>
  <div >
      <header class="header">
            <nuxt-link to='/website/website'>
                <h6 class="title">Monique's Boutique</h6>
            </nuxt-link>
            <ul>
                <li>
                    <nuxt-link to='/website/products'>All Products</nuxt-link>
                </li>
                <li>
                    <nuxt-link to='/website/faq'>FAQ</nuxt-link>
                </li>
                <li>
                    <nuxt-link to='/website/contact'>Contact</nuxt-link>
                </li>
                <li>
                    <nuxt-link to='/website/placeorder'>Place an Order</nuxt-link>
                </li>
            </ul>
        </header>
        <nuxt />
  </div>
</template>
<script>
export default {
   
}
</script>
<style lang="scss">
 
.header{
    overflow: hidden;
    padding: 20px 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    padding-bottom: 1rem;
}
.header .title{
    margin-left: 2em;
    font-size: 2rem;
    color:black;
}
.header ul{
    list-style: none;
    display: flex;
}
.header a{
    color: black;
    padding: 0.3rem 1rem;
    margin-right: 0.5rem;
    float: left;
    text-align: center;
    text-decoration: none;
    font-size: 18px; 
    line-height: 25px;
    border-radius: 4px;
}
.header a:hover {
  background-color: #ddd;
  color: black;
}

</style>
