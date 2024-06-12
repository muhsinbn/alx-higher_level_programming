// A script that adds, removes and clears LI elements from a list when the user clicks
$(document).ready(function () {

    // Add a new item to the list
    $('DIV#add_item').click(function () {
        $('UL.my_list').append('<li>Item</li>');
    });

    // Remove an item from the list
    $('DIV#remove_item').click(function () {
        $('UL.my_list li').last().remove();
    });

    // Clear the list
    $('DIV#clear_list').click(function () {
        $('UL.my_list').empty();
    });
});
