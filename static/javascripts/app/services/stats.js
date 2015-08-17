angular.module('Jaza')
  .factory('Stats', function($http) {
    return {
      getAgentStats: function(agentId) {
        return $http.get('/api/v1/crunch/agents/' + agentId);
      },
      getProductStats: function(productId) {
        return $http.get('/api/v1/crunch/products/', + productId);
      }
    }
  });
