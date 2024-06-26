<template>
  <div>
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
    <div class="comments-section">
      <Comment v-for="(comment, index) in postComments" :key="index" :comment="comment" />
    </div>
  </div>
</template>

<script>
import Post from './Post.vue'
import Comment from './Comment.vue'
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

export default {
  components: {
    Post,
    Comment
  },
  data(){
    return {
      router: useRouter(),
      // post: {
      //   header: 'header',
      //   text: 'text',
      //   postTopic: 'topic',
      //   postOwner: 'owner',
      //   postLiked: 3
      // },
      // postComments: [
      //   {
      //     commentOwner: 'User1',
      //     commentText: 'This is the first comment',
      //     likes: 2,
      //     replies: []
      //   },
      //   {
      //     commentOwner: 'User2',
      //     commentText: 'This is the second comment',
      //     likes: 1,
      //     replies: [
      //       {
      //         commentOwner: 'User3',
      //         commentText: 'This is a reply to the second comment',
      //         likes: 0,
      //         replies: []
      //       }
      //     ]
      //   }
      // ]
      post: {},
      postComments: []
    }
  },
  async mounted(){
    const post = await this.getPost(`https://portaliyte-jq7n5xwowq-uc.a.run.app/api/post/${this.router.currentRoute.params.id}`)
    let image = ''
    if (post.image) {
      if(post.image.includes('data')){
        image = post.image
      }else{
        image = `data:image/jpeg;base64,${post.image}`
      }
    }
    this.post = {
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
    };
    this.postComments = post.comments
    console.log("asdasds",this.post)
  },
  methods:{
    async getPost(fetchDestination) {
      let returnedPost;
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
          returnedPost = data;
        })
        .catch(error => {
          console.error('An error occurred during fetching posts:', error);
        });
      return returnedPost;
    },
  }
}


// const post = {
//   header: 'header',
//   text: 'text',
//   postTopic: 'topic',
//   postOwner: 'owner',
//   postLiked: 3
// }

// const postComments = ref([
//   {
//     commentOwner: 'User1',
//     commentText: 'This is the first comment',
//     likes: 2,
//     replies: []
//   },
//   {
//     commentOwner: 'User2',
//     commentText: 'This is the second comment',
//     likes: 1,
//     replies: [
//       {
//         commentOwner: 'User3',
//         commentText: 'This is a reply to the second comment',
//         likes: 0,
//         replies: []
//       }
//     ]
//   }
// ])
onMounted(() => {
  console.log(router.currentRoute.value.params.id)
})
</script>

<style scoped>
.comments-section {
  margin-top: 20px;
  padding-left: 10px;
}
</style>
