$.ajax({
    dataType: 'json',
    url: 'http://127.0.0.1:8000/api/twii_5_mins',
    data: { 'key': 'value' },
    success: function (data) {
        const Time = data.Time
        const Index = data.Index
        // const Json = data.Json

        const min = Math.min.apply(Math, Index)
        const max = Math.max.apply(Math, Index)
        const color = data.Color
        const Rise = document.getElementById("Rise");
        const Fall = document.getElementById("Fall");
        console.log(Json)
        Rise.innerHTML = data.Rise;
        Fall.innerHTML = data.Fall;
        
        // var ctx = document.getElementById("myDiv").getContext("2d");
        let ctx_key_time = document.getElementById("myDiv").getContext('2d');

        var Json = [{"x": "2019-03-07", "y": 2},
        {"x": "2019-03-08", "y": 2},
        {"x": "2019-03-09", "y": 13}]

        function showtimechart(Json) {
            const myoptions = {
                type: 'line',
                data: {
                    datasets:
                        [{
                            borderColor: color,
                            data: Json,
                        }]
                },
                options: {
                    legend: {
                        display: false,
                    },
                    scales: {
                        // y: {
                        //     min: 1000,
                        //     max: max
                        //   },
                        yAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                            },
                            
                        }],
                        xAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true,
                            },
                            
                        }]
                    }
                }
            };
    
    
            // console.log(chart);
            // if (chart)
            //    chart.destroy();
    
    
            //if (window.chart) {
            //    chart.destroy();
            //}
    
            chart = new Chart(ctx_key_time, myoptions); //the chart variable is define outside of this function
        }
        // var myLineChart = new Chart(ctx).Line(plotdata);
        showtimechart(Json);
        

    }

});




