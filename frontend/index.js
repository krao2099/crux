const express = require('express');
const path = require('path');
const axios = require('axios');

const app = express();

app.engine('.html', require('ejs').__express);

app.use('/styles', express.static(path.join(__dirname, '/styles')));
app.use('/nav', express.static(path.join(__dirname, '/nav')));


app.use('/home', express.static(path.join(__dirname, '/home')));

app.get('/', (req, res) => {
  res.render(path.join(__dirname, 'home', 'home.html'));
});

app.get('/admin', async (req, res) => {
  try {
    let response = await axios.get('http://127.0.0.1:5000/check_admin', {
      withCredentials: true,
    });
    let data = response.data;
    if (data.Admin){
      res.sendFile(path.join(__dirname, 'admin', 'admin.html'));
    } else {
      res.redirect('/error');
    }
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
