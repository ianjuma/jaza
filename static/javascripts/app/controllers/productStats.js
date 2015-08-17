angular.module('Jaza')
  .controller('StatsController', function($scope, $routeParams, Stats) {

    $scope.getAgentStats = function() {
      var param1 = $routeParams.param1;
      var param2 = $routeParams.param2;
      Stats.getAgentStats({
        title: $scope.title,
        data: $scope.data
      })
        .then(function (result) {
          console.log(result);
          $scope.Stats = result.data;
        })
        .catch(function (response) {
          console.log(response);
          $scope.title = '';
          $scope.data = '';
        });
    };

    $scope.getProductStats = function() {
      var param1 = $routeParams.param1;
      var param2 = $routeParams.param2;
      Stats.getProductStats({
        title: $scope.title,
        data: $scope.data
      })
        .then(function (result) {
          console.log(result);
          $scope.Stats = result.data;
        })
        .catch(function (response) {
          console.log(response);
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
          type: 'bar'
        }
      },
      series: [{
        data: [10, 15, 12, 8, 7]
      }],
      xAxis: {
        categories: ['Fast Airtime', 'DMG', 'Sonic Airtime', 'Mikes Fast Point', 'Jaza Airtime']
      },
      yAxis: {
        title: {
          text: 'Airtime Sold'
        }
      },
      size: {
        width: 600,
        height: 450
      },
      title: {
        text: 'Product Sales'
      },

      loading: false
    }

  });
