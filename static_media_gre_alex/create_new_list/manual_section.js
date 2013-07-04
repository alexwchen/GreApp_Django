$(document).ready(function(){

});

/*******************************************************
**			Hover Effects
**
********************************************************/

$('.more_button_outter').mouseenter(function () {
	$(this).css('background-color', '#f0d7af');
});
$('.more_button_outter').mouseleave(function () {
	$(this).css('background-color', 'white');
});

$('.save_button_outter').mouseenter(function () {
	$(this).css('background-color', '#bdfbe4');
});
$('.save_button_outter').mouseleave(function () {
	$(this).css('background-color', 'white');
});

/*******************************************************
**			Save Button 
**
********************************************************/

$('.save_button_outter').click(function () {
	$('.save_button_outter').css('display','none');
	$('.more_button_outter').css('display','none');
	$('.message_container').css('display','block');
	$('.manual_big_container').css('display','none');
	user_new_created_list = []
	// Construct json
    $('.manual_input_container').each(function(){
        var number = $(this).find('.number_label').text();
        var term = $(this).find('.term_input_box').attr('value');
        var def = $(this).find('.def_input_box').attr('value');
		user_new_created_list.push({term: term, definition: def});
    });

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

	var list_name = $('#list_title').text().replace(/^\s*|\s*$/g,'');
	var author_name = $('#author_name').text().replace(/^\s*|\s*$/g,'');
	
	if (list_name == "Please Type Your Title")
	{
		alert(list_name);
	}
	else if(author_name == "Please Type Your Name")
	{
		alert(author_name);		
	}
	else
	{
		$.post("/create/save_user_list/", {'result':user_new_created_list, 'author_name':author_name, 'list_name':list_name},function(data){		
			if (data!='fail')
			{
				var url = '/training/' + list_name.split(' ').join('_') + '/' + author_name.split(' ').join('_') + '/' + data;
				window.location.href = url;
			}
			else
			{
				alert('fail');
			}
		});	
	}		
});

/*******************************************************
**			More Button 
**
********************************************************/

$('.more_button_outter').click(function () {
	
	var newest_count = $('.manual_input_container').last().find('.number_label').text();
	var updated_1 = parseInt(newest_count)+1;
	var updated_2 = parseInt(newest_count)+2;
	var updated_3 = parseInt(newest_count)+3;

	var new_block = 
	"<div class='manual_input_container'>"+
		"<div class='number_label'>" + updated_1 + ".</div>"+
		"<input type='text' class='term_input_box'></input>"+
		"<input type='text' class='def_input_box'></input>"+
	"</div>";
	$('.manual_big_container').append(new_block);

	var new_block = 
	"<div class='manual_input_container'>"+
		"<div class='number_label'>" + updated_2 + ".</div>"+
		"<input type='text' class='term_input_box'></input>"+
		"<input type='text' class='def_input_box'></input>"+
	"</div>";
	$('.manual_big_container').append(new_block);

	var new_block = 
	"<div class='manual_input_container'>"+
		"<div class='number_label'>" + updated_3 + ".</div>"+
		"<input type='text' class='term_input_box'></input>"+
		"<input type='text' class='def_input_box'></input>"+
	"</div>";
	$('.manual_big_container').append(new_block);
	
});
















