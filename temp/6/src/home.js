Vue.component('todo-item', {
    props: ['todo'],
    template: '<li> {{ todo.text }} </li>'
})


var app = new Vue({
    el: '#app',
    data: {
        isActive: false,
        message: 'Hello Vue!'
    }
})

var app2 = new Vue({
    el: '#app-2',
    data: {
        message: '页面加载于 ' + new Date().toLocaleString()
    }
})

var app3 = new Vue({
    el: '#app-3',
    data: {
        seen: true
    }
})
1
var app4 = new Vue({
    el: '#app-4',
    data: {
        todos: [
            { text: '1' },
            { text: '2' },
        ]
    }
})

var app5 = new Vue({
    el: '#app-5',
    data: {
        message: 'lolita'
    },
    methods: {
        reverseMessage: function() {
            this.message = "wulala"
        }
    }
})

var app6 = new Vue({
    el: '#app-6',
    data: {
        message: "loli"
    }
})

var app7 = new Vue({
    el: '#app-7',
    data: {
        items: [
            { id: 0, text: '0' },
            { id: 1, text: '1' },
            { id: 2, text: '2' }
        ]
    }
})