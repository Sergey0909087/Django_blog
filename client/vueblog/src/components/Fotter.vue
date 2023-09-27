<script setup>
import Button from './ButtonForm.vue';

</script>
<style>
footer {


    width: 100%;
    height: 20%;
    background: black;

}

.form {


    display: flex;
    flex-wrap: wrap;

    margin: 10px;
    margin-left: 900px;
    margin-top: 200px;


    width: 500px;
    height: 300px;
}

input {
    display: flex;
    flex-wrap: wrap;
    margin-top: 10ox;
}

.fotter-main {
    margin-top: 20px;
}

form {
    margin-top: -50px;
    width: 400px;
    height: 150px;
}

h2 {
    margin-bottom: 10px;
    margin-top: 120px;
    margin-left: 50px;
    color: white;
}

h2, input {
    margin-left: 110px;
}
input {
    margin-top: 10px;
    border-radius: 20px;
}

</style>
<template>
    <footer>

            <div class="form">
            <form>
                <h2>Фома обработки</h2>
                <input v-model="title">
                <input v-model="content">
                <input v-on:click.prevent="addItem" type="submit" value="отправить">
                
            </form>
        </div>

    </footer>




</template>
<script>
import axios from 'axios';

export default {

    data() {
        return {
            newItem: {
            title: '',
            content: '',
            titlels: []
            }
        }
    },
    
    methods: {
        async addItem () {
            await  axios.post('http://localhost:8000/titls/', {
                title: this.title,
                content: this.content
            })
            .then(response => {
                console.log( this.titls = response.data);
            })
            .catch(err => {
                console.log(err)
            })
        }
    }
    
    
}

</script>
