<template>
  <v-alert
    v-if="visible"
    type="success"
    dismissible
    @input="visible = false"
    :text="this.successMessage"
  ></v-alert>
  <div class="logo">
    <v-img src="/src/assets/iyte-logo-eng.png"></v-img>
  </div>
  <div class="text-fields">
    <v-card class="register-form" title="Register" variant="flat">
      <v-container>
        <v-text-field
          v-model="username"
          color="#9A1220"
          label="Username"
          variant="underlined"
        ></v-text-field>

        <v-text-field
          v-model="email"
          color="#9A1220"
          label="IZTECH Mail Address"
          variant="underlined"
        ></v-text-field>

        <v-text-field
          v-model="phone"
          color="#9A1220"
          label="Phone Number"
          variant="underlined"
        ></v-text-field>

        <v-text-field
          v-model="password1"
          color="#9A1220"
          label="Password"
          placeholder="Enter your password"
          type="password"
          variant="underlined"
        ></v-text-field>

        <v-text-field
          v-model="password2"
          color="#9A1220"
          label="Password Again"
          placeholder="Enter your password again"
          type="password"
          variant="underlined"
        ></v-text-field>

        <v-checkbox
          v-model="terms"
          color="#9A1220"
          label="I agree to site terms and conditions"
        ></v-checkbox>
      </v-container>

      <v-card-actions>
        <v-btn @click="this.register" class="button">
          Complete Registration
          <v-icon icon="mdi-chevron-right" end></v-icon>
        </v-btn>
      </v-card-actions>

      <v-card-actions>
        <v-btn @click="$emit('login-page')" class="button">
          Login
          <v-icon icon="mdi-chevron-right" end></v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    username: null,
    email: null,
    password1: null,
    password2: null,
    phone: null,
    terms: false,
    visible: false,
    successMessage: 'Please confirm your e-mail account. After that, you can go to Login page'
  }),

  methods: {
    async register() {
      if (!this.username || !this.email || !this.password1 || !this.password2 || !this.phone) {
        alert('Please fill all the fields')
        return
      }
      if (
        this.email.split('@')[1] !== 'iyte.edu.tr' &&
        this.email.split('@')[1] !== 'std.iyte.edu.tr'
      ) {
        alert('Please enter a valid IZTECH mail address')
        return
      }
      if (this.password1 !== this.password2) {
        alert('Passwords do not match')
        return
      }
      if (!this.terms) {
        alert('You must agree to the terms and conditions')
        return
      }
      await fetch('https://portaliyte-jq7n5xwowq-uc.a.run.app/api/user/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: this.username,
          phoneNumber: this.phone,
          email: this.email,
          password: this.password1
        })
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error('An error occurred during registration')
          }
          this.visible = true
          username = null
          email = null
          password1 = null
          password2 = null
          phone = null
          terms = false
          visible = false
        })
        .then((data) => {
          this.$emit('login-page', data)
        })
        .catch((error) => {
          console.error('An error occurred during registration:', error)
        })
    }
  }
}
</script>

<style scoped>
/*.register-container {
  height: 65vh;
  width: 25vw;
  margin: auto;
  padding: 2em;
  background-color: rgba(128, 128, 128, 0.1);
  border-radius: 10px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.25);
  display: flex;
  flex-direction: column;
}*/

.register-form {
  margin: auto;
  padding: 2em;
  display: flex;
  flex-direction: column;
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

:deep(.v-card-title) {
  font-size: 1.5vw;
  font-weight: bold;
}
</style>
