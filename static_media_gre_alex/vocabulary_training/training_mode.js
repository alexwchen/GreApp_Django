var shortcut_flag=0;

$(document).ready(function(){

	// select first questoin in the "fresh queue"
	var selected_block = $('.fresh_queue').find('.training_block').first();
	selected_block.css('display', 'block');

});

// training mode short cuts
$(document).keypress(function(e){
	if ($('#Train_Tab').css('display')=='block')
	{

		var first_block = $('.fresh_queue').find('.training_block').first();		
		
		if ( shortcut_flag == 0)
		{
			// handles Ok button & Next button
			if(e.charCode == 13){

				// Ok button is visible, click it
				if (first_block.find('.training_button_ok').css('display') == "block")
				{
					first_block.find('.training_button_ok').click();			
				}

				// Next button is visible, click it
				else if (first_block.find('.training_button_next').css('display') == "block")
				{
					first_block.find('.training_button_next').click();
				}
			}
	
			// handles  " 1st Option A=65, a=97, 1=49"
			else if(e.charCode == 65 || e.charCode == 97 || e.charCode == 49){
				first_block.find('.training_option_frame:eq(0)').click();			
			}
			// handles  " 2nd Option S=83, s=115, 2=50"
			else if(e.charCode == 83 || e.charCode == 115 || e.charCode == 50){
				first_block.find('.training_option_frame:eq(1)').click();			
			}
			// handles  " 3rd Option D=68, d=100, 3=51"
			else if(e.charCode == 68 || e.charCode == 100 || e.charCode == 51){
				first_block.find('.training_option_frame:eq(2)').click();			
			}
			// handles  " 4th Option F=70, f=102, 4=52"
			else if(e.charCode == 70 || e.charCode == 102 || e.charCode == 52){
				first_block.find('.training_option_frame:eq(3)').click();			
			}
		
		
			// handles  "Q=81, q=113"
			else if(e.charCode == 81 || e.charCode == 113){
				var content = first_block.find('.training_option_frame:eq(0)').find('.training_option_frame_inner').text().replace(/^\s*|\s*$/g,'');
				var firefox = "<embed height='0px' src='http://translate.google.com/translate_tts?tl=en&q="+content+"' type='audio/mpeg'></embed>";
				var chrome = "<embed height='0px' src='http://translate.google.com/translate_tts?tl=en&q="+content+"'></embed>";
			
				$(firefox).appendTo('#training_garbage');				
				$(chrome).appendTo('#training_garbage');				
			
			}
			// handles  "W=87, w=119"
			else if(e.charCode == 87 || e.charCode == 119){
				var content = first_block.find('.training_option_frame:eq(1)').find('.training_option_frame_inner').text().replace(/^\s*|\s*$/g,'');
				var firefox = "<embed height='0px' src='http://translate.google.com/translate_tts?tl=en&q="+content+"' type='audio/mpeg'></embed>";
				var chrome = "<embed height='0px' src='http://translate.google.com/translate_tts?tl=en&q="+content+"'></embed>";
				$(firefox).appendTo('#training_garbage');
				$(chrome).appendTo('#training_garbage');				
			
			}
			// handles  "e=101, E=69"
			else if(e.charCode == 101 || e.charCode == 69){
				var content = first_block.find('.training_option_frame:eq(2)').find('.training_option_frame_inner').text().replace(/^\s*|\s*$/g,'');
				var firefox = "<embed height='0px' src='http://translate.google.com/translate_tts?tl=en&q="+content+"' type='audio/mpeg'></embed>";
				var chrome = "<embed height='0px' src='http://translate.google.com/translate_tts?tl=en&q="+content+"'></embed>";
				$(firefox).appendTo('#training_garbage');
				$(chrome).appendTo('#training_garbage');				
			}
			// handles  "F=82, f=114"
			else if(e.charCode == 82 || e.charCode == 114){
				var content = first_block.find('.training_option_frame:eq(3)').find('.training_option_frame_inner').text().replace(/^\s*|\s*$/g,'');
				var firefox = "<embed height='0px' src='http://translate.google.com/translate_tts?tl=en&q="+content+"' type='audio/mpeg'></embed>";
				var chrome = "<embed height='0px' src='http://translate.google.com/translate_tts?tl=en&q="+content+"'></embed>";
				$(firefox).appendTo('#training_garbage');
				$(chrome).appendTo('#training_garbage');				
			
			}
		}
	}
});


