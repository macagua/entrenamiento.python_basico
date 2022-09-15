// https://www.iamrohit.in/create-simple-responsive-material-design-vcard-html5css3/
$('body').on('click', '.icon', function() {
    var element = $(this).children().last();
    console.log(element);

    element.css('animation', 'ripple 1s ease-out');
    setTimeout(function() {
        element.css('animation', '');
    }, 1000);
});
