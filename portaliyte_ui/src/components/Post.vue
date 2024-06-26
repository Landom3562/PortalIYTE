<template>
  <v-card class="mx-auto border" variant="flat">
    <v-card-title class="post-header" style="cursor: pointer" @click="$emit('post-details', id)">{{ header }}</v-card-title>
    <img v-if="image" :src="image" alt="Post Image" style="max-width: 100%; height: auto;" />
    <v-card-text class="py-2">
      {{ text }}
    </v-card-text>

    <v-card-actions>
      <v-list-item class="w-100">
        <v-list-item-title>{{ postTopic }}</v-list-item-title>

        <v-list-item-subtitle style="cursor: pointer" @click="handleOtherProfile">{{ postOwner }}</v-list-item-subtitle>
        
        <template v-slot:append>
          <div class="justify-self-end" style="margin-right: 5px" @click="handleComment">
            <v-icon class="me-1" icon="mdi-comment"></v-icon>
            <span class="subheading me-2">{{ postCommentCount }}</span>
          </div>
          <div class="justify-self-end" @click="handleLike">
            <v-icon class="me-1" icon="mdi-heart"></v-icon>
            <span class="subheading me-2">{{ likeCount }}</span>
          </div>
        </template>
      </v-list-item>
    </v-card-actions>
  </v-card>
  <v-list-item v-if="showReplyInput" style="border-top: 2px solid #9a1220">
    <div style="display: flex; align-items: center">
      <v-text-field
        hide-details="auto"
        v-model="newReplyText"
        placeholder="Write a reply..."
        style="flex: 1"
        append-inner-icon="mdi-send-circle"
        @click.stop
        @click:append-inner="submitReply"
        @keyup.enter="submitReply"
        variant="solo"
      />
    </div>
  </v-list-item>
</template>

<script>
import { id, th } from 'vuetify/locale';
import VueCookies from 'vue-cookies'
import { useRouter } from 'vue-router'

export default {
  props: {
    id: {
      type: Number,
      default: -1
    },
    userId: {
      type: Number,
      default: -1
    },
    topicId: {
      type: Number,
      default: -1
    },
    header: {
      type: String,
      default: 'Header'
    },
    text: {
      type: String,
      default: 'Text'
    },
    postTopic: {
      type: String,
      default: 'Topic'
    },
    postOwner: {
      type: String,
      default: 'Post Owner'
    },
    postLiked: {
      type: Number,
      default: 0
    },
    postCommentCount: {
      type: Number,
      default: 0
    },
    image: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      likeCount: this.postLiked,
      isLiked: false,
      router: useRouter(),
      showReplyInput: false,
      newReplyText: ''
    }
  },
  methods: {
    mounted(){
      console.log("adasd",this.postLiked)
    },
    async handleLike() {
      if (this.isLiked) {
        await fetch(`https://portaliyte-jq7n5xwowq-uc.a.run.app/api/post/unlike`, {
          method: 'PUT',
          headers: {
          'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            postId: this.id,
            userId: VueCookies.get('user')
          })
        })
        this.likeCount--;
        this.isLiked = false;
      } else {
        await fetch(`https://portaliyte-jq7n5xwowq-uc.a.run.app/api/post/like`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            postId: this.id,
            userId: VueCookies.get('user')
          })
        })
        this.likeCount++;
        this.isLiked = true;
      }
    },
    async handleComment() {
      if(!this.router.currentRoute.name === 'PostDetails'){
        this.$emit('post-details', this.id)
      }else{
        this.showReplyInput = !this.showReplyInput
      }
    },

    async submitReply(){
      if(this.newReplyText.trim()){
        await fetch('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/comment/post', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            postId: this.id,
            parentId: null,
            userId: VueCookies.get('user'),
            content: this.newReplyText
          })
        })
        this.newReplyText = ''
        this.showReplyInput = false
        window.location.reload()
      }
    },
    handleOtherProfile() {
      console.log("adasd",this.userId)
      console.log("adasd",VueCookies.get('user'))
      if(this.userId.toString() === VueCookies.get('user').toString()){
        this.router.push('/profilePage')
      }else{
        this.router.push(`/other-profile/${this.userId}`)
      }
    },
    handlePostDetails() {
      this.router.push(`/postdetails/${this.id}`)
    }
  }
}
</script>

<style scoped>
.v-card-actions {
  padding: 0;
}

.border {
  border: 2px solid #9a1220 !important;
}

.post-header{
  font-size: 1.5vw;
}
</style>
