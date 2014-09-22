var Map = {

	init: function (markers, count){
		$(function(){
			jQuery(document).ready(function(){
				jQuery('#button-9')
				.button({
					icons: { 
						primary: 'ui-icon-play'
					},
					text: false
				})
				.click(function animacao (){
					console.log("play!");
					val += 1;
					$( "#slider" ).slider( "value", val );
					if( val < markers.length){
						setTimeout(animacao, 1000);
					}
				});
			});

			var val = 0;

			console.log(markers);
			console.log(count);

			mapObject = $('#world-map').vectorMap({
				map: 'world_mill_en',
				scaleColors: ['#C8EEFF', '#0071A4'],	
				normalizeFunction: 'polynomial',
				hoverOpacity: 0.7,
				hoverColor: false,

				backgroundColor: '#383f47',

				markers: markers,

				series: {
					markers: [{
						attribute: 'fill',
						scale: ['#FEE5D9', '#A50F15'],
						values: count
					},{
						attribute: 'r',
						scale: [5,10],
						values: count
					}]
				},

				onMarkerLabelShow: function(event, label, index){
				label.html(
					'<p>City: '+markers[index].city+'</p>'+
					'<p>Type: '+markers[index].name+'</p>'+
					'<p>Port: '+markers[index].port+'</p>'+
					'<p>count: ' +markers[index].count+'</p>'
				);
				},
				onRegionLabelShow: function(event, label, code){
				label.html(
					'<b>'+label.html()+'</b></br>'
				);
				}
			});

			var mapObject = $('#world-map').vectorMap('get', 'mapObject');

			$("#slider").slider({
				value: val,
				min: 0,
				max: markers.length,
				animated: true,
				step: 1,
				slide: function( event, ui ){
					val = ui.value;
					if ( val == markers.length) {
						mapObject.removeAllMarkers();
						mapObject.addMarkers( markers);
						mapObject.series.markers[0].setValues(count);
						mapObject.series.markers[1].setValues(count);
					} else{
						mapObject.removeAllMarkers();
						mapObject.addMarker( val, markers[val]);
						mapObject.series.markers[0].setValues(count);
						mapObject.series.markers[1].setValues(count);
					}					
				}
			});
		});
	}

};