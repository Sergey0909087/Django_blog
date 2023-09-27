

<script setup>
import { RouterLink } from 'vue-router';
import Button from './ButtonForm.vue';

const props = defineProps({
    cocktail: {
        type: Object,
        required: true,
    },
});


</script>

<style>
.headers {
    display: flex;
    flex-wrap: wrap;

    border: 20px 20px;
    box-shadow: 12px 12px 2px 1px rgba(0, 0, 255, .2);


}

.header {
    display: flex;
    flex: 1;
    justify-content: space-between;
    margin-left: auto; 



    align-content: space-between;
    padding: 10px;
    margin: 10px;
    width: 100%;
    margin-left: 200px;




}

li, a {
    list-style-type: none;

}

a {
    font-size: 20px;
}

h1 {
    margin-top: 3px;
}

.header-nave {
    text-align: right;
    float: right;
}

.header-1 {
    display: flex;
    align-content: space-between;
    margin-right: 200px;
    margin-left: auto;
}

.header-nav {
    display: flex;
    align-content: space-between;
    justify-content: center;
    text-align: center;
    margin-left: auto;
    margin-right: auto;
    position: absolute;


}



.nav-form {
    display: flex;
    align-content: space-between;
    justify-content: flex-end;
    left: 1600px;
    top: 10px;
    position: absolute;
}

.a-1, .a-2 {
    margin-left: 20px;
}

.nav-link {

    display: flex;
    align-content: space-between;
    justify-content: flex-end;
    left: 850px;
    top: 10px;
    position: absolute;

}

</style>

<template>
    <div class="headers">
         <h1>Python</h1>
 
 
         <div class="header-nave" style="margin: 0 200px;">
             <nav class="header" style="float: right;">
                 <div>
                      <nav class="nav-link">
 
                     <li><a class="a-2" href="#home">Home</a></li>
                     <li><a class="a-2"  href="#block">Block</a></li>
                     <li><a class="a-2" href="#Aboute">Aboute</a></li>
                     </nav>
                     </div>
 
                 <div>
                  <nav class="nav-form">
                     <li><a class="a-1">Registrasion</a></li>
                     <li><a class="a-1">Autorisasion</a></li>
                  </nav>
 
                 </div>
 
 
             </nav>
 
 
         </div>
     </div>
 
 
 
 
 
 
 </template>
 