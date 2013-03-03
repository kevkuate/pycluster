//contaminationData = {
// "EcoliM": [
//  99.66,
//  0.0,
//  0.12,
//  0.08,
//  0.14
// ],
// "Hsap": [
//  99.94,
//  0.02,
//  0.0,
//  0.04,
//  0.0
// ],
// "IllCont": [
//  100.0,
//  0.0,
//  0.0,
//  0.0,
//  0.0
// ],
// "Insects": [
//  97.51,
//  0.0,
//  0.0,
//  0.42,
//  2.06
// ],
// "Mmus": [
//  99.98,
//  0.0,
//  0.0,
//  0.02,
//  0.0
// ],
// "PhX174": [
//  100.0,
//  0.0,
//  0.0,
//  0.0,
//  0.0
// ],
// "Sce": [
//  100.0,
//  0.0,
//  0.0,
//  0.0,
//  0.0
// ],
// "Slyc": [
//  18.02,
//  16.24,
//  33.82,
//  8.2,
//  23.72
// ],
// "UniVec": [
//  62.43,
//  1.24,
//  5.55,
//  5.29,
//  25.48
// ],
// "Viruses": [
//  99.48,
//  0.0,
//  0.0,
//  0.18,
//  0.34
// ],
// "Viruses2": [
//  99.96,
//  0.0,
//  0.0,
//  0.02,
//  0.02
// ]
//}


//"Per base GC content": {
// "data": [
//  "#Base\t%GC",
//  "1\t40.209569984588065",
//  "2\t39.756647339140365",
//  "3\t31.249341790815045",
//  "4\t31.88163648036422",
//  "5\t32.2819751546254",
//  "6\t32.377434302193706",
//  "7\t41.120478926465914",
//  "8\t32.6178927649233",
//  "9\t32.50502252033311",
//  "10-14\t35.859647360509896",
//  "15-19\t35.114788587204615",
//  "20-24\t35.325849650726376",
//  "25-29\t35.70465710100971",
//  "30-34\t33.965669623798114",
//  "35-39\t34.457597563173785",
//  "40-44\t35.437577388264735",
//  "45-49\t34.95701772188628",
//  "50-59\t35.04570102672547",
//  "60-69\t34.97659101149966",
//  "70-79\t35.01887038994846",
//  "80-89\t34.999117779553465",
//  "90-99\t35.01365636394439",
//  "100-149\t35.0432905608735",
//  "150-199\t35.20572280412317",
//  "200-249\t35.532121021527296",
//  "250-299\t35.950811486682674",
//  "300-349\t36.37576968912036",
//  "350-399\t36.86563896540507",
//  "400-449\t37.39376926729655",
//  "450-499\t37.970197512858206",
//  "500-599\t37.22410480925408",
//  "600-699\t41.12712975098296",
//  "700-799\t44.667274384685506",
//  "800-899\t44.0251572327044",
//  "900-999\t27.884615384615387",
//  "1000-1038\t38.46153846153847"
// ],

//categoriesX = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49'];
//data        = [{
//                name: 'Tokyo',
//                data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
//            }, {
//                name: 'New York',
//                data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
//            }, {
//                name: 'Berlin',
//                data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
//            }, {
//                name: 'London',
//                data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
//            }];
//
//title    = "Relative Enrichment Over Read Length";
//subTitle = "FastQC Report";
//titleY   = "%";
//unityY   = "%";
//titleX   = "Position in Read (bp)"
//unityX   = "bp";


