<template>
  <p>欢迎使用</p>
</template>

<script>
    import { getProjectTypes } from '@/services/apiv1'
    export default {
      name: 'TableCrawle',
      data() {
        return {
          data: '',
        }
      },
    }
  </script>
