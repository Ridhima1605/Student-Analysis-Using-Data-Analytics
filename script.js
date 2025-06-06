Here’s how you can implement interactive elements (tooltips and hover effects) in your Chart.js visualizations, including the relevant JavaScript code snippets.
// script.js - Student Analysis Visualizations with Interactivity

// Bar Chart - Average Grades by Subject
const barCtx = document.getElementById('barChart').getContext('2d');
const barChart = new Chart(barCtx, {
  type: 'bar',
  data: {
    labels: ['Math', 'Science', 'English', 'History', 'Art'],
    datasets: [{
      label: 'Average Grade (%)',
      data: [78, 85, 82, 75, 90],
      backgroundColor: 'rgba(54, 162, 235, 0.7)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1,
      hoverBackgroundColor: 'rgba(54, 162, 235, 0.9)' // Hover color
    }]
  },
  options: {
    plugins: {
      tooltip: {
        enabled: true,
        callbacks: {
          label: ctx => `${ctx.dataset.label}: ${ctx.parsed.y}%`
        }
      },
      legend: {
        display: true
      }
    },
    hover: {
      mode: 'nearest',
      intersect: true
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 100,
        title: {
          display: true,
          text: 'Grade Percentage'
        }
      },
      x: {
        title: {
          display: true,
          text: 'Subjects'
        }
      }
    }
  }
});

// Pie Chart - Attendance Distribution
const pieCtx = document.getElementById('pieChart').getContext('2d');
const pieChart = new Chart(pieCtx, {
  type: 'pie',
  data: {
    labels: ['Present', 'Absent', 'Late'],
    datasets: [{
      label: 'Attendance',
      data: [80, 15, 5],
      backgroundColor: [
        'rgba(75, 192, 192, 0.7)', // Greenish
        'rgba(255, 99, 132, 0.7)', // Redish
        'rgba(255, 206, 86, 0.7)'  // Yellowish
      ],
      hoverOffset: 30, // Pops out slice on hover
      hoverBackgroundColor: [
        'rgba(75, 192, 192, 0.9)',
        'rgba(255, 99, 132, 0.9)',
        'rgba(255, 206, 86, 0.9)'
      ]
    }]
  },
  options: {
    plugins: {
      tooltip: {
        enabled: true,
        callbacks: {
          label: ctx => `${ctx.label}: ${ctx.parsed}%`
        }
      },
      legend: {
        position: 'bottom',
        labels: {
          padding: 20
        }
      }
    },
    hover: {
      mode: 'nearest',
      intersect: true
    }
  }
});

// Scatter Plot - Hours Studied vs Score
const scatterCtx = document.getElementById('scatterPlot').getContext('2d');
const scatterChart = new Chart(scatterCtx, {
  type: 'scatter',
  data: {
    datasets: [{
      label: 'Student Scores',
      data: [
        { x: 1, y: 50 },
        { x: 2, y: 55 },
        { x: 3, y: 60 },
        { x: 4, y: 70 },
        { x: 5, y: 75 },
        { x: 6, y: 80 },
        { x: 7, y: 85 },
        { x: 8, y: 90 },
        { x: 9, y: 92 },
        { x: 10, y: 95 }
      ],
      backgroundColor: 'rgba(153, 102, 255, 0.7)',
      hoverBackgroundColor: 'rgba(153, 102, 255, 1)',
      pointRadius: 7,
      pointHoverRadius: 10
    }]
  },
  options: {
    plugins: {
      tooltip: {
        enabled: true,
        callbacks: {
          label: ctx => `Hours Studied: ${ctx.parsed.x}, Score: ${ctx.parsed.y}`
        }
      },
      legend: {
        display: true
      }
    },
    hover: {
      mode: 'nearest',
      intersect: true
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Hours Studied'
        },
        beginAtZero: true,
        max: 12
      },
      y: {
        title: {
          display: true,
          text: 'Score (%)'
        },
        beginAtZero: true,
        max: 100
      }
    }
  }
});
