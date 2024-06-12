// A script that adds a <li> element to a list when user clicks tag DIV3add_item
$('div#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
