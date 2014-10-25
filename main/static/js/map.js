var Map = {

	init: function (markers, count, regionsData){
		$(function(){
			//TODO:
			// - Change regions colors with sliders
			// - Set marker color by attack type

			var val = 0;

			console.log(markers);
			console.log(count);
			console.log(regionsData);

			// Internal value used to set the same opacity for each marker
			var opacityData = [];
			var colorData =[]
			for (var i = 0; i < count.length; i++) {
				opacityData[i] = 0.7;
				colorData[i] = markers[i].name;
			};

			console.log(colorData);

			// This section is where you can customize most of the looks of the map
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

						// Sets up the colors for each attack type, maybe a more elegant solution can be done in the future
						scale: {
							'smbd' : '#ff0000',
							'httpd' : '#00ff04',
							'epmapper' : '#0021ff',
							'mssqld' : '#fff500'
						},
						values: colorData
					},
					{
						attribute: 'fill-opacity',
						values: opacityData
					},
					{
						attribute: 'r',
						scale: [10,15],
						values: count
					}],

					regions: [{
						values: regionsData,
						scale: ['#00efff','#002bff']
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

			// Implements the slider functionality
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