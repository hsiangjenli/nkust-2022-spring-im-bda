// const layout = {
//     autosize: true,
//     margin: {
//         l: 60,
//         r: 60,
//         b: 40,
//         t: 40,
//         pad: 0
//     },

//     paper_bgcolor: 'rgba(0,0,0,0)',
//     // plot_bgcolor: 'rgba(0,0,0,0)',
//     yaxis: {
//         range: [17500, 18000],
//         fixedrange: true,
//       }
// };

// const config = {
//     // displayModeBar: false,
//     // responsive: true,
// };

// var trace1 = {
//     x: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
//     y: [30, 36, 67,  3, 23, 15, 80, 53, 93, 67, 27, 63, 32, 31, 79, 91, 14, 4,  3, 94],
//     fill: 'tozeroy',
//     type: 'scatter'
// };

// var data = [trace1];

// Plotly.newPlot('myDiv', data, layout, config);


// d3.json('http://127.0.0.1:8000/api/twii_5_mins', function (err, rows) {

//     function unpack(rows, key) {
//         return rows.map(function (row) {
//             return row[key];
//         });
//     }

//     var traceTWSE5 = {
//         x: unpack(rows, 'Time'),
//         y: unpack(rows, 'TAIEX'),
//         type: 'scatter',
//         mode: 'lines',
//         line: {color: 'grey'}
//     };

//     var dataTWSE5 = [traceTWSE5];



//     Plotly.newPlot('myDiv', dataTWSE5, layout, config);
// });

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

        const layout = {
            autosize: true,
            margin: {
                l: 30,
                r: 30,
                b: 30,
                t: 30,
                pad: -20
            },

            // paper_bgcolor: 'rgba(0,0,0,0)',
            yaxis: {
                range: [min - 50, max + 50],
                fixedrange: true,
            }
        };
        const config = {
            // displayModeBar: false,
            // responsive: true,
        };
        var traceTWSE5 = {
            x: Time,
            y: Index,
            type: 'scatter',
            mode: 'lines',
            fill: 'tozeroy',
            line: { color: color, shape: 'spline' }
        };

        var dataTWSE5 = [traceTWSE5];
        Plotly.newPlot('myDiv', dataTWSE5, layout, config);
        const Rise = document.getElementById("Rise");
        const Fall = document.getElementById("Fall");
        Rise.innerHTML = data.Rise;
        Fall.innerHTML = data.Fall;
    }

});




