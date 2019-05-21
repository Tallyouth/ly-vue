<template>
  <div class="hello">
    <!-- 头部搜索 -->
    <div class="com_head">
      <el-row>
        <el-col :span="6">
          <div class="demo-input-suffix">
            <el-input v-model="nname" placeholder="请输入姓名" size="medium"></el-input>
          </div>
        </el-col>
        <el-col :span="2">

        </el-col>
        <el-col :span="8">
          <div class="demo-input-suffix">
            <el-input placeholder="请输入日期" size="medium" prefix-icon="el-icon-date" v-model="ndate">
            </el-input>
          </div>
        </el-col>
        <el-col :span="2">

        </el-col>
        <el-col :span="5">
          <el-button type="primary" size="medium">搜索</el-button>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data() {
      return {
      }
    },
    methods: {

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .hello {
    padding: 0px 10px;
  }
</style>


<style scoped>
  .hello {
    padding: 0px 10px;
  }

  .com_head {
    background: lightgray;
    padding: 15px 10px;
    margin: 30px 0;
    border-radius: 3px;
  }
</style>