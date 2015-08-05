angular.module('Jaza')
  .factory('TopUp', function($http) {
    return {
      topUpAgent: function() {
        return $http.post('/api/v1/topup/');
      }
    };
  });
