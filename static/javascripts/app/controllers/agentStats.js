angular.module('Jaza')
  .controller('AgentStatsController', function($scope, $routeParams, Stats) {

    (function() {
      var agentId = $routeParams.param1;

      Stats.getAgentStats(agentId)
        .then(function (result) {
          console.log(result);
          $scope.Stats = result.data;
        })
        .catch(function (response) {
          console.log(response);
          $scope.title = '';
          $scope.data = '';
        });
    })();

    $scope.addPoints = function () {
      var seriesArray = $scope.chartConfig.series;
      var rndIdx = Math.floor(Math.random() * seriesArray.length);
      seriesArray[rndIdx].data = seriesArray[rndIdx].data.concat([1, 10, 20]);
    };

    $scope.chartConfig = {
      options: {
        chart: {
          type: 'line'
        }
      },
      title: {
        text: 'Agent Sales',
        x: -20
      },
      subtitle: {
        text: 'Agent sales per Product',
        x: -20
      },
      series: [{
        data: [10, 15, 12, 8, 7]
      }],
      xAxis: {
        categories: ['Fast Airtime', 'DMG', 'Sonic Airtime', 'Mikes Fast Point', 'Jaza Airtime']
      },
      yAxis: {
        title: {
          text: 'Units Sold'
        },
        plotLines: [{
          value: 0,
          width: 1,
          color: '#808080'
        }]
      },
      legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle',
        borderWidth: 0
      },
      size: {
        width: 600,
        height: 450
      },

      loading: false
    }

  });
