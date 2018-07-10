const content = new Vue({
    el: "#content",
    created: function() {
        // console.log("create")
    },
    mounted: function() {
        // console.log("mounted", this.page);
        this.fetchData(this.page);
    },
    data: {
        items: [],
        page: 1,
        isLoading: false,
    },
    methods: {
        loadMore: function() {
            console.log("load more");
            const page = this.page + 1;
            this.fetchData(page);
        },
        fetchData: function(page) {
            if (this.isLoading) {
                console.log("return");
                return;
            }

            const _this = this;
            // Vue.set(content, 'isLoading', true);
            this.isLoading = true;

            // fetch('http://140.143.239.212:5000/user/moments')
            const url = 'http://192.168.3.21:5000/user/moments?p=' + page;

            fetch(url)
                .then(function(response) {
                    return response.json();
                })
                .then(function(data) {
                    Vue.set(content, 'isLoading', false);
                    Vue.set(content, 'page', page);

                    const items = data.items;
                    let result = _this.items || [];
                    result.push.apply(result, items);
                    Vue.set(content, 'items', result);
                });
        },
    }
})

window.onload = function() {
    console.log("onload")
}