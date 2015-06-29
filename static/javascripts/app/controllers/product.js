angular.module('Jaza')
  .controller('ProductController', function($scope, Product) {
    //.$promise

    //$scope.getProducts = function() {
      Product.getProducts({
        name: $scope.name,
        category: $scope.category,
        owner: $scope.owner
      })
        .then(function (result) {
          console.log(result);
          $scope.Product = result.data;
        })
        .catch(function (response) {
          console.log(response);
          $scope.name = '';
          $scope.category = '';
          $scope.owner = '';
        });
    //};

  });
