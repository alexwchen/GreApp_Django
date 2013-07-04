var original_color = "";

$(document).ready(function(){
	
	// give definition, synonyms, example sentences their own color
	$('.vocabulary_more_content').each(function () {
		var ClassID = $(this).parent().parent().attr('id');
		if ( ClassID == 'example'){
			$(this).css('background-color', '#bde9fb');			
		}
		else if ( ClassID == 'synonym'){
			$(this).css('background-color', '#bdfbe4');			
		}
		else if ( ClassID == 'definition'){
			$(this).css('background-color', '#fbbdc3');			
		}	
	});
	
});

/*******************************************************
**			Hover Effects
**				Study List
**
********************************************************/
// Vocabulary - Study Section
$('.vocabulary_add_info_button').mouseenter(function () {
	$(this).css('background-color', '#fcae14');
});
$('.vocabulary_add_info_button').mouseleave(function () {
	$(this).css('background-color', 'white');
});

//  Vocabulary Name & Definition - Study Section
$('.vocabulary_name').mouseenter(function () {
	$(this).css('background-color', '#f0d7af');
});
$('.vocabulary_name').mouseleave(function () {
	$(this).css('background-color', 'white');
});
$('.vocabulary_definition').mouseenter(function () {
	$(this).css('background-color', '#f0d7af');
});
$('.vocabulary_definition').mouseleave(function () {
	$(this).css('background-color', 'white');
});

//  Vocabulary Content Swich - Study Section
$('.vocabulary_more_content_additional').mouseenter(function () {
	$(this).css('background-color', '#f0d7af');
});
$('.vocabulary_more_content_additional').mouseleave(function () {
	$(this).css('background-color', 'white');
});

/*******************************************************
**			Term and Definition Change
**
********************************************************/
$('.vocabulary_name').click(function () {
	var term_content = $(this).text().replace(/^\s*|\s*$/g,'');
	var input_box = $(this).parent().find('.vocabulary_name_input_box');
	$(input_box).css('display','block');
	$(input_box).text(term_content);
	$(input_box).focus();
	$(this).css('display','none');
});

$('.vocabulary_definition').click(function () {
	var def_content = $(this).text().replace(/^\s*|\s*$/g,'');
	var input_box = $(this).parent().find('.vocabulary_definition_input_box');
	$(input_box).css('display','block');
	$(input_box).text(def_content);
	$(input_box).focus();
	$(this).css('display','none');
});

$('.vocabulary_definition_input_box').keypress(function(e) {
	
	var content_box = $(this).parent().find('.vocabulary_definition');
	if(e.which == 13) {
		$(this).css('display', 'none');
		$(content_box).css('display', 'block');				
		
		// CSRF code, used for POST
		jQuery(document).ajaxSend(function(event, xhr, settings) {
		    function getCookie(name) {
		        var cookieValue = null;
		        if (document.cookie && document.cookie != '') {
		            var cookies = document.cookie.split(';');
		            for (var i = 0; i < cookies.length; i++) {
		                var cookie = jQuery.trim(cookies[i]);
		                // Does this cookie string begin with the name we want?
		                if (cookie.substring(0, name.length + 1) == (name + '=')) {
		                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		                    break;
		                }
		            }
		        }
		        return cookieValue;
		    }
		    function sameOrigin(url) {
		        // url could be relative or scheme relative or absolute
		        var host = document.location.host; // host + port
		        var protocol = document.location.protocol;
		        var sr_origin = '//' + host;
		        var origin = protocol + sr_origin;
		        // Allow absolute or scheme relative URLs to same origin
		        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
		            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
		            // or any other URL that isn't scheme relative or absolute i.e relative.
		            !(/^(\/\/|http:|https:).*/.test(url));
		    }
		    function safeMethod(method) {
		        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		    }

		    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
		        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		    }
		});

		
		var author_name = $('#author_name').text();
		var list_name = $('#list_title').text();
		$word = $(this).closest('.main_vocabulary_frame').find('.vocabulary_name').text().replace(/^\s*|\s*$/g,'').replace(/\s/g,'_');
		var modified_content = $(this).val();

		// Send a "POST" to server
		$.post("/training/store_word_definition/"+$word+"/", {'modified':modified_content, 'author_name':author_name, 'list_name':list_name},function(data){

			// indicating if saving is successful
			if (data=="success"){
				
				$(content_box).text(modified_content);				
			}
			else{
				alert('fail');
			}			
		});
		
    } 
});

