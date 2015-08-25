angular.module('Jaza')
  .controller('AgentController', function($scope, Agent) {

    Agent.getAgents({
      name: $scope.name,
      product: $scope.product
    })
      .then(function (result) {
        console.log(result);
        // _.map(result, getAgents(result));
        // $scope.Products = result.data.products; // comma separated list ? of products
        $scope.Agent = result.data;
      })
      .catch(function (response) {
        console.log(response);
        $scope.name = '';
        $scope.product = '';
      });

  });
