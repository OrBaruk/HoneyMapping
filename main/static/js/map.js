var Map = {

	init: function (markers, radiusData, regionsData){
		$(function(){
			var val = 0;

			console.log(markers);
			
			// Internal value used to set the same opacity for each marker
			var opacityData = [];
			var colorData =[];

			for (var i = 0; i < markers.length; i++) {
				var opacityAux = [];
				var colorAux = [];

				for (var j = 0; j < markers[i].length; j++) {
					opacityAux[j] = 0.7;
					colorAux[j] = markers[i][j].name;
				};

				opacityData[i] = opacityAux;
				colorData[i] = colorAux;
			};

			
			// This section is where you can customize most of the looks of the map
			mapObject = $('#world-map').vectorMap({
				map: 'world_mill_en',
				scaleColors: ['#C8EEFF', '#0071A4'],	
				normalizeFunction: 'polynomial',
				hoverOpacity: 0.7,
				hoverColor: false,

				backgroundColor: '#647284',

				markers: markers[val],

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
						values: colorData[val]
					},
					{
						attribute: 'fill-opacity',
						values: opacityData[val]
					},
					{
						attribute: 'r',
						scale: [10,15],
						values: radiusData[val]
					}],

					regions: [{
						scale: ['#b9b9ff','#0000ff'],
						values: regionsData[val]
					}]
				},

				onMarkerLabelShow: function(event, label, index){
				label.html(
					'<p>City: '+markers[val][index].city+'</p>'+
					'<p>Type: '+markers[val][index].name+'</p>'+
					'<p>Port: '+markers[val][index].port+'</p>'+
					'<p>Packets Sent: ' +markers[val][index].radiusData+'</p>'
				);
				},
				onRegionLabelShow: function(event, label, code){
				label.html(
					'<b>'+label.html()+'</b></br>'+
					'<p>Packets Sent: '+regionsData[val][code]+'</p>'
				);
				}
			});

			// Implements the slider functionality
			var mapObject = $('#world-map').vectorMap('get', 'mapObject');
			$("#slider").slider({
				value: val,
				min: 0,
				max: markers.length - 1,
				animated: true,
				step: 1,
				slide: function( event, ui ){
					val = ui.value;
					mapObject.reset();
					mapObject.addMarkers(markers[val]);
					mapObject.series.markers[0].setValues(colorData[val]);
					mapObject.series.markers[1].setValues(opacityData[val]);
					mapObject.series.markers[2].setValues(radiusData[val]);
					mapObject.series.regions[0].setValues(regionsData[val]);
				}
			});


		});
	}

};