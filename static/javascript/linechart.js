
var colors = ["#C0AA7A", "#404040", "#D9D9D9"]
var Name = ['Yang', 'Huang', 'Powell']

let chart_H = document.getElementById(`Chart__TimeLine_Huang`).getContext('2d');
var neg_H = chart_H.createLinearGradient(0, 0, 0, 250);
neg_H.addColorStop(0, 'rgba(97, 97, 97, 0.4)');
neg_H.addColorStop(0.1, 'rgba(97, 97, 97,0.2)');
neg_H.addColorStop(1, 'rgba(97, 97, 97,0)');

var pos_H = chart_H.createLinearGradient(0, 0, 0, 250);
pos_H.addColorStop(0, 'rgba(192, 170, 122, 0.4)');
pos_H.addColorStop(0.3, 'rgba(192, 170, 122,0.2)');
pos_H.addColorStop(1, 'rgba(192, 170, 122,0)');

call_ajax('楊金龍 央行', 4, '全部', 'or', chart_H, pos_H, neg_H);


function call_ajax(uk, w, cat, con, linechartElem, gradient_pos, gradient_neg) {

    const userkey = uk;
    const weeks = w;
    const cate = cat;
    const cond = con;

    if (userkey.length < 2) {
        alert("輸入關鍵字不可空白或小於兩個中文字!");
        return 0;
    }

    $.ajax({
        type: "POST",
        url: "api/get_userkey_sentiment",
        data: {
            userkey: userkey,
            cate: cate,
            weeks: weeks,
            cond: cond,
        },
        success: function (received) {

            const data_pos = received["data_pos"];
            const data_neg = received["data_neg"];


            if (window.linechart) linechart.destroy();

            linechart = drawLineChart(linechartElem, data_pos, data_neg);
        },
    });
}
function drawLineChart(linechartElem, data_pos, data_neg, gradient_pos, gradient_neg) {
    console.log(linechartElem);
    let dataPos = {
        label: "正面",
        data: data_pos,
        borderColor: "rgba(192, 170, 122, 1)",
        backgroundColor: gradient_pos,
        borderWidth: 3,
        fill: true,

    };

    let dataNeg = {
        label: "負面",
        data: data_neg,
        borderColor: "rgba(97, 97, 97, 0.7)",
        backgroundColor: gradient_neg,
        borderWidth: 3,
        fill: true,
    };

    let options_detail = {
        responsive: true,

        elements: {
            point: {
                radius: 0,
            }
        },
        legend: {
            display: false,
        },
        scales: {
            y: {
                grid: {
                    display: false
                }
            },
            xAxes: [{
                type: "time",
                time: {
                    unit: "day", displayFormats: { day: "MM/DD", },
                },
                gridLines: {
                    display: false,
                }
            },],
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                    },
                    display: true,
                    scaleLabel: {
                        display: false,
                        labelString: "篇數",
                    },
                    gridLines: {
                        display: false,
                        zeroLineColor: '#fff'
                    }
                },
            ],
        },
    };

    let chart_spec = {
        type: "line",
        data: {
            datasets: [dataPos, dataNeg], //有兩條線，兩組資料使用陣列存放即可
        },
        options: options_detail,
    };

    return new Chart(linechartElem, chart_spec);
}
</script >