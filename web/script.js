const bars = document.querySelectorAll(".bar");

function handleBarClick(clickedBarId) {
  bars.forEach((bar) => {
    const barId = bar.id;
    const isSelected = barId === clickedBarId;
    console.log(barId, clickedBarId);
    bar.style.backgroundColor = isSelected
      ? "rgb(219, 211, 255)"
      : "transparent";
    if (isSelected) {
      bar_val = bar.innerHTML.trim();
    }
  });

  if (bar_val == "Status") {
    console.log("Status");
    document.getElementById("display1").style.display = "flex";
  } else {
    document.getElementById("display1").style.display = "none";
  }

  if (bar_val == "Logs") {
    console.log("Compass");
    document.getElementById("display2").style.display = "flex";
  } else {
    document.getElementById("display2").style.display = "none";
  }

  if (bar_val == "Mission") {
    console.log("Mission");
    document.getElementById("display3").style.display = "flex";
  } else {
    document.getElementById("display3").style.display = "none";
  }

  if (bar_val == "Drone") {
    console.log("Drone");
    document.getElementById("display4").style.display = "flex";
  } else {
    document.getElementById("display4").style.display = "none";
  }
}

async function connect() {
  await eel.connect_vehicle()();
}

document.getElementById("connect").addEventListener("click", connect);

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
    document.getElementById("alt-value").innerHTML =
      "Alt: " + rounded_output + " m";
  } else {
    document.getElementById("alt-value").innerHTML = "";
  }

  output = output * 18;
  document.getElementById("outer-circle-alt").style.transform =
    "rotate(" + output + "deg)";
}

async function check_status() {
  const output = await eel.check_status()();
  document.getElementById("status-value").innerHTML = output;
  // document.getElementById("status-value2").innerHTML = output;
}

async function Ground_speed() {
  output = await eel.ground_speed()();
  if (bar_val == "Status") {
    document.getElementById("speed-value").innerHTML =
      "Ground Speed: " + output.toFixed(1) + " m/s";
  } else {
    document.getElementById("speed-value").innerHTML = "";
  }

  output = output * 36;
  document.getElementById("outer-circle-speed").style.transform =
    "rotate(" + output + "deg)";
}

async function arm() {
  const output = await eel.check_armed()();
  if (output == true) {
    document.getElementById("arm-value").innerHTML = "True";
  } else {
    // document.getElementById("arm-value").innerHTML = "False";
  }
}

async function check_mode() {
  const output = await eel.check_mode()();
  document.getElementById("mode-value").innerHTML = output;
}

async function compass_calibration() {
  if (compass == true) {
    compass_value(); // document.getElementById("compass-value2").innerHTML = "True";
  } else {
    document.getElementById("compass-box").style.display = "none";
    document.get; // document.getElementById("compass-value2").innerHTML = "True";
    ElementsByClassName("compass")[0].innerHTML = "Compass Not Found";
    document.getElementById("compass-value2").innerHTML = "False";
  }
}

async function compass_value() {
  var output = await eel.compass()();
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
  document.getElementById("compass-img").style.transform =
    "translate(-50%, -50%) rotate(" + output + "deg)";
}

async function mission_check() {
  // const output = await eel.mission_check()();
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

async function roll() {
  var output = await eel.check_roll()();
  var rounded_output = output.toFixed(2);
  if (rounded_output == -0.0) {
    rounded_output = 0.0;
  }
  rounded_output = rounded_output * 60;
  document.getElementById("gyro-1-container").style.transform =
    "rotate(" + rounded_output + "deg)";
}

async function pitch() {
  var output2 = await eel.check_pitch()();
  var rounded_output = output2.toFixed(2);
  if (rounded_output == -0.0) {
    rounded_output = 0.0;
  }
  rounded_output = rounded_output * 66.66;
  g1 = document.getElementById("gyro-img1");
  g2 = document.getElementById("gyro-img2");

  g1.style.height = 100 + rounded_output + "%";
  g2.style.height = 100 - rounded_output + "%";
}

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

// location_coordinates();

setInterval(() => {
  check_altitude();
  check_battery();
  // check_temperature();
  check_status();
  check_mode();
  // compass_calibration();
  Ground_speed();
  arm();
  //   // version();
  //   // check_location();
  roll();
  pitch();
  //   // updateGyroMeter();
  compass_value();

}, 400)

mission_check();

async function calibrate(){
  await eel.calibrate_sensors()();
}

calibrate()

// async function log() {
//   await eel.logging_info()();
// }

// async function print_log() {
//   document.getElementById("log-bar-value").style.display = "flex";
//   var output = await eel.print_log()();
//   document.getElementById("log-bar-value").innerHTML = output;
// }

// setInterval(() => {
//   log();
// }, 10000);