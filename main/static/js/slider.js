var isPlaying = false

var startDate = moment(new Date(2015, 05, 1, 0, 0));
var endDate = moment(new Date(2015, 05, 30, 23, 59));
var timeout = 500; // miliseconds?

var sliderVal = 0;
var sliderMax = (endDate - startDate)/60000;
var sliderStep = 60*24; // Minutes

var queryStart = new moment(startDate); 
var queryEnd = new moment(startDate).add(sliderStep, "minutes");

function animateSlider(){
	sliderVal += sliderStep;
	queryStart.add(sliderStep, "minutes");
	queryEnd.add(sliderStep, "minutes");

	if(sliderVal > sliderMax){
		sliderVal = 0;
		queryStart = new moment(startDate); 
		queryEnd = new moment(startDate).add(sliderStep, "minutes").add(sliderStep, "minutes");
	}
	queryString = "http://127.0.0.1:8000/report/"+queryStart.format("YYYY/MM/DD/HH/mm/")+queryEnd.format("YYYY/MM/DD/HH/mm/")

	$.getJSON(queryString, function(data){
		Map.update(data["markers"], data["count"], data["regions"]);
		$( "#slider" ).slider( "value", sliderVal );

		document.getElementById("curentTimeText").innerHTML = queryString;

		if (isPlaying){
			setTimeout(animateSlider, timeout);
		}
	});
};

$(function () {
	$("#startDatePicker").datetimepicker({
		defaultDate: startDate,
	});
	$("#endDatePicker").datetimepicker({
		defaultDate: endDate,
    	useCurrent: false //Important! See issue #1075
	});
	$("#startDatePicker").on("dp.change", function (e) {
		$("#endDatePicker").data("DateTimePicker").minDate(e.date);
	});
	$("#endDatePicker").on("dp.change", function (e) {
    	$("#startDatePicker").data("DateTimePicker").maxDate(e.date);
	});

	$("#play-toggle").click( function(){
		$(this).find("i").toggleClass("glyphicon-play").toggleClass("glyphicon-pause");
		if (isPlaying) {
			isPlaying = false;
		}else{
	    	isPlaying = true;
		}

		if (isPlaying){
			animateSlider();
		}
	});

	$("#reloadSlider").click( function(){
		isPlaying = false;

		startDate = $("#startDatePicker").data("DateTimePicker").date();
		endDate = $("#endDatePicker").data("DateTimePicker").date();
		timeout = document.getElementById("inputTimeout").value;
		sliderVal = 0;
		sliderMax = (endDate - startDate)/60000;

		var step = document.getElementById("inputSliderStep").value;
		var unity = document.getElementById("stepSelect").value;
		switch(unity){
			case "Minutes":
				sliderStep = step;
			break;

			case "Hours":
				sliderStep = step*60;
			break;

			case "Days":
				sliderStep = step*1440;
			break;

			case "Months":
				sliderStep = step*43200;
			break;
		}
		
		queryStart = new moment(startDate); 
		queryEnd = new moment(startDate).add(sliderStep, "minutes");
		$( "#slider" ).slider( "option", 
			{ value : sliderVal,  min : 0,  max : sliderMax, step : sliderStep });

		// TODO: Reset map
	});

	$("#slider").slider({
		value: sliderVal,
		min: 0,
		max: sliderMax,
		animate: true,
		step: sliderStep,
		slide: function( event, ui){
			sliderVal = ui.value;

			queryStart = new moment(startDate); 
			queryEnd = new moment(startDate);

			queryStart.add(sliderVal, "minutes");
			queryEnd.add(sliderVal + sliderStep, "minutes");

			queryString = "http://127.0.0.1:8000/report/"+queryStart.format("YYYY/MM/DD/HH/mm/")+queryEnd.format("YYYY/MM/DD/HH/mm/")

			$.getJSON(queryString, function(data){
				Map.update(data["markers"], data["count"], data["regions"]);
				$( "#slider" ).slider( "value", sliderVal );
			});
		}
	});

});

