angular.module('Jaza')
  .factory('Sales', function($http) {
    return {
      getSales: function() {
        return $http.get('/api/v1/sales/');
      }
    }
  });
