const express = require('express');
const path = require('path');
const axios = require('axios');

const app = express();

// Serve static files from the "public" folder
//app.use(express.static(path.join(__dirname, 'public')));

// Define a route for the root URL
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'home', 'home.html'));
});

app.get('/admin', async (req, res) => {
  try {
    let response = await axios.get('http://127.0.0.1:5000/check_admin');
    let data = response.data;
    if (data.Admin){
      res.sendFile(path.join(__dirname, 'admin', 'admin.html'));
    }
    res.redirect('/error');
  }  catch (error) {
    console.error('Error making request:', error);
    res.redirect('/error');
  }
});

app.get('/error', (req, res) => {
  res.sendFile(path.join(__dirname, 'error', 'error.html'));
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