$('.vocabulary_name_input_box').keypress(function(e) {
	
	var content_box = $(this).parent().find('.vocabulary_name');
	if(e.which == 13) {
		
		$(this).css('display', 'none');
		$(content_box).css('display', 'block');				
		
		// CSRF code, used for POST
		jQuery(document).ajaxSend(function(event, xhr, settings) {
		    function getCookie(name) {
		        var cookieValue = null;
		        if (document.cookie && document.cookie != '') {
		            var cookies = document.cookie.split(';');
		            for (var i = 0; i < cookies.length; i++) {
		                var cookie = jQuery.trim(cookies[i]);
		                // Does this cookie string begin with the name we want?
		                if (cookie.substring(0, name.length + 1) == (name + '=')) {
		                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		                    break;
		                }
		            }
		        }
		        return cookieValue;
		    }
		    function sameOrigin(url) {
		        // url could be relative or scheme relative or absolute
		        var host = document.location.host; // host + port
		        var protocol = document.location.protocol;
		        var sr_origin = '//' + host;
		        var origin = protocol + sr_origin;
		        // Allow absolute or scheme relative URLs to same origin
		        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
		            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
		            // or any other URL that isn't scheme relative or absolute i.e relative.
		            !(/^(\/\/|http:|https:).*/.test(url));
		    }
		    function safeMethod(method) {
		        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		    }

		    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
		        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		    }
		});
		
		var author_name = $('#author_name').text();
		var list_name = $('#list_title').text();
		$word = $(this).closest('.main_vocabulary_frame').find('.vocabulary_name').text().replace(/^\s*|\s*$/g,'').replace(/\s/g,'_');
		var modified_content = $(this).val();

		// Send a "POST" to server
		$.post("/training/store_word_name/"+$word+"/", {'modified':modified_content, 'author_name':author_name, 'list_name':list_name},function(data){
			// indicating if saving is successful
			if (data=="success"){
				$(content_box).text(modified_content);				
			}
			else{
				alert('fail');
			}			
		});
    } 		
});


/*******************************************************
**		Storing Selected Information About Vocabulary
**			Study List
**
********************************************************/

