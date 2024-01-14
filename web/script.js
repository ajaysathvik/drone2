async function check_battery() {
  var output = await eel.check_battery()();
  document.getElementById("battery-value").innerHTML = output + "%";
  document.getElementById("battery-value2").innerHTML = output + "%";
  if (output == 0) {
    output = 0;
  } else {
    output = (2.25 * output) / 100;
    console.log(output);
  }

  if (output < 0.45) {
    document.getElementById("battery-value-bar").style.backgroundColor =
      "#ff3b30";
  } else if (output <= 1.125 && output > 0.45) {
    document.getElementById("battery-value-bar").style.backgroundColor =
      "#ffcc0a";
  }
  document.getElementById("battery-value-bar").style.width = output + "vw";
}

async function check_altitude() {
  var output = await eel.check_altitude()();
  rounded_output = output.toFixed(2);
  if (output < 0) {
    rounded_output = 0;
  }
  document.getElementById("altitude-value").innerHTML = rounded_output + " m";
  document.getElementById("altitude-value2").innerHTML = rounded_output + " m";
  document.getElementById("gyro-text1").innerHTML = rounded_output + " m";
  output = -(output / 4) - 19.4;
  document.getElementById("gyro-value1").style.transform =
    "translateY(" + output + "vh)";
}

async function check_roll() {
  const output = await eel.check_roll()();
  rounded_output = output.toFixed(2);
  if (rounded_output == -0.0) {
    rounded_output = 0.0;
  }
  document.getElementById("gyro-text2").innerHTML = rounded_output + " °";
  document.getElementById("gyro-value2").style.transform =
    "translate(0vw, -39.5vh) rotate(" + output + "deg)";
}

async function check_temperature() {
  const output = await eel.check_temperature()();
  document.getElementById("temperature-value").innerHTML = output + " °C";
  document.getElementById("temperature-value2").innerHTML = output + " °C";
}

async function check_status() {
  const output = await eel.check_status()();
  document.getElementById("status-value").innerHTML = output;
  document.getElementById("status-value2").innerHTML = output;
}

async function Ground_speed() {
  const output = await eel.ground_speed()();
  document.getElementById("ground-speed-value").innerHTML =
    output.toFixed(1) + " m/s";
}

async function arm() {
  const output = await eel.check_armed()();
  if (output == true) {
    document.getElementById("arm-value").innerHTML = "True";
  } else {
    document.getElementById("arm-value").innerHTML = "False";
  }
}

async function version() {
  const output = await eel.version_major()();
  const output2 = await eel.version_minor()();
  document.getElementById("version-value").innerHTML = output + "." + output2;
}

async function check_mode() {
  const output = await eel.check_mode()();
  document.getElementById("mode-value").innerHTML = output;
  document.getElementById("mode-value2").innerHTML = output;
}

async function compass_calibration() {
  var compass = await eel.compass_calibration()();
  if (compass == true) {
    compass_value();
    document.getElementById("compass-value2").innerHTML = "True";
  } else {
    document.getElementById("compass-box").style.display = "none";
    document.getElementsByClassName("compass")[0].innerHTML =
      "Compass Not Found";
    document.getElementById("compass-value2").innerHTML = "False";
  }
}

async function compass_value() {
  output = await eel.compass()();
  a = output % 90;
  b = Math.floor(output / 90);
  if (b == 0) {
    b = "N";
  } else if (b == 1) {
    b = "E";
  } else if (b == 2) {
    b = "S";
  } else if (b == 3) {
    b = "W";
  }
  output = output - 45;
  document.getElementById("compass-needle").style.transform =
    "rotate(" + output + "deg)";
  document.getElementsByClassName("compass-value")[0].innerHTML = a + "° " + b;
  document.getElementById("direction-value2").innerHTML = a + "° " + b;
}

