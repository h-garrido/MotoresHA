let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -33.3905, lng: -70.5724 },
    zoom: 10,
  });
  new google.maps.Marker({
    position: {lat: -33.3905, lng: -70.5724},
    map,
    title: "Mazda CX-9",
  });
}

window.initMap = initMap;
