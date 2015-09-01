angular.module('Jaza')
  .controller('ProfileController', function($scope, User, snackbar) {

    User.getUser( username )
      .then(function(result) {
        console.log(result);
        $scope.firstName = result.data.first_name;
        $scope.lastName = result.data.last_name;
        $scope.email = result.data.email;
      })
      .catch(function(response) {
        console.log(response);
        $scope.firstName = '';
        $scope.lastName = '';
        $scope.email = '';
      });

    $scope.updateUser = function() {
      User.updateUser( username ,{ firstName: $scope.firstName, lastName: $scope.lastName, email: $scope.email })
        .then(function(result) {
          snackbar.create("User information successfully updated");
          console.log(result);
        })
        .catch(function(response) {
          console.log(response);
          snackbar.create("Something failed, user could not be updated");
          $scope.firstName = '';
          $scope.lastName = '';
          $scope.email = '';
        });
    };
  });
