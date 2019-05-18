<template>
  <div id="app">
    <div class="div_left">
      <ul class="left_ul"
        v-for="(btn,index) in btns"
        :key="index">
        <li @click="goIndex(index)" :class="nactive==index?'left_ul_active':''">{{btn}}</li>
      </ul>
    </div>
    <div class="div_right">
      <p class="right_bread"><span class="bread">首页</span> / <span class="bread">项目</span> / {{bread}}</p>
      <router-view />
    </div>

  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      btns: ['页面1', '页面2', '页面2'],
      nactive:0,
      bread:'页面1'
    }
  },
  methods: {
    goIndex (index) {
      console.log(index)
      switch (index) {
        case 0:
          this.$router.push('/')
          this.nactive = 0
          this.bread = '页面1'
          break
        case 1:
          this.$router.push('/1')
          this.nactive = 1
            this.bread = '页面2'
          break
        case 2:
          this.$router.push('/2')
          this.nactive = 2
            this.bread = '页面3'
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
  height:100%;
}
#app > div {
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
}
.left_ul_active {
  background: lightblue;
  color: blue;
}
.bread {
  font-weight: bold;
}
.right_bread {
  padding: 15px 10px 0px 10px;
}
</style>
