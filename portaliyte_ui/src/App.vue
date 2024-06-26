<template>
  <div class="body">
    <div class="top">
      <TopBar :showSearchAndIcons="router.currentRoute.value.meta.showTopBar" />
    </div>

    <div class="bottom">
      <div class="left-container">
        <Leftbar :showSidebars="router.currentRoute.value.meta.showSidebars" />
      </div>

      <div class="main-container">
        <RouterView
          @registerPage="goRegisterPage()"
          @succesfullyLogin="goSuccessfullyLoginPage()"
          @loginPage="goLoginPage()"
          @postDetails="goPostDetails($event)"
        ></RouterView>
      </div>

      <div class="right-container">
        <Rightbar :showSidebars="router.currentRoute.value.meta.showSidebars"/>
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { RouterView, useRouter, useRoute } from 'vue-router'
import TopBar from './components/TopBar.vue'
import Leftbar from './components/leftbar.vue'
import Rightbar from './components/rightbar.vue'

const router = useRouter()
const route = useRoute()


function goSuccessfullyLoginPage() {
  router.push('/postcontainer')
}

function goLoginPage() {
  router.push('/')
}

function goRegisterPage() {
  router.push('/register')
}

function goPostDetails(id) {
  router.push('/postdetails/' + id)
}
</script>

<style scoped>
.body {
  display: grid;
  grid-template-rows: 1fr 8fr;
  height: 100%;
  width: 100%;
  
}

.bottom {
  display: grid;
  grid-template-columns: 2fr 7fr 2fr;
}

.right-container,
.left-container,
.main-container {
  padding: 1em;
}

</style>
./components/common/TopBar.vue