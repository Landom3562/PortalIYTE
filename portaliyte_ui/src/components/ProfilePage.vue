<template>
  <div class="user-info">
    <div class="username">
      <img v-if="profilePicture" :src="profilePicture" width="128" height="128" @click="handleAccount"/>
      <v-icon v-else class="account-icon" @click="handleAccount">mdi-account-circle</v-icon>
      {{ username }}
    </div>
    <div class="user-stats">
      <div class="stat">
        <span class="info-label">Followers</span>
        <span class="info-value">{{ followers }}</span>
      </div>
      <div class="stat">
        <span class="info-label">Following</span>
        <span class="info-value">{{ following }}</span>
      </div>
      <div class="stat">
        <span class="info-label">Posts</span>
        <span class="info-value">{{ posts.length }}</span>
      </div>
    </div>
  </div>
  <div class="search-button-container">
    <div class="search-content">
        <v-btn 
            :class="{'search-button': true, 'active': activeButton === 'posts'}"
            @click="setActiveButton('posts')"
        >Posts</v-btn>
        <v-btn 
            :class="{'search-button': true, 'active': activeButton === 'comments'}"
            @click="setActiveButton('comments')"
        >Comments</v-btn>
        <v-btn 
            :class="{'search-button': true, 'active': activeButton === 'likes'}"
            @click="setActiveButton('likes')"
        >Likes</v-btn>
        <v-btn 
            :class="{'search-button': true, 'active': activeButton === 'saved'}"
            @click="setActiveButton('saved')"
        >Saved</v-btn>
    </div>
  </div>
  <div v-if="activeButton === 'posts'" class="post-container">
    <v-container>
      <v-row>
        <v-col v-for="(post, index) in posts" :key="index" cols="12">
          <Post
            @postDetails="$emit('post-details')"
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
  <div v-if="activeButton === 'comments'" class="">
    <div v-for="(comment, index) in comments" @click="handleCommentClick(comment.post_id)">
      <Comment :key="index" :comment="comment"/>
    </div>
  </div>
  <div v-if="activeButton === 'likes'" class="post-container">
    <v-container>
      <v-row>
        <v-col v-for="(post, index) in liked" :key="index" cols="12">
          <Post
            @postDetails="$emit('post-details', post.id)"
            @otherProfile="navigateToOtherProfile()"
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
  <div v-if="activeButton === 'saved'" class="post-container">
    <v-container>
      <v-row>
        <v-col v-for="(post, index) in saved" :key="index" cols="12">
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
import Comment from './Comment.vue';
import Post from './Post.vue'
import VueCookies from 'vue-cookies'

