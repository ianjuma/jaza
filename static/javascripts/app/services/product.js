angular.module('Jaza')
  .factory('Product', function($http) {
    return {
      getProducts: function(_id) {
        return $http.get('/api/v1/product', _id);
      }
    };
  });
