angular.module('Jaza')
  .factory('TopUp', function($http) {
    return {
      topUpAgent: function(Agent) {
        return $http.post('/api/v1/billing/add', { agentID: Agent.agentID,
          amount: Agent.amount, source: Agent.source, refID: Agent.refID });
      }
    };
  });
