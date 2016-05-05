
angular.module("todayApp", [])
  .config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
  })
  .controller("LoginCtrl", function($scope) {
    $scope.namex = "xxx";
  })
;
