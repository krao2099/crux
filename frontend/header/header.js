function login() {
    const data = {
      username: 'test',
      password: 'test1'
    };
    fetch('http://127.0.0.1:5000/login', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(data), // Convert the data to JSON format
    }).then(response => {
          if (!response.ok) {
              throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
      })
      .then(responseData => {
          // Handle the response data
          console.log('Response:', responseData);
      })
      .catch(error => {
          // Handle errors during the fetch
          console.error('Error:', error);
      });
}