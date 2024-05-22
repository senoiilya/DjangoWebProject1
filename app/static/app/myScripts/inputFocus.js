$(document).ready(function () {
    // .form-control .form-select .form-check-input
    // Text input and textarea
    $('.form-control').on('focus', function () {
        $(this).addClass('input_background');
    }).on('blur', function () {
        $(this).removeClass('input_background');
    })
    // select
    $('.form-select').on('focus', function () {
        $(this).addClass('input_background');
    }).on('blur', function () {
        $(this).removeClass('input_background');
    })
    $('form-check-input').on('focus', function () {
        $(this).addClass('input_background');
    }).on('blur', function () {
        $(this).removeClass('input_background');
    })
})