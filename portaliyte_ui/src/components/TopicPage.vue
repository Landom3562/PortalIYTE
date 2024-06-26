<template>
    <div class="topic-info">
      <div class="topicname">
        <img v-if="topicImage" :src="topicImage" alt="topic image" class="topic-image" width="128" height="128"/>
        <!-- <v-icon class="topic-icon">mdi-account-circle</v-icon> -->
        {{ topicName }}
      </div>
    </div>
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
  import Post from './Post.vue'
  
  export default {
    components: {
      Post
    },
    data() {
      return {
        istopic: false,
        topicName: '',
        posts: [],
        newtopics: [],
        topicImage: ''
      }
    },

    async created() {
      const topicId = this.$route.params.id; 
      const topicResponse = await fetch(`https://portaliyte-jq7n5xwowq-uc.a.run.app/api/topic/${topicId}`);
      const topicData = await topicResponse.json();
      this.topicName = topicData.name; 
      this.topicImage = topicData.logo;

      
      const allPosts = await this.getPostsForTopic(`https://portaliyte-jq7n5xwowq-uc.a.run.app/api/post/topic/${topicId}`)
      console.log('All posts:', allPosts)
      allPosts.forEach(post => {
        let image = ''
        if (post.image) {
          if(post.image.includes('data:image')){
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
    navigateToOtherProfile() {
      this.$router.push('/other-profile')
    },
    async getPostsForTopic(fetchDestination) {
      let returnedPosts;
      await fetch(fetchDestination, {
        method: 'GET',
        redirect: 'follow',
      })
        .then(response => {
          if (!response.ok) {
            throw new Error(response.text());
          }
          return response.json();
        })
        .then(data => {
          console.log('Posts fetched successfully:', data);
          returnedPosts = data;
        })
        .catch(error => {
          console.error('An error occurred during fetching posts:', error);
        });
      return returnedPosts;
    },
  },
  }
  </script>
  
  <style scoped>
  .post-container {
    background-color: #9a1220;
    border-radius: 10px;
  }
  
  .topics {
    padding: 16px;
    padding-bottom: 0px;
    display: flex;
    justify-content: space-between;
  }
  
  .topic-icon{
    font-size: 5vw;
  }
  
  /* .topicname{
    font-size: 1vw;
  }
  
  .topic-info {
    margin-bottom: 10px;
    width: 100%;
    border-radius: 10px;
    border: 2px solid #9a1220;
    padding: 10px;
    font-size: 1.25rem;
    font-weight: 500;
    display: flex;
    justify-content: space-between;
    background-color: rgba(128, 128, 128, 0.1);
  } */

  .topicname {
    font-size: 1vw;
    width: 40%;
    display: flex;
    align-items: center;
  }

  .topic-info {
    margin-bottom: 10px;
    width: 100%;
    border-radius: 10px;
    padding: 10px;
    font-size: 1.25rem;
    font-weight: 500;
    display: flex;
    justify-content: space-between; /* This will help in spacing out the username and stats */
    background-color: rgba(128, 128, 128, 0.1);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border: 2px solid #9a1220;
  }
  
  .buttons {
    display: flex;
    align-items: center;
  }
  
  .topic-button {
    margin-left: 10px;
    font-size: 0.5vw;
  }
  
  :deep(.v-btn__content) {
    font-weight: 500;
  }
  
  :deep(.v-btn__content) {
    color: black;
  }
  </style>
  