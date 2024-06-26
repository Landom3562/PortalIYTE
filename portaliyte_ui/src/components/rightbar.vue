<template>
    <div class="sidebar" v-if="showSidebars">
      <div class="top-post-of-week">
        <div class="rightbar-header">Hot Posts</div>
        <div class="hot-posts-list">
          <ul>
            <li v-for="post in hotposts" :key="post.postId">
              <button class="post-button" @click="handlePostClick(post)">{{ post.title }}</button>
            </li>
        </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router'

  const router = useRouter()
  
  const props = withDefaults(defineProps<{
    showSidebars?: boolean
  }>(), {
    showSidebars: false
  })
  
  const hotposts = ref<{ postId: string, title: string }[]>([])

  const handlePostClick = (post: { postId: string, title: string }) => {
    router.push(`/postdetails/${post.postId}`).then(() => {
    window.location.reload()
  })
  }

  const fetchHot = async () => {
    try {
      const response = await fetch('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/post/mostLiked')
      const data = await response.json()
      console.log('All hots:', data)
      hotposts.value = data.map((post: { postId: string, title: string }) => ({
        postId: post.postId,
        title: post.title
      }))
    } catch (error) {
      console.error('Failed to fetch posts:', error)
    }
  }
  onMounted(fetchHot)
  </script>
  
  <style scoped>
  .sidebar {
    height: 100%;
    border-radius: 10px;
    background-color: rgba(128, 128, 128, 0.2);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.25);
  }
  
  .top-post-of-week {
    padding: 10px;
  }

  .rightbar-header {
    width: 100%;
    display: flex;
    justify-content: center;
    font-size: 1.2vw;
    margin-bottom: 20px;
    border-bottom: 2px solid #9a1220;
    font-weight: bold;
  }

  .content {
    font-size: 1vw;
  }

  ul {
    font-size: 1vw;
    list-style-type: none;
    padding: 0;
  }
  
  li {
    padding: 5px 0;
    border-bottom: 1px solid #ddd;
  }
  
  </style>
  