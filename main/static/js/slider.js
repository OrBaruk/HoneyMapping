	jQuery(document).ready(function(){
		jQuery('#button-9')
		.button({
			icons: { 
				primary: 'ui-icon-play'
			},
			text: false
		})
		.click(function animation (){
			$.getJSON("http://127.0.0.1:8000/report/2015/09/1"+day, function(data){
				Map.update(data['markers'], data['count'], data['regions']);			
				day = day + 1;
				$( "#slider" ).slider( "value", day );
							
				if( day !=  10){ // NUMBER OF DAYS IN A MONTH HERE										
					setTimeout(animation, 500);
				}
			});
		});	
	});

var day = 0;

// Implements the slider functionality
$("#slider").slider({
	value: day,
	min: 0,
	max: 10, // HERE GOES THE NUMBER OF DAYS LEFT IN THE MONTH
	animate: true,
	step: 1,
	slide: function( event, ui){
		day = ui.value;

		if (day != 0) {
			aux = "http://127.0.0.1:8000/report/2015/09/1"+day;
			$.getJSON(aux, function(data){
				console.log(aux);
				Map.update(data['markers'], data['count'], data['regions']);
			});
		}
		else{
			aux = "http://127.0.0.1:8000/report/2015/09";
			Map.update(initialMonth['markers'], initialMonth['count'], initialMonth['regions']);
		}	
		
	}
});