angular.module('Jaza')
  .controller('TopUpController', function($scope, TopUp) {

    $scope.topUpAgent = function() {
      TopUp.topUpAgent({
        agentID: $scope.agentID,
        refID: $scope.refId,
        amount: $scope.amount,
        source: $scope.source
      })
        .then(function (result) {
          console.log(result);
          $scope.agentID = result.agentID;
          $scope.refId = result.refId;
          $scope.amount = result.amount;
          $scope.source = result.source;
        })
        .catch(function (response) {
          console.log(response);
          $scope.agentID = '';
          $scope.refId = '';
          $scope.amount = '';
          $scope.source = '';
        });
    };

  });
