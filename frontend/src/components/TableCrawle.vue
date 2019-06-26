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
      <el-table :data="newTable" stripe style="width: 100%">
        <el-table-column label="名称" width="200">
          <template slot-scope="scope">
            <span style="margin-left: 5px">{{ scope.row.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="描述" width="200">
          <template slot-scope="scope">
            <span style="margin-left: 5px">{{ scope.row.desc }}</span>
          </template>
        </el-table-column>
        <el-table-column label="状态" width="200">
          <template slot-scope="scope">
            <span :class="scope.row.statu==1?'el-icon-success':'el-icon-error'" style="margin-left: 5px"></span>
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
            <el-button size="mini" @click="dialogFormVisible = true; handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button size="mini" plain type="success" @click="startPro(scope.$index, scope.row)">
              开始</el-button>
            <el-dialog title="项目介绍" :visible.sync="dialogFormVisible" width="30%">
              <el-form :model="form">
                <el-form-item label="名称" :label-width="formLabelWidth">
                  <el-input v-model="form.name" style="max-width: 70%"></el-input>
                </el-form-item>
                <el-form-item label="描述" :label-width="formLabelWidth">
                  <el-input v-model="form.desc" style="max-width: 70%"></el-input>
                </el-form-item>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">取 消</el-button>
                <el-button type="primary" @click="dialogFormVisible = false; projectEdit()">确 定</el-button>
              </div>
            </el-dialog>
            <el-button size="mini" type="danger" @click="stopPro(scope.$index, scope.row)">停止</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div class="block">
      <el-pagination layout="prev, pager, next" :total="50">
      </el-pagination>
    </div>
  </div>
</template>

<script>
  import { getProjectList, updateProject } from '@/services/apiv1'
  import { formatDate } from '@/utils/data'
  import { getCookie } from '@/utils/cookie'
  export default {
    name: 'TableCrawle',
    data() {
      return {
        nname: '',
        ndate: '',
        tableData: [],
        typeId: this.$route.query.type,
        dialogFormVisible: false,
        form: {
          name: '',
          desc: '',
          id: ''
        },
        formLabelWidth: '50px'
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
        getProjectList(!this.typeId ? 1 : this.typeId).then((res) => {
          this.tableData = res.data
        }).catch(function (error) {
          console.log(error);
        });
      },
      handleEdit(index, row) {
        this.form.name = row.name
        this.form.desc = row.desc
        this.form.id = row.id
      },
      startPro(index, row) {
        if (this.notifyInstance) {
          this.notifyInstance.close();
        }
        this.notifyInstance = this.$notify({
          title: '成功',
          message: '爬虫启动成功',
          type: 'success'
        });
      },
      stopPro(index, row) {
        if (this.notifyInstance) {
          this.notifyInstance.close();
        }
        this.notifyInstance = this.$notify({
          title: '成功',
          message: '爬虫停止成功',
          type: 'success'
        });
      },
      projectEdit() {
        let projectId = this.form.id
        let itemInfo = {
          name: this.form.name,
          desc: this.form.desc,
          id: this.form.id
        }
        var csrftoken = getCookie('csrftoken');
        console.log(csrftoken)
        updateProject(projectId, itemInfo, csrftoken).then((res) => {
          getProjectList(!this.typeId ? 1 : this.typeId).then((res) => {
            this.tableData = res.data
          }).catch(function (error) {
            console.log(error);
          });
        }).catch(function (error) {
          console.log(error);
        });
      },
    },
    computed: {
      newTable() {
        return this.tableData.filter((ndata) => {
          return ndata.name.match(this.nname) && ndata.updated_at.match(this.ndate)
        })
      }
    },
    watch: {
      // 利用watch方法检测路由变化：
      '$route': function (to, from) {
        this.typeId = to.query.type
        this.getTasksList()
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
    height: 100%;
    max-height: 100%;
  }

  .com_head {
    background: lightgray;
    padding: 15px 10px;
    margin: 30px 0;
    border-radius: 3px;
    position: 2%;
  }

  .el-icon-success {
    color: rgb(17, 221, 95);
  }

  .el-icon-error {
    color: rgb(240, 14, 14);
  }
</style>