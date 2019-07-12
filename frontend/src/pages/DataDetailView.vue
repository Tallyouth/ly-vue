<template>
    <div class="data_all">
        <div class="data">
            <div class="search">
                <el-select v-model="selectV" filterable placeholder="请选择">
                    <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
                    </el-option>
                </el-select>
                <el-button type="primary" icon="el-icon-search" @click="Getchart">搜索</el-button>
            </div>
            <div class="data_detail">
                <el-tabs v-model="activeName" @tab-click="handleClick">
                    <el-tab-pane label="数据库信息" name="first">数据库信息</el-tab-pane>
                    <el-tab-pane label="字段信息" name="second">字段信息</el-tab-pane>
                    <el-tab-pane label="数据预览" name="third">
                        <table border="1">
                            <tr>
                                <th>Month</th>
                                <th>Savings</th>
                            </tr>
                            <tr>
                                <td>January</td>
                                <td>$100</td>
                            </tr>
                        </table>
                    </el-tab-pane>
                    <el-tab-pane label="其他信息" name="fourth">暂无</el-tab-pane>
                </el-tabs>
            </div>
        </div>
        <div class="chart">
            <ve-line :data="chartData"></ve-line>
        </div>
    </div>
</template>


<script>
    import { getOptions } from '@/services/apiv1'
    export default {
        data() {
            return {
                chartData: {

                    columns: ['日期', '访问用户'],
                    rows: [
                        { '日期': '1/1', '访问用户': 1393, '下单用户': 1093, '下单率': 0.32 },
                    ]
                },
                options: '',
                selectV: '',
                activeName: ''
            };
        },
        methods: {
            getSelect() {
                getOptions().then((res) => {
                    this.options = res.data.data
                }).catch(function (error) {
                    console.log(error);
                });
            },
            handleClick() {
                return ''
            },
            Getchart(){
                console.log(this.selectV)
            }
        },
        mounted() {
            this.getSelect()
        },
    };
</script>

<style>
    .data {
        display: flex;
    }

    .search {
        margin: 5%;
        margin-left: 7%;
        display: flex
    }

    .chart {
        width: 30%;
        margin-top: 2%;
        margin-left: 5%;
    }

    .data_detail {
        width: 45%;
        margin-top: 4%;
        margin-left: 15%;
    }
</style>