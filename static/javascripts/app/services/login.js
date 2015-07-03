angular.module('Jaza')
  .factory('Login', function($http) {
    return {
      loginUser: function() {
        return $http.post('/api/v1/login/');
      }
    };
  });
