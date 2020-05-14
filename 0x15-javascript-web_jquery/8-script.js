$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (resp) {
  resp.results.forEach(function (film) {
    $('#list_movies').append('<li>' + film.title + '</li>');
  });
});
