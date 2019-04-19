function createCharts(tones){
    var charts = Array(tones.length);
    var i, id, ctx, color, toneId;
    var white = "#ffffff";
    for(i=0; i<charts.length;i++){
        toneId = tones[i]['tone_id']
        id = "#"+toneId;
        ctx = $(id);

        if(toneId == 'Anger'){
            color = '#f4452'
        }
        else if(toneId == 'Fear'){
            color = '#ff9123'
        }
        else if(toneId == 'Joy'){
            color = '#9fff22'
        }
        else if(toneId == 'Sadness'){
            color = '#2121ff'
        }
        else if(toneId == 'Analytical'){
            color = '#e520ff'
        }
        else if(toneId == 'Confident'){
            color = '#ffe120'
        }
        //id == tentative
        else{
            color = '#20e8ff'
        }

        charts[i] = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: [toneId," "],
                datasets: [{
                label: toneId,
                backgroundColor: [color,white],
                data: [tones[i]['score'],(1-tones[i]['score'])]
                           }]
                   },
            options: {
            title: {
            display: true,
            text: toneId + ' on a scale of 0 to 1'
                   }
                }
             });
    }
}