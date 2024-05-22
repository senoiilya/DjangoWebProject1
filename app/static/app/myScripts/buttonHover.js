$(document).ready(function () {
    $('#input_color').on('mouseenter', function () {
        $('#input_color').addClass('btn_hover');
    }).on('mouseleave', function () {
        $('#input_color').removeClass('btn_hover');
    });
})