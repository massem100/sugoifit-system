import BarChart from '@/components/charts/BarChart'
import LineChart from '@/components/charts/LineChart'
import PieChart from '@/components/charts/PieChart'
import {
  barChartData,
  barChartOptions,
  lineChartData,
  lineChartOptions,
  pieChartData, pieChartOptions
} from "@/assets/data/chartData";
export default {
  data() {
    return {
      selectedTitle: '',
      selectedYear: '',
      titleOptions: ['CASHFLOW', 'REVENUE'],
      yearOptions: [2021, 2020, 2019],
      barChartData: barChartData,
      lineChartData: lineChartData,
      pieChartData: pieChartData,
      barChartOptions: barChartOptions,
      pieChartOptions: pieChartOptions,
      lineChartOptions: lineChartOptions,
      trendItems: [
        {value: 90},
        {value: 60},
        {value: 75},
        {value: 85},
        {value: 74},
        {value: 85},
      ]
    }
  },
  components: {
    BarChart,
    LineChart,
    PieChart,

  },
}
