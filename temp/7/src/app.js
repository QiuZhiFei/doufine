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
        items: [],
        items1: [{
                title: "title",
                url: "https://source.unsplash.com/900x920"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/820x900"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/500x500"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/550x520"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/660x630"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/700x770"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/880x820"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/898x820"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/8998x920"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/898x960"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/999x888"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/1000x777"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/2000x777"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/2000x1000"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/3000x1000"
            },
            {
                title: "title",
                url: "https://source.unsplash.com/9000x9000"
            },
        ]
    }
})

window.onload = function() {
    console.log("onload")
}