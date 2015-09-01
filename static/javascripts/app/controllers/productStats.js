angular.module('Jaza')
  .controller('ProductStatsController', function($scope, $routeParams, ProductService, snackbar) {

    $scope.getStats = function () {
      var productId = $routeParams.productId;
      var startDate = $scope.startDate;
      var endDate = $scope.endDate;
      var category = $scope.category;

      console.log(startDate, endDate, category);

      ProductService.getProductStats(productId, startDate, endDate, category)
        .then(function (result) {
          console.log(result.data);

          if (Object.keys(result.data).length === 0) {
            $scope.Stats = {'datum': 0};
          } else {
            $scope.Stats = {'data': result.data};
          }
        })
        .catch(function (response) {
          snackbar.create("Couldn't get Product Sales Metrics");
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
        data: [10, 15, 12, 8]
      }],
      xAxis: {
        categories: ['Sent', 'Delivered', 'Commission', 'Failed']
      },
      yAxis: {
        title: {
          text: 'Airtime Status'
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
