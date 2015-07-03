angular.module('Jaza')
  .controller('ProfileController', function($scope, User) {

    $scope.getUser = function(username) {
      User.getUser(username)
        .then(function(result) {
          console.log(result);
          $scope.User = result.data;
        })
        .catch(function(response) {
          console.log(response);
          $scope.firstName = '';
          $scope.lastName = '';
          $scope.email = '';
        });
    };

    $scope.updateUser = function(username) {
      User.updateUser(username)
        .then(function(result) {
          console.log(result);
        })
        .catch(function(response) {
          console.log(response);
          $scope.firstName = '';
          $scope.lastName = '';
          $scope.email = '';
        });
    };
  });
