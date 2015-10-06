function run($http) {
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  $http.defaults.xsrfCookieName = 'csrftoken';
}

angular.module('Jaza', ['ngResource', 'ngMessages', 'ngRoute', 'mgcrea.ngStrap', 'highcharts-ng', 'angular.snackbar'])
  .config(function ($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true);

    $routeProvider
      .when('/', {
       templateUrl: 'static/views/product.html',
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
      .when('/topup/:agentId/', {
        templateUrl: 'static/views/topup.html',
        controller: 'TopUpController'
      })
      .when('/logout', {
        templateUrl: 'static/views/topup.html',
        controller: 'LogoutController'
      })
      .when('/product_stats/:productId/', {
        templateUrl: 'static/views/product_stats.html',
        controller: 'ProductStatsController'
      })
      .when('/agent/:productId/', {
        templateUrl: 'static/views/agent.html',
        controller: 'AgentController'
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