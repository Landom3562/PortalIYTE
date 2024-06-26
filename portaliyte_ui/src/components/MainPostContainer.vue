<template>
  <div class="post-container">
    <v-container>
      <v-row>
        <v-col v-for="(post, index) in posts" :key="index" cols="12">
          <Post
            @postDetails="$emit('post-details', post.id)"
            :id="post.id"
            :userId="post.userId"
            :topicId="post.topicId"
            :header="post.header"
            :text="post.text"
            :postTopic="post.postTopic"
            :postOwner="post.postOwner"
            :postLiked="post.postLiked"
            :postCommentCount="post.commentCount"
            :image="post.image"
          />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { id } from 'vuetify/locale'
import Post from './Post.vue'

export default {
  components: {
    Post
  },
  data() {
    return {
      // posts: [
      //   {
      //     header: 'Biri sürekli denk diyo',
      //     text: 'bunu nasıl engelleriz',
      //     postTopic: 'Gündem',
      //     postOwner: 'kimsinsen',
      //     postLiked: 45
      //   },
      //   {
      //     header: 'beşiktaş',
      //     text: 'gene şampiyon',
      //     postTopic: 'spor',
      //     postOwner: 'ENBÜYÜKKARTAL',
      //     postLiked: 12372901731
      //   }
      // ]
      posts: []
    }
  },
  async mounted() {
    console.log("adasdsd")
    const allPosts = await this.getPostsForMainPage('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/post')
    console.log('All posts:', allPosts)
    allPosts.forEach((post) => {
      let image = ''
      if (post.image) {
        if(post.image.includes('data')){
          image = post.image
        }else{
          image = `data:image/jpeg;base64,${post.image}`
        }
      }
      this.posts.push({
        id: post.postId,
        userId: post.user.userId,
        topicId: post.topic.topicId,
        header: post.title,
        text: post.content,
        postTopic: post.topic.name,
        postOwner: post.user.username,
        postLiked: post.likeCount,
        postCommentCount: post.commentCount,
        image: image
      });
    })
  },
  methods: {
    async getPostsForMainPage(fetchDestination) {
      let returnedPosts
      await fetch(fetchDestination, {
        method: 'GET',
        redirect: 'follow'
      })
        .then((response) => {
          if (!response.ok) {
            // const errorMessages = await response.text();
            // alert(errorMessages);
            throw new Error(response.text())
          }
          return response.json()
        })
        .then((data) => {
          console.log('Posts fetched successfully:', data)
          returnedPosts = data
        })
        .catch((error) => {
          console.error('An error occurred during fetching posts:', error)
        })
      return returnedPosts
    }
  }
}
</script>

<style scoped>
.post-container {
  background-color: #9a1220;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

:deep(.v-btn__content) {
  font-weight: 500;
}
</style>
