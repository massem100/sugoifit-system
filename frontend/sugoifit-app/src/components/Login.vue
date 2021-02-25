<template>
    <div>
         <div class = 'main-area'>
                <form>
                    <br>

                    <br><br>
                    Email:<br>
                    <input type="text" name="email" id="email">
                    <br><br>
                    Password:<br>
                    <input type="text" name="password" id="password">
                </form>

            </div>
            <div id="result">

            </div>

            <div>
                <button class="submit" id="submit" type="button">Submit</button>
            </div>

    </div>
</template>

<script>
export default {
    name: 'Login',
    data(){

    }
}
</script>

<style scoped>

input[type=text], input[type=password] {
  width: 60%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
  border-radius: 10px;
  background-color: Gainsboro;
}

button {
  background-color: deepskyblue;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 20%;
  border-radius: 10px;
  
}
</style>