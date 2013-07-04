$(document).ready(function(){

});

/*******************************************************
** Import Button
**
********************************************************/

// Hover
$('.import_button_outter').mouseenter(function () {
	$(this).css('background-color', '#f0d7af');
});
$('.import_button_outter').mouseleave(function () {
	$(this).css('background-color', 'white');
});

// Click - Parse List
$('.import_button_outter').click(function () {
	var user_pasted_list = $('.import_input_box').val();
	
    $.get("/create/process_pasted_list/",{'user_pasted_list':user_pasted_list}, function(data)
    {
	    var organized = JSON.parse(data);
		var keys = Object.keys(organized).sort();

		
		// clean out all manual input box
        $('.manual_input_container').each(function(){
            $(this).remove();
        });


		// start adding new input box
		count = 0;		
		for(var key in keys)
        {
	
			count = count + 1;
			var new_block = 
			"<div class='manual_input_container'>"+
				"<div class='number_label'>" + count + ".</div>"+
				"<input type='text' class='term_input_box' value='" + keys[key] + "' ></input>"+
				"<input type='text' class='def_input_box' value='" + organized[keys[key]] + "' ></input>"+
			"</div>";
			$('.manual_big_container').append(new_block);
            
        }

		// hide import section tab
		// display manual tab
		$('#Manual_Tab').css('display','block');
		$('#Import_Tab').css('display','none');

		// dealing with menu option selection effects
		$('.graph_tabs_top_menu').children('.graph_tabs_top_menu_options_selected').addClass('graph_tabs_top_menu_options');
		$('.graph_tabs_top_menu').children('.graph_tabs_top_menu_options_selected').removeClass('graph_tabs_top_menu_options_selected');
		$('#import_option').addClass('graph_tabs_top_menu_options_selected');
		$('#import_option').removeClass('graph_tabs_top_menu_options');
		
	});
});
