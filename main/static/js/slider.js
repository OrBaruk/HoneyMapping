var day = 0;

jQuery(document).ready(function(){	
	jQuery('#button-9')
	.button({
		icons: { 
			primary: 'ui-icon-play'
		},
		text: false
	})
	.click(function animation (){
		$.getJSON("http://127.0.0.1:8000/report/2014/09/"+day+"/0/0/2014/09/"+day+"/23/59/", function(data){
			Map.update(data['markers'], data['count'], data['regions']);			
			day = day + 1;
			$( "#slider" ).slider( "value", day );
						
			if( day !=  monthSize){ // NUMBER OF DAYS IN A MONTH HERE										
				setTimeout(animation, 500);
			}
		});
	});	
});

// Implements the slider functionality
$("#slider").slider({
	value: day,
	min: 0,
	max: monthSize,
	animate: true,
	step: 1,
	slide: function( event, ui){
		day = ui.value;

		if (day != 0) {
			aux = "http://127.0.0.1:8000/report/2014/09/"+day+"/0/0/2014/09/"+day+"/23/59/";
			$.getJSON(aux, function(data){
				Map.update(data['markers'], data['count'], data['regions']);
			});
		}
		else{
			aux = "http://127.0.0.1:8000/report/2014/08/"+day+"/0/0/2014/09/"+day+"/23/59/";
			Map.update(initialMonth['markers'], initialMonth['count'], initialMonth['regions']);
		}	
		
	}
});