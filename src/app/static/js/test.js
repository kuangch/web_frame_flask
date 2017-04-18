/**
 * Created by Thinkpad on 2017/4/18.
 */

var SOCKET_NAMESPACE = '/notification_push';
var MsgTpye = {
    HEADER_PERSON_PASS_INFO: "person_pass_info"
};
var module = angular.module('app_index', ['ngAnimate']);
module.controller(
    'ctrl_index', function ($scope, $http) {


        // socket connect
        socket = io.connect('http://' + document.domain + ':' + location.port + SOCKET_NAMESPACE);
        socket.on('connect', function () {
            console.log('connect');
        });
        socket.on('disconnect', function () {
            console.log('disconnect');
        });

        // start record
        socket.on(MsgTpye.HEADER_PERSON_PASS_INFO, function (msg) {
            var person = JSON.parse(msg.data);

            if (person.ip && person.ip == 'localhost')
                $scope.person2 = person.data;
            else if (person.ip && person.ip == '10.0.1.50')
                $scope.person3 = person.data;
            else
                $scope.person = person.data;
            $scope.$apply();

        });

    }
);