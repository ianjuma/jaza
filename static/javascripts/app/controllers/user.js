angular.module('Jaza')
  .controller('ProfileController', function($scope, User, snackbar) {

    User.getUser( username )
      .then(function(result) {
        $scope.firstName = result.data.first_name;
        $scope.lastName = result.data.last_name;
        $scope.email = result.data.email;
      })
      .catch(function(response) {
        console.log(response);
        $scope.oldPassword = '';
        $scope.password = '';
        $scope.repeatPassword = '';
      });

    $scope.updateUser = function() {
      User.updateUser( username ,{ firstName: $scope.firstName, lastName: $scope.lastName,
        email: $scope.email, password: $scope.password, repeatPassword: $scope.repeatPassword })
        .then(function(result) {
          snackbar.create("User Information Successfully Updated");
          window.location.href = '/';
        })
        .catch(function(response) {
          console.log(response);
          snackbar.create("Something failed, User could not be Updated");
          $scope.oldPassword = '';
          $scope.password = '';
          $scope.repeatPassword = '';
        });
    };
  });
