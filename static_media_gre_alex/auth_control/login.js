$(document).ready(function(){
});


/*******************************************************
**			Hover Effects
**				Top Menu
**				Study List
**
********************************************************/

// Top Menu
$('.login_ok_bottom_outter').mouseenter(function () {
	$(this).css('background-color', '#bdfbe4');
});
$('.login_ok_bottom_outter').mouseleave(function () {
	$(this).css('background-color', 'white');
});



$('.input_box_text').focus(function () {
	$(this).attr('value', '');
});


