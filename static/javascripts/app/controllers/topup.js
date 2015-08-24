angular.module('Jaza')
  .controller('TopUpController', function($scope, TopUp) {

    $scope.topUpAgent = function() {
      TopUp.topUpAgent({
        agentID: $scope.agentID,
        refID: $scope.refID,
        amount: $scope.amount,
        source: $scope.source
      })
        .then(function (result) {
          console.log(result);
          $scope.agentID = result.agentID;
          $scope.refId = result.refID;
          $scope.amount = result.amount;
          $scope.source = result.source;
        })
        .catch(function (response) {
          console.log(response);
          $scope.agentID = '';
          $scope.refID = '';
          $scope.amount = '';
          $scope.source = '';
        });
    };

  });
