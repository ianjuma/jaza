angular.module('Jaza')
  .factory('Logout', function($http) {
    return {
      logoutUser: function() {
        return $http.post('/api/v1/logout/');
      }
    };
  });
