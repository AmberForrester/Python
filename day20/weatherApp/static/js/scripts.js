document.addEventListener("DOMContentLoaded", function () {
    const locationButton = document.getElementById("locationButton");

    if (locationButton) {
        locationButton.addEventListener("click", function (event) {
            event.preventDefault();

            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(sendPositionToServer, handleError);
            } else {
                alert("Geolocation is not supported by this browser.");
            }
        });
    }

    function sendPositionToServer(position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        window.location.href = `/weather?lat=${latitude}&lon=${longitude}`;
    }

    function handleError(error) {
        alert("Unable to retrieve your location: " + error.message);
    }
});