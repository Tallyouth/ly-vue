<template>
    <div class="data">
        <div class="ldata">
            <ve-pie :data="chartData" :settings="chartSettings"></ve-pie>
            <div class="title">
                <p align="center">总数据占比
                </p>
            </div>
        </div>
        <div class="rdata">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span>数据预览</span>
                </div>
                <div class="text item">数据库类型: Mongodb</div>
                <div class="text item">总项目数: {{ chartData.totalcollection }}</div>
                <div class="text item">总数据量: {{ chartData.totaldata }}</div>
                <div class="text item">当前时间: {{ chartData.Nowdate }}</div>
            </el-card>
        </div>
    </div>
</template>

<script>
    import { getDB } from '@/services/apiv1'
    import { getNowFormatDate } from '@/utils/data'
    export default {
        name: 'DateView',
        data() {
            this.chartSettings = {
                dimension: 'collection',
                limitShowNum: 10
            }
            return {
                chartData: {
                    columns: ['collection', 'count'],
                    rows: [],
                    totalcollection: '',
                    totaldata: '',
                    Nowdate: getNowFormatDate()
                }
            }
        },
        methods: {
            getDBdata() {
                getDB().then((res) => {
                    this.chartData.rows = res.data.data.school
                    this.chartData.totalcollection = this.chartData.rows.length
                    for (var i=0, number=0, len=this.chartData.rows.length; i<len; i++) {
                        number += this.chartData.rows[i].count
                    }
                    this.chartData.totaldata = number
                }).catch(function (error) {
                    console.log(error);
                });
            },
        },
        mounted() {
            this.getDBdata()
        },
    }
</script>

<style>
    .data {
        display: flex
    }

    .ldata {
        width: 60%;
        margin: 8% 0 0 5%;
    }

    .rdata {
        width: 40%;
        margin: 8% 0 0 5%;
    }

    .text {
        font-size: 14px;
    }

    .item {
        margin-bottom: 18px;
    }

    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }

    .clearfix:after {
        clear: both
    }

    .box-card {
        width: 250px;
    }

    .title p {
        margin: 0%;

    }
</style>