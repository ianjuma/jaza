angular.module('Jaza')
  .controller('TopUpController', function($scope, $routeParams , TopUp, snackbar) {

    $scope.topUpAgent = function() {
      TopUp.topUpAgent({
        agentID: $routeParams.agentId,
        refID: $scope.refID,
        amount: $scope.amount,
        source: $scope.source
      })
        .then(function (result) {
          snackbar.create("Agent successfully topped up");
          $scope.refId = result.refID;
          $scope.amount = result.amount;
          $scope.source = result.source;
        })
        .catch(function (response) {
          console.log(response);
          snackbar.create("Agent top up failed");
        });
    };

  });
