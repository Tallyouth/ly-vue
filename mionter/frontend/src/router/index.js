import Vue from 'vue'
import Router from 'vue-router'
import TableCrawle from '@/components/TableCrawle'
import ItemDetailPage from '@/pages/ItemDetailPage'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'TableCrawle',
      component: TableCrawle
    },
    {
      path: '/1',
      name: 'ItemDetailPaged',
      component: ItemDetailPage
    },
  ]
})
