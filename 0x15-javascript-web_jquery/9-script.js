$(document).ready(function() {
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
    // Update the text of the DIV#hello element with the translation
    $("#hello").text(data.hello);
  });
});
