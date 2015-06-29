angular.module('Jaza')
  .controller('ProductController', function($scope, Product) {
    //.$promise

    $scope.getProducts = function() {
      Product.getProducts({
        name: $scope.name,
        category: $scope.category,
        owner: $scope.owner,
        created_at: $scope.created_at
      })
        .then(function (result) {
          console.log(result);
          $scope.name = result.name;
          $scope.category = result.category;
          $scope.owner = result.owner;
          $scope.created_at = result.created_at;
        })
        .catch(function (response) {
          console.log(response);
          $scope.name = '';
          $scope.category = '';
          $scope.owner = '';
          $scope.created_at = '';
        });
    };

  });
