<script>

import image from "../assets/Image/fon.png"

export default {
  data: function () {
    return {
      image: image
    }
  }
}

</script>



<style scoped>
image {





    width: 500px;
    height: 500px;
}
</style>

<template>
    <img :src="image" />
</template>