<template>
    <div class="chat-container">
      <div class="chat-header">
        <div class="user-icon"> 
           <v-icon class="user-icon">mdi-account-circle</v-icon>
        </div>
        <div class="user-name">userName</div>
      </div>
      <div class="chat-content">
        
      </div>
      <div class="chat-footer">
        <input type="text" class="chat-input" placeholder="TextBox"/>
        <button class="send-button">
            <v-icon>mdi-send</v-icon>
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ChatPage'
  }
  </script>
  
  <style scoped>
  .chat-container {
    display: flex;
    flex-direction: column;
    height: 90%;
    padding: 20px;
    border-radius: 10px;
    margin: 0 auto;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.25);
  }
  
  .chat-header {
    background-color: rgba(154, 18, 32, 0.8);
    display: flex;
    align-items: center;
    padding: 10px;
  }
  
  .user-icon {
    font-size: 24px;
    margin-right: 10px;
  }
  
  .user-name {
    font-size: 18px;
  }
  
  .chat-content {
    flex: 1;
    padding: 10px;
    background-color: #fff;
    overflow-y: auto;
  }
  
  .chat-footer {
    background-color: rgba(154, 18, 32, 0.8);
    display: flex;
    align-items: center;
    padding: 10px;
  }
  
  .chat-input {
    flex: 1;
    padding: 5px;
    border: none;
    border-radius: 5px;
  }
  
  .send-button {
    background: none;
    border: none;
    font-size: 20px;
    cursor: pointer;
    margin-left: 10px;
  }
  </style>
  