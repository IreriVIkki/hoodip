$(document).ready(function () {
    $('.pfb').click(function (e) {
        e.preventDefault();
        $('.pbf').addClass('d-none');
        $('.lob').removeClass('d-none');
    });
    $('.gbb').click(function (e) {
        e.preventDefault();
        $('.pbf').addClass('d-none');
        $('.lob').removeClass('d-none');
    });
    $('.abb').click(function (e) {
        e.preventDefault();
        $('.lob').addClass('d-none');
        $('.pbf').removeClass('d-none');
    });
});
// $(document).ready(function () {
//     $('.pfb').click(function (e) {
//         e.preventDefault();
//         $('.pbf').toggleClass('d-none');
//         $('.lob').toggleClass('d-none');
//     });

// });