function graph_lines(dataHash) {
    var data        = dataHash['data'       ];
    var container   = dataHash['container'  ];
    var categoriesX = dataHash['categoriesX'];

    var title       = dataHash['title'      ];
    var subTitle    = dataHash['subTitle'   ];
    var titleY      = dataHash['titleY'     ];
    var unityY      = dataHash['unityY'     ];
    var titleX      = dataHash['titleX'     ];
    var unityX      = dataHash['unityX'     ];

    var minX        = dataHash['minX'       ];
    var maxX        = dataHash['maxX'       ];
    var minY        = dataHash['minY'       ];
    var maxY        = dataHash['maxY'       ];


    //console.log("graph lines :: data " + data +
    //            ' container ' + container +
    //            ' title ' + title +
    //            ' sub title ' + subTitle +
    //            ' titleY ' + titleY +
    //            ' unityY ' + unityY +
    //            ' titleX ' + titleX +
    //            ' unityX ' + unityX +
    //            ' categoriesX ' + categoriesX
    //            );



    var chartOpts = {
        chart: {
            renderTo    : container,
            type        : 'line',
            marginRight : 130,
            marginBottom: 25,
        },
        title: {
            text: title,
            x   : -20 //center
        },
        subtitle: {
            text: subTitle,
            x   : -20
        },
        xAxis: {
            categories  : categoriesX,
            title       : {
                text    : titleX
            }
        },
        yAxis: {
            title: {
                text: titleY
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            formatter: function() {
                    return '<b>'+ this.series.name +'</b><br/>'+
                    this.x +unityX+': '+ this.y +unityY;
            }
        },
        legend: {
            layout       : 'vertical',
            align        : 'right',
            verticalAlign: 'top',
            x            : -10,
            y            : 100,
            borderWidth  : 0
        },
        series      : data,
        hideDuration: 0,
        showDuration: 0,
        animation   : false,
        plotOptions : {
            series  : {
                animation: false
            }
        },
    };

    if ( categoriesX.length > 15 ) {
        var intervalNew = Math.ceil( categoriesX.length / 15 );
        chartOpts['xAxis']['tickInterval'] = intervalNew;
        console.log("tick interval " + intervalNew);
    }

    if ( minX !== null ) {
        chartOpts['xAxis']['min'] = minX;
        console.log("+minX " + minX);
    } else {
        console.log("!minX " + minX);
    }

    if ( maxX !== null ) {
        chartOpts['xAxis']['max'] = maxX;
        console.log("+maxX " + maxX);
    } else {
        console.log("!maxX " + maxX);
    }

    if ( minY !== null ) {
        chartOpts['yAxis']['min'] = minY;
        console.log("+minY " + minY);
    } else {
        console.log("!minY " + minY);
    }

    if ( maxY !== null ) {
        chartOpts['yAxis']['max'] = maxY;
        console.log("+maxY " + maxY);
    } else {
        console.log("!maxY " + maxY);
    }

    var chart = new Highcharts.Chart(chartOpts);
};
//http://www.highcharts.com/demo/column-stacked-percent

function graph_stacked(dataHash) {
    var data        = dataHash['data'       ];
    var container   = dataHash['container'  ];
    var categoriesX = dataHash['categoriesX'];

    var title       = dataHash['title'      ];
    var titleY      = dataHash['titleY'     ];
    var unityY      = dataHash['unityY'     ];
    var titleX      = dataHash['titleX'     ];
    var unityX      = dataHash['unityX'     ];

    var minX        = dataHash['minX'       ];
    var maxX        = dataHash['maxX'       ];
    var minY        = dataHash['minY'       ];
    var maxY        = dataHash['maxY'       ];


    //var categoriesX = ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas'];
    //var data        = [{
    //        name: 'John',
    //        data: [5, 3, 4, 7, 2]
    //    }, {
    //        name: 'Jane',
    //        data: [2, 2, 3, 2, 1]
    //    }, {
    //        name: 'Joe',
    //        data: [3, 4, 4, 2, 5]
    //    }];


    var chartOpts = {
        chart: {
            renderTo: container,
            type: 'column'
        },
        title: {
            text: title
        },
        xAxis: {
            categories: categoriesX
        },
        yAxis: {
            min: 0,
            title: {
                text: titleY
            }
        },
        tooltip: {
            formatter: function() {
                return ''+
                    this.series.name +': '+ this.y +' ('+ Math.round(this.percentage) +'%)';
            }
        },
        series      : data,
        hideDuration: 0,
        showDuration: 0,
        animation   : false,
        plotOptions : {
            column: {
                stacking: 'percent'
            },
            series  : {
                animation: false
            }
        }
    };



    //if ( categoriesX.length > 15 ) {
    //    var intervalNew = Math.ceil( categoriesX.length / 15 );
    //    chartOpts['xAxis']['tickInterval'] = intervalNew;
    //    console.log("tick interval " + intervalNew);
    //}

    if ( minX !== null ) {
        chartOpts['xAxis']['min'] = minX;
        console.log("+minX " + minX);
    } else {
        console.log("!minX " + minX);
    }

    if ( maxX !== null ) {
        chartOpts['xAxis']['max'] = maxX;
        console.log("+maxX " + maxX);
    } else {
        console.log("!maxX " + maxX);
    }

    if ( minY !== null ) {
        chartOpts['yAxis']['min'] = minY;
        console.log("+minY " + minY);
    } else {
        console.log("!minY " + minY);
    }

    if ( maxY !== null ) {
        chartOpts['yAxis']['max'] = maxY;
        console.log("+maxY " + maxY);
    } else {
        console.log("!maxY " + maxY);
    }

    var chart = new Highcharts.Chart(chartOpts);
};
//http://www.highcharts.com/stock/demo/candlestick

function graph_candle(dataHash) {
    var data1       = dataHash['data1'      ];
    var data2       = dataHash['data2'      ];
    var data3       = dataHash['data3'      ];
    var data4       = dataHash['data4'      ];
    var container   = dataHash['container'  ];

    var title       = dataHash['title'      ];
    var subTitle    = dataHash['subTitle'   ];
    var titleY      = dataHash['titleY'     ];
    //var unityY      = dataHash['unityY'     ];
    var titleX      = dataHash['titleX'     ];
    //var unityX      = dataHash['unityX'     ];
    //var categoriesX = dataHash['categoriesX'];

    var minX        = dataHash['minX'       ];
    var maxX        = dataHash['maxX'       ];
    var minY        = dataHash['minY'       ];
    var maxY        = dataHash['maxY'       ];




    var chartOpts = {
        chart: {
            renderTo: container,
            type: 'arearange'
        },

        title: {
            text: title
        },

        xAxis: {
            type: 'linear',
            title: {
                text: titleX
            }
        },

        yAxis: {
            title: {
                text: titleY
            }
        },

        //tooltip: {
        //    crosshairs: true,
        //    shared: true,
        //    valueSuffix: '°C'
        //},

        legend: {
            enabled: true
        },

        series: [{
                name: subTitle + ' quartile',
                data: data1,
                //yAxis: 1
            },
            {
                name: subTitle + ' percentile',
                data: data2,
                //yAxis: 1
            },
            {
                name: subTitle + ' mean',
                data: data3,
                type: 'line',
                //yAxis: 1
            },
            {
                name: subTitle + ' median',
                data: data4,
                type: 'line',
                //yAxis: 1
            }
        ],
        hideDuration: 0,
        showDuration: 0,
        animation   : false,
        plotOptions : {
            series  : {
                animation: false
            }
        }
    };



    //if ( categoriesX.length > 15 ) {
    //    var intervalNew = Math.ceil( categoriesX.length / 15 );
    //    chartOpts['xAxis']['tickInterval'] = intervalNew;
    //    console.log("tick interval " + intervalNew);
    //}

    if ( minX !== null ) {
        chartOpts['xAxis']['min'] = minX;
        console.log("+minX " + minX);
    } else {
        console.log("!minX " + minX);
    }

    if ( maxX !== null ) {
        chartOpts['xAxis']['max'] = maxX;
        console.log("+maxX " + maxX);
    } else {
        console.log("!maxX " + maxX);
    }

    if ( minY !== null ) {
        chartOpts['yAxis']['min'] = minY;
        console.log("+minY " + minY);
    } else {
        console.log("!minY " + minY);
    }

    if ( maxY !== null ) {
        chartOpts['yAxis']['max'] = maxY;
        console.log("+maxY " + maxY);
    } else {
        console.log("!maxY " + maxY);
    }

    var chart = new Highcharts.Chart(chartOpts);
};
