// https://dev.to/atif_dev/get-real-time-date-and-time-using-javascript-5eep
// https://www.twilio.com/blog/converting-formatting-dates-timezones-javascript
//--------------------------------------------------
// Get Current Time from a specific Time Zone START
//--------------------------------------------------
$(document).ready(function(){
    if ( document.getElementById("time") ) {
        const getCurrentTime = () => {
            const now = new Date();
            const locale = new Intl.Locale('es-VE');
            const currentTime = new Intl.DateTimeFormat(locale.baseName, {
                hour: 'numeric',
                hour12: true,
                minute: 'numeric',
                timeZone: locale.timeZones,
            });
            document.getElementById("time").innerHTML = currentTime.format(now);
            setTimeout(getCurrentTime, 500);
        }
    }
});
//--------------------------------------------------
// Get Current Time from a specific Time Zone END
//--------------------------------------------------