export default {
  name: "SearchButtons",
  components: {
    Post,
    Comment
  },
  data() {
    return {
      activeButton: null,
      isUser: false,
      username: "",
      followers: 0,
      following: 0,
      posts: [],
      comments: [],
      likes: [],
      saved: [],
      profilePicture: '',
    }
  },
  async mounted(){
    const user = await this.getUserDetails('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/user/' + VueCookies.get('user'));
    this.username = user.username;
    this.followers = user.followerCount;
    this.following = user.followingCount;
    const profilePicture = `data:image/jpeg;base64,${user.profilePicture}`;
    this.profilePicture = user.profilePicture ? profilePicture : '';
    await this.initPosts();
    await this.initComments();
    await this.initLikes();
    await this.initSaved(); 
  },
  methods: {
    async initPosts(){
      const posts = await this.getPostsOfUser('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/post/user/' + VueCookies.get('user'));
      posts.forEach(post => {
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
    async initComments(){
      this.comments = await this.getCommentsOfUser('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/user/comments/' + VueCookies.get('user'));
      console.log('Comments:', this.comments);
    },
    async initLikes(){
      const likes = await this.getPostsOfUser('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/user/likedPosts/' + VueCookies.get('user'));
      likes.forEach(like => {
        let image = ''
        if (like.image) {
          if(like.image.includes('data')){
            image = like.image
          }else{
            image = `data:image/jpeg;base64,${like.image}`
          }
        }
        this.likes.push({
          id: like.postId,
          userId: like.user.userId,
          topicId: like.topic.topicId,
          header: like.title,
          text: like.content,
          postTopic: like.topic.name,
          postOwner: like.user.username,
          postLiked: like.likeCount,
          postCommentCount: like.commentCount,
          image: image
        });
      })
    },
    async initSaved(){
      const saved = await this.getPostsOfUser('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/user/savedPosts/' + VueCookies.get('user'));
      saved.forEach(save => {
        let image = ''
        if (save.image) {
          if(save.image.includes('data:image')){
            image = save.image
          }else{
            image = `data:image/jpeg;base64,${save.image}`
          }
        }
        this.saved.push({
          id: save.postId,
          userId: save.user.userId,
          topicId: save.topic.topicId,
          header: save.title,
          text: save.content,
          postTopic: save.topic.name,
          postOwner: save.user.username,
          postLiked: save.likeCount,
          postCommentCount: save.commentCount,
          image: image
        });
      })
    },
    handleCommentClick(postId) {
      this.$router.push('/postdetails/' + postId);
    },
    handleAccount() {
      this.$router.push('/account-settings');
    },
    setActiveButton(button) {
        this.activeButton = button;
    },
    async getCommentsOfUser(fetchDestination){
      let returnedComments;
      await fetch(fetchDestination, {
        method: 'GET',
        redirect: 'follow',
      })
        .then(response => {
          if (!response.ok) {
            // const errorMessages = await response.text();
            // alert(errorMessages);
            throw new Error(response.text());
          }
          return response.json();
        })
        .then(data => {
          console.log('Comments fetched successfully:', data);
          returnedComments = data;
        })
        .catch(error => {
          console.error('An error occurred during fetching comments:', error);
        });
      return returnedComments;
    },
    async getUserDetails(fetchDestination){
      let returnedUser;
      await fetch(fetchDestination, {
        method: 'GET',
        redirect: 'follow',
      })
        .then(response => {
          if (!response.ok) {
            // const errorMessages = await response.text();
            // alert(errorMessages);
            throw new Error(response.text());
          }
          return response.json();
        })
        .then(data => {
          console.log('User fetched successfully:', data);
          returnedUser = data;
        })
        .catch(error => {
          console.error('An error occurred during fetching user:', error);
        });
      return returnedUser;
    },
    async getPostsOfUser(fetchDestination) {
      let returnedPosts;
      await fetch(fetchDestination, {
        method: 'GET',
        redirect: 'follow',
      })
        .then(response => {
          if (!response.ok) {
            // const errorMessages = await response.text();
            // alert(errorMessages);
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
  }
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

.account-icon{
  font-size: 5vw;
}

.username {
  font-size: 1vw;
  width: 40%;
  display: flex;
  align-items: center;
}

.user-info {
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

.user-button {
  margin-left: 10px;
  font-size: 0.5vw;
}

.user-stats{
  display: flex;
  align-items: center;
}

.stat{
  display: flex;
  flex-direction: column-reverse;
  margin-right: 15px; 
}

.info-value{
  font-size: 1.2vw;
  display: flex;
  justify-content: center;
}

.search-button-container {
    width: 100%;
    display: flex;
    justify-content: center;
    padding: 20px 0;
}

.search-content {
    display: flex;
    width: 50%;
    justify-content: space-between;
    gap: 20px; 
}

.search-button {
    display: flex;
    flex: 1;
    padding: 10px 20px;
    margin: 0 10px;
    border: none;
    border-radius: 5px; 
    font-size: 1vw;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.3s ease;
}   

.search-button:hover {
    transform: scale(1.05); 
}

.search-button:active {
    transform: scale(1); 
}

.active {
    background-color: rgba(154, 18, 32, 0.8);
}
</style>
