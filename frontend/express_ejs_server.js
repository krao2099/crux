const express = require('express');
const path = require('path');
const axios = require('axios');

const app = express();

app.engine('.html', require('ejs').__express);



app.use('/src', express.static(path.join(__dirname, '/src')));

app.use(express.static('public'));
app.use('/img', express.static('img'));

app.get('/', async (req, res) => {

  let config = {
    logged_in: false,
    admin: false
  }

  try {
    let response = await axios.get('https://127.0.0.1:5000/user_details', {
      withCredentials: true,
    });
    let data = response.data;
    console.log(data)
    config.logged_in = data.logged_in;
    config.admin = data.admin
  }  catch (error) {
    console.error('Error making request:', error);
    //res.redirect('/error'); FOR DEVELOPMENT COMMENT THIS OUT
  }

  res.render(path.join(__dirname, 'src', 'index.html'), config);
});

app.get('/error', (req, res) => {
  res.sendFile(path.join(__dirname, 'error', 'error.html'));
});



const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
