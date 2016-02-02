var day = 1;
var isPlaying = false


var startDate = moment(new Date(2015, 05, 1, 0, 0));
var endDate = moment(new Date(2015, 05, 30, 23, 59));
var timeout = 500; // miliseconds?

var sliderVal = 0;
var sliderMax = (endDate - startDate)/60000;
var sliderStep = 60*24; // Minutes


var queryStart = moment(new Date(2015, 05, 1, 0, 0)); 
var queryEnd = moment(new Date(2015, 05, 1, 0, 0));
queryEnd.add(sliderStep, 'minutes');


console.log(sliderMax);

console.log(startDate.add(1, 'hour'));
console.log(queryStart.format("YYYY/MM/DD/HH/mm"));
console.log(queryEnd.format("YYYY/MM/DD/HH/mm"));

function animation(){
	console.log(sliderVal);
	console.log(queryStart.format("YYYY/MM/DD/HH/mm"));
	console.log(queryEnd.format("YYYY/MM/DD/HH/mm"));


	sliderVal += sliderStep;
	queryStart.add(sliderStep, 'minutes');
	queryEnd.add(sliderStep, 'minutes');

	if(sliderVal > sliderMax){
		sliderVal = 0;
		queryStart = moment(new Date(2015, 05, 1, 0, 0)); 
		queryEnd = moment(new Date(2015, 05, 1, 0, 0));
		queryEnd.add(sliderStep, 'minutes');
	}

	queryString = "http://127.0.0.1:8000/report/"+queryStart.format("YYYY/MM/DD/HH/mm/")+queryEnd.format("YYYY/MM/DD/HH/mm/")

	$.getJSON(queryString, function(data){
		Map.update(data['markers'], data['count'], data['regions']);
		$( "#slider" ).slider( "value", sliderVal );
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
				setTimeout(timeout_loop, timeout);
			}
		}; timeout_loop();

	});	
});

$("#slider").slider({
	value: sliderVal,
	min: 0,
	max: sliderMax,
	animate: true,
	step: sliderStep,
	slide: function( event, ui){
		sliderVal = ui.value;

		queryStart = moment(new Date(2015, 05, 1, 0, 0)); 
		queryEnd = moment(new Date(2015, 05, 1, 0, 0));
		queryStart.add(sliderVal, 'minutes');
		queryEnd.add(sliderVal + sliderStep, 'minutes');

		queryString = "http://127.0.0.1:8000/report/"+queryStart.format("YYYY/MM/DD/HH/mm/")+queryEnd.format("YYYY/MM/DD/HH/mm/")

		$.getJSON(queryString, function(data){
			Map.update(data['markers'], data['count'], data['regions']);
			$( "#slider" ).slider( "value", sliderVal );
		});
	};
});


function reloadSlider(){
	//$( "#slider" ).slider( "option", "min", day );
	//$( "#slider" ).slider( "option", "min", day );
	//$( "#slider" ).slider( "option", "min", day );
	//$( "#slider" ).slider( "option", "min", day );
	//$( "#slider" ).slider( "option", "min", day );
	//$( "#slider" ).slider( "option", "min", day );
	//$( "#slider" ).slider( "option", "min", day );
	//$( "#slider" ).slider( "option", "min", day );
};
