const express = require('express');
const path = require('path');
const axios = require('axios');
const cookieParser = require('cookie-parser');

const app = express();

app.engine('.html', require('ejs').__express);
app.use(cookieParser());



app.use('/src', express.static('src'));

app.use('/img', express.static('img'));
app.use('/leaflet', express.static('node_modules/leaflet/dist'));

app.get('/', async (req, res) => {

  let config = {
    logged_in: false,
    admin: false,
    username: "",
  }
  let user_id = req.cookies.user_id || null
  try {
    let response = await axios.get('http://server:5000/user_details', {
      headers: {
        'Content-Type': 'application/json',
        'Cookie': `user_id=${user_id}`,
      },
    });
    let data = response.data;
    console.log(data)
    config.logged_in = data.logged_in;
    config.admin = data.admin;
    config.username = data.username;
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