var selected_answer = "";
var original_background = "";
var global_question_counter = 10;
var global_random_number = 0;

var question_answered = 0;
var question_answered_right = 0;
var question_answered_wrong = 0;

var question_answered_wrong_word = "";

/*******************************************************
**	OK_Button
**
********************************************************/

// OK Button
$('.training_button_ok').live({
		
	// Check if ansewer is correct, display answer or increment points	
    click: function(){
	
		//update total answered question
		question_answered++;
		$('#question_answered').text(question_answered);		
		
		// hide statistic frame
		$('.statistic_frame').css('display','none');
		
		// show Next Button
		$(this).parent().find('.training_button_next').css('display', 'block');
		// show Message Frame
		$(this).parent().find('.training_message_frame').css('display', 'block');	

		// show Important Frame	
		$(this).parent().find('.mark_as_important_frame').css('display', 'block');
		$(this).parent().find('.mark_as_important_inner').text('Mark As Important');	

		// hide Ok Button
		$(this).css('display', 'none');

		// update content in message frame
		if (selected_answer==1){
			$(this).parent().find('.training_message_frame').find('.training_message_inner').text('Correct');
			$(this).parent().find('.training_message_frame').css('background-color','#bdfbe4');
			

			// ----------------------------------
			//  Statistic Count
			// ----------------------------------
			//update total answered question right
			question_answered_right++;
			$('#question_answered_right').text(question_answered_right);
			// find the ansewr word
			var answer_word = "";
			$(this).parent().parent().find('.training_option_frame').children('.training_answer_frame').each(function () {
				if ($(this).text()==1){
					answer_word = $(this).parent().find('.training_option_frame_inner').text().replace(/^\s*|\s*$/g,'');
				}
			});	
			// add to individual word count
			$('.weak_words_word_hidden_count').each(function () {
				var word = $(this).parent().find('.weak_words_word_inner').text().replace(/^\s*|\s*$/g,'');
				if( word == answer_word)
				{
					var weak_word_count = parseInt($(this).text().replace(/^\s*|\s*$/g,'')) + 1;
					
					if (weak_word_count>2){
						$(this).parent().css('background-color','#bdfbe4');
					}
					else if(weak_word_count<=2 && weak_word_count>=-2)
					{
						$(this).parent().css('background-color','#bde9fb');						
					}
					else if(weak_word_count<-2)
					{
						$(this).parent().css('background-color','#fbbdc3');
					}
					
					$(this).text(weak_word_count);
				}				
			});
			
			
		}
		// user answer wrong
		else{
			
			// ----------------------------------
			//  Statistic Count
			// ----------------------------------
			//update total answered question wrong
			question_answered_wrong++;
			$('#question_answered_wrong').text(question_answered_wrong);
			var answer_word = "";
			$(this).parent().parent().find('.training_option_frame').children('.training_answer_frame').each(function () {
				if ($(this).text()==1){
					answer_word = $(this).parent().find('.training_option_frame_inner').text().replace(/^\s*|\s*$/g,'');
				}
			});	
			// add to individual word count
			$('.weak_words_word_hidden_count').each(function () {
				var word = $(this).parent().find('.weak_words_word_inner').text().replace(/^\s*|\s*$/g,'');

				if( word == answer_word)
				{
					var weak_word_count = parseInt($(this).text().replace(/^\s*|\s*$/g,'')) - 1;
					if (weak_word_count>2){
						$(this).parent().css('background-color','#bdfbe4');
					}
					else if(weak_word_count<=2 && weak_word_count>=-2)
					{
						$(this).parent().css('background-color','#bde9fb');						
					}
					else if(weak_word_count<-2)
					{
						$(this).parent().css('background-color','#fbbdc3');
					}
					
					$(this).text(weak_word_count);
				}				
				if( word == question_answered_wrong_word)
				{
					var weak_word_count = parseInt($(this).text().replace(/^\s*|\s*$/g,'')) - 1;
					
					if (weak_word_count>2){
						$(this).parent().css('background-color','#bdfbe4');
					}
					else if(weak_word_count<=2 && weak_word_count>=-2)
					{
						$(this).parent().css('background-color','#bde9fb');						
					}
					else if(weak_word_count<-2)
					{
						$(this).parent().css('background-color','#fbbdc3');
					}
					
					$(this).text(weak_word_count);
					question_answered_wrong_word = "";
				}		
						
			});
			
			// ----------------------------------
			//  Highlight work
			// ----------------------------------
			// highlight correct answer
			$(this).parent().parent().find('.training_option_frame').children('.training_answer_frame').each(function () {
				if ($(this).text()==1){
					$(this).parent().css('background-color','#fbbdc3');
				}
			});
			// display message and mark_as_important
			$(this).parent().find('.training_message_frame').find('.training_message_inner').text('Wrong');	
			$(this).parent().find('.training_message_frame').css('background-color','#fbbdc3');
		}
		
		

		// ----------------------------------
		//  Display Word Meaning either you get it right or wrong
		// ----------------------------------
		
	    $('.training_ans_main_vocabulary_frame').each(function(){
			var first_block = $('.fresh_queue').find('.training_block').first();
			var compare_block = $(this);
			var compare_text = $(this).find('.training_ans_vocabulary_name_parent').text().replace(/^\s*|\s*$/g,'');
			var marking_tag = $(this).find('.marking_div_tag').text();

			first_block.children('.training_option_frame').each(function(){
				var question_text = $(this).find('.training_option_frame_inner').text();
				if (compare_text==question_text){
					compare_block.css('display','block');
				}
		    });
	    });
	
		
    },

	mouseenter: function () {
		$(this).css('background-color', '#aff0cb');
	},
	mouseleave: function () {
		$(this).css('background-color', 'white');
	}
});

