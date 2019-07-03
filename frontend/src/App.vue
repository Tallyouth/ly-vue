<template>
  <div id="app">
    <header class="el-header" style="height: 80px; background-color: rgb(64, 158, 255);">
      <img src='/static/kindle.ico' alt="logo" class="header-logo">
      <ul class="header-operations">
        <li>切换主题色</li>
        <li>帮助</li>
      </ul>
    </header>
    <!-- <div class="div_left">
      <ul class="left_ul" v-for="(btn,index) in btns" :key="index">
        <el-menu-item v-bind:index=btn.name @click="goIndex(index, btn.id)" :class="nactive==index?'left_ul_active':''">
          {{btn.name}}</el-menu-item>
      </ul>
    </div> -->
    <el-row class="div_left">
      <el-menu default-active="2" class="el-menu-vertical-demo">
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>导航一</span>
          </template>
          <!-- <el-menu-item index="1-1">选项1</el-menu-item> -->
          <ul class="left_ul" v-for="(btn,index) in btns" :key="index">
            <el-menu-item v-bind:index=btn.name @click="goIndex(index, btn.id)"
              :class="nactive==index?'left_ul_active':''">
              {{btn.name}}</el-menu-item>
          </ul>
        </el-submenu>
        <el-menu-item index="2">
          <i class="el-icon-menu"></i>
          <span slot="title">导航二</span>
        </el-menu-item>
        <el-menu-item index="3">
          <i class="el-icon-setting"></i>
          <span slot="title">导航三</span>
        </el-menu-item>
      </el-menu>
    </el-row>
    <div class="div_right">
      <router-view />
    </div>
  </div>
</template>

<script>
  import { getProjectTypes } from '@/services/apiv1'
  export default {
    name: 'App',
    data() {
      return {
        btns: [],
        nactive: 0,
      }
    },
    methods: {
      getTasksList() {
        getProjectTypes().then((res) => {
          this.btns = res.data
        }).catch(function (error) {
          console.log(error);
        });
      },
      goIndex(index, type) {
        this.$router.push({
          name: 'project',
          query: { type: type },
        })
        this.nactive = index
      }
    },
    mounted() {
      this.getTasksList()
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
    /* position: fixed; */
    height: 100%;
  }

  /* #app::after {
    content: ".";
    clear: both;
    display: block;
    font-size: 0;
    height: 0;
  }

  #app {
    zoom: 1;
  } */

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
    border: none;
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
    background: #ecf5ff;
    color: #409eff;
  }

  .bread {
    font-weight: bold;
  }

  .right_bread {
    padding: 15px 10px 0px 10px;
  }
</style>