<template>
    <div class="root">
        <div class="header">
        </div>
        <div id="content" class="content">
            <!-- <div class="content-container" v-infinite-scroll="loadMore"> -->
            <div class="content-container">
                <div class="item" v-for="item in items" v-on:click.stop="handleItemClick(item)" :style="{backgroundImage:`url(${item.original_pic})`, color: `#fff`}">
                    <div class="dete-container">
                        {{ item.created_at }}
                    </div>
                    <div class="des-container">
                        <div>
                            {{ item.text }}
                        </div>
                    </div>
                    <div class="logo-container">
                        <!-- <h4> A </h4> -->
                        <div>
                            {{ item.title }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import Vue from "vue"
import infiniteScroll from "vue-infinite-scroll"

export default {
  name: "UserMoments",
  component: {
    infiniteScroll
  },
  props: {
    items: {
      type: Array,
      default: function() {
        return [];
      }
    },
    page: {
      type: Number,
      default: 1
    },
    isLoading: {
      type: Boolean,
      default: false
    }
  },
  mounted: function() {
    console.log("mounted", this.page);
    this.fetchData(this.page);
  },
  methods: {
    handleItemClick: function(item) {
      console.log("click", item);
      window.open(item.scheme);
    },
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
      Vue.set(content, 'isLoading', true);

      const url = "http://140.143.239.212:5000/user/moments?p=" + page;
      // const url = 'http://192.168.3.21:5000/user/moments?p=' + page;

      fetch(url)
        .then(function(response) {
          return response.json();
        })
        .then(function(data) {
          Vue.set(content, "isLoading", false);
          Vue.set(content, "page", page);

          const items = data.items;
          let result = _this.items || [];
          result.push.apply(result, items);
          Vue.set(content, "items", result);
        });
    }
  }
};
</script>

<style>
.content {
    width: 100%;
    height: 100%;
}

.content-container {
    width: 100%;
    height: 100%;
    display: flex;
    flex-wrap: wrap;
}

.content-container .item {
    width: 290px;
    height: 390px;
    margin: 12px;
    /* overflow: hidden; */
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 3px;
    -webkit-transition: 200ms ease-in-out;
    -o-transition: 200ms ease-in-out;
    transition: 200ms ease-in-out;
    -webkit-box-shadow: 0 0 5px rgba(0, 0, 0, 0.7);
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.7);
    text-decoration: none;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
}

.content-container .item:hover {
    -webkit-box-shadow: 0 0 15px rgba(0, 0, 0, 0.7);
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.7);
}

.content-container .item .dete-container {
    width: 100%;
    height: 22px;
    margin: 22px 0;
    color: #fff;
    text-align: center;
    text-shadow: 0 0 3px rgba(0, 0, 0, 0.9);
}

.content-container .item .des-container {
    width: 100%;
    background: rgba(0, 0, 0, 0.8);
    height: 96px;
    margin-top: 81px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.content-container .item .des-container div {
    padding: 20px;
}

.content-container .item .logo-container {
    position: relative;
    margin-top: 60px;
    width: 80px;
    height: 80px;
    border-radius: 40px;
    /* width: 80px;
    height: 80px;
    position: relative;
    border-radius: 100px;
    margin: 85px auto; */
    /*  */
    background: #2b5876;
    /* fallback for old browsers */
    background: -webkit-linear-gradient(to right, #4e4376, #2b5876);
    /* Chrome 10-25, Safari 5.1-6 */
    background: -webkit-gradient(linear, left top, right top, from(#4e4376), to(#2b5876));
    background: -webkit-linear-gradient(left, #4e4376, #2b5876);
    background: -o-linear-gradient(left, #4e4376, #2b5876);
    background: linear-gradient(to right, #4e4376, #2b5876);
    /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    -webkit-box-shadow: 0 0 20px darkblue;
    box-shadow: 0 0 20px darkblue;
    /* background: #2b5876;
    box-shadow: 0 0 20px #2b5876; */
    /* background: #f857a6; */
    /* box-shadow: 0 0 20px #f857a6; */
    display: flex;
    align-items: center;
    text-align: center;
    justify-content: center;
}

.content-container .item .logo-container h4 {
    color: #fff;
    font-size: 40px;
    text-align: center;
    font-weight: 100;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    /* top: 16px; */
}
</style>

