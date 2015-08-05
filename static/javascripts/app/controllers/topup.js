angular.module('Jaza')
  .controller('TopUpController', function($scope, TopUp) {

    $scope.topUpAgent = function() {
      TopUp.topUpAgent({
        agentID: $scope.agentID,
        agentID: $scope.tranCode,
        amountTopup: $scope.amountTopup
      })
        .then(function (result) {
          console.log(result);
          $scope.agentID = result.agentID;
          $scope.tranCode = result.tranCode;
          $scope.amountTopup = result.amountTopup;
        })
        .catch(function (response) {
          console.log(response);
          $scope.agentID = '';
          $scope.tranCode = '';
          $scope.amountTopup = '';
        });
    };

  });
