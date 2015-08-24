function run($http) {
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  $http.defaults.xsrfCookieName = 'csrftoken';
}

angular.module('Jaza', ['ngResource', 'ngMessages', 'ngRoute', 'mgcrea.ngStrap', 'highcharts-ng'])
  .config(function ($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true);

    $routeProvider
      .when('/', {
        templateUrl: 'static/views/dashboard.html',
        controller: 'ProductController'
      })
      .when('/profile', {
        templateUrl: 'static/views/profile.html',
        controller: 'ProfileController'
      })
      .when('/products', {
        templateUrl: 'static/views/product.html',
        controller: 'ProductController'
      })
      .when('/topup', {
        templateUrl: 'static/views/topup.html',
        controller: 'TopUpController'
      })
      .when('/agents', {
        templateUrl: 'static/views/agent.html',
        controller: 'AgentController'
      })
      .when('/sales', {
        templateUrl: 'static/views/sales.html',
        controller: 'SalesController'
      })
      .when('/prod_stats/:productId/', {
        templateUrl: 'static/views/product_stats.html',
        controller: 'ProductStatsController'
      })
      .when('/agent_stats/:agentId/', {
        templateUrl: 'static/views/agent_stats.html',
        controller: 'AgentStatsController'
      })
      .otherwise({
        redirectTo: '/'
      });
  }).run(run);

run.$inject = ['$http'];