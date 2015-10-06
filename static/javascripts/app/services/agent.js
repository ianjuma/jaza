angular.module('Jaza')
  .factory('Agent', function($http) {
    return {
      getAgents: function(productId) {
        var url = '/api/v1/distributors/agents/' + productId;
        return $http.get(url);
      }
    };
  });
