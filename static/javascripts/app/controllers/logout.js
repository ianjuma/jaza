angular.module('Jaza')
  .controller('LogoutController', function($scope, Logout) {
    Logout.logoutUser({
    })
      .then(function (result) {
        window.location.href = '/';
      })
      .catch(function (response) {
        window.location.href = '/';
        console.log(response);
      });

  });
