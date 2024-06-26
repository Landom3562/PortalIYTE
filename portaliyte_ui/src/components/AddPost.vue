<template>
  <v-alert
    v-if="visible"
    type="error"
    dismissible
    @input="visible = false"
    :text="this.errorMessage"
  ></v-alert>
  <div class="add-header">Create Post</div>
  <form @submit.prevent="submitPost">
    <div>
      <label for="topic" class="input-header">Topic</label>
      <v-select
        v-model="chosenTopic"
        :items="topics"
        color="#9A1220"
        variant="underlined"
      ></v-select>
    </div>
    <div>
      <label for="title" class="input-header">Title</label>
      <v-text-field v-model="title" color="#9A1220" variant="underlined"></v-text-field>
    </div>
    <div>
      <label for="text" class="input-header">Text</label>
      <v-textarea class="textarea" v-model="text" color="#9A1220" variant="underlined"></v-textarea>
    </div>
    <div>
      <label for="image" class="input-header">Add Image</label>
      <input type="file" @change="onFileChange" />
    </div>
    <div class="bottom-container">
      <v-btn class="button" color="#9a1220" type="submit">Post</v-btn>
    </div>
  </form>
</template>

<script>
import VueCookies from 'vue-cookies'

export default {
  data() {
    return {
      dictionary: {},
      topics: [],
      chosenTopic: null,
      title: null,
      text: null,
      image: null,
      errorMessage: null,
      visible: false
    }
  },
  methods: {
    onFileChange(event) {
      const file = event.target.files[0]
      if (file) {
        const reader = new FileReader()
        reader.onload = (e) => {
          this.image = e.target.result
        }
        reader.readAsDataURL(file)
      }
    },
    async submitPost() {
      if (!this.chosenTopic || !this.title || !this.text) {
        this.errorMessage = 'Please fill all the fields'
        this.visible = true
        return
      }
      await fetch('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/post', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          topicId: this.dictionary[this.chosenTopic],
          userId: VueCookies.get('user'),
          title: this.title,
          content: this.text,
          image: this.image
        })
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error('An error occurred during registration')
          }
          this.visible = false
          this.chosenTopic = null
          this.title = null
          this.text = null
          this.image = null
        })
        .then(() => {
          this.$router.push('/postcontainer')
        })
        .catch((error) => {
          console.error('An error occurred during post submission:', error)
        })
    }
  },
  async mounted() {
    await fetch('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/topic', {
      method: 'GET'
    })
      .then(async (response) => {
        if (!response.ok) {
          throw new Error(response.text())
        }
        return response.json()
      })
      .then((data) => {
        data.forEach((item) => {
          this.topics.push(item.name)
          this.dictionary[item.name] = item.id
        })
      })
      .catch((error) => {
        console.error('An error occurred during getting topics:', error)
      })
  }
}
</script>


<style scoped>
.add-header {
  text-align: start;
  margin-bottom: 20px;
  font-size: 1.5vw;
  font-weight: bold;
}

.input-header {
  font-size: 1vw;
}

form div {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type='text'],
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

textarea {
  resize: vertical;
  height: 100px;
}

.bottom-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.add-images {
  width: 20%;
  display: flex;
  font-size: 1vw;
  flex-direction: column;
}

.add-images button {
  width: 30px;
  height: 30px;
  font-size: 20px;
  margin-left: 10px;
  cursor: pointer;
}

button[type='submit'] {
  padding: 10px 20px;
  border-radius: 10px;
  cursor: pointer;
  width: 20%;
  height: 50%;
  text-align: center;
  background-color: #d9d9d9;
  font-size: 1vw;
}

.add-icon {
  font-size: 2vw;
}
</style>
