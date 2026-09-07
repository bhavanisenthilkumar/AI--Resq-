// ===============================
// AI-ResQ - Frontend JavaScript
// ===============================


// START MISSION
async function startMission() {

    const status = document.getElementById("missionStatus");

    status.innerText = "🔄 Connecting to AI-ResQ Backend...";

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/api/status"
        );

        const data = await response.json();

        if (data.status === "Active") {

            alert("🚁 AI-ResQ Mission Started!");

            status.innerText =
                "🚁 Mission Status: DRONE SCANNING...";

            setTimeout(() => {
                status.innerText =
                    "🤖 AI Detection: SEARCHING FOR SURVIVORS...";
            }, 2000);

            setTimeout(() => {
                status.innerText =
                    "🚨 Survivor Detected: S1 — HIGH PRIORITY";
            }, 4000);

            setTimeout(() => {
                status.innerText =
                    "🗺️ Rescue Route Calculated — MISSION ACTIVE";
            }, 6000);
        }

    } catch (error) {

        status.innerText =
            "❌ Backend Connection Failed";

        console.error(error);
    }
}


// ===============================
// DRONE SCANNING
// ===============================

function startScanning() {

    const droneStatus =
        document.getElementById("droneStatus");

    const progress =
        document.getElementById("scanProgress");

    droneStatus.innerText = "SCANNING...";

    let value = 0;

    const scan = setInterval(function () {

        value += 10;

        progress.innerText = value + "%";

        if (value >= 100) {

            clearInterval(scan);

            droneStatus.innerText =
                "SCAN COMPLETED ✅";
        }

    }, 500);
}


// ===============================
// AI SURVIVOR DETECTION
// ===============================

function detectSurvivor() {

    const status =
        document.getElementById("detectionStatus");

    const count =
        document.getElementById("survivorCount");

    const message =
        document.getElementById("survivorMessage");

    status.innerText = "SEARCHING...";

    setTimeout(function () {

        status.innerText =
            "SURVIVOR DETECTED ✅";

        count.innerText = "1";

        message.innerText =
            "🚨 Survivor S1 detected — Rescue Required!";

    }, 2000);
}


// ===============================
// PRIORITY ASSESSMENT
// ===============================

function analyzePriority() {

    const result =
        document.getElementById("priorityResult");

    result.innerText =
        "🤖 AI Analyzing Survivor Priorities...";

    setTimeout(function () {

        result.innerText =
            "🚨 Highest Priority: S1 — CRITICAL — HIGH PRIORITY";

    }, 2000);
}


// ===============================
// RESCUE ROUTE
// ===============================

function calculateRoute() {

    const routeStatus =
        document.getElementById("routeStatus");

    const routeDistance =
        document.getElementById("routeDistance");

    routeStatus.innerText =
        "CALCULATING...";

    setTimeout(function () {

        routeDistance.innerText =
            "520 m";

        routeStatus.innerText =
            "ROUTE READY ✅";

    }, 2000);
}
// =========================================
// RESCUE TEAM COMMUNICATION
// =========================================

function notifyRescueTeam() {

    const status = document.getElementById("teamStatus");
    const message = document.getElementById("teamMessage");

    status.innerText = "SENDING ALERT...";

    message.innerText = "📡 Sending survivor information to Rescue Team...";

    setTimeout(function () {

        status.innerText = "TEAM NOTIFIED ✅";

        message.innerText =
            "🚨 Rescue Team Alert Sent! S1 — Critical survivor located. Immediate rescue required.";

        alert("📡 Rescue Team has been notified!");

    }, 2000);
}
// =========================================
// EMERGENCY KIT DELIVERY
// =========================================

function deliverEmergencyKit() {

    const status = document.getElementById("kitStatus");
    const distance = document.getElementById("kitDistance");
    const message = document.getElementById("kitMessage");

    status.innerText = "🚁 DRONE LOADING KIT...";
    message.innerText = "📦 Preparing Emergency Medical Kit for S1...";

    setTimeout(function () {

        status.innerText = "🚁 FLYING TO S1...";
        message.innerText = "📡 Drone is delivering the emergency kit...";

    }, 2000);

    setTimeout(function () {

        status.innerText = "📦 KIT DELIVERED ✅";
        distance.innerText = "0 m";

        message.innerText =
            "🚨 Emergency Medical Kit successfully delivered to Survivor S1.";

        alert("📦 Emergency Kit Delivered to S1!");

    }, 5000);
}
// =========================================
// MEDICAL AI ROBOT
// =========================================

