<template>
    <div class="search-button-container">
        <div class="search-content">
            <v-btn 
                :class="{'search-button': true, 'active': activeButton === 'posts'}"
                @click="setActiveButton('posts')"
            >Posts</v-btn>
            <v-btn 
                :class="{'search-button': true, 'active': activeButton === 'topics'}"
                @click="setActiveButton('topics')"
            >Topics</v-btn>
            <v-btn 
                :class="{'search-button': true, 'active': activeButton === 'users'}"
                @click="setActiveButton('users')"
            >Users</v-btn>
        </div>
    </div>
    <div class="post-container" v-if=" activeButton === 'posts'">
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
    <div class="topic-container" v-if=" activeButton === 'topics'">
        <ul>
          <li v-for="topic in topics" :key="topic.id">
            <button class="topic-button" @click="handleTopicClick(topic)">{{ topic.title }}</button>
          </li>
        </ul>
    </div>
    <div class="user-container" v-if=" activeButton === 'users'">
        <ul>
          <li v-for="user in users" :key="user.id">
            <button class="topic-button" @click="handleUserClick(user)">{{ user.title }}</button>
          </li>
        </ul>
    </div>
    
    
</template>

<script>
import Post from './Post.vue'
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue'

export default {
    name: "SearchButtons",
    components: {
        Post
    },
    data() {
        return {
            activeButton: "posts" ,
            posts: [],
            topics: [],
            users: []
        }
    },

    setup() {
        const router = useRouter();
        return { router };
    },

    async created() {
      const query = this.$route.params.query;

      const allPosts = await this.getPostsForTopic(`https://portaliyte-jq7n5xwowq-uc.a.run.app/api/search/post/${query}`)
      console.log('search post:', allPosts)
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

      const allTopics = await this.getTopics(`https://portaliyte-jq7n5xwowq-uc.a.run.app/api/search/topic/${query}`)
      console.log('search topic: ', allTopics)
      allTopics.forEach(topic => {
        this.topics.push({
            id: topic.id,
            title: topic.name
        })
      })

      const allUsers = await this.getUsers(`https://portaliyte-jq7n5xwowq-uc.a.run.app/api/search/user/${query}`)
      console.log('search user: ', allUsers)
      allUsers.forEach(user => {
        this.users.push({
            id: user.id,
            title: user.username
        })
      })

    },

    methods: {
        setActiveButton(button) {
            this.activeButton = button;
        },

        handleTopicClick(topic) {
            this.router.push(`/topic-page/${topic.id}`)
        },

        handleTopicClick(user) {
            this.router.push(`/other-page/${user.id}`)
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
        async getTopics(fetchDestination) {
        let returnedTopics;
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
            console.log('Topics fetched successfully:', data);
            returnedTopics = data;
            })
            .catch(error => {
            console.error('An error occurred during fetching topics:', error);
            });
        return returnedTopics;
        },
        async getUsers(fetchDestination) {
        let returnedUsers;
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
            console.log('Topics fetched successfully:', data);
            returnedUsers = data;
            })
            .catch(error => {
            console.error('An error occurred during fetching topics:', error);
            });
        return returnedUsers;
        }
    }
}
</script>

<style>
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
    font-weight: bold;
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

.post-container {
  background-color: #9a1220;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

:deep(.v-btn__content) {
  font-weight: 500;
}

ul {
  display: flex;
  font-size: 1vw;
  list-style-type: none;
  padding: 0;
  flex-direction: column;
  align-items: flex-start;
}

.topic-button {
  width: 100%;
  text-align: left;
  padding: 5px 0;
  border-bottom: 1px solid #ddd;
}
</style>
