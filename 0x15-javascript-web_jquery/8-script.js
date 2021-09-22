// JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$(function () {
  $.get(url, function (data, statusText) {
    if (statusText === 'success') {
      const films = data.results;
      for (const i in films) {
        $('#list_movies').append('<li>' + films[i].title + '</li>');
      }
    }
  });
});
