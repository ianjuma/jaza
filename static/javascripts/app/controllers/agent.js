angular.module('Jaza')
  .controller('AgentController', function($scope, Agent) {
    //.$promise

    $scope.getAgents = function() {
      Agent.getAgents({
        name: $scope.name,
        product: $scope.product
      })
        .then(function (result) {
          console.log(result);
          $scope.name = result.name;
          $scope.product = result.product;
        })
        .catch(function (response) {
          console.log(response);
          $scope.name = '';
          $scope.product = '';
        });
    };

  });
