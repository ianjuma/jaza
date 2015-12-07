angular.module('Jaza')
  .factory('CrunchService', function($http) {
    return {
      getProductStats: function(productId, startDate, endDate, category) {
        var url = '/api/v1/crunch/products/';
        return $http.get( url, { params: { "productId": productId,
          "startDate": startDate, "endDate": endDate, "category": category } } );
      },
      getAgentStats: function(agentId, startDate, endDate, category) {
        var url =  '/api/v1/crunch/agents/';
        return $http.get( url, { params: { "agentId": agentId,
          "startDate": startDate, "endDate": endDate, "category": category } } );
      }
    }
  });