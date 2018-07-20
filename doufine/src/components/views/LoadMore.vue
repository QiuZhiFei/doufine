<template>
    <div class="load-more-root">
        <div class="grid-row">
            <div class="col">
                <ul class="loading">
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>

            </div>
        </div>
    </div>
</template>


<script>
export default {
    name: "LoadMore"
}
</script>


<style>
.load-more-root {
    width: 100%;
    height: 100%;
    /* height: 100px; */
    /* width: 1000px; */
    /* height: 1000px; */
    /* background: gray; */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.loading {
    list-style: none;
    margin: 0;
    padding: 0;
    position: absolute;
    /* top: 50%; */
    /* left: 50%; */
    -webkit-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    font-size: 0;
}

.loading.reversed li {
    border: 3px solid white;
    -webkit-animation: LOADINGREV 2s infinite;
    animation: LOADINGREV 2s infinite;
}

.loading.reversed li:nth-child(1n) {
    -webkit-animation-delay: 0s;
    animation-delay: 0s;
}

.loading.reversed li:nth-child(2n) {
    -webkit-animation-delay: 0.2s;
    animation-delay: 0.2s;
}

.loading.reversed li:nth-child(3n) {
    -webkit-animation-delay: 0.4s;
    animation-delay: 0.4s;
}

.loading li {
    height: 0;
    position: absolute;
    top: 50%;
    left: 0;
    width: 0;
    margin: 0;
    height: 10px;
    width: 10px;
    border: 3px solid #2b8ccd;
    border-radius: 100%;
    -webkit-transform: transformZ(0);
    transform: transformZ(0);
    -webkit-animation: LOADING 2s infinite;
    animation: LOADING 2s infinite;
}

.loading li:nth-child(1n) {
    left: -20px;
    -webkit-animation-delay: 0s;
    animation-delay: 0s;
}

.loading li:nth-child(2n) {
    left: 0;
    -webkit-animation-delay: 0.2s;
    animation-delay: 0.2s;
}

.loading li:nth-child(3n) {
    left: 20px;
    -webkit-animation-delay: 0.4s;
    animation-delay: 0.4s;
}

.grid-row:after {
    content: '';
    display: table;
    clear: both;
}

.grid-row {
    width: 100%;
    height: 100%;
}

.grid-row .col {
    /* position: absolute; */
    /* top: 0;
    left: 0;
    bottom: 0; */
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.grid-row .col+.col {
    background: #2b8ccd;
    left: auto;
    right: 0;
}

@-webkit-keyframes LOADING {
    0% {
        -webkit-transform: scale(0.5);
        transform: scale(0.5);
        background: #2b8ccd;
    }
    50% {
        -webkit-transform: scale(0.60);
        transform: scale(0.60);
        background: white;
    }
    100% {
        -webkit-transform: scale(0.5);
        transform: scale(0.5);
        background: #2b8ccd;
    }
}

@keyframes LOADING {
    0% {
        -webkit-transform: scale(0.5);
        transform: scale(0.5);
        background: #2b8ccd;
    }
    50% {
        -webkit-transform: scale(0.60);
        transform: scale(0.60);
        background: white;
    }
    100% {
        -webkit-transform: scale(0.5);
        transform: scale(0.5);
        background: #2b8ccd;
    }
}

@-webkit-keyframes LOADINGREV {
    0% {
        -webkit-transform: scale(0.5);
        transform: scale(0.5);
        background: white;
    }
    50% {
        -webkit-transform: scale(0.60);
        transform: scale(0.60);
        background: #2b8ccd;
    }
    100% {
        -webkit-transform: scale(0.5);
        transform: scale(0.5);
        background: white;
    }
}

@keyframes LOADINGREV {
    0% {
        -webkit-transform: scale(0.5);
        transform: scale(0.5);
        background: white;
    }
    50% {
        -webkit-transform: scale(0.60);
        transform: scale(0.60);
        background: #2b8ccd;
    }
    100% {
        -webkit-transform: scale(0.5);
        transform: scale(0.5);
        background: white;
    }
}
</style>
