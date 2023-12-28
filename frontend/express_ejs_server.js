const express = require('express');
const path = require('path');
const axios = require('axios');
const cookieParser = require('cookie-parser');

const app = express();

app.engine('.html', require('ejs').__express);
app.use(cookieParser());



app.use('/src', express.static(path.join(__dirname, '/src')));

app.use(express.static('public'));
app.use('/img', express.static('img'));

app.get('/', async (req, res) => {

  let config = {
    logged_in: false,
    admin: false
  }
  let user_data = {
    user_id: req.cookies.user_id
  }
  try {
    let response = await axios.get('http://server:5000/user_details', {
      params: user_data,
      headers: {
        'Content-Type': 'application/json',
      },
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
