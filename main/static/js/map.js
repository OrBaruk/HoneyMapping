var Map = {

	init: function (markers, count){
		$(function(){
			var val = 0;

			console.log(markers);
			console.log(count);

			// Internal value used to set the same opacity for each marker
			var opacity = [];
			for (var i = 0; i < count.length; i++) {
				opacity[i] = 0.5
			};

			mapObject = $('#world-map').vectorMap({
				map: 'world_mill_en',
				scaleColors: ['#C8EEFF', '#0071A4'],	
				normalizeFunction: 'polynomial',
				hoverOpacity: 0.7,
				hoverColor: false,

				backgroundColor: '#647284',

				markers: markers,

				series: {
					markers: [{
						attribute: 'fill',
						scale: ['#8385ff', '#0014ff'],
						values: count
					},
					{
						attribute: 'fill-opacity',
						values: opacity
					},
					{
						attribute: 'r',
						scale: [10,15],
						values: count
					}]
				},

				onMarkerLabelShow: function(event, label, index){
				label.html(
					'<p>City: '+markers[index].city+'</p>'+
					'<p>Type: '+markers[index].name+'</p>'+
					'<p>Port: '+markers[index].port+'</p>'+
					'<p>Packets received: ' +markers[index].count+'</p>'
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