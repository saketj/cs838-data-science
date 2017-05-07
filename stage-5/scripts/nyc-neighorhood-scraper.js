var content = $('#content > table > tbody > tr');
var borough = '';
for (var i = 1; i < content.length; ++i) {
  var td = $(content[i]).find('td');
  var idx = 0;
  if (td.length == 3) {
    borough = $(td[0]).text().trim();
    idx = 1;
  }
  var neighborhood = $(td[idx]).text().trim();
  var zipcodes = $(td[idx+1]).text().trim().split(",");
  for (var j = 0; j < zipcodes.length; ++j) {
    var zipcode = zipcodes[j].trim();
    console.log(borough + "," + neighborhood + "," + zipcode);
  }
}
