<template>
    <div class="container">
      <div class="add-header">Settings</div>
      <div class="settings">
            <div class="setting-row" v-for="(setting, index) in settings" :key="index">
                <span>{{ setting.name }}</span>
                <label class="switch">
                <input type="checkbox" v-model="setting.enabled">
                <span class="slider round"></span>
                </label>    
            </div>
        </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        post: {
          topic: '',
          title: '',
          text: ''
        },
        settings: [
          { name: 'Setting 1', enabled: false },
          { name: 'Setting 2', enabled: false },
          { name: 'Setting 3', enabled: false },
          { name: 'Setting 4', enabled: false },
          { name: 'Setting 5', enabled: false }
        ]
      };
    },
    methods: {
      addImage() {
        // Logic to add image
      },
      submitPost() {
        // Logic to handle post submission
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

  .settings{
    display: flex;
    height: 80%;
    flex-direction: column;
    justify-content: space-evenly;
  }
  
  .setting-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 1vw;
  }
  
  .switch {
    position: relative;
    display: inline-block;
    width: 40px;
    height: 20px;
  }
  
  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  
  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    transition: 0.4s;
    border-radius: 34px;
  }
  
  .slider:before {
    position: absolute;
    content: "";
    height: 14px;
    width: 14px;
    left: 3px;
    bottom: 3px;
    background-color: white;
    transition: 0.4s;
    border-radius: 50%;
  }
  
  input:checked + .slider {
    background-color: #2196F3;
  }
  
  input:checked + .slider:before {
    transform: translateX(20px);
  }
  </style>
  