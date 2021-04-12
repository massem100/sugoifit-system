export const barChartData = {
  labels: [
    '2019-06',
    '2019-07',
    '2019-08',
    '2019-09',
    '2019-10',
    '2019-11',
    '2019-12',
    '2020-01',
    '2020-02',
    '2020-03',
    '2020-04',
    '2020-05'
  ],
  datasets: [
    {
      label: 'Visits',
      data: [10, 15, 20, 30, 40, 50, 60, 70, 34, 45, 11, 78, 45],
      backgroundColor: '#003f5c'
    },
    {
      label: 'Pages Views',
      data: [30, 24, 57, 23, 68, 72, 25, 64, 133, 143, 165, 33, 56],
      backgroundColor: '#2f4b7c'
    },
    {
      label: 'Users',
      data: [45, 65, 30, 53, 34, 35, 26, 37, 34, 45, 67, 87, 98],
      backgroundColor: '#665191'
    }
  ]
}
export const lineChartData = {
  labels: [
    '2019-06',
    '2019-07',
    '2019-08',
    '2019-09',
    '2019-10',
    '2019-11',
    '2019-12',
    '2020-01',
    '2020-02',
    '2020-03',
    '2020-04',
    '2020-05'
  ],
  datasets: [
    {
      label: 'Visits',
      data: [10, 15, 20, 30, 40, 50, 60, 70, 34, 45, 11, 78, 45],
      borderColor: '#2f4b7c',
      fill: false
    },
    {
      label: 'Pages Views',
      data: [30, 24, 57, 23, 68, 72, 25, 64, 133, 143, 165, 33, 56],
      borderColor: '#636E7C',
      fill: false
    }
  ]
}
export const pieChartData = {
  labels: [
    'Maintenance',
    'Labour Cost',
    'Rent',
    'Other',
  ],
  datasets: [
    {
      label: 'Visits',
      data: [32, 25, 15, 3],
      backgroundColor: ['#2f4b7c', '#7c327a', '#7c4f58', '#71707c'],
    }
  ]
}
export const barChartOptions = {
  responsive: true,
  legend: {
    display: false
  },
  title: {
    display: true,
    text: 'Google analytics data',
    fontSize: 24,
    fontColor: '#6b7280'
  },
  tooltips: {
    backgroundColor: '#17BF62'
  },
  scales: {
    xAxes: [
      {
        gridLines: {
          display: false
        }
      }
    ],
    yAxes: [
      {
        ticks: {
          beginAtZero: true
        },
        gridLines: {
          display: false
        }
      }
    ]
  }
}
export const lineChartOptions = {
  responsive: true,
  legend: {
    display: false
  },
  title: {
    display: true,
    fontSize: 24,
    fontColor: '#6b7280'
  },
  tooltips: {
    backgroundColor: '#17BF62'
  },
  scales: {
    xAxes: [
      {
        gridLines: {
          display: false
        }
      }
    ],
    yAxes: [
      {
        ticks: {
          beginAtZero: true
        },
        gridLines: {
          display: false
        }
      }
    ]
  }
}
export const pieChartOptions = {
  responsive: true,
  legend: {
    display: true,
    position: 'right',
    labels: {
      fontSize: 20,
    },
  },
  title: {
    display: true,
    text: 'Expenses',
    fontSize: 24,
    fontColor: '#6b7280'
  },
  tooltips: {
    backgroundColor: '#17BF62'
  },
  scales: {
    xAxes: [
      {
        gridLines: {
          display: false
        },
      }
    ],
    yAxes: [
      {
        ticks: {
          beginAtZero: true
        },
        gridLines: {
          display: false
        }
      }
    ]
  }
}
