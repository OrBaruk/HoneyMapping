var Map = {
	//Variable to store the information related to mapobject
	obj: [],
	opacityData: [],
	colorData: [],

	init: function (markers, radiusData, regionsData){
		
		$(function(){
			// console.log("markers");
			// console.log(markers);
			// console.log("radius");
			// console.log(radiusData);
			// console.log("regions");
			// console.log(regionsData);

			// Internal value used to set the same opacity for each marker
			// This computation in the future should be done by the server and cached
			for (var i = 0; i < markers.length; i++) {
				Map.opacityData[i] = 0.7;
				Map.colorData[i] = markers[i].name;
			};
			
			// This section is where you can customize most of the looks of the map
			$('#world-map').vectorMap({
				map: 'world_mill',
				// scaleColors: ['#C8EEFF', '#0071A4'],	
				normalizeFunction: 'polynomial',
				hoverOpacity: 0.7,
				hoverColor: false,

				backgroundColor: '#6699cc',

				markers: markers,

				series: {
					markers: [
					{
						attribute: 'fill',

						// Sets up the colors for each attack type, maybe a more elegant solution can be done in the future
						scale: {
							'smbd' 			: '#0000ff',
							'httpd' 		: '#00ff00',
							'mssqld' 		: '#ff8000',
							'epmapper' 		: '#ff0080',
							'ftpd' 			: '#66ffff',
							'SipSession' 	: '#ff0000'
						},
						values: Map.colorData
					},
					{
						attribute: 'fill-opacity',
						values: Map.opacityData
					},
					{
						attribute: 'r',
						scale: [5,15],
						values: radiusData
					}
					],

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
						'<p>LatLng: '+markers[index].latLng+'</p>'+
						'<p>Packets Sent: '+markers[index].count+'</p>'+
						'<p>Collector: '+markers[index].collector+'</p>'
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

			Map.obj = $('#world-map').vectorMap('get', 'mapObject');			
		});
	},

	update: function (markers, radiusData, regionsData){
		//TEM ALGUMA COISA MUITO ERRADA AQUI

		//Map.obj.removeAllMarkers();
		Map.obj.remove();
		Map.init(markers, radiusData, regionsData)
		//Map.obj.addMarkers(markers);
		//Map.obj.series.markers[0].setValues(Map.colorData);
		//Map.obj.series.markers[1].setValues(Map.opacityData);
		//Map.obj.series.markers[2].setValues(radiusData);
		//Map.obj.series.regions[0].setValues(regionsData);
	}
};