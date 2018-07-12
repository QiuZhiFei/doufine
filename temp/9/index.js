const outerWidth = window.outerWidth;
const scale = outerWidth / 375;

console.log("scale == ", scale);

const viewport = document.getElementById("viewport");
const viewport_content = "width=device-width, maximum-scale=1, initial-scale=" + scale;

viewport.setAttribute("content", viewport_content);


window.onload = function() {
    if (/Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)) {
        this.console.log("mobile");
    } else {
        this.console.log("pc");
    }
};