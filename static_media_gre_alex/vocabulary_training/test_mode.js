
$(document).ready(function(){
});

var original_background = "";
/*******************************************************
**	Config_Button
**
********************************************************/

// Config Button
$('.test_button_config').live({
		
	// Check if ansewer is correct, display answer or increment points	
    click: function(){
		var label = $(this).text().replace(/^\s*|\s*$/g,'');
		if (label=='Configuration')
		{
			$(this).parent().parent().find('.test_header_config_section').css('display','block');
			$(this).parent().parent().css('border','1px solid #042614');
			$(this).find('.test_button_inner').find('b').text('Generate');	
		}
		else if (label=='Generate')
		{
			var author_name = $('#author_name').text();
			var list_name = $('#list_title').text();	
			var dropdown_val = $('#test_category').val();
			var amount_requested = $('.test_question_number_input').attr('value');
			
			$.get("/training/get_test_question_given_amount/", {'author_name':author_name, 'list_name':list_name, 'category':dropdown_val, 'amount':amount_requested},function(data){
				
				// remove all questions in test mode
				$('.test_frame').children('.test_block').each(function () {
					$(this).remove();
				});
				$('.submit_button_outter').remove();
				
				// append the amount of questions we want
				var counter = 1;
				var new_test_questions = JSON.parse(data);
				for (question in new_test_questions)
				{
					var Q = question;
					var A = new_test_questions[question];
					var new_block = 
						"<div class='test_block'>"+
							"<div class='test_loop_counter'>"+
								counter +
							"</div>" +
							"<div class='test_question_frame'>" +
								Q +
							"</div>" +

							"<div class='test_option_frame'>" +
								"<div class='test_option_frame_inner'>" + A[0][1] + "</div>"+
								"<div class='test_answer_frame'>"+ A[0][0] + "</div>" +
								"<div class='test_result_frame'>n</div>" +
							"</div>" +
							"<div class='test_option_frame'>" +
								"<div class='test_option_frame_inner'>" + A[1][1] + "</div>"+
								"<div class='test_answer_frame'>"+ A[1][0] + "</div>" +
								"<div class='test_result_frame'>n</div>" +
							"</div>" +
							"<div class='test_option_frame'>" +
								"<div class='test_option_frame_inner'>" + A[2][1] + "</div>"+
								"<div class='test_answer_frame'>"+ A[2][0] + "</div>" +
								"<div class='test_result_frame'>n</div>" +
							"</div>" +
							"<div class='test_option_frame'>" +
								"<div class='test_option_frame_inner'>" + A[3][1] + "</div>"+
								"<div class='test_answer_frame'>"+ A[3][0] + "</div>" +
								"<div class='test_result_frame'>n</div>" +
							"</div>" +
							
						"</div>";
					
						// append new generated question to test frame
						var test_frame = $('.test_frame');
				        $(new_block).appendTo(test_frame);
						counter++;
				}
				
				// append a new submit button
				var submit_button = 
					"<div class='submit_button_outter'>"+
						"<div class='submit_button_inner'>"+
							"<b>Submit</b>"+
						"</div>"+
					"</div>";
				$(submit_button).appendTo(test_frame);					
					
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
**	Option_Button
**
********************************************************/
$('.test_option_frame').live({
		
    click: function(){
		
		// highlight selected answer
		$(this).parent().children('.test_option_frame').each(function () {
			$(this).css('background-color', 'white');					
		});
		$(this).css('background-color', '#fcae14');					
		original_background = '#fcae14';

		// update global answer variable
		selected_answer = $(this).find('.test_answer_frame').text().replace(/^\s*|\s*$/g,'');
		if (selected_answer==1){
			$(this).children('.test_result_frame').each(function () {
				$(this).text('n');
			});
			$(this).find('.test_result_frame').text('y');
		}
		else
		{
			$(this).children('.test_result_frame').each(function () {
				$(this).text('n');
			});
		}
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
**	Submit_Button_Outter
**
********************************************************/

$('.submit_button_outter').live({
		
    click: function(){
		
		var total_q = 0;
		var correct_ans = 0;
		$(this).parent().children('.test_block').each(function () {
			total_q++;			
			$(this).children('.test_option_frame').each(function () {
				result = $(this).find('.test_result_frame').text().replace(/^\s*|\s*$/g,'');
				ans = $(this).find('.test_answer_frame').text().replace(/^\s*|\s*$/g,'');
				
				if (ans=="1"){
					$(this).css('background-color', '#fbbdc3');
					
				}
				if (result=="y"){
					
					correct_ans++;
					$(this).css('background-color', '#aff0cb');
				}
			
			});
		});
		$(this).find('.submit_button_inner').find('b').text('You Got '+correct_ans+' Out of '+total_q);
    },

	mouseenter: function () {
		$(this).css('background-color', '#f0d7af');
	},
	mouseleave: function () {
		$(this).css('background-color', 'white');
	}
});