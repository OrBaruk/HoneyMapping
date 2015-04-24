	jQuery(document).ready(function(){
		jQuery('#button-9')
		.button({
			icons: { 
				primary: 'ui-icon-play'
			},
			text: false
		})
		.click(function animation (){
			Map.update(day2['markers'], day2['count'], day2['regions']);
		});	
		});



//Implements the slider functionality
// $("#slider").slider({
// 	value: val,
// 	min: 0,
// 	max: markers.length - 1,
// 	animate: true,
// 	step: 1,
// 	slide: function( event, ui ){
// 		val = ui.value;
// 		mapObject.removeAllMarkers();
// 		mapObject.reset();
// 		mapObject.addMarkers(markers[val]);
// 		mapObject.series.markers[0].setValues(colorData[val]);
// 		mapObject.series.markers[1].setValues(opacityData[val]);
// 		//mapObject.series.markers[2].setValues(radiusData[val]);
// 		//mapObject.series.regions[0].setValues(regionsData[val]);		
// 	}
// });