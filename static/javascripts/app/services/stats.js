angular.module('Jaza')
  .factory('Stats', function($http) {
    return {
      getAgentStats: function(agentId) {
        return $http.get('/api/v1/stats/agents', {agentId: agentId});
      },
      getProductStats: function(productId) {
        return $http.get('/api/v1/stats/products', {productId: productId});
      }
    }
  });
