/**
 * Created by Thinkpad on 2017/4/18.
 */

//引入gulp和gulp插件
var gulp = require('gulp'),
    sass = require('gulp-sass'),
    runSequence = require('run-sequence'),
    rev = require('gulp-rev'),
    convertNewline = require("gulp-convert-newline"),
    revCollector = require('gulp-rev-collector');

//定义css、js源文件路径
var cssSrc = 'src/app/static/css/*.css',
    jsSrc = 'src/app/static/js/*.js';
    sassSrc = ['src/sass/**/*.{scss,sass}','src/sass/*.{scss,sass}'];


//CSS生成文件hash编码并生成 rev-manifest.json文件名对照映射
gulp.task('revCss', function(){
    return gulp.src(cssSrc)
        .pipe(rev())
        .pipe(rev.manifest())
        .pipe(gulp.dest('rev/css'));
});


//js生成文件hash编码并生成 rev-manifest.json文件名对照映射
gulp.task('revJs', function(){
    return gulp.src(jsSrc)
        .pipe(rev())
        .pipe(rev.manifest())
        .pipe(gulp.dest('rev/js'));
});


//Html替换css、js文件版本
gulp.task('revHtml', function () {
    return gulp.src(['rev/**/*.json', 'src/app/templates/*.html'])
        .pipe(revCollector())
        .pipe(gulp.dest('rev/templates'));
});


//开发构建
gulp.task('dev', function (done) {
    condition = false;
    runSequence(
        ['sass'],
        ['revCss'],
        ['revJs'],
        ['revHtml'],
        done);
});

// sass
gulp.task('sass', function () {
  return gulp.src(sassSrc)
    .pipe(sass().on('error', sass.logError))
    .pipe(convertNewline({
            newline: "lf"
        }))
    .pipe(gulp.dest('src/app/static/css'));
});

gulp.task('sass:watch', function () {
  gulp.watch(sassSrc, ['sass']);
});

gulp.task('default', ['dev']);