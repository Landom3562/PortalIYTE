<template>
  <v-card class="ms-auto border" style="margin-bottom: 10px" variant="flat">
    <v-card-title style="font-size: small">{{ commentOwner }}</v-card-title>

    <v-card-text class="py-2">
      {{ commentText }}
    </v-card-text>

    <v-list-item class="w-100">
      <template v-slot:append>
        <div class="justify-self-end" style="margin-right: 5px">
          <v-icon class="me-1" icon="mdi-comment" @click="addReply"></v-icon>
        </div>
        <div class="justify-self-end">
          <v-icon class="me-1" icon="mdi-heart" @click="likeComment"></v-icon>
          <span class="subheading me-2">{{ likes }}</span>
        </div>
      </template>
    </v-list-item>

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
  </v-card>
  <v-list-item v-if="commentReplies.length">
    <div v-for="(reply, index) in commentReplies" @click="handleCommentClick(reply.postId)">
      <Comment :key="index" :comment="reply" />
    </div>
  </v-list-item>
</template>

<script setup>
import { ref } from 'vue'
import VueCookies from 'vue-cookies';

const props = defineProps({
  comment: {
    type: Object,
    required: true
  }
})
const id = ref(props.comment.id)
const postId = ref(props.comment.post_id)
const userId = ref(props.comment.user_id)
const parentId = ref(props.comment.parent_id)
const commentOwner = ref(props.comment.username)
const commentText = ref(props.comment.content)
const likes = ref(props.comment.like_count)
const commentReplies = ref(props.comment.replies || [])

const showReplyInput = ref(false)
const newReplyText = ref('')

const likeComment = () => {
  likes.value++
}

const handleCommentClick = (postId) => {
  this.$router.push('/postdetails/' + postId);
}

const addReply = () => {
  showReplyInput.value = true
}

const submitReply = async () => {
  if (newReplyText.value.trim()) {
    await fetch('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/comment/comment', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        postId: postId.value,
        parentId: id.value,
        userId: VueCookies.get('user'),
        content: newReplyText.value
      })
    })
    newReplyText.value = ''
    showReplyInput.value = false
    window.location.reload()
  }
}
</script>

<style scoped>
.border {
  border: 2px solid #9a1220 !important;
}

:deep(.v-icon) {
  opacity: 1 !important;
}

.v-list-item {
  padding-right: 0;
}
</style>
