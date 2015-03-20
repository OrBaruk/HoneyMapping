var Map = {

	init: function (markers, radiusData, regionsData){
		$(function(){
			var val = 0;

			console.log("markers");
			console.log(markers);
			console.log("radius");
			console.log(radiusData);
			console.log("regions");
			console.log(regionsData);


			jQuery(document).ready(function(){
				jQuery('#button-9')
				.button({
					icons: { 
						primary: 'ui-icon-play'
					},
					text: false
				})
				.click(function animation (){
					val = val + 1;
					
					$( "#slider" ).slider( "value", val );
					mapObject.removeAllMarkers();
					mapObject.reset();
					mapObject.addMarkers(markers[val]);
					mapObject.series.markers[0].setValues(colorData[val]);
					mapObject.series.markers[1].setValues(opacityData[val]);
					//mapObject.series.markers[2].setValues(radiusData[val]);
					//mapObject.series.regions[0].setValues(regionsData[val]);

					if( val != markers.length - 1){										
						setTimeout(animation, 500);
					}
				});
			});

			// Internal value used to set the same opacity for each marker
			// This computation in the future should be done by the server and cached
			var opacityData = [];
			var colorData =[];
			for (var i = 0; i < markers.length; i++) {
				opacityData[i] = 0.7;
				colorData[i] = markers[i].name;
			};
			
			// This section is where you can customize most of the looks of the map
			var mapObject = $('#world-map').vectorMap({
				map: 'world_mill_en',
				// scaleColors: ['#C8EEFF', '#0071A4'],	
				normalizeFunction: 'polynomial',
				hoverOpacity: 0.7,
				hoverColor: false,

				backgroundColor: '#6699cc',

				markers: markers,

				series: {
					markers: [{
						attribute: 'fill',

						// Sets up the colors for each attack type, maybe a more elegant solution can be done in the future
						scale: {
							'smbd' : '#0000ff',
							'httpd' : '#00ff00',
							'mssqld' : '#ff8000',
							'epmapper' : '#ff0080',
							'ftpd' : '#66ffff',
							'SipSession' : '#ff0000'
						},
						values: colorData
					},
					{
						attribute: 'fill-opacity',
						values: opacityData
					},
					{
						attribute: 'r',
						scale: [5,15],
						values: radiusData
					}],

					regions: [{
						scale: ['#ffcccc','#996666'],
						values: regionsData
					}]
				},

				onMarkerLabelShow: function(event, label, index){
					label.html(
						'<p>City: '+markers[index].city+'</p>'+
						'<p>Type: '+markers[index].name+'</p>'+
						'<p>Port: '+markers[index].port+'</p>'+
						'<p>Packets Sent: '+markers[index].count+'</p>'
					);
				},

				onRegionLabelShow: function(event, label, code){
					if (regionsData[code]){
						label.html(
							'<b>'+label.html()+'</b></br>'+
							'<p>Packets Sent: '+regionsData[code]+'</p>'
						);
					}
					else{
						label.html(
							'<b>'+label.html()+'</b></br>'
						);
					}
				;}
			});

			// Implements the slider functionality
			var mapObject = $('#world-map').vectorMap('get', 'mapObject');
			$("#slider").slider({
				value: val,
				min: 0,
				max: markers.length - 1,
				animate: true,
				step: 1,
				slide: function( event, ui ){
					val = ui.value;
					mapObject.removeAllMarkers();
					mapObject.reset();
					mapObject.addMarkers(markers[val]);
					mapObject.series.markers[0].setValues(colorData[val]);
					mapObject.series.markers[1].setValues(opacityData[val]);
					//mapObject.series.markers[2].setValues(radiusData[val]);
					//mapObject.series.regions[0].setValues(regionsData[val]);				
				}
			});


		});
	}

};