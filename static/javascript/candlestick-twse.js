// d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv', function (err, rows) {

//     function unpack(rows, key) {
//         return rows.map(function (row) {
//             return row[key];
//         });
//     }

//     var traceTWSE = {
//         x: unpack(rows, 'Date'),
//         close: unpack(rows, 'AAPL.Close'),
//         high: unpack(rows, 'AAPL.High'),
//         low: unpack(rows, 'AAPL.Low'),
//         open: unpack(rows, 'AAPL.Open'),

//         // cutomise colors
//         increasing: { line: { color: '#d92323' } },
//         decreasing: { line: { color: '#23d932' } },

//         type: 'candlestick',
//         xaxis: 'x',
//         yaxis: 'y'
//     };

//     var dataTWSE = [traceTWSE];

//     var layout = {
//         dragmode: 'zoom',
//         showlegend: false,
//         xaxis: {
//             autorange: true,
//             title: 'Date',
//             rangeslider: {
//                 visible: false
//             },
//             rangeselector: {
//                 x: 0,
//                 y: 1.2,
//                 xanchor: 'left',
//                 font: { size: 8 },
//                 buttons: [{
//                     step: 'month',
//                     stepmode: 'backward',
//                     count: 1,
//                     label: '1 month'
//                 }, {
//                     step: 'month',
//                     stepmode: 'backward',
//                     count: 6,
//                     label: '6 months'
//                 }, {
//                     step: 'all',
//                     label: 'All dates'
//                 }]
//             }
//         },
//         yaxis: {
//             autorange: true,
//         }
//     };

//     Plotly.newPlot('myDiv2', dataTWSE, layout);
// });


d3.csv('http://127.0.0.1:8000/api_twii', function (err, rows) {

    function unpack(rows, key) {
        return rows.map(function (row) {
            return row[key];
        });
    }

    var traceTWSE = {
        x: unpack(rows, 'Date'),
        close: unpack(rows, 'C'),
        high: unpack(rows, 'H'),
        low: unpack(rows, 'L'),
        open: unpack(rows, 'O'),

        // cutomise colors
        increasing: { line: { color: '#d92323' } },
        decreasing: { line: { color: '#23d932' } },

        type: 'candlestick',
        xaxis: 'x',
        yaxis: 'y'
    };

    var dataTWSE = [traceTWSE];

    var layout = {
        dragmode: 'zoom',
        showlegend: false,
        xaxis: {
            autorange: true,
            title: 'Date',
            rangeslider: {
                visible: false
            },
            rangeselector: {
                x: 0,
                y: 1.2,
                xanchor: 'left',
                font: { size: 8 },
                buttons: [
                    {
                        step: 'month',
                        stepmode: 'backward',
                        count: 1,
                        label: '1 month'
                    }, {
                        step: 'month',
                        stepmode: 'backward',
                        count: 3,
                        label: '3 month'
                    }, {
                        step: 'month',
                        stepmode: 'backward',
                        count: 6,
                        label: '6 months'
                    }, {
                        step: 'all',
                        label: 'All dates'
                    }]
            }
        },
        yaxis: {
            autorange: true,
        }
    };

    Plotly.newPlot('myDiv2', dataTWSE, layout);
});
