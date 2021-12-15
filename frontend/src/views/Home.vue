<template>
  <div class="home">
    <h1>Страница Home</h1>
    <BlogPostList :posts='posts'/>
  </div>
</template>

<script>
// @ is an alias to /src
import BlogPostList from '@/components/BlogPostList.vue'
import axios from 'axios'

export default {
  name: 'Home',
  components: {
    BlogPostList
  },
  data () {
    return {
      posts: []
    }
  },
  methods: {
    async getBlogPost () {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/')
        // console.log(response.data)
        this.posts = response.data
      } catch (e) {
        console.log('Error!!!')
      }
    }
  },
  mounted () {
    this.getBlogPost()
  }
}
</script>
