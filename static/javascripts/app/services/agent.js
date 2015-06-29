angular.module('Jaza')
  .factory('Agent', function($http) {
    return {
      getAgents: function() {
        return $http.get('/api/task');
      }
    };
  });
