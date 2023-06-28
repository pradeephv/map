// Initialize the map asynchronously
function initMap() {
  const directionsRenderer = new google.maps.DirectionsRenderer();
  const directionsService = new google.maps.DirectionsService();

  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 14,
    center: { lat: 37.77, lng: -133.1447 },
  });

  directionsRenderer.setMap(map);

  const startBtn = document.getElementById("startBtn");

  // Event listener for the start button
  startBtn.addEventListener("click", () => {
    calculateAndDisplayRoute(directionsService, directionsRenderer);
  });

  // Add autocomplete to origin and destination input fields
  const autocompleteOrigin = new google.maps.places.Autocomplete(
    document.getElementById("from")
  );
  const autocompleteDestination = new google.maps.places.Autocomplete(
    document.getElementById("to")
  );
}

// Calculate and display the route

function calculateAndDisplayRoute(directionsService, directionsRenderer) {
  const selectedMode = document.getElementById("mode").value;
  const origin = document.getElementById("from").value;
  const destination = document.getElementById("to").value;

  console.log(origin)
  console.log(destination)
  directionsService.route(
    {
      origin: origin,
      destination: destination,
      travelMode: google.maps.TravelMode[selectedMode],
    },
    (response, status) => {
      if (status === "OK") {
        directionsRenderer.setDirections(response);

        // Display time required and distance
        const route = response.routes[0];
        const timeRequired = route.legs[0].duration.text;
        const distance = route.legs[0].distance.text;

        document.querySelector(".TimeRequired").textContent =
          "Time Required: " + timeRequired;
        document.querySelector(".km").textContent = "Distance: " + distance;
      } else {
        window.alert("Direction request failed: " + status);
      }
    }
  );
}
