import Vue from 'vue'
import Router from 'vue-router'
import TableCrawle from '@/components/TableCrawle'
import DataAllView from '@/pages/DataAllView'
import DataDetailView from '@/pages/DataDetailView'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/project',
      name: 'project',
      component: TableCrawle
    },
    {
      path: '/',
      name: 'project',
      component: TableCrawle
    },
    {
      path: '/data/all',
      name: 'DataAllView',
      component: DataAllView
    },
    {
      path: '/data/detail',
      name: 'DataDetailView',
      component: DataDetailView
    },
  ]
})
