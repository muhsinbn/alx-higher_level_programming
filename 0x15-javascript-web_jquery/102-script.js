// A script that fetches and prints how to say “Hello” depending on the language
$(document).ready(function () {
    const url = 'https://fourtonfish.com/hellosalut/hello/';
    $('INPUT#btn_translate').click(function () {
        const lang = $('INPUT#language_code').val();
        $.get(url + $.param({ lang: lang }), function (data) {
            $('DIV#hello').text(data.hello);
        });
    });
});
