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
      .when('/prod_stats/:product_id/', {
        templateUrl: 'static/views/product_stats.html',
        controller: 'AgentStatsController'
      })
      .when('/agent_stats/:agent_id/', {
        templateUrl: 'static/views/agent_stats.html',
        controller: 'ProductStatsController'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
