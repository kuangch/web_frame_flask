/**
 * Created by Thinkpad on 2017/1/12.
 */
QUnit.begin(function(details){
    console.log( "Test amount:", details.totalTests );
    this.testDiv = test_div = document.createElement('div');
    test_div.setAttribute('id', 'testDiv');
    test_div.style.display = 'none';
    document.body.appendChild(test_div)
});
QUnit.done(function(details){
    console.log(
        "Total: ", details.total,
        " Failed: ", details.failed,
        " Passed: ", details.passed,
        " Runtime: ", details.runtime
    );
});

QUnit.module('new instance');
QUnit.test('create instance of number-growth failed', function (assert) {
    assert.throws(
        function(){
            NumberGrowth();
        },
        new Error('please appoint div ID you want to append to'),
        'throws Error: no parameter div ID'
    );
    assert.throws(
        function(){
            NumberGrowth('testDiv');
        },
        new Error('please appoint number you want to show'),
        'throws Error: no parameter number'
    );
    assert.throws(
        function(){
            NumberGrowth('testDiv','not a number');
        },
        new Error('second parameter is not a number'),
        'throws Error: second parameter not a number'
    );
});

QUnit.test('create instance of number-growth success', function (assert) {
    var ng = NumberGrowth('testDiv', 100);
    assert.notEqual(ng.startGrow, undefined, 'instance of number-growth has attribute: startGrow');
    assert.notEqual(ng.changeNumber, undefined, 'instance of number-growth has attribute: changeNumber');
    assert.equal(ng.xx, undefined, 'instance of number-growth not has attribute: xx');
});

QUnit.module('KiloCharacter');
QUnit.test('show kilo-character', function (assert) {

    assert.expect( 1 );
    var done = assert.async( 1 );

    var ng = NumberGrowth('testDiv', 5000, {
        showKiloCharacter: true,
        growNumberAnimateTime: 100
    });
    ng.startGrow();

    setTimeout(function(){
        var ngNum = document.getElementById('testDiv').innerHTML;
        assert.equal(ngNum, '5,000', 'has kilo-character number is 5,000');
        done();

    },200);

});

QUnit.test('hide kilo-character', function (assert) {

    assert.expect(1);
    var done = assert.async(1);

    var ng = NumberGrowth('testDiv', 5000, {
        showKiloCharacter: false,
        growNumberAnimateTime: 100
    });
    ng.startGrow();
    setTimeout(function () {
        var ngNum = document.getElementById('testDiv').innerHTML;
        assert.equal(parseInt(ngNum), 5000, 'no kilo-character number is 5000');
        done();
    }, 200);
});

QUnit.module('number animator');
QUnit.test('growing number', function (assert) {

    assert.expect( 3 );
    var done = assert.async( 3 );

    var ng = NumberGrowth('testDiv', 1000, {
        showKiloCharacter: false,
        growNumberAnimateTime: 200
    });
    ng.startGrow();

    setTimeout(function(){
        var ngNum = document.getElementById('testDiv').innerHTML;
        assert.ok(400<parseInt(ngNum)<600, 'at 100ms number is between 400 and 600');
        done();

    },100);
    setTimeout(function(){
        var ngNum = document.getElementById('testDiv').innerHTML;
        assert.ok(700<parseInt(ngNum)<800, 'at 150ms number is between 700 and 800');
        done();

    },150);
    setTimeout(function(){
        var ngNum = document.getElementById('testDiv').innerHTML;
        assert.ok(parseInt(ngNum)>950, 'at 200ms number is big than 950');
        done();

    },200);

});

QUnit.test('reducing number', function (assert) {

    assert.expect( 3 );
    var done = assert.async( 3 );

    var ng = NumberGrowth('testDiv', 600, {
        showKiloCharacter: false,
        startNumber: 1000,
        growNumberAnimateTime: 200
    });
    ng.startGrow();

    setTimeout(function(){
        var ngNum = document.getElementById('testDiv').innerHTML;
        assert.ok(790<parseInt(ngNum)<810, 'at 100ms number is between 790 and 810');
        done();

    },100);
    setTimeout(function(){
        var ngNum = document.getElementById('testDiv').innerHTML;
        assert.ok(690<parseInt(ngNum)<710, 'at 150ms number is between 690 and 710');
        done();

    },150);
    setTimeout(function(){
        var ngNum = document.getElementById('testDiv').innerHTML;
        assert.ok(parseInt(ngNum)<610, 'at 200ms number is small than 610');
        done();

    },200);

});

QUnit.module('change number');
QUnit.test('growing number', function (assert) {

    assert.expect( 3 );
    var done = assert.async( 3 );

    var ng = NumberGrowth('testDiv', 1000, {
        showKiloCharacter: false,
        growNumberAnimateTime: 100,
        changeNumberAnimateTime: 200
    });

    var startGrow = function (time) {
        var deferred = $.Deferred();
        ng.startGrow();
        setTimeout(function () {
            deferred.resolve();
        }, time + 100);
        return deferred.promise();
    };
    var changeNum = function (number,time) {
        time = time||200;
        var deferred = $.Deferred();
        ng.changeNumber(number,{

        });
        setTimeout(function () {
            deferred.resolve();
            VerifyNum(number);
        }, time + 100);
        return deferred.promise();
    };

    $.when(startGrow(200)).then(function(){
        return changeNum(100)
    }).then(function () {
        return changeNum(500)
    }).then(function () {
        return changeNum(200)
    });

    function VerifyNum(number){
        var ngNum = document.getElementById('testDiv').innerHTML;
        assert.equal(parseInt(ngNum), number, 'change number to '+ number + ' correct!');
        done();
    }

});