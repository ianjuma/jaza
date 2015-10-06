angular.module('Jaza')
  .controller('AgentController', function($scope, $routeParams, Agent) {

    var productId = $routeParams.productId;
    Agent.getAgents(productId)
      .then(function (result) {
        if (Object.keys(result.data).length === 0) {
          $scope.Agent = 0;
        } else {
          $scope.Agent = result.data;
        }
      })
      .catch(function (response) {
        console.log(response);
        $scope.name = '';
        $scope.product_name = '';
        $scope.phone_number = '';
        $scope.id = '';
      });

  });
