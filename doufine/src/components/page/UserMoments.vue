<template>
    <div class="root">{{ msg }}</div>
</template>


<script>
export default {
    name: "UserMoments",
    props: {
        msg: String
    }
}
</script>

<style>
.root {
    background: yellow;
    width: 100px;
    height: 100px;
}
</style>

