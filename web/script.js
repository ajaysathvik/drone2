const bars = document.querySelectorAll(".bar");
let bar_val = "";

function handleBarClick(clickedBarId) {
  bars.forEach((bar) => {
    const barId = bar.id;
    const isSelected = barId === clickedBarId;
    bar.style.backgroundColor = isSelected
      ? "rgb(219, 211, 255)"
      : "transparent";
    if (isSelected) {
      bar_val = bar.innerHTML.trim();
    }
  });
}

bars.forEach((bar) => {
  bar.addEventListener("click", () => handleBarClick(bar.id));
});

async function check_battery() {
  output = await eel.check_battery()();
  // console.log(output);
  document.getElementById("battery-value").innerHTML = output + "%";
  // document.getElementById("battery-value2").innerHTML = output + "%";
  if (output == 0) {
    output = 0;
  } else {
    output = (1.9 * output) / 100;
  }

  if (output < 0.45) {
    document.getElementById("battery-value-bar").style.backgroundColor =
      "#ff3b30 !important";
  } else if (output <= 1.125 && output > 0.45) {
    document.getElementById("battery-value-bar").style.backgroundColor =
      "#ffcc0a";
  }
  document.getElementById("battery-value-bar").style.width = output + "vw";
}

async function check_altitude() {
  var output = await eel.check_altitude()();
  rounded_output = output.toFixed(1);
  if (rounded_output == -0.0) {
    rounded_output = 0;
  }
  if (bar_val == "Status") {
    document.getElementById("altitude-value").innerHTML =
      "Alt: " + rounded_output + " m";
  } else {
    document.getElementById("altitude-value").innerHTML = "";
  }
  // document.getElementById("altitude-value2").innerHTML = rounded_output + " m";
  // document.getElementById("gyro-text1").innerHTML = rounded_output + " m";
}

async function check_status() {
  const output = await eel.check_status()();
  document.getElementById("status-value").innerHTML = output;
  // document.getElementById("status-value2").innerHTML = output;
}

async function Ground_speed() {
  const output = await eel.ground_speed()();
  if (bar_val == "Status") {
    document.getElementById("ground-speed-value").innerHTML =
      "Ground Speed: " + output.toFixed(1) + " m/s";
  } else {
    document.getElementById("ground-speed-value").innerHTML = "";
  }
}

async function arm() {
  const output = await eel.check_armed()();
  if (output == true) {
    document.getElementById("arm-value").innerHTML = "True";
  } else {
    // document.getElementById("arm-value").innerHTML = "False";
  }
}

async function version() {
  const output = await eel.version_major()();
  const output2 = await eel.version_minor()();
  // document.getElementById("version-value").innerHTML = output + "." + output2;
}

async function check_mode() {
  const output = await eel.check_mode()();
  document.getElementById("mode-value").innerHTML = output;
  // document.getElementById("mode-value2").innerHTML = output;
}

