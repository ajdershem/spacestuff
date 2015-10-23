function showISSPassDates(lat, lon) {
  var base_url = window.location.origin;
  var url = base_url + "/api/v1/issposition/" + lat + "/" + lon;
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
      for (var item in response['dates']) {
        var date = response['dates'][item]['date'];
        var time = response['dates'][item]['time'];
        $('#issPassTable').append('<tr><td>' + date + '</td>' + '<td>' + time + '</td></tr>');
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
      },
      function (error){
        console.log(error.message);
      },
      {
        timeout: 100,
        enableHighAccuracy: true
      }
    );
  } else {
    var issPass = document.getElementById("issPass");
    issPass.innerHTML = "Geolocation is not supported by this browser.";
  }
}

window.onload = getLocation();
