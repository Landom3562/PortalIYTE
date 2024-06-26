<template>
  <div>
    <v-alert
      v-if="visible"
      type="error"
      dismissible
      @input="visible = false"
      :text="this.errorMessage"
    >
    </v-alert>
    <div class="login-container">
      <div class="text-fields">
        <v-card class="register-form" title="Login" variant="outline">
          <v-container>
            <v-text-field @keyup.enter="login"
              v-model="phoneNumber"
              color="#9A1220"
              label="Phone Number"
              variant="underlined"
            ></v-text-field>

            <v-text-field @keyup.enter="login"
              v-model="password"
              color="#9A1220"
              label="Password"
              placeholder="Enter your password"
              type="password"
              variant="underlined"
            ></v-text-field>
          </v-container>

          <v-card-actions>
            <v-btn class="button" @click="this.login">
              Login <v-icon icon="mdi-chevron-right" end></v-icon>
            </v-btn>
          </v-card-actions>
          <v-card-actions>
            <v-btn class="button" @click="$emit('register-page')">
              Register <v-icon icon="mdi-chevron-right" end></v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </div>
    </div>
  </div>
</template>

<script>
import VueCookies from 'vue-cookies'

export default {
  data: () => ({
    visible: false,
    errorMessage: '',
    phoneNumber: null,
    password: null
  }),
  methods: {
    async login() {
      await fetch('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/user/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          phoneNumber: this.phoneNumber,
          password: this.password
        })
      })
        .then(async (response) => {
          if (!response.ok) {
            this.errorMessage = await response.text()
            this.visible = true
            throw new Error(response.text())
          }
          return response.json()
        })
        .then((data) => {
          console.log('Login successful:', data)
          VueCookies.set('user', data.id, '4w')
          this.$emit('succesfully-login', data)
        })
        .catch((error) => {
          console.error('An error occurred during login:', error)
        })
    }
  }
}
</script>

<style scoped>
.login-container {
  max-width: 80%;
  margin: auto;
  display: flex;
  flex-direction: column;
}

.register-form {
  padding: 2em;
  box-shadow: none;
  height: 100%;
}

.button {
  color: white;
  background-color: #9a1220;
  padding: 0.5em 1em;
  margin: 0.5em 0;
  border-radius: 5px;
}

.button:hover {
  background-color: #7f0e1a;
}

.v-text-field {
  margin-bottom: 1.5em;
}

:deep(.v-card-title) {
  font-size: 1.5vw;
  font-weight: bold;
}
</style>
