angular.module('Jaza', ['ngResource', 'ngMessages', 'ngRoute', 'mgcrea.ngStrap'])
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
      .when('/agents', {
        templateUrl: 'static/views/agent.html',
        controller: 'AgentController'
      })
      .when('/sales', {
        templateUrl: 'static/views/sales.html',
        controller: 'ProductController'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
