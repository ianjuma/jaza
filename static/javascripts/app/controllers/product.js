angular.module('Jaza')
  .controller('ProductController', function($scope, Product) {

    // $scope.getProducts = function() {
      Product.getProducts({
        name: $scope.name,
        category: $scope.category,
        created_at: $scope.created_at
      })
        .then(function (result) {
          console.log(result);
          $scope.Product = result.data;
        })
        .catch(function (response) {
          console.log(response);
          $scope.name = '';
          $scope.category = '';
          $scope.created_at = '';
        });
    // };

  });
