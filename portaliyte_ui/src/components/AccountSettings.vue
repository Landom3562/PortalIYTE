<template>
  <div class="container">
    <div class="picture">
      <v-icon class="account-icon">mdi-account-circle</v-icon>
      <input type="file" @change="uploadImage" class="change-image" />
    </div>
    <form @submit.prevent="submitPost">
      <div>
        <label for="topic" class="input-header">Username</label>
        <input type="text" id="topic" v-model="post.topic" />
      </div>
      <div>
        <label for="text" class="input-header">Description</label>
        <textarea id="text" v-model="post.text"></textarea>
      </div>
      <div class="bottom-container">
        <button type="submit">Save</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      post: {
        topic: '',
        text: '',
        image: null
      }
    };
  },
  methods: {
    async uploadImage(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.readAsArrayBuffer(file);
        reader.onload = () => {
          this.post.image = new Uint8Array(reader.result);
          console.log('Image uploaded:', this.post.image);
        };
        reader.onerror = error => console.error('Error reading file:', error);
      }
    },
    submitPost() {
      console.log('Post submitted:', this.post);
    }
  }
};
</script>

<style scoped>
.container {
  height: 70%;
  width: 70%;
  padding: 20px;
  border-radius: 10px;
  margin: 0 auto;
  background-color: rgba(128, 128, 128, 0.1);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.25);
}

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

input[type="text"],
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
  justify-content: flex-end;
}

button[type="submit"] {
  padding: 10px 20px;
  border-radius: 10px;
  cursor: pointer;
  width: 20%;
  height: 50%;
  text-align: center;
  background-color: #D9D9D9;
  font-size: 1vw;
}

.account-icon {
  font-size: 5vw;
  margin-bottom: 10px;
}

.picture {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 40%;
}

.change-image {
  cursor: pointer;
}
</style>