// extract example sentences, synoyms, definition for user to select which one is useful to them
$('.vocabulary_add_info_button').toggle(       
	function (){
		
		// change display text from "More" to "Save"
		$(this).find('.vocabulary_add_info_button_inner').text('Save');
		
		
		// get the vocabulary term, which we will send to "GET"
		$word = $(this).closest('.main_vocabulary_frame').find('.vocabulary_name').text().replace(/^\s*|\s*$/g,'').replace(/\s/g,'_');

		// display additoinal info box
        var new_block = $(this).closest('.main_vocabulary_frame').find('.vocabulary_more_outter_additional');
        new_block.css('display', 'block');


        var v_definition = $(this).closest('.main_vocabulary_frame').find('.vocabulary_more_content_definition_additional');
        var v_synonym = $(this).closest('.main_vocabulary_frame').find('.vocabulary_more_content_synonym_additional');
        var v_example = $(this).closest('.main_vocabulary_frame').find('.vocabulary_more_content_example_additional');
        

        // send a "GET" to server
        $.get("/training/retrive_word_info/"+$word+"/", function(data)
        {
			// returned data from server
            var organized = JSON.parse(data);
	        
			for(var i=0; i<organized['extra_def_idx']; i++)
            {
				// add the div tag for additional words
                var new_div = 	"<div class='vocabulary_more_content_outter'>"+
									"<div class='vocabulary_more_content_additional'>" + 
										organized['extra_def'][i] + 
									"</div>"+
									"<textarea class='vocabulary_more_content_input'></textarea>"+
								"</div>";
                $(v_definition).append(new_div);
            }
			
            for(var i=0; i<organized['meaning_idx']; i++)
            {
				// add the div tag for additional words
                var new_div = 	"<div class='vocabulary_more_content_outter'>"+
									"<div class='vocabulary_more_content_additional'>" + 
										organized['meaning'][i] + 
									"</div>"+
									"<textarea class='vocabulary_more_content_input'></textarea>"+
								"</div>";
                $(v_definition).append(new_div);
            }
			
			for(var i=0; i<organized['synonym_idx']; i++)
            {
				// add the div tag for additional words
                var new_div = 	"<div class='vocabulary_more_content_outter'>"+
									"<div class='vocabulary_more_content_additional'>" + 
										organized['synonym'][i] + 
									"</div>"+
									"<textarea class='vocabulary_more_content_input'></textarea>"+
								"</div>";
                $(v_synonym).append(new_div);
            }

            for(var i=0; i<organized['example_idx']; i++)
            {
				// add the div tag for additional words
                var new_div = 	"<div class='vocabulary_more_content_outter'>"+
									"<div class='vocabulary_more_content_additional'>" + 
										organized['example'][i] + 
									"</div>"+
									"<textarea class='vocabulary_more_content_input'></textarea>"+
								"</div>";
                $(v_example).append(new_div);
            }
			
        });
	},
	function (){
		
		// change display text from "Save" to "More"
		var status_block = $(this).find('.vocabulary_add_info_button_inner');
						
		// hide additoinal info box
        var new_block = $(this).closest('.main_vocabulary_frame').find('.vocabulary_more_outter_additional');
        new_block.css('display', 'none');
		
		// remove all contents
        new_block.find('.vocabulary_more_content_additional').each(function(){
            $(this).remove();
        });
		
		// walk through all user selected content and store and store them in json
		result =[];
		// definition		
		$(this).parent().find('.vocabulary_more_content_definition').children('.vocabulary_more_content_outter').each(function(index){
			var content = $(this).text().replace(/^\s*|\s*$/g,'');
			var category = $(this).parent().attr('class');	
			result.push({label: category, data: content});
		});
		// synonym
		$(this).parent().find('.vocabulary_more_content_synonym').children('.vocabulary_more_content_outter').each(function(index){
			var content = $(this).text().replace(/^\s*|\s*$/g,'');
			var category = $(this).parent().attr('class');	
			result.push({label: category, data: content});
		});
		// example 
		$(this).parent().find('.vocabulary_more_content_example').children('.vocabulary_more_content_outter').each(function(index){
			var content = $(this).text().replace(/^\s*|\s*$/g,'');
			var category = $(this).parent().attr('class');	
			result.push({label: category, data: content});
		});
		var author_name = $('#author_name').text();
		var list_name = $('#list_title').text();
		
		
		// CSRF code, used for POST
		jQuery(document).ajaxSend(function(event, xhr, settings) {
		    function getCookie(name) {
		        var cookieValue = null;
		        if (document.cookie && document.cookie != '') {
		            var cookies = document.cookie.split(';');
		            for (var i = 0; i < cookies.length; i++) {
		                var cookie = jQuery.trim(cookies[i]);
		                // Does this cookie string begin with the name we want?
		                if (cookie.substring(0, name.length + 1) == (name + '=')) {
		                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		                    break;
		                }
		            }
		        }
		        return cookieValue;
		    }
		    function sameOrigin(url) {
		        // url could be relative or scheme relative or absolute
		        var host = document.location.host; // host + port
		        var protocol = document.location.protocol;
		        var sr_origin = '//' + host;
		        var origin = protocol + sr_origin;
		        // Allow absolute or scheme relative URLs to same origin
		        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
		            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
		            // or any other URL that isn't scheme relative or absolute i.e relative.
		            !(/^(\/\/|http:|https:).*/.test(url));
		    }
		    function safeMethod(method) {
		        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		    }

		    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
		        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		    }
		});
		
		
		// send a "POST" to server
		$.post("/training/store_word_info/"+$word+"/", {'result':result, 'author_name':author_name, 'list_name':list_name},function(data){
			
			// indicating if saving is successful
			if (data=="success"){
				//status_block.text('Saving Succeed!');
				status_block.parent().parent().find('.vocabulary_status_info').text('Saving Succeed!');				
				status_block.parent().parent().find('.vocabulary_status_info').fadeIn(500).delay(1000).fadeOut(500);
				status_block.parent().find('.vocabulary_status_info').text('');	
			}
			else{
				//status_block.text('Saving Failed!');													
			}			
		});
		status_block.text('More');	
    }
);


/*******************************************************
**		Throwing additional words information betweeen 
**	 	vocabulary_more_content & vocabulary_more_outter_additional
**
**		Main Purpose:
**		1.
** 		user can select the additional information they want
**		if selected, we will put it into "vocabulary_more_content"
** 		if deleted, it will be put into "vocabulary_more_outter_additional"
**
**		2. 
**		change to input box, so user can modify the content of word information
** 		and will be able to store them on the fly
**
**
********************************************************/

