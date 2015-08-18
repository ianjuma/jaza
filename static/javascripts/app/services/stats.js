angular.module('Jaza')
  .factory('ProductService', function($http) {
    return {
      getProductStats: function(productId) {
        var url = '/api/v1/crunch/products/' + productId;
        return $http.get( url );
      }
    }
  });

angular.module('Jaza')
  .factory('AgentService', function($http) {
    return {
      getAgentStats: function(agentId) {
        var url =  '/api/v1/crunch/agents/' + agentId;
        // '/api/v1/crunch/agents/', {params: {agentId: agentId}}

        return $http.get( url );
      }
    }
  });