$.ajax({
    dataType: 'json',
    url: 'http://127.0.0.1:8000/api/twii_5_mins',
    data: { 'key': 'value' },
    success: function (data) {
        const Time = data.Time
        const Index = data.Index
        const Json = data.Json

        const min = Math.min.apply(Math, Index)
        const max = Math.max.apply(Math, Index)
        const color = data.Color
        const fcolor = data.FColor
        const Rise = document.getElementById("Rise");
        const Fall = document.getElementById("Fall");

        Rise.innerHTML = data.Rise;
        Fall.innerHTML = data.Fall;

        // let ctx_key_time = document.getElementById("myDiv").getContext('2d');

        // var Json = [{"x": "2019-03-07", "y": 1},
        // {"x": "2019-03-08", "y": 2},
        // {"x": "2019-03-09", "y": 3}]

        var ctx = document.getElementById("myDiv").getContext('2d');
        var gradient = ctx.createLinearGradient(0, 0, 0, 150);
        gradient.addColorStop(0, 'rgba(192, 170, 122, 0.4)');
        gradient.addColorStop(0.3, 'rgba(250,174,50,0.1)');
        gradient.addColorStop(1, 'rgba(250,174,50,0)');

        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: Time,
                datasets: [{
                    // label: 'Series 1', // Name the series
                    data: Json, // Specify the data values array
                    borderColor: color, // Add custom color border (Line)
                    backgroundColor: gradient, // Add custom color background (Points and Fill)
                    borderWidth: 3,// Specify bar border widt
                }]
            },
            options: {
                responsive: true, // Instruct chart js to respond nicely.
                maintainAspectRatio: false, // Add to prevent default behaviour of full-width/height 
                legend: {
                    display: false,
                },
                elements: {
                    point: {
                        radius: 0,
                    }
                },
                scales: {
                    xAxes: [{
                        ticks: {
                            fontSize: 0
                        }
                    }]
                }
            }
        });
    }

});




