angular.module('Jaza')
  .factory('Product', function($http) {
    return {
      addProduct: function(Ticket) {
        return $http.post('/api/support', { title: Ticket.title, ticket: Ticket.ticket,
          support_urgency: Ticket.support_urgency });
      },
      getProducts: function(_id) {
        return $http.get('/api/v1/product', _id);
      },
      updateProduct: function(_id) {
        return $http.put('/api/v1/product', _id);
      },
      deleteProduct: function(_id) {
        return $http.delete('/api/v1/product', _id);
      }
    };
  });
