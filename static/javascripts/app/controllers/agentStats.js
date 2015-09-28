angular.module('Jaza')
  .controller('AgentStatsController', function($scope, $routeParams, AgentService, snackbar) {

    $scope.getStats = function () {
      var agentId = $routeParams.agentId;
      var startDate = $scope.startDate;
      var endDate = $scope.endDate;
      var category = $scope.category;

      AgentService.getAgentStats(agentId, startDate, endDate, category)
        .then(function (result) {
          console.log(result.data);

          if (Object.keys(result.data).length === 0) {
            $scope.Stats = {'datum': 0};
          } else {
            $scope.Stats = {'data': result.data};
          }
          // TODO: check length on object
        })
        .catch(function (response) {
          snackbar.create("Could not get Agent Sales Metrics");
          $scope.title = '';
          $scope.data = '';
        });
    };

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
        data: []
      }],
      xAxis: {
        categories: []
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
