// https://dev.to/atif_dev/get-real-time-date-and-time-using-javascript-5eep
// https://codepen.io/Atitemp/pen/xxqGXOO
const getCurrentTime = () => {
    if ( document.getElementById("time") ) {
        let currentTimeDate = new Date();

        var hours = currentTimeDate.getHours();
        var minutes = currentTimeDate.getMinutes();
        minutes = minutes < 10 ? '0'+minutes : minutes;

        var AMPM = hours >= 12 ? 'PM' : 'AM';

        if ( hours === 12 ) {
            hours = 12;
        } else {
            hours = hours%12;
        }

        var currentTime = `${hours}:${minutes}${AMPM}`;
        document.getElementById("time").innerHTML = currentTime;
        setTimeout(getCurrentTime, 500);
    }
}
// Call getCurrentTime function
getCurrentTime();
