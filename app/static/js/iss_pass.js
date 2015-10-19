var userCoords = document.getElementById("userCoords");

function showISSPassDates(lat, lon) {
  var url = "http://localhost:5000/api/v1/issposition/" + lat + "/" + lon;
  $.ajax({
    url: url,
    method: 'GET',
    beforeSend: function (XMLHttpRequest) {
      XMLHttpRequest.setRequestHeader("Accept", "application/json; odata=verbose");
    },

    cache: true,
    error: function (response) {
      console.log('no dice: ' + response);
    },
    success: function (response) {
      console.log(response);
      for (var date in response['dates']) {
        $('#isspass').append('<li>' + response['dates'][date] + '</li>');
      }
    }
  });
}

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var lat = position.coords.latitude;
      var lon = position.coords.longitude;

      document.getElementById("userLat").innerHTML = lat;
      document.getElementById("userLon").innerHTML = lon;
      showISSPassDates(lat, lon);
    });
  } else {
    userCoords.innerHTML = "Geolocation is not supported by this browser.";
  }
}

window.onload = getLocation();