/*******************************************************
**	Option_Button
**
********************************************************/
$('.training_option_frame').live({
		
    click: function(){
		// highlight selected answer
		$(this).parent().children('.training_option_frame').each(function () {
			$(this).css('background-color', 'white');					
		});
		$(this).css('background-color', '#fcae14');	
		
		// this is for statistic count, weak words
		question_answered_wrong_word = $(this).find('.training_option_frame_inner').text().replace(/^\s*|\s*$/g,'');
		
		original_background = '#fcae14';

		// update global answer variable
		selected_answer = $(this).find('.training_answer_frame').text();
    },

	mouseenter: function () {
		original_background = $(this).css('background-color');
		$(this).css('background-color', '#f0d7af');
	},
	mouseleave: function () {
		$(this).css('background-color', original_background);
	}
});

/*******************************************************
**	Mark_As_Important_Button
**
********************************************************/

$('.mark_as_important_frame').live({
		
    click: function(){
		var this_block = $(this).parent().parent();
		$(this_block).clone().appendTo(enchance_queue);
		$(this_block).clone().appendTo(enchance_queue);
		
		$.get("http://translate.google.com/translate_tts", function(data){
			alert(data);
		});
		
    },

	mouseenter: function () {
		$(this).css('background-color', '#bde9fb');
	},
	mouseleave: function () {
		$(this).css('background-color', 'white');
	}
});

/*******************************************************
**	Training_Button_Next
**
********************************************************/

