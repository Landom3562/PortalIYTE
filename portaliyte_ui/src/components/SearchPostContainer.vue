<template>
  <div class="post-container">
    <v-container>
      <v-row>
        <v-col v-for="(post, index) in posts" :key="index" cols="12">
          <Post
            @postDetails="$emit('post-details')"
            :header="post.header"
            :text="post.text"
            :postTopic="post.postTopic"
            :postOwner="post.postOwner"
            :postLiked="post.postLiked"
          />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import Post from './Post.vue'

const router = useRoute()
const posts = [
  {
    header: 'Biri sürekli denk diyo',
    text: 'bunu nasıl engelleriz',
    postTopic: 'Gündem',
    postOwner: 'kimsinsen',
    postLiked: 45
  },
  {
    header: 'beşiktaş',
    text: 'gene şampiyon',
    postTopic: 'spor',
    postOwner: router.params.query,
    postLiked: 12372901731
  }
]
</script>

<style scoped>
.post-container {
  background-color: #9a1220;
  border-radius: 10px;
}
</style>
