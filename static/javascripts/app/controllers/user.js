angular.module('Jaza')
  .controller('ProfileController', function($scope, User) {
    //.$promise
    $scope.getUser = function() {
      User.getUser()
        .then(function(result) {
          console.log(result);
          $scope.User = result.data;
        })
        .catch(function(response) {
          console.log(response);
          $scope.first_name = '';
          $scope.last_name = '';
          $scope.email = '';
        });
    };

    $scope.updateUser = function() {
      User.updateUser()
        .then(function(result) {
          console.log(result);
        })
        .catch(function(response) {
          console.log(response);
          $scope.first_name = '';
          $scope.last_name = '';
          $scope.email = '';
        });
    };
  });
