angular.module('Jaza')
  .controller('ProductStatsController', function($scope, $routeParams, ProductService) {

    (function() {
      var productId = $routeParams.productId;
      console.log($routeParams);

      ProductService.getProductStats(productId)
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
