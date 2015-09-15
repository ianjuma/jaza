angular.module('Jaza')
  .controller('AgentController', function($scope, Agent) {

    Agent.getAgents({
      name: $scope.name,
      product_name: $scope.product_name,
      phone_number: $scope.phone_number,
      id: $scope.id
    })
      .then(function (result) {
        if (Object.keys(result.data).length === 0) {
          $scope.Agent = 0;
        } else {
          $scope.Agent = result.data;
        }

        console.log(result);
      })
      .catch(function (response) {
        console.log(response);
        $scope.name = '';
        $scope.product_name = '';
        $scope.phone_number = '';
        $scope.id = '';
      });

  });
