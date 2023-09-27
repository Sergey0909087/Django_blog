<script setup>
import Button from './Button.vue';
</script>


<script>
import axios from 'axios'

export default {
  data () {
    return {
        titls: []
    }
  },
  mounted () {
    axios.get('http://localhost:8000/titls/')
      .then(response => {
        console.log(this.titls = response.data);

      })
      .catch(error => {
        console.log(error)
      })
  }
}



</script>


<style scoped>

.Content {
    display: flex;
    flex-wrap: wrap;
    top: 10px;
    widows: 100%;
    height: 100%;

    margin: 10px;
    padding: 10px;

    left: 900px;
    right: 900px;
}

.Card {

    justify-content: center;
    text-align: center;
    margin-left: 850px;
    margin-top: 20px;

    border: 30px;
    box-shadow: 0 0 10px 5px rgb(38, 107, 172);

}

.h1 {
    font-size: 40px;
    text-align: center;
    color: cadetblue;

}

.Card-mini {
    width: 250px;
    height: 250px;
    margin: 20px;

    border: 15px;
    box-shadow: 0 0 10px 5px rgb(32, 117, 111);

}

p {
    font-size: 15px;
    font-family: cursive;
}

.Image {
    display: flex;
    position: fixed;
    width: 600px;
    height: 600px;

    margin-top: -900px;


}






</style>

<template>
    <div class="main">
        <div class="Content" v-for="t of titls" :key="t._id">


            <div class="Card" id="app">
                     <h1 class="h1">{{ t.title }}</h1>

                <div class="Card-mini">
                    <p> {{ t.content }} </p>
                </div>

                <div class="button">
                    <Button></Button>
                </div>
            </div>





        </div>

        <div class="Image">
             <Image></Image>
        </div>





    </div>




</template>