// Selected
$('.vocabulary_more_content_additional').live({
		
    click: function(){
		var classID = $(this).parent().parent().attr('id');
		var category = ('.vocabulary_more_content_'+classID);		
		var new_block = $(this).closest('.main_vocabulary_frame').find(category);
        $(this).removeClass();
        $(this).addClass('vocabulary_more_content');		
        $(this).parent().appendTo(new_block);
    },

	// hover color change, can chnage three colors, looks nicer
	mouseenter: function () {
		var ClassID = $(this).parent().parent().attr('id');
		if ( ClassID == 'example'){
			$(this).css('background-color', '#bde9fb');	
			original_color = $(this).css('background-color');			
		}
		else if ( ClassID == 'synonym'){
			$(this).css('background-color', '#bdfbe4');		
			original_color = $(this).css('background-color');	
		}
		else if ( ClassID == 'definition'){
			$(this).css('background-color', '#fbbdc3');			
			original_color = $(this).css('background-color');
		}	
		
	},
	mouseleave: function () {
		$(this).css('background-color', 'white');
	}
});
	

$('.vocabulary_more_content').live({
	
	// change to input box
    click: function(){
		var more_button = $(this).closest('.main_vocabulary_frame').find('.vocabulary_add_info_button');
		if (more_button.text().replace(/^\s*|\s*$/g,'') == "More")
		{
			var height = $(this).height();
			var width = $(this).width();
			var original_block = $(this).parent().find('.vocabulary_more_content');
			var input_block = $(this).parent().find('.vocabulary_more_content_input');
			var original_text = original_block.text().replace(/^\s*|\s*$/g,'');
			
			// setting proper wdith, value for the input box
			$(input_block).css('width', width);
			$(input_block).attr('value', original_text);
			$(input_block).attr('rows', Math.ceil(original_text.length/70));
			
			// display input block & hide original block
			$(input_block).css('display', 'block');
			$(original_block).css('display', 'none');
			$(input_block).selectionStart = $(input_block).selectionEnd = $(input_block).val().length;
			$(input_block).focus();
			
			
			// change input block size while user typing
			$(input_block).keyup(function(e) {
				var input_rows = $(input_block).attr('rows');
				var original_text = $(this).val().replace(/^\s*|\s*$/g,'');
				$(this).attr('rows', Math.ceil(original_text.length/68));
			});
			
			// if enter is pressed, store the content
			$(input_block).keypress(function(e) {
				if(e.which == 13) {
					$(input_block).css('display', 'none');
					$(original_block).css('display', 'block');	
										
					// CSRF code, used for POST
					jQuery(document).ajaxSend(function(event, xhr, settings) {
					    function getCookie(name) {
					        var cookieValue = null;
					        if (document.cookie && document.cookie != '') {
					            var cookies = document.cookie.split(';');
					            for (var i = 0; i < cookies.length; i++) {
					                var cookie = jQuery.trim(cookies[i]);
					                // Does this cookie string begin with the name we want?
					                if (cookie.substring(0, name.length + 1) == (name + '=')) {
					                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					                    break;
					                }
					            }
					        }
					        return cookieValue;
					    }
					    function sameOrigin(url) {
					        // url could be relative or scheme relative or absolute
					        var host = document.location.host; // host + port
					        var protocol = document.location.protocol;
					        var sr_origin = '//' + host;
					        var origin = protocol + sr_origin;
					        // Allow absolute or scheme relative URLs to same origin
					        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
					            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
					            // or any other URL that isn't scheme relative or absolute i.e relative.
					            !(/^(\/\/|http:|https:).*/.test(url));
					    }
					    function safeMethod(method) {
					        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
					    }

					    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
					        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
					    }
					});
					
					var author_name = $('#author_name').text();
					var list_name = $('#list_title').text();
					var category = $(this).parent().parent().attr('id');
					$word = $(this).closest('.main_vocabulary_frame').find('.vocabulary_name').text();

					// Send a POST to server
					$.post("/training/store_word_input_box/"+$word+"/", 
						{	'original':original_block.text().replace(/^\s*|\s*$/g,''), 
						 	'modified':input_block.val().replace(/^\s*|\s*$/g,''),
							'author_name':author_name, 
							'list_name':list_name, 
							'category':category,
						},function(data){
							// indicating if saving is successful
							if (data=="success"){
								$(input_block).css('display', 'none');
								$(original_block).css('display', 'block');	
								$(original_block).text($(input_block).val());
							}
							else{
								$(input_block).css('display', 'none');
								$(original_block).css('display', 'block');	
								$(original_block).text('Sorry, Something Is Wrong With The System');
							}
					});
					
					
			    } 
			});			
			
		}
		else if (more_button.text().replace(/^\s*|\s*$/g,'') == "Save")
		{
			var classID = $(this).parent().parent().attr('id');		
			var category = ('.vocabulary_more_content_'+classID+'_additional');
			var new_block = $(this).closest('.main_vocabulary_frame').find(category);			
	        $(this).removeClass();
	        $(this).addClass('vocabulary_more_content_additional');		
	        $(this).parent().appendTo(new_block);
		}
    },

	mouseenter: function () {		
		original_color = $(this).css('background-color');
		$(this).css('background-color', '#f0d7af');
	},
	mouseleave: function () {
		$(this).css('background-color', original_color);
	}
});


