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

//Functions handling user log in and log out
const loginButton = document.getElementById('login-button');
const loginDiv = document.getElementById('login');
const createAccountButton = document.getElementById('create-account-button');
const createAccountDiv = document.getElementById('create-account');

function loginClick() {
    console.log("click");
    loginDiv.style.display = 'flex';
    createAccountDiv.style.display = 'none';

}

function createAccountClick() {
    console.log("click");
    loginDiv.style.display = 'none';
    createAccountDiv.style.display = 'flex';
}

loginButton.addEventListener('click', loginClick);
createAccountButton.addEventListener('click', createAccountClick)

getLocation();