async function mission_check() {
  const output = await eel.mission_check()();
  if (output == 0) {
    const mission = document.getElementById("mission");
    mission.innerHTML = "Mission Not Set";
    button = mission.appendChild(document.createElement("button"));
    button.setAttribute("class", "action mission-button");
    button.appendChild(document.createElement("h4"));
    button.innerHTML = "Set Mission";
    button.addEventListener("click", async function () {
      document.getElementById("mission-window").style.display = "flex";
    });

    button2 = mission.appendChild(document.createElement("button"));
    button2.setAttribute("class", "mission-button map-button");
    button2.appendChild(document.createElement("h4"));
    button2.innerHTML = "Set Mission Using Map";
    button2.addEventListener("click", async function () {
      document.getElementById("map-window").style.display = "flex";
    });

    document
      .getElementById("cancel-button")
      .addEventListener("click", async function () {
        document.getElementById("mission-window").style.opacity = "0";
      });

    document
      .getElementById("confirm-button")
      .addEventListener("click", async function () {
        var lat = document.getElementById("lat").value;
        var lon = document.getElementById("lon").value;
        var alt = document.getElementById("alt").value;
        document.getElementById("mission-window").style.opacity = "0";
        const mission = document.getElementById("mission");
        mission.innerHTML =
          "lattitude: " +
          lat +
          "<br/>" +
          "longitude: " +
          lon +
          "<br/>" +
          "altitude: " +
          alt;
        document
          .getElementById("action-button")
          .addEventListener("click", async function () {
            await eel.set_status("ACTIVE")();
            await eel.set_mode("GUIDED")();
            await eel.set_mission(lat, lon, alt)();
          });
      });
  }
}

async function check_location() {
  latitude = await eel.check_location_lat()();
  longitude = await eel.check_location_lon()();
  document.getElementById("latitude-value2").innerHTML = latitude.toFixed(5);
  document.getElementById("longitude-value2").innerHTML = longitude.toFixed(5);
}

async function location_coordinates() {
  latitude = await eel.check_location_lat()();
  longitude = await eel.check_location_lon()();
  const map = L.map("map").setView([latitude, longitude], 13);
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "",
  }).addTo(map);
  let markers = [];

  newmarker = L.marker([latitude, longitude]);
  newmarker.addTo(map);
  markers.push(newmarker);
  newmarker.setIcon(
    L.icon({
      iconUrl: "./assests/camera-drone (2).png",
      iconSize: [40, 40],
      iconAnchor: [20, 20],
    })
  );

  let line = L.polyline([], { color: "red" }).addTo(map);

  map.on("click", (e) => {
    const newMarker = L.marker(e.latlng).addTo(map);
    markers.push(newMarker);
    if (markers.length > 1) {
      var lastMarker = markers[markers.length - 2];
      const lastLatLng = lastMarker.getLatLng();
      line.addLatLng(lastLatLng);
    }
    const lastLatLng = newMarker.getLatLng();
    line.addLatLng(lastLatLng);
  });

  setInterval(async () => {
    if (markers.length > 1) {
      document.getElementsByClassName("map-button")[0].style.display = "flex";
    }
    var latitude = await eel.check_location_lat()();
    var longitude = await eel.check_location_lon()();
    newmarker.setLatLng([latitude, longitude]);
  }, 100);

  document
    .getElementsByClassName("map-button")[0]
    .addEventListener("click", async function () {
      await eel.set_status("ACTIVE")();
      await eel.set_mode("GUIDED")();
      for (let i = 1; i < markers.length;i++ ) {
        var lat = markers[i]._latlng.lat;
        var lon = markers[i]._latlng.lng;
        console.log(lat);
        console.log(lon);
        await eel.set_mission(lat, lon, 10)();
        // while (true) {
        //   latitude = await eel.check_location_lat()();
        //   longitude = await eel.check_location_lon()();
        //   if (
        //     latitude.toFixed(4) == lat.toFixed(4) &&
        //     longitude.toFixed(4) == lon.toFixed(4)
        //   ) {
        //     if (i >= 2) {
        //       markers.splice(i - 1, i);
        //     }
        //     i++;
        //     break;
        //   }
        // }
        const coordinateTolerance = 0.0001; // Adjust the tolerance as needed

        while (true) {
          latitude = await eel.check_location_lat()();
          longitude = await eel.check_location_lon()();

          if (
            Math.abs(latitude - lat) < coordinateTolerance &&
            Math.abs(longitude - lon) < coordinateTolerance
          ) {
            // if (i >= 2) {
            //   markers.splice(i - 3, 1); // Fix for removing only one element
            // }
            // i++;
            break;
          }

          // Introduce a delay or yield control to prevent blocking the event loop
          await new Promise((resolve) => setTimeout(resolve, 100));
        }
      }
    });
}

location_coordinates();

setInterval(() => {
  check_altitude();
  check_battery();
  check_temperature();
  check_status();
  check_mode();
  compass_calibration();
  Ground_speed();
  arm();
  version();
  check_roll();
  check_location();
}, 100);

mission_check();
