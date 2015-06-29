angular.module('Jaza')
  .factory('User', function($http) {
    return {
      getUser: function() {
        return $http.get('/api/v1/user');
      },
      updateUser: function(_id) {
        return $http.put('/api/v1/user', _id);
      }
    };
  });
