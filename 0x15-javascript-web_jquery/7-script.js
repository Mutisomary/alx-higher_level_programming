$(document).ready(function() {
    // Use jQuery to make an AJAX GET request to the API URL
    $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
      // Update the text of the DIV#character element with the character name
      $("#character").text("Character Name: " + data.name);
    });
});
