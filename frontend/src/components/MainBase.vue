<template>
  <section class="el-container wrapper is-vertical">
    <header class="el-header" style="height: 80px; background-color: rgb(64, 158, 255);">
      <ul class="header-operations">
        <li>切换主题色</li>
        <li>帮助</li>
      </ul>
    </header>
    <section class="el-container">
        <aside class="el-aside menu" style="width: 300px;"><ul role="menubar" class="el-menu"><li role="menuitem" tabindex="-1" class="el-menu-item is-active" style="padding-left: 20px;">页面1</li> <li role="menuitem" tabindex="-1" class="el-menu-item" style="padding-left: 20px;">页面2</li> <li role="menuitem" tabindex="-1" class="el-menu-item" style="padding-left: 20px;">页面3</li></ul></aside>
        <main class="el-main content"><div aria-label="Breadcrumb" role="navigation" class="el-breadcrumb"><span class="el-breadcrumb__item"><span role="link" class="el-breadcrumb__inner">首页</span><span role="presentation" class="el-breadcrumb__separator">/</span></span> <span class="el-breadcrumb__item"><span role="link" class="el-breadcrumb__inner">项目</span><span role="presentation" class="el-breadcrumb__separator">/</span></span> <span class="el-breadcrumb__item" aria-current="page"><span role="link" class="el-breadcrumb__inner">页面一</span><span role="presentation" class="el-breadcrumb__separator">/</span></span></div> <form class="el-form query-form el-form--label-right el-form--inline"><div class="el-form-item el-form-item--medium"><label for="name" class="el-form-item__label" style="width: 60px;">姓名</label><div class="el-form-item__content"><div class="el-input el-input--medium"><!----><input autocomplete="off" placeholder="请输入姓名" type="text" rows="2" validateevent="true" class="el-input__inner"><!----><!----><!----></div><!----></div></div> <div class="el-form-item el-form-item--medium"><label for="date" class="el-form-item__label" style="width: 60px;">日期</label><div class="el-form-item__content"><div class="el-date-editor el-range-editor el-input__inner el-date-editor--daterange el-range-editor--medium"><i class="el-input__icon el-range__icon el-icon-date"></i><input id="" name="" class="el-range-input"><span class="el-range-separator">-</span><input id="" name="" class="el-range-input"><i class="el-input__icon el-range__close-icon"></i></div><!----></div></div> <div class="el-form-item el-form-item--medium"><!----><div class="el-form-item__content"><button type="button" class="el-button el-button--primary el-button--medium"><!----><!----><span>搜索</span></button><!----></div></div></form> <div class="el-table table el-table--fit el-table--striped el-table--border el-table--enable-row-hover el-table--enable-row-transition el-table--medium"><div class="hidden-columns"><div></div> <div></div> <div></div> <div></div> <div></div></div><div class="el-table__header-wrapper"><table cellspacing="0" cellpadding="0" border="0" class="el-table__header" style="width: 840px;"><colgroup><col name="el-table_1_column_1" width="200"><col name="el-table_1_column_2" width="200"><col name="el-table_1_column_3" width="80"><col name="el-table_1_column_4" width="200"><col name="el-table_1_column_5" width="160"><col name="gutter" width=""></colgroup><thead class="has-gutter"><tr class=""><th colspan="1" rowspan="1" class="el-table_1_column_1     is-leaf is-sortable" style="cursor: pointer;"><div class="cell">日期<span class="caret-wrapper"><i class="sort-caret ascending"></i><i class="sort-caret descending"></i></span></div></th><th colspan="1" rowspan="1" class="el-table_1_column_2     is-leaf"><div class="cell">姓名</div></th><th colspan="1" rowspan="1" class="el-table_1_column_3     is-leaf"><div class="cell">地址</div></th><th colspan="1" rowspan="1" class="el-table_1_column_4     is-leaf"><div class="cell">邮编</div></th><th colspan="1" rowspan="1" class="el-table_1_column_5     is-leaf"><div class="cell">操作</div></th><th class="gutter" style="width: 0px;"></th></tr></thead></table></div><div class="el-table__body-wrapper is-scroll-left"><table cellspacing="0" cellpadding="0" border="0" class="el-table__body" style="width: 840px;"><colgroup><col name="el-table_1_column_1" width="200"><col name="el-table_1_column_2" width="200"><col name="el-table_1_column_3" width="80"><col name="el-table_1_column_4" width="200"><col name="el-table_1_column_5" width="160"></colgroup><tbody><tr class="el-table__row"><td class="el-table_1_column_1  "><div class="cell">2016-05-08</div></td><td class="el-table_1_column_2  "><div class="cell">王小虎</div></td><td class="el-table_1_column_3  "><div class="cell">上海市普陀区金沙江路 1518 弄</div></td><td class="el-table_1_column_4  "><div class="cell">200333</div></td><td class="el-table_1_column_5  "><div class="cell"><button type="button" class="el-button el-button--default el-button--mini"><!----><!----><span>编辑</span></button> <button type="button" class="el-button el-button--danger el-button--mini"><!----><!----><span>删除</span></button></div></td></tr><tr class="el-table__row el-table__row--striped"><td class="el-table_1_column_1  "><div class="cell">2016-05-07</div></td><td class="el-table_1_column_2  "><div class="cell">王小虎</div></td><td class="el-table_1_column_3  "><div class="cell">上海市普陀区金沙江路 1518 弄</div></td><td class="el-table_1_column_4  "><div class="cell">200333</div></td><td class="el-table_1_column_5  "><div class="cell"><button type="button" class="el-button el-button--default el-button--mini"><!----><!----><span>编辑</span></button> <button type="button" class="el-button el-button--danger el-button--mini"><!----><!----><span>删除</span></button></div></td></tr><tr class="el-table__row"><td class="el-table_1_column_1  "><div class="cell">2016-05-09</div></td><td class="el-table_1_column_2  "><div class="cell">王小虎</div></td><td class="el-table_1_column_3  "><div class="cell">上海市普陀区金沙江路 1518 弄</div></td><td class="el-table_1_column_4  "><div class="cell">200333</div></td><td class="el-table_1_column_5  "><div class="cell"><button type="button" class="el-button el-button--default el-button--mini"><!----><!----><span>编辑</span></button> <button type="button" class="el-button el-button--danger el-button--mini"><!----><!----><span>删除</span></button></div></td></tr><tr class="el-table__row el-table__row--striped"><td class="el-table_1_column_1  "><div class="cell">2016-05-10</div></td><td class="el-table_1_column_2  "><div class="cell">王小虎</div></td><td class="el-table_1_column_3  "><div class="cell">上海市普陀区金沙江路 1518 弄</div></td><td class="el-table_1_column_4  "><div class="cell">200333</div></td><td class="el-table_1_column_5  "><div class="cell"><button type="button" class="el-button el-button--default el-button--mini"><!----><!----><span>编辑</span></button> <button type="button" class="el-button el-button--danger el-button--mini"><!----><!----><span>删除</span></button></div></td></tr><tr class="el-table__row"><td class="el-table_1_column_1  "><div class="cell">2016-05-06</div></td><td class="el-table_1_column_2  "><div class="cell">王小虎</div></td><td class="el-table_1_column_3  "><div class="cell">上海市普陀区金沙江路 1518 弄</div></td><td class="el-table_1_column_4  "><div class="cell">200333</div></td><td class="el-table_1_column_5  "><div class="cell"><button type="button" class="el-button el-button--default el-button--mini"><!----><!----><span>编辑</span></button> <button type="button" class="el-button el-button--danger el-button--mini"><!----><!----><span>删除</span></button></div></td></tr><tr class="el-table__row el-table__row--striped"><td class="el-table_1_column_1  "><div class="cell">2016-05-03</div></td><td class="el-table_1_column_2  "><div class="cell">王小虎</div></td><td class="el-table_1_column_3  "><div class="cell">上海市普陀区金沙江路 1518 弄</div></td><td class="el-table_1_column_4  "><div class="cell">200333</div></td><td class="el-table_1_column_5  "><div class="cell"><button type="button" class="el-button el-button--default el-button--mini"><!----><!----><span>编辑</span></button> <button type="button" class="el-button el-button--danger el-button--mini"><!----><!----><span>删除</span></button></div></td></tr><tr class="el-table__row"><td class="el-table_1_column_1  "><div class="cell">2016-05-02</div></td><td class="el-table_1_column_2  "><div class="cell">王小虎</div></td><td class="el-table_1_column_3  "><div class="cell">上海市普陀区金沙江路 1518 弄</div></td><td class="el-table_1_column_4  "><div class="cell">200333</div></td><td class="el-table_1_column_5  "><div class="cell"><button type="button" class="el-button el-button--default el-button--mini"><!----><!----><span>编辑</span></button> <button type="button" class="el-button el-button--danger el-button--mini"><!----><!----><span>删除</span></button></div></td></tr><tr class="el-table__row el-table__row--striped"><td class="el-table_1_column_1  "><div class="cell">2016-05-04</div></td><td class="el-table_1_column_2  "><div class="cell">王小虎</div></td><td class="el-table_1_column_3  "><div class="cell">上海市普陀区金沙江路 1518 弄</div></td><td class="el-table_1_column_4  "><div class="cell">200333</div></td><td class="el-table_1_column_5  "><div class="cell"><button type="button" class="el-button el-button--default el-button--mini"><!----><!----><span>编辑</span></button> <button type="button" class="el-button el-button--danger el-button--mini"><!----><!----><span>删除</span></button></div></td></tr><tr class="el-table__row"><td class="el-table_1_column_1  "><div class="cell">2016-05-01</div></td><td class="el-table_1_column_2  "><div class="cell">王小虎</div></td><td class="el-table_1_column_3  "><div class="cell">上海市普陀区金沙江路 1518 弄</div></td><td class="el-table_1_column_4  "><div class="cell">200333</div></td><td class="el-table_1_column_5  "><div class="cell"><button type="button" class="el-button el-button--default el-button--mini"><!----><!----><span>编辑</span></button> <button type="button" class="el-button el-button--danger el-button--mini"><!----><!----><span>删除</span></button></div></td></tr><!----></tbody></table><!----><!----></div><!----><!----><!----><!----><div class="el-table__column-resize-proxy" style="display: none;"></div><div class="resize-triggers"><div class="expand-trigger"><div style="width: 427px; height: 1085px;"></div></div><div class="contract-trigger"></div></div></div></main>
    </section>
  </section>
