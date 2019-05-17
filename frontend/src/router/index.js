import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/MainBase'
import VueResource from 'vue-resource'

Vue.use(Router)

const first = {template: '<div><h2>1</h2></div>'}
const second = {template: '<h2>2</h2>'}

export default new Router({

  routes: [
    {
      path: '/1',
      name: 'HelloWorld',
      component: first
    },
    {
      path: '/2',
      component: second
    },
    {
      path: '/',
      component: HelloWorld
    }
  ]
})
