$.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/',
    type: 'GET',
    data: {
        lang: 'fr'
    },
    success: function(response) {
        $('DIV#hello').text(response.hello);}
});
