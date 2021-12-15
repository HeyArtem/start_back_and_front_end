<template>
  <div class="post-list">
    <h1>My first project backend & frontend</h1>
    <div class="post" v-for="post in posts" :key="post.id" >
      <h2>Title: {{ post.title }}</h2>
      <div class="post-img">
        <img :src="post.img" alt="">
      </div>
      <hr>
      <div class="post-description">
        <h4>Description: {{ post.description }}</h4>
      </div>
      <div class="post-date">
        <h4>Updated_at: {{ post.updated_at}}</h4>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BlogPostList',
  props: {
    posts: Array
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.post-list {
  background-color: burlywood;
}
.post {
  background-color: greenyellow;
  /* bottom: 2px solid rgb(192, 32, 32); */
  /* padding: 20px; */
  margin: 20px;
  border: 2px solid black;
  border-radius: 15px;
}
/* .post-img {
  width: 200px;
  height: 150px;
} */
</style>
