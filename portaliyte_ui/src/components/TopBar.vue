<template>
  <div class="top-bar">
    <div class="logo" style="display: flex; max-width: 15em; min-width: 5em">
      <v-img style="cursor: pointer" @click="handleLogoClick" src="/logo.png"></v-img>
    </div>
    <v-text-field
      v-if="showSearchAndIcons"
      class="search-bar"
      label="Search"
      variant="underlined"
      prepend-inner-icon="mdi-magnify"
      clearable
      hide-details="auto"
      v-model="searchText"
      @keyup.enter="handleEnter"
      color="#9a1220"
    ></v-text-field>
    <div v-if="showSearchAndIcons" class="buttons">
      <v-icon class="icon" @click="handleAdd" style="cursor: pointer">mdi-plus-box</v-icon>
      <!-- <v-icon class="icon">mdi-bell-outline</v-icon> -->
      <v-menu>
        <template v-slot:activator="{ props }">
          <v-icon class="icon" v-bind="props" style="cursor: pointer">mdi-account</v-icon>
        </template>
        <v-list>
          <v-list-item
            class="menu-content"
            v-for="(item, index) in items"
            :key="index"
            :value="index"
            @click="handleItemClick(index)"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <div class="item-content">
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </div>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import VueCookies from 'vue-cookies'
import { useRouter } from 'vue-router'

const router = useRouter()

export default defineComponent({
  data() {
    return {
      searchText: '',
      items: [
        { title: 'Profile Page', route: '/profilepage', icon: 'mdi-account-circle' },
        { title: 'Log out', route: '/', icon: 'mdi-logout' }
      ]
    }
  },
  props: {
    showSearchAndIcons: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    handleEnter() {
      const searchParam = this.searchText
      this.searchText = ''
      this.$router.push(`/search-page/${searchParam}`).then(() => {
      location.reload()
    })
    },
    handleAccount() {
      this.$router.push('/profilepage')
    },
    handleAdd() {
      this.$router.push('/add-post')
    },
    handleItemClick(index: number) {
      const route = this.items[index].route
      if (route === '/') {
        const allCookies = VueCookies.keys()
        allCookies.forEach((cookie) => VueCookies.remove(cookie))
      }
      this.$router.push(route)
    },
    handleLogoClick() {
      if (this.showSearchAndIcons) {
        this.$router.push('/postcontainer')
      }
    }
  }
})
</script>

<style scoped>
.top-bar {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  height: 100%;
  padding: 0.5rem 1.5rem;
}

.logo,
.search-bar,
.buttons {
  margin-left: 3em;
  margin-right: 3em;
}

.search-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.buttons {
  display: flex;
  align-items: center;
  justify-content: end;
}

.icon {
  margin-left: 1em;
  font-size: 2vw;
}

.v-menu__activator .icon {
  display: flex;
  align-items: center;
}

.menu-content {
  cursor: pointer;
  font-size: 1vw;
}

.v-list-item-title {
  font-size: 1vw;
}

.item-content {
  font-size: 1vw;
}
</style>
