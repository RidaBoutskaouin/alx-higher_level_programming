$('DIV#toggle_header').on('click', function () {
    if ($('header').attr('class') === 'green') {
        $('header').toggleClass('red');
    }

    if ($('header').attr('class') === 'red') {
        $('header').toggleClass('green');
    }
});