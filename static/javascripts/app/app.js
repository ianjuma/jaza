angular.module('Jaza', ['ngResource', 'ngMessages', 'ngRoute', 'mgcrea.ngStrap'])
  .config(function ($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true);

    $routeProvider
      .when('/', {
        templateUrl: 'static/views/dashboard.html',
        controller: 'GetProductsController'
      })
      .when('/profile', {
        templateUrl: 'static/views/profile.html',
        controller: 'ProfileController'
      })
      .when('/products', {
        templateUrl: 'static/views/product.html',
        controller: 'UpdateProductsController'
      })
      .when('/agents', {
        templateUrl: 'static/views/agents.html',
        controller: 'UpdateProductsController'
      })
      .when('/update', {
        templateUrl: 'static/views/updateProduct.html',
        controller: 'UpdateProductsController'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
