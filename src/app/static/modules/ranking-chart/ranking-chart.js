/**
 * Created by kuangch on 2016/10/17.
 * depend on jquery
 */

(function(window, document){

    var rank_chart_title_html = '';
    rank_chart_title_html += '<div class="rank-chart-title">';
    rank_chart_title_html +=    '<div class="name"><strong></strong></div>';
    rank_chart_title_html += '</div>';

    var rank_chart_item_html = '';
    rank_chart_item_html += '<div class="rank-chart-item">';
    rank_chart_item_html += '   <div class="serial-number"></div>';
    rank_chart_item_html += '   <a class="name" href="#"></a>';
    rank_chart_item_html += '   <div class="bar-container">';
    rank_chart_item_html += '       <div class="value-bar"></div>';
    rank_chart_item_html += '   </div>';
    rank_chart_item_html += '   <div class="value"></div>';
    rank_chart_item_html += '</div>';

    window.RankingChart = function(){
        if (!arguments[0]) {
            throw new Error('please appoint div you want to append to');
        }
        if (!arguments[1]) {
            throw new Error('please give the data you want to show');
        }

        // default setting parameters
        var mSettings = {
            titleTxt: 'Title',
            titleTxtColor: '#197EE8',
            titleColor: 'white',
            itemNoBgColor: '#F5E401',
            firstitemNoBgColor: '#fe6a6d',
            seconditemNoBgColor: '#64c3df',
            thirditemNoBgColor: '#46b7af',
            itemNoColor: 'black',
            itemNameColor: 'black',
            itemBarColor:'#B1D6FF',
            itemValueColor: 'black',
            itemValueShowKiloCharacter: true
        };


        var configCustomSetting = function(settings){
            var customSettings = settings;
            for(var key in customSettings){
                var newSettingItem = customSettings[key];
                if( key in mSettings ){
                    mSettings[key] = newSettingItem;
                }
            }
        };

        // get custom setting parameters
        if(arguments[2]){
            configCustomSetting(arguments[2]);
        }

        function addKiloCharacter(str) {
            var iNum = str.length%3;
            var prev = '';
            var arr = [];
            var iNow = 0;
            var tmp = '';
            if(iNum !=0) {
                prev = str.substring(0,iNum);
                arr.push(prev);
            }
            str = str.substring(iNum);
            for(var i=0;i<str.length;i++) {
                iNow++;
                tmp +=str[i];
                if(iNow ==3 && tmp) {
                    arr.push(tmp);
                    tmp = '';
                    iNow = 0;
                }
            }
            return arr.join(',');
        }

        /*
        add data item
         */
        var appendItem = function(container, index, name, value, percent, isLast){
            var item = $(rank_chart_item_html);
            container.append(item);
            item.find('.serial-number').html(index);
            var dom_name = item.find('.name');
            dom_name.html(name);
            dom_name.attr('title', name);
            item.find('.value').html(mSettings.itemValueShowKiloCharacter ? addKiloCharacter(value.toString()): value);

            // must be set timeout that it can play transition animate
            setTimeout(function(){
                item.find('.bar-container .value-bar').css('width', percent + '%');
            },0);

            item.find('.serial-number').css('background-color', mSettings.itemNoBgColor);
            item.find('.serial-number').css('color', mSettings.itemNoColor);
            item.find('.name').css('color', mSettings.itemNameColor);
            item.find('.bar-container .value-bar').css('background-color', mSettings.itemBarColor);
            item.find('.value').css('color', mSettings.itemValueColor);
            $(".rank-chart-item").eq(0).find('.serial-number').css('background-color', mSettings.firstitemNoBgColor);
            $(".rank-chart-item").eq(1).find('.serial-number').css('background-color', mSettings.seconditemNoBgColor);
            $(".rank-chart-item").eq(2).find('.serial-number').css('background-color', mSettings.thirditemNoBgColor);
            $(".rank-chart-item").eq(0).find('.bar-container .value-bar').css('background-color', mSettings.firstitemNoBgColor);
            $(".rank-chart-item").eq(1).find('.bar-container .value-bar').css('background-color', mSettings.seconditemNoBgColor);
            $(".rank-chart-item").eq(2).find('.bar-container .value-bar').css('background-color', mSettings.thirditemNoBgColor);

            // keep last item margin bottom same with title dom margin bottom
            if(isLast)
                item.css('margin-bottom', chart_container.find('.rank-chart-title').css('margin-bottom'));
        };

        /*
        render data
         */
        var showDataChart = function(container, data){
            // clear timer
            for(var each in intervals){
                try{ clearInterval(intervals[each]);}catch (error){}
            }

            if (data === undefined || data.length < 1){
                $(".rank-chart-title").css("display","block")
                title_container.find('.name>strong').html('没有数据...');
                return;
            }
            var dataLen = data.length;

            // sort
            data = data.sort(function(a,b){
                return b.value - a.value;
            });
            var maxValue = data[0].value;

            for(var i = 0; i < dataLen ; i++){
                var name = data[i].name;
                var value = data[i].value;
                var percent = maxValue > 0 ? value/maxValue * 100 : 0;
                var isLast = i === dataLen -1;
                appendItem(container, i+1, name, value, percent, isLast);
            }

            // make the background color same of item dom and background of item dom
            chart_container.css('background-color', container.find('.rank-chart-item').css('background-color'));
        };

        /*
        reader title
         */
        var showTitle = function(container, settings){
            var title = $(rank_chart_title_html);
            container.empty();
            container.append(title);
            title.find('.name>strong').html(settings.titleTxt);
            title.find('.name>strong').css('color', settings.titleTxtColor);
            title.css('background-color', settings.titleColor)
        };

        // dom of chart
        var chart_container = $(arguments[0]);
        // data of chart
        var data = arguments[1];

        // global variate for timer
        var intervals = {};

        /*
        show loading interface
         */
        var loading = function () {
            title_container.find('.name>strong').html('正在加载数据...');
            item_container.find('.name').html('-- + -- + --');
            item_container.find('.name').attr('title', '');
            item_container.find('.value').html('---');
            var bars = item_container.find('.bar-container .value-bar');
            var len = bars.length;

            var animateBar = function(index){
                var isFirst = true;
                intervals['animateBar' + index.toString()] = setInterval(function(){
                    var bar_value = 2;
                    if(!isFirst){
                        bar_value = Math.floor(Math.random() * (30 - 5) + 5);
                    }
                    bars[index].style.width = bar_value + '%';
                    isFirst = false;
                },800);
            };
            for(var i = 0; i< len; i++){
                animateBar(i);
            }
        };

        /*
        change data
         */
        var changeData = function(){

            // clear timer
            for(var each in intervals){
                try{ clearInterval(intervals[each]);}catch (error){}
            }

            // get custom setting parameters
            if(arguments[1]){
                configCustomSetting(arguments[1]);
                showTitle(title_container, mSettings);
            }

            data = arguments[0];

            chart_container.find('.rank-chart-title .name>strong').html(mSettings.titleTxt);
            item_container.empty();
            showDataChart(item_container, data);
        };

        // container of title and data
        var title_container = $('<div>');
        var item_container = $('<div>');

        // fill in title and data item
        chart_container.append(title_container);
        chart_container.append(item_container);

        // render chart
        showTitle(title_container, mSettings);
        showDataChart(item_container, data);

        return {changeData: changeData, perLoading: loading};
    }

})(window, document);