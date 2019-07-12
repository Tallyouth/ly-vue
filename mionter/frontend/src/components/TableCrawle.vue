<template>
  <div class="hello">
    <!-- 头部搜索 -->
    <div class="com_head">
      <el-row>
        <el-col :span="6">
          <div class="demo-input-suffix">
            <el-input v-model="nname" placeholder="请输入名称" size="medium"></el-input>
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
    <!-- 表格 -->
    <div>
      <el-table :data="newTable" style="width: 100%">
        <el-table-column label="名称" width="200">
          <template slot-scope="scope">
            <span style="margin-left: 5px">{{ scope.row.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="类型" width="200">
            <template slot-scope="scope">
              <span style="margin-left: 5px">{{ scope.row.name }}</span>
            </template>
          </el-table-column>
          <el-table-column label="状态" width="200">
              <template slot-scope="scope">
                <span style="margin-left: 5px">{{ scope.row.name }}</span>
              </template>
            </el-table-column>
          <el-table-column label="日期" width="200">
              <template slot-scope="scope">
                <i class="el-icon-time"></i>
                <span style="margin-left: 10px">{{ scope.row.updated_at | formatDate }}</span>
              </template>
            </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
  import { getProjectTypes } from '@/services/apiv1'
  import { formatDate } from '@/utils/data'
  export default {
    name: 'TableCrawle',
    data() {
      return {
        nname: '',
        ndate: '',
        tableData: []
      }
    },
    filters: {
      formatDate(time) {
        let date = new Date(time)
        return formatDate(date)
      }
    },
    methods: {
      getTasksList() {
        getProjectTypes().then((res) => {
          this.tableData = res.data
        }).catch(function (error) {
          console.log(error);
        });
      },
      handleEdit(index, row) {
        //console.log(index, row);
      },
      handleDelete(index, row) {
        //console.log(index, row);
      }
    },
    computed: {
      newTable() {
        return this.tableData.filter((ndata) => {
          return ndata.name.match(this.nname) && ndata.updated_at.match(this.ndate)
        })
      }
    },
    mounted() {
      this.getTasksList()
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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