$('.training_button_next').live({
		
    click: function(){

		// to prevent memorizing the last state, we reset the selected answer to 5, if nothing is selected, we will know.
		selected_answer = 5;
		
		// clean up garbage collection to avoid random sound trigger
		$('#training_ans_garbage_collection').children('embed').each(function () {
			$(this).remove();
		});		
		
		// clean up additional message box
		$('.training_ans_main_vocabulary_frame').each(function(){
			$(this).css('display','none');
	    });	
		
		// show statistic frame
		$('.statistic_frame').css('display','block');
		
		
	
		// if random number is 0, we put in the next question from the enchancement queue
		if ( global_random_number == 0){
			
			// extract enhancement block
			var enchance_block = $('.enchance_queue').find('.training_block').first();
			$('.fresh_queue').prepend(enchance_block);
			
			// update random number
			global_random_number = Math.floor(Math.random()*3+2);			
		}
		
		if (global_question_counter > 5)
		{
			var result = $(this).parent().find('.training_message_frame').text().replace(/^\s*|\s*$/g,'');
			// if we get it Wrong, append it to the other queue
			if (result == "Wrong")
			{	
				var enchance_queue = $('.enchance_queue');
				
				$(this).parent().find('.training_button_ok').css('display','block'); 	// show ok button
				$(this).parent().find('.training_message_frame').css('display','none');	// hide message 
				$(this).parent().find('.mark_as_important_frame').css('display','none');	// hide mark_as_important_button
				$(this).css('display','none');	// next button
				$('.training_option_frame').css('background-color','white'); // make option unselected
				
				// append clones to enhance queue, so it will be asked again shortly
				var this_block = $(this).parent().parent();
				$(this_block).clone().appendTo(enchance_queue);
				$(this_block).clone().appendTo(enchance_queue);
				$(this_block).appendTo(enchance_queue);
				
				global_question_counter--;
				global_random_number--;
				//alert('Wrong '+global_question_counter+' Random '+global_random_number);
				
				// display next question
				var selected_block = $('.fresh_queue').find('.training_block').first();
				selected_block.css('display', 'block');
				
			}
			// if we get it Right, remove and proceed to next question
			else if(result == "Correct")
			{
				// remove current question
				var remove_block = $('.fresh_queue').find('.training_block').first();
				remove_block.remove();
				// display next question
				var selected_block = $('.fresh_queue').find('.training_block').first();
				selected_block.css('display', 'block');
				global_question_counter--;
				global_random_number--;
				//alert('Correct '+global_question_counter+' Random '+global_random_number);
				
			}
			
		}
		
		// if global_question_counter is too low, we add more questions in the queue
		else
		{
			// remove current question
			var remove_block = $('.fresh_queue').find('.training_block').first();
			remove_block.remove();
			// display next question
			var selected_block = $('.fresh_queue').find('.training_block').first();
			selected_block.css('display', 'block');
			global_question_counter--;
			global_random_number--;
			

			// when global_question_counter is less than 5, we call 10 more
			var author_name = $('#author_name').text();
			var list_name = $('#list_title').text();
			var dropdown_val = $('.training_header_select').val();
			$.get("/training/get_next_list_of_question/", {'author_name':author_name, 'list_name':list_name, 'category':dropdown_val},function(data){
				var new_training_questions = JSON.parse(data);
				for (question in new_training_questions)
				{
					var Q = question;
					var A = new_training_questions[question];

					// append question as training block
					var new_block = 
					"<div class='training_block'>"+
						"<div class='training_question_frame'>"+
							Q+
						"</div>"+
						
						"<div class='vocabulary_sound_training'>" +
							"<div class='vocabulary_sound_image'>" +
								"<img src='/media/Images/speaker.jpeg' width='25px' height='25px'/>" +
							"</div>" +
							"<div class='vocabulary_sound_training_text'>" +
								A[0][1] +
							"</div>" +
						"</div>"+
						
						"<div class='training_option_frame'>"+
							"<div class='training_option_frame_inner'>"+ A[0][1] +"</div>"+			
							"<div class='training_answer_frame'>" + A[0][0] + "</div>"+
						"</div>"+
						
						"<div class='vocabulary_sound_training'>" +
							"<div class='vocabulary_sound_image'>" +
								"<img src='/media/Images/speaker.jpeg' width='25px' height='25px'/>" +
							"</div>" +
							"<div class='vocabulary_sound_training_text'>" +
								A[1][1] +
							"</div>" +
						"</div>"+
						
						"<div class='training_option_frame'>"+
							"<div class='training_option_frame_inner'>"+ A[1][1] +"</div>"+			
							"<div class='training_answer_frame'>" + A[1][0] + "</div>"+
						"</div>"+
						
						"<div class='vocabulary_sound_training'>" +
							"<div class='vocabulary_sound_image'>" +
								"<img src='/media/Images/speaker.jpeg' width='25px' height='25px'/>" +
							"</div>" +
							"<div class='vocabulary_sound_training_text'>" +
								A[2][1] +
							"</div>" +
						"</div>"+
						
						"<div class='training_option_frame'>"+
							"<div class='training_option_frame_inner'>"+ A[2][1] +"</div>"+			
							"<div class='training_answer_frame'>" + A[2][0] + "</div>"+
						"</div>"+
						
						"<div class='vocabulary_sound_training'>" +
							"<div class='vocabulary_sound_image'>" +
								"<img src='/media/Images/speaker.jpeg' width='25px' height='25px'/>" +
							"</div>" +
							"<div class='vocabulary_sound_training_text'>" +
								A[3][1] +
							"</div>" +
						"</div>"+
						
						"<div class='training_option_frame'>"+
							"<div class='training_option_frame_inner'>"+ A[3][1] +"</div>"+			
							"<div class='training_answer_frame'>" + A[3][0] + "</div>"+
						"</div>"+

						"<div class='training_button_frame'>"+
							"<div class='training_button_next'>"+
								"<div class='training_button_inner'>NEXT</div>"+
							"</div>"+

							"<div class='training_button_ok'>"+
								"<div class='training_button_inner'>OK</div>"+
							"</div>"+

							"<div class='training_message_frame'>"+
								"<div class='training_message_inner'>"+
								"</div>"+
							"</div>"+

							"<div class='mark_as_important_frame'>"+
								"<div class='mark_as_important_inner'>"+
									"Mark as Important"+
								"</div>"+
							"</div>"+
						"</div>"+
					"</div>";
					
					// append new generated question to fresh queue
					var fresh_queue = $('.fresh_queue');
			        $(new_block).appendTo(fresh_queue);
					global_question_counter++;
					// debug use
					//alert('Reload '+global_question_counter+' Random '+global_random_number);
				}
			});	
		}
    },

	mouseenter: function () {
		$(this).css('background-color', '#f0d7af');
	},
	mouseleave: function () {
		$(this).css('background-color', 'white');
	}
});


