/*
var owner_products;

function getProduct(product) {
  if (product.owner == ownerId) {
    owner_products += product.id;
  }
}

function getAgents(result) {
  var prod = _.map(result.products, getProduct());
  _.each(prod);
}
*/

angular.module('Jaza')
  .controller('AgentController', function($scope, Agent) {

     // $scope.getAgents = function() {
      Agent.getAgents({
        name: $scope.name,
        product: $scope.product
      })
        .then(function (result) {
          console.log(result);
          // _.map(result, getAgents(result));
          $scope.Agent = result.data;
        })
        .catch(function (response) {
          console.log(response);
          $scope.name = '';
          $scope.product = '';
        });
     // };

  });
