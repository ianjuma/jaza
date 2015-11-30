angular.module('Jaza')
  .controller('ProductController', function($scope, Product) {
    $scope.searchText   = ''; // set the default filter term

    Product.getProducts({
      name: $scope.name,
      category: $scope.category,
      created_at: $scope.created_at,
      ussd_channel: $scope.ussd_channel
    })
      .then(function (result) {
        if (Object.keys(result.data).length === 0) {
          $scope.Product = 0;
        } else {
          $scope.Product = result.data;
        }
      })
      .catch(function (response) {
        console.log(response);
        $scope.name = '';
        $scope.category = '';
        $scope.created_at = '';
        $scope.ussd_channel = '';
      });

  });
