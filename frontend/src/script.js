const BASE_URL = "http://localhost/api/";
const MIN_USERNAME_LENGTH = 2
const MAX_USERNAME_LENGTH = 50
const MIN_PASSWORD_LENGTH = 8
const USERNAME_REGEX = /^[a-zA-Z0-9]*$/;
const EMAIL_REGEX = /^\S+@\S+\.\S+$/;
const PASSWORD_REGEX = /^^(?=.*[a-z])(?=.*[0-9])(?=.*\W).*$/;

/**
 * Abstract post to server
 * @param {*} route route to call
 * @param {*} payload json payload
 * @returns 
 */
async function post_crux_server_call(route, payload) {
  var response;
  try {
    response = await fetch(BASE_URL + route, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: payload,
      });
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      var data = await response.json();
      return data;
  } catch(error) {
    console.error(error);
    return {
        error: 'Encountered unknown error'
    }
  }
}

/**
 * Reuseable debounce code
 * @param {*} function to debounce 
 * @param {*} delay delay to wait
 * @returns timeout
 */
function debounce(func, delay = 1000) {
  let timeout;

  return (...args) => {
    clearTimeout(timeout)
    timeout = setTimeout(() => {
      func(...args)
    }, delay)
  }
}

// config map
let config = {
    minZoom: 7,
    maxZoom: 18,
  };
  // magnification with which the map will start
  const zoom = 18;
  // co-ordinates
  const lat = 52.22977;
  const lng = 21.01178;
  
  // calling map
  const map = L.map("map", config).setView([lat, lng], zoom);
  
  // Used to load and display tile layers on the map
  // Most tile servers require attribution, which you can set under `Layer`
  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);
//Config map

//Side nav

  // --------------------------------------------------
  // sidebar
  
  const menuItems = document.querySelectorAll(".menu-item");
  const sidebar = document.querySelector(".sidebar");
  const buttonClose = document.querySelector(".close-button");
  
  menuItems.forEach((item) => {
    item.addEventListener("click", (e) => {
      const target = e.target;
  
      if (
        target.classList.contains("active-item") ||
        !document.querySelector(".active-sidebar")
      ) {
        document.body.classList.toggle("active-sidebar");
      }
  
      // show content
      showContent(target.dataset.item);
      // add active class to menu item
      addRemoveActiveItem(target, "active-item");
    });
  });
  
  // close sidebar when click on close button
  buttonClose.addEventListener("click", () => {
    closeSidebar();
  });
  
  // remove active class from menu item and content
  function addRemoveActiveItem(target, className) {
    const element = document.querySelector(`.${className}`);
    target.classList.add(className);
    if (!element) return;
    element.classList.remove(className);
  }
  
  // show specific content
  function showContent(dataContent) {
    const idItem = document.querySelector(`#${dataContent}`);
    addRemoveActiveItem(idItem, "active-content");
  }
  
  // --------------------------------------------------
  // close when click esc
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      closeSidebar();
    }
  });
  
  // close sidebar when click outside
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".sidebar")) {
      closeSidebar();
    }
  });
  
  // --------------------------------------------------
  // close sidebar
  
  function closeSidebar() {
    document.body.classList.remove("active-sidebar");
    const element = document.querySelector(".active-item");
    const activeContent = document.querySelector(".active-content");
    if (!element) return;
    element.classList.remove("active-item");
    activeContent.classList.remove("active-content");
  }
