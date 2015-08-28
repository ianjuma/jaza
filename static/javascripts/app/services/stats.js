angular.module('Jaza')
  .factory('ProductService', function($http) {
    return {
      getProductStats: function(productId, startDate, endDate, category) {
        var url = '/api/v1/crunch/products/';
        console.log(productId, startDate, endDate, category);
        return $http.get( url, { params: { "productId": productId,
          "startDate": startDate, "endDate": endDate, "category": category } } );
      }
    }
  });

angular.module('Jaza')
  .factory('AgentService', function($http) {
    return {
      getAgentStats: function(agentId, startDate, endDate, category) {
        var url =  '/api/v1/crunch/agents/';
        return $http.get( url, { params: { "agentId": agentId,
          "startDate": startDate, "endDate": endDate, "category": category } } );
      }
    }
  });