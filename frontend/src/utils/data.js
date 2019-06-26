const p = (s) => s < 10 ? '0' + s : s
export function formatDate (date) {
    date = p(date.getFullYear()) + '-' + p((date.getMonth() + 1)) + '-' + p(date.getDate()) + ' ' + p(date.getHours()) + ':' + p(date.getMinutes()) + ':' + p(date.getSeconds())
    return date
}