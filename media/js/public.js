var map;

function initialize() {
	var myLatlng = new google.maps.LatLng(-34.905833, -56.191389);
	var myOptions = {
		zoom : 11,
		center : myLatlng,
		mapTypeId : google.maps.MapTypeId.ROADMAP
	}
	map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
	var parameters = {};
	parameters["cantidad"] = 40
	$.get('/update.ajax', parameters, function(data) {
		clear();
		var locations = eval(data)
		for( i = 0; i < locations.length; i++) {
			marker = new google.maps.Marker({
				position : new google.maps.LatLng(locations[i][1], locations[i][2]),
				map : map,
				icon : image,
				title : locations[i][0]
			});
		}
	})
}

function clear() {
	var myLatlng = new google.maps.LatLng(-34.905833, -56.191389);
	var myOptions = {
		zoom : 11,
		center : myLatlng,
		mapTypeId : google.maps.MapTypeId.ROADMAP
	}
	map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
}

function actualizar() {
	var parameters = {};
	if(parseInt($('#minaccidentnum').val()) > 0) {
		parameters["cantidad"] = $('#minaccidentnum').val();
	} else {
		parameters["cantidad"] = 40;
		$('#minaccidentnum').val(40);
	}
	parameters["yearfilter"] = $('#yearfilter').val();
	if(parseInt($('#tipofilter').val()) > 0) {
		parameters["tipofilter"] = $('#tipofilter').val();
	} else {
		parameters["tipofilter"] = 'todo'
		$('#tipofilter').val('todo')
	}
	$.get('/update.ajax', parameters, function(data) {
		clear();
		var locations = eval(data)
		for( i = 0; i < locations.length; i++) {
			marker = new google.maps.Marker({
				position : new google.maps.LatLng(locations[i][1], locations[i][2]),
				map : map,
				icon : image,
				title : locations[i][0]
			});
		}
	})
}

function showAboutUs() {
	$("#about-us").dialog({
		height : 600,
		width : 500,
		modal : true
	});
}

function ranking() {
	$("#ranking-modal").dialog({
		height : 600,
		width : 659,
		modal : true
	});
}

$(document).ready(function($) {
	$("#minaccidentnum").spinner({
		min : 1,
		max : 500,
		increment : 2
	});
});

function getRanking() {
	var output = "<table>"
	$.get('/ranking.ajax', function(data) {
		clear();
		var locations = eval(data)
		for( i = 0; i < locations.length; i++) {
			output += "<tr>"
			output += "<td>"
			output += "</td>"
			output += "<td>"
			output += "</td>"
			output += "</tr>"
		}
		output += "</table>"
	})
}