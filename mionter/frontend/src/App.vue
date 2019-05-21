<template>
  <div id="app">
    <header class="el-header" style="height: 80px; background-color: rgb(126, 175, 223);">
      <img src='/static/kindle.ico' alt="logo" class="header-logo">
      <ul class="header-operations">
        <li>切换主题色</li>
        <li>帮助</li>
      </ul>
    </header>
    <div class="div_left">
      <ul class="left_ul" v-for="(btn,index) in btns" :key="index">
        <li @click="goIndex(index)" :class="nactive==index?'left_ul_active':''">{{btn}}</li>
      </ul>
    </div>
    <div class="div_right">
      <p class="right_bread"><span class="bread">{{ btn }}</span> / {{bread}}</p>
      <router-view />
    </div>

  </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {
        btns: ['项目1', '项目2', '项目3'],
        nactive: 0,
        bread: '页面1',
        btn: '项目1'
      }
    },
    methods: {
      goIndex(index) {
        switch (index) {
          case 0:
            this.$router.push('/')
            this.nactive = 0
            this.btn = '项目1'
            this.bread = '页面1'
            break
          case 1:
            this.$router.push('/1')
            this.nactive = 1
            this.btn = '项目2'
            this.bread = '页面1'
            break
          case 2:
            this.$router.push('/1')
            this.nactive = 2
            this.btn = '项目3'
            this.bread = '页面1'
            break
        }

      }
    }
  }
</script>

<style>
  * {
    margin: 0;
    padding: 0;
  }

  #app {
    width: 100%;
    margin: 0 auto;
    overflow: hidden;
    position: fixed;
    height: 100%;
  }

  .el-header {
    padding: 0 20px;
    box-sizing: border-box;
  }

  .header-operations {
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
    line-height: 80px;
    cursor: pointer;
  }

  .header-logo {
    width: 80px;
  }

  #app>div {
    float: left;
    height: 100%;
  }

  .div_left {
    width: 19%;

    /* border-right:1px solid #ddd; */
  }

  .div_right {
    width: 80%;
    border-left: 1px solid #ddd;
  }

  .left_ul {
    list-style: none;
  }

  .left_ul li {
    padding: 8px 10px;
    border-radius: 2px;
    cursor: pointer;
    height: 56px;
    line-height: 56px;
    padding: 0 20px;
    position: relative;
    cursor: pointer;
    white-space: nowrap;
  }

  .left_ul_active {
    background: rgb(182, 211, 223);
  }

  .bread {
    font-weight: bold;
  }

  .right_bread {
    padding: 15px 10px 0px 10px;
  }
</style>