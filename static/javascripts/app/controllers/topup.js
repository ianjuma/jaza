angular.module('Jaza')
  .controller('TopUpController', function($scope, TopUp, snackbar) {

    $scope.topUpAgent = function() {
      TopUp.topUpAgent({
        agentID: $scope.agentID,
        refID: $scope.refID,
        amount: $scope.amount,
        source: $scope.source
      })
        .then(function (result) {
          console.log(result);
          snackbar.create("Agent successfully topped up");
          $scope.agentID = result.agentID;
          $scope.refId = result.refID;
          $scope.amount = result.amount;
          $scope.source = result.source;
        })
        .catch(function (response) {
          console.log(response);
          snackbar.create("Agent top up failed");
          $scope.agentID = '';
          $scope.refID = '';
          $scope.amount = '';
          $scope.source = '';
        });
    };

  });