/*******************************************************
**		Showing/ Hiding information according to dropdown list
**		Dropdown List
**
********************************************************/
$('.vocabulary_header_select').change(function () {

	var dropdown_val = $(this).val();

	// hide all detail information
	if (dropdown_val=="Simple")
	{
		$('.vocabulary_more_outter').css('display', 'none');
	}

	// show all detail information
	else if (dropdown_val=="Detailed")
	{
		$('.vocabulary_more_outter').css('display', 'block');
	}
});

/*******************************************************
**		Sound Effects
**		
**
********************************************************/
$('.vocabulary_sound').click(function () {
	var content = $(this).parent().find('.vocabulary_name_parent').text().replace(/^\s*|\s*$/g,'');
	var firefox = "<embed height='0px'  src='http://translate.google.com/translate_tts?tl=en&q="+content+"' type='audio/mpeg'></embed>";
	var chorme = "<embed height='0px'  class='shit' src='http://translate.google.com/translate_tts?tl=en&q="+content+"' ></embed>";
	$(firefox).appendTo('#garbage_collection');
	$(chorme).appendTo('#garbage_collection');
	
});


/*******************************************************
**		Sound Effects
**		
**
********************************************************/
$('.vocab_delete_button_frame').mouseenter(function () {
	$(this).find('img').attr('src', '/media/Images/delete_hover.png');			
});
$('.vocab_delete_button_frame').mouseleave(function () {
	$(this).find('img').attr('src', '/media/Images/delete.png');
});
$('.vocab_delete_button_frame').click(function () {
	if (confirm("Are You Sure You Want To Delete This Word?"))
	{
		// CSRF code, used for POST
		jQuery(document).ajaxSend(function(event, xhr, settings) {
		    function getCookie(name) {
		        var cookieValue = null;
		        if (document.cookie && document.cookie != '') {
		            var cookies = document.cookie.split(';');
		            for (var i = 0; i < cookies.length; i++) {
		                var cookie = jQuery.trim(cookies[i]);
		                // Does this cookie string begin with the name we want?
		                if (cookie.substring(0, name.length + 1) == (name + '=')) {
		                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		                    break;
		                }
		            }
		        }
		        return cookieValue;
		    }
		    function sameOrigin(url) {
		        // url could be relative or scheme relative or absolute
		        var host = document.location.host; // host + port
		        var protocol = document.location.protocol;
		        var sr_origin = '//' + host;
		        var origin = protocol + sr_origin;
		        // Allow absolute or scheme relative URLs to same origin
		        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
		            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
		            // or any other URL that isn't scheme relative or absolute i.e relative.
		            !(/^(\/\/|http:|https:).*/.test(url));
		    }
		    function safeMethod(method) {
		        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		    }

		    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
		        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		    }
		});
		
		var author_name = $('#author_name').text();
		var list_name = $('#list_title').text();
		$word = $(this).closest('.main_vocabulary_frame').find('.vocabulary_name').text().replace(/^\s*|\s*$/g,'').replace(/\s/g,'_');
		var button_frame = $(this);
		// send a "POST" to server
		$.post("/training/delete_vocabulary_word_from_list/"+$word+"/", {'author_name':author_name, 'list_name':list_name},function(data){
			
			// indicating if saving is successful
			if (data=="success"){
				$(button_frame).parent().parent().parent().css('display','none');
			}
			else{
				alert('Delete Failed!');
			}			
		});
	}
});
