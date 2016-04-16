

function myCtrl($scope) {
  $scope.name = 'World';
  $scope.title = 'Angular tutorial';
  $scope.author = 'Huang Bo';

  $scope.clickMe = function() {
    $scope.isHidden = !$scope.isHidden;
  };

  $scope.contacts = [
    {
      name: 'Kally',
      'phone': '215466464',
      'email': 'zzz@zzz.com',
    },
    {
      'name': 'The BBB',
      'phone': '415657',
      'email': 'bbb@bbb.com',
    }
  ];

  $scope.setStyle = function() {
    if ($scope.styler) {
      return {
        'background': 'red',
      };
    } else
      return;
  };

}

