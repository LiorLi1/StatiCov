// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example

$(document).ready(() => {
  var ctx2 = document.getElementById("myPieChart");
  var myPieChart = new Chart(ctx2, {
    type: 'doughnut',
    data: {
      labels: ["החלימו", "חולים בקורונה", "בדיקות שבוצעו היום"],
      datasets: [{
        data: [340217, 24356, 9783],
        backgroundColor: ['#66BB6A', '#FF0000', '#36b9cc'],
        hoverBackgroundColor: ['#61b865', '#E74C3C', '#2c9faf'],
        hoverBorderColor: "rgba(234, 236, 244, 1)",
      }],
    },
    options: {
      maintainAspectRatio: false,
      tooltips: {
        backgroundColor: "rgb(255,255,255)",
        bodyFontColor: "#858796",
        borderColor: '#dddfeb',
        borderWidth: 1,
        xPadding: 15,
        yPadding: 15,
        displayColors: false,
        caretPadding: 10,
      },
      legend: {
        display: false
      },
      cutoutPercentage: 80,
    },
  });
  
})