function dispatchMedicalRobot() {

    const status = document.getElementById("robotStatus");
    const distance = document.getElementById("robotDistance");
    const support = document.getElementById("medicalSupport");
    const message = document.getElementById("robotMessage");

    status.innerText = "🤖 DISPATCHING...";
    support.innerText = "PREPARING";
    message.innerText =
        "🤖 Medical AI Robot is being dispatched to critical survivor S1.";

    setTimeout(function () {

        status.innerText = "🤖 MOVING TO S1...";
        distance.innerText = "60 m";
        support.innerText = "EN ROUTE";
        message.innerText =
            "🚑 Robot is moving towards Survivor S1.";

    }, 2000);

    setTimeout(function () {

        status.innerText = "📍 ARRIVED AT S1";
        distance.innerText = "0 m";
        support.innerText = "READY";

        message.innerText =
            "🤖 Medical Robot reached S1. Beginning simulated first-aid assistance...";

    }, 4000);

    setTimeout(function () {

        status.innerText = "✅ ASSISTANCE COMPLETED";
        support.innerText = "STABILIZED";

        message.innerText =
            "🩺 Simulated medical assistance completed. Survivor S1 is ready for rescue team evacuation.";

        alert("🤖 Medical AI Robot completed simulated assistance!");

    }, 6500);
}

// ===============================
// SAVE MISSION → SQLITE DATABASE
// ===============================

async function saveMission() {

    const message =
        document.getElementById("recordMessage");

    message.innerHTML =
        "<p>💾 Saving mission...</p>";

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/api/save-mission",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    survivor: "S1",

                    condition: "Critical",

                    priority: "HIGH",

                    distance: "120 m",

                    status: "RESCUED"
                })
            }
        );

        const data = await response.json();

        message.innerHTML =
            "<p>💾 " +
            data.message +
            " ✅</p>" +
            "<p>Survivor: S1 | Priority: HIGH | Status: RESCUED</p>";

    } catch (error) {

        message.innerHTML =
            "<p>❌ Failed to save mission</p>";

        console.error(error);
    }
}


// ===============================
// VIEW MISSION RECORDS
// ===============================

async function viewRecords() {

    const message =
        document.getElementById("recordMessage");

    message.innerHTML =
        "<p>🔄 Loading mission records...</p>";

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/api/missions"
        );

        const records = await response.json();

        if (records.length === 0) {

            message.innerHTML =
                "<p>📋 No mission records found.</p>";

            return;
        }

        let html =
            "<h3>📋 Mission Records</h3>";

        records.forEach(function (record) {

            html +=
                "<p>" +
                "🆔 " + record.id +
                " | 🚨 " + record.survivor +
                " | " + record.condition +
                " | " + record.priority +
                " | " + record.distance +
                " | " + record.status +
                "</p>";

        });

        message.innerHTML = html;

    } catch (error) {

        message.innerHTML =
            "<p>❌ Failed to load mission records</p>";

        console.error(error);
    }
}
// =========================================
// LIVE DRONE NAVIGATION
// =========================================

function startDroneMovement() {

    const drone = document.getElementById("droneMarker");
    const status = document.getElementById("liveDroneStatus");
    const distance = document.getElementById("distanceRemaining");

    status.innerText = "🚁 MOVING TO S1...";

    let progress = 0;

    const movement = setInterval(function () {

        progress += 10;

        drone.style.left = (10 + progress * 0.8) + "%";
        drone.style.top = (67 - progress * 0.49) + "%";

        const remaining = Math.max(0, 520 - (progress * 5.2));

        distance.innerText = Math.round(remaining) + " m";

        if (progress >= 100) {

            clearInterval(movement);

            drone.style.left = "82%";
            drone.style.top = "18%";

            status.innerText = "✅ S1 LOCATION REACHED";

            distance.innerText = "0 m";

            alert("🚁 Drone reached Survivor S1!");
        }

    }, 500);
}