async function compass_calibration() {
  var compass = await eel.compass_calibration()();
  if (compass == true) {
    compass_value();
    // document.getElementById("compass-value2").innerHTML = "True";
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
  // document.getElementById("compass-needle").style.transform =
  //   "rotate(" + output + "deg)";
  // document.getElementsByClassName("compass-value")[0].innerHTML = a + "° " + b;
  document.getElementById("direction-value2").innerHTML = a + "° " + b;
}

async function mission_check() {
  const output = await eel.mission_check()();
  // if (output == 0) {
  //   const mission = document.getElementById("mission");
  //   // mission.innerHTML = "Mission Not Set";
  //   // button = mission.appendChild(document.createElement("button"));
  //   button.setAttribute("class", "action mission-button");
  //   button.appendChild(document.createElement("h4"));
  //   button.innerHTML = "Set Mission";
  //   button.addEventListener("click", async function () {
  //     document.getElementById("mission-window").style.display = "flex";
  //   });

  // button2 = mission.appendChild(document.createElement("button"));
  // button2.setAttribute("class", "mission-button map-button");
  // button2.appendChild(document.createElement("h4"));
  // button2.innerHTML = "Set Mission Using Map";
  // button2.addEventListener("click", async function () {
  //   document.getElementById("map-window").style.display = "flex";
  // });

  // document
  //   .getElementById("cancel-button")
  //   .addEventListener("click", async function () {
  //     document.getElementById("mission-window").style.opacity = "0";
  //   });

  // document
  //   .getElementById("confirm-button")
  //   .addEventListener("click", async function () {
  //     var lat = document.getElementById("lat").value;
  //     var lon = document.getElementById("lon").value;
  //     var alt = document.getElementById("alt").value;
  //     document.getElementById("mission-window").style.opacity = "0";
  //     const mission = document.getElementById("mission");
  //     mission.innerHTML =
  //       "lattitude: " +
  //       lat +
  //       "<br/>" +
  //       "longitude: " +
  //       lon +
  //       "<br/>" +
  //       "altitude: " +
  //       alt;
  //     document
  //       .getElementById("action-button")
  //       .addEventListener("click", async function () {
  //         await eel.set_status("ACTIVE")();
  //         await eel.set_mode("GUIDED")();
  //         await eel.set_mission(lat, lon, alt)();
  //       });
  //   });
}

// async function roll() {
//   var output = await eel.check_roll()();
//   var rounded_output = output.toFixed(2);
//   if (rounded_output == -0.0) {
//     rounded_output = 0.0;
//   }
//   rounded_output = rounded_output * -60;
//   document.getElementById("gyro-meter").style.transform =
//     "rotate(" + rounded_output + "deg)";
// }

// async function pitch() {
//   var output2 = await eel.check_pitch()();
//   var rounded_output = output2.toFixed(2);
//   if (rounded_output == -0.0) {
//     rounded_output = 0.0;
//   }
//   rounded_output = rounded_output * 60;
//   console.log(rounded_output);
//   document.getElementById("gyro-meter").style.transform =
//     "TranslateY(" + rounded_output + "px)";
// }

async function updateGyroMeter() {
  try {
    // Get roll and pitch values concurrently
    const [rollOutput, pitchOutput] = await Promise.all([
      eel.check_roll()(),
      eel.check_pitch()(),
    ]);

    // Process roll value
    const roundedRoll = rollOutput.toFixed(2);
    if (roundedRoll === "-0.0") {
      roundedRoll = "0.0";
    }
    const rollDegrees = roundedRoll * -60;

    // Process pitch value
    const roundedPitch = pitchOutput.toFixed(2);
    if (roundedPitch === "-0.0") {
      roundedPitch = "0.0";
    }
    const pitchPixels = roundedPitch * 60;

    // Apply transformations to the element
    const gyroMeter = document.getElementById("gyro-meter");
    gyroMeter.style.transform = `rotate(${rollDegrees}deg) translateY(${pitchPixels}px)`;
  } catch (error) {
    console.error("Error updating gyro meter:", error);
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

  // const map = new google.maps.Map(document.getElementById("map"), {
  //   center: { lat: latitude, lng: longitude },
  //   zoom: 8,
  // });

  // // Create a marker for the specified location
  // const marker = new google.maps.Marker({
  //   position: { lat, lng },
  //   map: map,
  // });

  // // Optionally, add a custom popup to the marker
  // const content = "This is my point!";
  // const infoWindow = new google.maps.InfoWindow({
  //   content,
  // });

  // marker.addListener("click", () => {
  //   infoWindow.open(map, marker);
  // });
}

location_coordinates();

setInterval(() => {
  check_altitude();
  check_battery();
  // check_temperature();
  check_status();
  check_mode();
  // compass_calibration();
  Ground_speed();
  // arm();
  // version();
  // check_location();
  // roll();
  // pitch();
  // updateGyroMeter();
}, 100);

mission_check();
