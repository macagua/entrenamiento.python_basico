// https://dev.to/atif_dev/get-real-time-date-and-time-using-javascript-5eep
// https://www.twilio.com/blog/converting-formatting-dates-timezones-javascript
//--------------------------------------------------
// Get Current Time from a specific Time Zone START
//--------------------------------------------------
$(document).ready(function(){
    if (document.getElementById("time")) {
        const getCurrentTime = () => {
            const now = new Date();
            const locale = new Intl.Locale('es-ES');
            const currentTime = new Intl.DateTimeFormat(locale.baseName, {
                hour: 'numeric',
                hour12: true,
                minute: 'numeric',
                timeZone: 'Europe/Madrid' // Fixed timezone specification
            });
            document.getElementById("time").innerHTML = currentTime.format(now);
            setTimeout(getCurrentTime, 500);
        }
        getCurrentTime(); // Added initial call
    }
});
//--------------------------------------------------
// Get Current Time from a specific Time Zone END
//--------------------------------------------------
