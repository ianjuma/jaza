angular.module('Jaza')
  .controller('AgentsController', function($scope, Agent) {

    //.$promise
    // TODO: scope this as well: as done above
      Agent.getAgents()
        .then(function (result) {
          console.log(result);
          $scope.Agent = result.data;
        })
        .catch(function (response) {
          console.log(response);
          $scope.name = '';
          $scope.product = '';
        });

  });