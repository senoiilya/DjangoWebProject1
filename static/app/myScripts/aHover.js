$(document).ready(function () {
    $('#readMore').on('mouseenter', function () {
        $('#readMore').addClass('read_more_hover');
    }).on('mouseleave', function () {
        $('#readMore').removeClass('read_more_hover');
    });
})