</template>

<script>
  export default {
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>


<style>
  .el-header {
    padding: 0 20px;
    box-sizing: border-box;
}
  .header-operations {
    display: inline-block;
    float: right;
    padding-right: 30px;
    height: 100%;
  }

  .header-operations li {
    color: #fff;
    display: inline-block;
    vertical-align: middle;
    padding: 0 10px;
    margin: 0 10px;
    line-height: 50px;
    cursor: pointer;
  }
  .el-container {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -ms-flex-direction: row;
    flex-direction: row;
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    box-sizing: border-box;
    min-width: 0;
  }
  .content {
    padding: 20px;
}

.el-main {
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    padding: 20px;
}
.el-breadcrumb__item {
    float: left;
}

* {
    padding: 0;
    margin: 0;
}
.el-breadcrumb {
    font-size: 14px;
    line-height: 1;
}
.query-form {
    margin-top: 20px;
    padding-top: 25px;
    background-color: #d5dce0f5;
}

* {
    padding: 0;
    margin: 0;
}
user agent stylesheet
form {
    display: block;
    margin-top: 0em;
}
.table {
    margin-top: 30px;
}

.el-table--border {
    border-right: none;
    border-bottom: none;
}
.el-table--border, .el-table--group {
    border: 1px solid #cfd5e4;
}
.el-table--fit {
    border-right: 0;
    border-bottom: 0;
}
.el-table {
    position: relative;
    overflow: hidden;
    box-sizing: border-box;
    -webkit-box-flex: 1;
    flex: 1;
    width: 100%;
    max-width: 100%;
    font-size: 14px;
    color: #25417a;
}
.el-table, .el-table__expanded-cell {
    background-color: #fff;
}
* {
    padding: 0;
    margin: 0;
}
.el-menu-item.is-active {
    color: #409eff;
}
</style>