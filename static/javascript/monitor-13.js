$.ajax({
    dataType: 'json',
    url: 'http://127.0.0.1:8000/api/twii_5_mins',
    data: { 'key': 'value' },
    success: function (data) {
        const Time = data.Time
        const Index = data.Index

        const min = Math.min.apply(Math, Index)
        const max = Math.max.apply(Math, Index)
        const color = data.Color
        const Rise = document.getElementById("Rise");
        const Fall = document.getElementById("Fall");
        
        Rise.innerHTML = data.Rise;
        Fall.innerHTML = data.Fall;
        
        var ctx = document.getElementById("myDiv").getContext("2d");
        
        var plotdata = {
            labels: Time,
            datasets: [
                {

                    fillColor: color,
                    data: JSON,
                    scaleShowGridLines : false,
                }
            ],
            options: {
                legend: {
                    display: false,
                },
            
        };

        var myLineChart = new Chart(ctx).Line(plotdata);
        

    }

});




