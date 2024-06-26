<template>
  <div class="sidebar" v-if="showSidebars">
    <div class="new-topics">
      <div class="leftbar-header">Topics</div>
      <div class="new-topics-list">
        <ul>
          <li v-for="topic in newtopics" :key="topic.id">
            <button class="topic-button" @click="handleTopicClick(topic)">{{ topic.title }}</button>
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

const newtopics = ref<{ id: string, title: string }[]>([])

const handleTopicClick = (topic: { id: string, title: string }) => {
  if (topic.id) {
    router.push(`/topic-page/${topic.id}`).then(() => {
      router.go(0)})
  } else {
    console.error('Topic ID is undefined')
  }
  
}

const fetchTopics = async () => {
  try {
    const response = await fetch('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/topic')
    const data = await response.json()
    console.log('All topics:', data)
    newtopics.value = data.map((topic: { id: string, name: string }) => ({
      id: topic.id,
      title: topic.name
    }))
  } catch (error) {
    console.error('Failed to fetch topics:', error)
  }
}

onMounted(fetchTopics)
</script>

<style scoped>
.sidebar {
  height: 100%;
  border-radius: 10px;
  background-color: rgba(128, 128, 128, 0.2);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.25);
}

.new-topics {
  padding: 10px;
  margin-bottom: 20px;
}

.leftbar-header {
  width: 100%;
  display: flex;
  justify-content: center;
  font-size: 1.2vw;
  margin-bottom: 20px;
  border-bottom: 2px solid #9a1220;
  font-weight: bold;
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
