$(document).ready(function(){

	// handle first appearence of the selection tab
	$('#default_tab').addClass('graph_tabs_top_menu_options_selected');	
	$('.graph_content').css('display','none');
	$('#Import_Tab').css('display','block');

});


/*******************************************************
**			Hover Effects
**				Top Menu
**				Study List
**
********************************************************/


$('.list_title_content').mouseenter(function () {
	$(this).css('background-color', '#fcae14');
});
$('.list_title_content').mouseleave(function () {
	$(this).css('background-color', 'white');
});

$('.list_title_content').click(function () {
	
	// hide original content
	$(this).find('.list_title_inner').css('display','none');
	$(this).css('border','0px solid white');

	// display input box
	$(this).find('input').css('display','block');	
	$(this).find('input').focus();	
	
});

$('.list_title_content').click(function () {
	
	// hide original content
	$(this).find('.list_title_inner').css('display','none');
	$(this).css('border','0px solid white');

	// display input box
	$(this).find('input').css('display','block');	
	$(this).find('input').focus();	
	
});


$(".input_box").keypress(function(event) {
	if ( event.which == 13 ) {
		// update content
		var modified_content = $(this).attr('value');
		$(this).parent().find('.list_title_inner').text(modified_content);
		
		// hide input box
		$(this).css('display','none');
		
		// show display box
		$(this).parent().find('.list_title_inner').css('display','block');
		$(this).parent().css('border','1px solid #042614');
   	}
});

/*******************************************************
**			Graph Tabs 
**				Tabs Selection
********************************************************/
$('.graph_tabs_top_menu_options').click(function () {

	// dealing tabs switching
	var str = $(this).text().split(" ");
	var div_name = str[2]+'_Tab';
	$('.graph_content').css('display','none');
	$('#'+div_name).css('display','block');

	// dealing with menu option selection effects
	$(this).closest('.graph_tabs_top_menu').children('.graph_tabs_top_menu_options_selected').addClass('graph_tabs_top_menu_options');
	$(this).closest('.graph_tabs_top_menu').children('.graph_tabs_top_menu_options_selected').removeClass('graph_tabs_top_menu_options_selected');
	$(this).addClass('graph_tabs_top_menu_options_selected');
	$(this).removeClass('graph_tabs_top_menu_options');

	$('#training_garbage').children('embed').each(function () {
		$(this).remove();
	});

	$('#training_ans_garbage_collection').children('embed').each(function () {
		$(this).remove();
	});
});


