let i = 0,
    probtn = document.querySelector("#probtn"),
    producbtn = document.querySelector("#producbtn"),
    mystoreBtn = document.getElementById('mystoreBtn'),
    /*not buttons*/
    sections = document.getElementById('section'),
    searchcover = document.getElementById("searchcover"),
    profile = document.querySelector("#profile"),
    mystore = document.getElementById("mystore"),
    product = document.getElementById("products"),
    viewpost = document.getElementById('viewpost'),
    apimyStore = document.getElementById('apimyStore'),
    wrapper = document.getElementById('wrapper'),
    img = [],
    productSpec = document.querySelector('.productSpec');

img[0] = document.getElementById('img1')
img[1] = document.getElementById('img2')
img[2] = document.getElementById('img3')


function callslide() {
    let header = document.getElementById('header'),
        h1 = document.getElementsByClassName('h1');

    if (i == 0) {
        header.src = img[0].src;
        i = 1
        h1[0].style.opacity = 1
    } else if (i == 1) {
        header.src = img[1].src;
        i = 2
        h1[0].style.opacity = 0

    } else {
        header.src = img[2].src;
        i = 0
        h1[0].style.opacity = 0

    }
    setTimeout("callslide()", 9000)
}

function displayRemove() {
    profile.style.opacity = 0
    profile.style.zIndex = -2
    product.style.opacity = 0
    product.style.zIndex = -3
    viewpost.style.opacity = 0;
    viewpost.style.zIndex = -3
    apimyStore.style.opacity = 0
    apimyStore.style.zIndex = -4
    mystore.style.opacity = 0
    mystore.style.zIndex = -4
    section.style.display = 'none'
    searchcover.style.display = "none"
    productSpec.style.zIndex = -5
    productSpec.style.opacity = 0
}

function homebt() {
    profile.style.opacity = 0
    profile.style.zIndex = -2
    section.style.display = 'none'

}


function secdisplay() {
    let section = document.getElementById('section');
    section.style.display = 'block'
}

function closesearch() {
    searchcover.style.zIndex = -4;
    searchcover.style.opacity = 0;
    document.getElementById('searchcover').innerHTML = ""

}

function closespec() {
    productSpec.style.zIndex = -5
    productSpec.style.opacity = 0
}

function closemsgDisplay() {
    document.getElementById('msgDisplay').style.zIndex = -5
    document.getElementById('msgDisplay').style.display = 'none'
}

function enter() {
    let searchbox = document.getElementById("searchinput");
    let submitttsearch = document.getElementById("submitttsearch");
    searchbox.addEventListener('keyup', (event) => {
        if (event.target.value.length > 0) {
            switch (event.keyCode) {
                case 13:
                    submitttsearch.click()
                    break;
            }
        }
    })
}