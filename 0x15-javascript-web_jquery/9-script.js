$(document).ready(function () {
    function hello() {
        return $.get({
            url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
            dataType: 'json'
        });
    }

    hello().done(function (data) {
        $('div#hello').text(data.hello);
    });

});