/*******************************************************
**	Header Dropdown Menu Change
**
********************************************************/

$('.training_header_select').change(function(){
	
	// clean out all questions in fresh queue
	$('.fresh_queue').children('.training_block').each(function () {
		$(this).remove();
	});
	// clean out all questions in enchance queue
	$('.enchance_queue').children('.training_block').each(function () {
		$(this).remove();
	});
	
	// get 10 new questions from server, and put it in fresh queue
	var author_name = $('#author_name').text();
	var list_name = $('#list_title').text();
	var dropdown_val = $('.training_header_select').val();
	global_question_counter = 0;
	$.get("/training/get_next_list_of_question/", {'author_name':author_name, 'list_name':list_name, 'category':dropdown_val},function(data){
		var new_training_questions = JSON.parse(data);
		for (question in new_training_questions)
		{
			var Q = question;
			var A = new_training_questions[question];
			// append question as training block
			var new_block = 
			"<div class='training_block'>"+
				"<div class='training_question_frame'>"+
					Q+
				"</div>"+

				"<div class='vocabulary_sound_training'>" +
					"<div class='vocabulary_sound_image'>" +
						"<img src='/media/Images/speaker.jpeg' width='25px' height='25px'/>" +
					"</div>" +
					"<div class='vocabulary_sound_training_text'>" +
						A[0][1] +
					"</div>" +
				"</div>"+

				"<div class='training_option_frame'>"+
					"<div class='training_option_frame_inner'>"+ A[0][1] +"</div>"+			
					"<div class='training_answer_frame'>" + A[0][0] + "</div>"+
				"</div>"+
				
				"<div class='vocabulary_sound_training'>" +
					"<div class='vocabulary_sound_image'>" +
						"<img src='/media/Images/speaker.jpeg' width='25px' height='25px'/>" +
					"</div>" +
					"<div class='vocabulary_sound_training_text'>" +
						A[1][1] +
					"</div>" +
				"</div>"+
				
				"<div class='training_option_frame'>"+
					"<div class='training_option_frame_inner'>"+ A[1][1] +"</div>"+			
					"<div class='training_answer_frame'>" + A[1][0] + "</div>"+
				"</div>"+
				
				"<div class='vocabulary_sound_training'>" +
					"<div class='vocabulary_sound_image'>" +
						"<img src='/media/Images/speaker.jpeg' width='25px' height='25px'/>" +
					"</div>" +
					"<div class='vocabulary_sound_training_text'>" +
						A[2][1] +
					"</div>" +
				"</div>"+
				
				"<div class='training_option_frame'>"+
					"<div class='training_option_frame_inner'>"+ A[2][1] +"</div>"+			
					"<div class='training_answer_frame'>" + A[2][0] + "</div>"+
				"</div>"+
				
				"<div class='vocabulary_sound_training'>" +
					"<div class='vocabulary_sound_image'>" +
						"<img src='/media/Images/speaker.jpeg' width='25px' height='25px'/>" +
					"</div>" +
					"<div class='vocabulary_sound_training_text'>" +
						A[3][1] +
					"</div>" +
				"</div>"+
				
				"<div class='training_option_frame'>"+
					"<div class='training_option_frame_inner'>"+ A[3][1] +"</div>"+			
					"<div class='training_answer_frame'>" + A[3][0] + "</div>"+
				"</div>"+

				"<div class='training_button_frame'>"+
					"<div class='training_button_next'>"+
						"<div class='training_button_inner'>NEXT</div>"+
					"</div>"+

					"<div class='training_button_ok'>"+
						"<div class='training_button_inner'>OK</div>"+
					"</div>"+

					"<div class='training_message_frame'>"+
						"<div class='training_message_inner'>"+
						"</div>"+
					"</div>"+

					"<div class='mark_as_important_frame'>"+
						"<div class='mark_as_important_inner'>"+
							"Mark as Important"+
						"</div>"+
					"</div>"+
				"</div>"+
			"</div>";
			
			// append new generated question to fresh queue
			var fresh_queue = $('.fresh_queue');
	        $(new_block).appendTo(fresh_queue);
			global_question_counter++;
			
			// display first question in the queue
			var selected_block = $('.fresh_queue').find('.training_block').first();
			selected_block.css('display', 'block');
			
			// debug use
			//alert('Reload '+global_question_counter+' Random '+global_random_number);
		}
	});	
	
});



/*******************************************************
**		Sound Effects
**		
**
********************************************************/
$('.vocabulary_sound_training').live({
		
    click: function(){
		var content = $(this).find('.vocabulary_sound_training_text').text().replace(/^\s*|\s*$/g,'');
		var firefox = "<embed height='0px'  src='http://translate.google.com/translate_tts?tl=en&q="+content+"' type='audio/mpeg'></embed>";
		var chorme = "<embed height='0px'  src='http://translate.google.com/translate_tts?tl=en&q="+content+"' ></embed>";
		$(firefox).appendTo('#training_garbage');
		$(chorme).appendTo('#training_garbage');
    },

	mouseenter: function () {
	},
	mouseleave: function () {
	}
});

