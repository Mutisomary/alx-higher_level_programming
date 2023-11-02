$(document).ready(function() {
  // Use jQuery to make an AJAX GET request to the API URL
  $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
    // Loop through the results and append each movie title to the UL#list_movies
    $.each(data.results, function(index, movie) {
      $("#list_movies").append("<li>" + movie.title + "</li>");
    });
  });
});
