// JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello

$(function () {
  $.ajax({
    type: 'Get',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $('#hello').text(data.hello);
    }
  });
});
