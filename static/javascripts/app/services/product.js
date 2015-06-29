angular.module('Jaza')
  .factory('Product', function($http) {
    return {
      getProducts: function() {
        return $http.get('/api/v1/product');
      }
    };
  });
