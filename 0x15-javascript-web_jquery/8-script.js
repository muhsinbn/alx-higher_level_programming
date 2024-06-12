// A script that fetches and list the titile for all movies using this URL:
// https://swapi-api.alx-tools.com/api/films/?format=json, all movies must be list in the tag UL#list_movies
$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
    $('UL#list_movies').append(data.results.map(movie => $('<li></li>').text(movie.title)));
});
