<template>
    <div class="container">
      <div class="report-content">
        <div class="report-header">Report</div>
        <form @submit.prevent="submitReport">
        <div>
          <label for="issue" class="input-header">Report Issue</label>
          <select id="issue" v-model="Report.issue">
            <option value="spam">Spam</option>
            <option value="harassment">Harassment</option>
            <option value="misinformation">Misinformation</option>
            <option value="other">Other</option>
          </select>
        </div>
          <div>
            <label for="text" class="input-header">Description</label>
            <textarea id="text" v-model="Report.text"></textarea>
          </div>
          <div class="bottom-container">
              <button type="submit">Report</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        Report: {
          issue: '',
          text: ''
        }
      };
    },
    methods: {
      reportImage() {
        console.log('Image reported', this.Report);
      },
      submitReport() {
        console.log('Report submitted:', this.Report);
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    height: 50%;
    width: 70%;
    padding: 20px;
    border-radius: 10px;
    margin: 0 auto;
    background-color: rgba(128, 128, 128, 0.1);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.25);
  }
  
  .report-header{
    text-align: start;
    margin-bottom: 20px;
    font-size: 1.5vw;
    font-weight: bold;
  }

  .input-header{
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
    background: #fff;
  } 
  
  textarea {
    resize: vertical;
    height: 100px;
  }

  .bottom-container{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
  
  .report-images {
    width: 20%;
    display: flex;
    font-size: 1vw;
    flex-direction: column;
  }
  
  .report-images button {
    width: 30px;
    height: 30px;
    font-size: 20px;
    margin-left: 10px;
    cursor: pointer;
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

  .report-icon{
    font-size: 2vw;
  }

  select {
    width: 50%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1vw;
    background-color: #fff;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
  }

  select:focus {
    outline: none;
    border-color: #aaa;
  }

  select option {
    padding: 10px;
  }
  </style>
  