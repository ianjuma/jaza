angular.module('Jaza')
  .factory('User', function($http) {
    return {
      getUser: function(_username) {
        var url = '/api/v1/accounts/' + _username + '/';
        return $http.get(url);
      },
      updateUser: function(_username, User) {
        var url = '/api/v1/accounts/' + _username + '/';
        return $http.put(url, {
          firstName: User.firstName, lastName: User.lastName,
          email: User.email, username: _username, password: User.password,
          repeatPassword: User.repeatPassword } );
      }
    };
  });
