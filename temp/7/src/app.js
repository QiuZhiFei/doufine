const content = new Vue({
    el: "#content",
    created: function() {
        // console.log("create")
    },
    mounted: function() {
        // console.log("mounted")
        // fetch('http://140.143.239.212:5000/user/moments')
        fetch('http://192.168.3.21:5000/user/moments')
            .then(function(response) {
                return response.json();
            })
            .then(function(data) {
                const items = data.items;
                Vue.set(content, 'items', items);
            });
    },
    data: {
        items: []
    }
})

window.onload = function() {
    console.log("onload")
}