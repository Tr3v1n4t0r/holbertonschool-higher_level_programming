$.getJSON('https://fourtonfish.com/hellosalut/?', function (resp) {
  $('#hello').text(resp.hello);
});
