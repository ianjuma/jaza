angular.module('Jaza')
  .controller('LoginController', function($scope, Login) {

    $scope.loginUser = function() {
      Login.loginUser({
        username: $scope.username,
        password: $scope.password
      })
        .then(function (result) {
          console.log(result);
          $scope.username = result.username;
          $scope.password = result.password;
        })
        .catch(function (response) {
          console.log(response);
          $scope.username = '';
          $scope.password = '';
        });
    };

  });
