var day = 1;
var isPlaying = false

// incremate(day, "2015/06/7"/){
// 	return "2015/06/8"
// }

function animation(){
	$.getJSON("http://127.0.0.1:8000/report/2015/06/"+day+"/0/0/2015/06/"+day+"/23/59/", function(data){
		Map.update(data['markers'], data['count'], data['regions']);			
		day = day + 1;
		if (day == monthSize){
			day = 1;
		};
		$( "#slider" ).slider( "value", day );
		$( "#slider" ).slider( "option", "min", day );
	});
};

jQuery(document).ready(function(){	
	jQuery('#button-9')
	.button({
		icons: { 
			primary: 'ui-icon-play'
		},
		text: false
	})
	.click(function (){
		if (isPlaying) {
			$(".ui-button-icon-primary", this).toggleClass("ui-icon-pause ui-icon-play");
			isPlaying = false;
		}else{
			$(".ui-button-icon-primary", this).toggleClass("ui-icon-pause ui-icon-play");
			isPlaying = true;
		}
		function timeout_loop (){
			if (isPlaying){
				animation();
				setTimeout(timeout_loop, 500);
			}
		}; timeout_loop();

	});	
});

// Implements the slider functionality
$("#slider").slider({
	value: day,
	min: 1,
	max: monthSize,
	animate: true,
	step: 1,
	slide: function( event, ui){
		day = ui.value;

		if (day != 0) {
			aux = "http://127.0.0.1:8000/report/2015/06/"+day+"/0/0/2015/06/"+day+"/23/59/";
			$.getJSON(aux, function(data){
				Map.update(data['markers'], data['count'], data['regions']);
			});
		}
		else{
			aux = "http://127.0.0.1:8000/report/2015/06/"+day+"/0/0/2015/07/"+day+"/23/59/";
			Map.update(initialMonth['markers'], initialMonth['count'], initialMonth['regions']);
		}	
		
	}
});