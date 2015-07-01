angular.module('Jaza')
  .factory('User', function($http) {
    return {
      getUser: function() {
        return $http.get('/api/v1/accounts/');
      },
      updateUser: function(_id) {
        return $http.put('/api/v1/accounts/', _id);
      }
    };
  });
