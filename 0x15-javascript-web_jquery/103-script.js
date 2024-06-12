// A script that fetches and prints how to say “Hello” depending on the language
$(document).ready(function () {
    // Fetch and display the hello translation when the button is clicked
    $('INPUT#btn_translate, INPUT#language_code').on('click keypress', function(e) {
        if (e.type === 'click' || (e.type === 'keypress' && e.which === 13)) {
            var language = $('INPUT#language_code').val();
            var url = 'https://fourtonfish.com/hellosalut/hello/' + language;
            $.get(url, function (data) {
                $('DIV#hello').text(data);
            });
        }
    });
});
