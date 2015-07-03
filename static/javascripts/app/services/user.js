angular.module('Jaza')
  .factory('User', function($http) {
    return {
      getUser: function(_username) {
        return $http.get('/api/v1/accounts/', _username);
      },
      updateUser: function(_username) {
        return $http.put('/api/v1/accounts/', _username);
      }
    };
  });
