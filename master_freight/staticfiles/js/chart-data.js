var randomScalingFactor = function(){ return Math.round(Math.random()*1000)};
	var lineChartData = {
			labels : ["Jan","Feb","Mar","Apr","May","Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
			datasets : [
				{
					label: "AIF Requests",
					fillColor : "rgba(220,220,220,0.2)",
					strokeColor : "rgba(220,220,220,1)",
					pointColor : "rgba(220,220,220,1)",
					pointStrokeColor : "#fff",
					pointHighlightFill : "#fff",
					pointHighlightStroke : "rgba(220,220,220,1)",
					data : aif_requests.slice(1, -1).split(',')
				},
				{
					label: "LCL Requests",
					fillColor : "rgba(48, 164, 255, 0.2)",
					strokeColor : "rgba(48, 164, 255, 1)",
					pointColor : "rgba(48, 164, 255, 1)",
					pointStrokeColor : "#fff",
					pointHighlightFill : "#fff",
					pointHighlightStroke : "rgba(48, 164, 255, 1)",
					data : lcl_requests.slice(1, -1).split(',')
				},
				{
					label: "FCL Requests",
					fillColor : "rgba(225, 86, 38, 0.2)",
					strokeColor : "rgba(225, 86, 38, 1)",
					pointColor : "rgba(225, 86, 38, 1)",
					pointStrokeColor : "#fff",
					pointHighlightFill : "#fff",
					pointHighlightStroke : "rgba(225, 86, 38, 1)",
					data : fcl_requests.slice(1, -1).split(',')
				}
			]

		}

	var barChartData = {
			labels : ["Jan","Feb","Mar","Apr","May","Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
			datasets : [
				{
					label: "Accepted",
					fillColor : "rgba(48, 164, 255, 0.2)",
					strokeColor : "rgba(48, 164, 255, 0.8)",
					highlightFill : "rgba(48, 164, 255, 0.75)",
					highlightStroke : "rgba(48, 164, 255, 1)",
					data : offers_acc.slice(1, -1).split(',')
				},
				{
					label: "Rejected",
					fillColor : "rgba(220,220,220,0.5)",
					strokeColor : "rgba(220,220,220,0.8)",
					highlightFill: "rgba(220,220,220,0.75)",
					highlightStroke: "rgba(220,220,220,1)",
					data : offers_rej.slice(1, -1).split(',')
				},
				{
					label: "Done",
					fillColor : "rgba(225, 86, 38, 0.2)",
					strokeColor : "rgba(225, 86, 38, 0.8)",
					highlightFill : "rgba(225, 86, 38, 0.75)",
					highlightStroke : "rgba(225, 86, 38, 1)",
					data : offers_done.slice(1, -1).split(',')
				}
			]

		}
	var pieData = []
	trucker_numbers = trucker_numbers.replace(/ /g,'').slice(1, -1).split(',')
	trucker_names = trucker_names.slice(1, -1).split(',')
	for (var i = 0; i < trucker_numbers.length; i++) {
		pieData.push({
			value: trucker_numbers[i],
			label: trucker_names[i].trim().slice(6,-5),
			color: '#'+(Math.random()*0xFFFFFF<<0).toString(16)
		})
	}

	var doughnutData = []
	shipping_line_numbers = shipping_line_numbers.replace(/ /g,'').slice(1, -1).split(',')
	shipping_line_names = shipping_line_names.slice(1, -1).split(',')

	for (var i = 0; i < shipping_line_numbers.length; i++) {
		// if (shipping_line_numbers[i] > 0) {
			console.log(shipping_line_numbers[i], shipping_line_names[i].trim().slice(6,-5));
			doughnutData.push({
				value: Math.floor(shipping_line_numbers[i]),
					// value: Math.floor(shipping_line_numbers[i]/shipping_line_numbers.length*100),
				label: shipping_line_names[i].trim().slice(6,-5),
				color: '#'+(Math.random()*0xFFFFFF<<0).toString(16)
			})
		// }
	}

	// var doughnutData = [
	// 				{
	// 					value: 2,
	// 					color:"#30a5ff",
	// 					highlight: "#62b9fb",
	// 					label: "Exercitationem"
	// 				},
	// 				{
	// 					value: 1,
	// 					color: "#ffb53e",
	// 					highlight: "#fac878",
	// 					label: "Animi error ab minima voluptatem et rerum ut voluptates recusandae Voluptatum elit sint voluptas"
	// 				},
	// 				{
	// 					value: 1,
	// 					color: "#1ebfae",
	// 					highlight: "#3cdfce",
	// 					label: "Autem excepturi a et est non mollitia deserunt est magna qui cillum ex nostrud aut sapiente ullamco aute sunt ex"
	// 				},
	// 				{
	// 					value: 5,
	// 					color: "#f9243f",
	// 					highlight: "#f6495f",
	// 					label: "Evelyn Mccoy"
	// 				}
	//
	// 			];

window.onload = function(){
	var chart1 = document.getElementById("line-chart").getContext("2d");
	window.myLine = new Chart(chart1).Line(lineChartData, {
		responsive: true
	});
	document.getElementById('line-legend').innerHTML = window.myLine.generateLegend();
	var chart2 = document.getElementById("bar-chart").getContext("2d");
	window.myBar = new Chart(chart2).Bar(barChartData, {
		responsive : true
	});
	document.getElementById('bar-legend').innerHTML = window.myBar.generateLegend();

	var chart3 = document.getElementById("doughnut-chart").getContext("2d");
	window.myDoughnut = new Chart(chart3).Doughnut(doughnutData, {responsive : true
	});
	var chart4 = document.getElementById("pie-chart").getContext("2d");
	window.myPie = new Chart(chart4).Pie(pieData, {responsive : true
	});

};
