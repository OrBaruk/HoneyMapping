var Map = {

	init: function (markers, count){
		$(function(){
			var val = 0;

			console.log(markers);
			console.log(count);

			mapObject = $('#world-map').vectorMap({
				map: 'world_mill_en',
				scaleColors: ['#C8EEFF', '#0071A4'],	
				normalizeFunction: 'polynomial',
				hoverOpacity: 0.7,
				hoverColor: false,

				/*
				markerStyle: {
					initial: {
						fill: '#F8E23B',
						stroke: '#383f47'
					}
				},
				*/				

				backgroundColor: '#383f47',

				markers: markers,

				series: {
					markers: [{
						attribute: 'fill',
						scale: ['#FEE5D9', '#A50F15'],
						values: count// markers[val].count
						//min: 1,
						//max: 200
					},{
						attribute: 'r',
						scale: [5,20],
						values: count// markers[val].count
						//min: 1,
						//max: 200
					}]
				},

				onMarkerLabelShow: function(event, label, index){
				label.html(
					'<p>City: '+markers[index].city+'</p>'+
					'<p>Type: '+markers[index].name+'</p>'+
					'<p>Port: '+markers[index].port+'</p>'+
					// '<p>IP: '  +markers[index].ip+'</p>'+
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
				max: markers.length - 1,
				step: 1,
				slide: function( event, ui ){
					val = ui.value;
					if ( val == 0) {
						mapObject.removeAllMarkers();
						mapObject.addMarkers( markers);
					} else{
						mapObject.removeAllMarkers();
						mapObject.addMarker( val, markers[val - 1]);
					}					
				}
			});
		});
	}

};