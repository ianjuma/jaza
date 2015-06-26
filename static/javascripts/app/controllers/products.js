angular.module('Jaza')
  .controller('GetProductsController', function($scope, Product) {
    //.$promise

    $scope.addProduct = function() {
      Product.addProduct({
        name: $scope.name,
        category: $scope.category,
        owner: $scope.owner
      })
        .then(function (result) {
          console.log(result);
          $scope.name = result.name;
          $scope.category = result.category;
          $scope.owner = result.owner;
        })
        .catch(function (response) {
          console.log(response);
          $scope.name = '';
          $scope.category = '';
          $scope.owner = '';
        });
    };

  });