//Side nav bar

  
//Functions handling user log in and log out and sign up
  const loginButton = document.getElementById('login-button');
  const loginDiv = document.getElementById('login');
  const createAccountButton = document.getElementById('create-account-button');
  const createAccountDiv = document.getElementById('create-account');
  
  function loginClick() {
    loginDiv.style.display = 'flex';
    createAccountDiv.style.display = 'none';
    
  }
  
  function createAccountClick() {
    loginDiv.style.display = 'none';
    createAccountDiv.style.display = 'flex';
  }

  if (loginButton) {
    loginButton.addEventListener('click', loginClick);
  }

  function checkUsernameError(text) {
    var error = document.getElementById("username-error");
    if (text.length < MIN_USERNAME_LENGTH || text.length > MAX_USERNAME_LENGTH) {
        error.innerHTML = "Invalid username length, must be between 2 and 50 characters";
        return true;
    } else if (!USERNAME_REGEX.test(text)) {
        error.innerHTML = "Invalid username, must only contain letters or numbers";
        return true;
    } else {
        error.innerHTML = "";
        return false;
    }
  }

  function checkEmailError(text){
    var error = document.getElementById("email-error");
    if (!EMAIL_REGEX.test(text)) {
        error.innerHTML = "Invalid email";
        return true;
    } else {
        error.innerHTML = "";
        return false;
    }
  }

  function checkPasswordError(text) {
    var error = document.getElementById("password-error");
    if (text.length < MIN_PASSWORD_LENGTH) {
        error.innerHTML = "Invalid password length, must be greater than 8 characters";
        return true;
    } else if (!PASSWORD_REGEX.test(text)) {
        error.innerHTML = "Invalid password, must contain at least one letter, digit, and special character";
        return true;
    } else {
        error.innerHTML = "";
        return false;
    }
  }

  function checkConfirmPasswordError(text) {
    var error = document.getElementById("confirm-password-error");
    var password = document.getElementById("create_password").value;
    if (text != password) {
        error.innerHTML = "Passwords do not match";
        return true;
    } else {
        error.innerHTML = "";
        return false;
    }
}

  if (createAccountButton) {
    createAccountButton.addEventListener('click', createAccountClick);
    document.getElementById("create_username").addEventListener("input", e => {
        debounce(text => checkUsernameError(text))(e.target.value);
    })
    document.getElementById("create_email").addEventListener("input", e => {
        debounce(text => checkEmailError(text))(e.target.value);
    })
    document.getElementById("create_password").addEventListener("input", e => {
        debounce(text => checkPasswordError(text))(e.target.value);
    })
    document.getElementById("create_password_confirm").addEventListener("input", e => {
        debounce(text => checkConfirmPasswordError(text))(e.target.value);
    })
  }
  
  async function login(event) {
    event.preventDefault()
    let formData = {
      username: document.getElementById("login_username").value,
      password: document.getElementById("login_password").value
    };
    let response = await post_crux_server_call("login", JSON.stringify(formData))
    if (response.success) {
      window.location.reload();
    } else {
      alert(response.error);
    }
  }
  
  async function createUser(event) {
    event.preventDefault()
    var formData = {
      username: document.getElementById("create_username").value,
      email: document.getElementById("create_email").value,
      password: document.getElementById("create_password").value
    };

    var confirmPassword = document.getElementById("create_password_confirm").value;

    if(!checkUsernameError(formData.username) 
        && !checkEmailError(formData.email) 
        && !checkPasswordError(formData.password) 
        && !checkConfirmPasswordError(confirmPassword)){
        
        let response = await post_crux_server_call("user", JSON.stringify(formData))
        if (response.success) {
            window.location.reload();
        } else {
            alert(response.error);
        }
    } else {
        document.getElementById("submit-error").innerHTML = "Error submitting form, please check all fields";
    }
  }
  
  async function logout() {
    let response = await post_crux_server_call("logout", null);
  if (response.success) {
    window.location.reload();
  } else {
    alert(response.error);
  }
}
//End of login code

//Geolocation code
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;

    //alert("Latitude: " + latitude + "\nLongitude: " + longitude);
    map.setView([latitude, longitude], 13);

    var marker = L.marker([latitude, longitude]).addTo(map);

    marker.bindPopup("<b>Hello!</b><br>You are here!").openPopup();
}

function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            alert("User denied the request for Geolocation.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Location information is unavailable.");
            break;
        case error.TIMEOUT:
            alert("The request to get user location timed out.");
            break;
        case error.UNKNOWN_ERROR:
            alert("An unknown error occurred.");
            break;
    }
}
getLocation();
//End of geolocation code.