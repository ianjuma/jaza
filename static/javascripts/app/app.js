angular.module('Jaza', ['ngResource', 'ngMessages', 'ngRoute', 'ngAnimate', 'mgcrea.ngStrap'])
  .config(function ($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true);

    $routeProvider
      .when('/', {
        templateUrl: 'static/views/dashboard.html',
        controller: 'GetTasksController'
      })
      .when('/profile', {
        templateUrl: 'static/views/profile.html',
        controller: 'TaskController'
      })
      .when('/products', {
        templateUrl: 'static/views/products.html',
        controller: 'PaymentController'
      })
      .when('/update', {
        templateUrl: 'static/views/updateProduct.html',
        controller: 'UserController'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
