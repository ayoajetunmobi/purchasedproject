let i = 0,
    probtn = document.querySelector("#probtn"),
    producbtn = document.querySelector("#producbtn"),
    mystoreBtn = document.getElementById('mystoreBtn'),
    /*not buttons*/
    searchcover = document.getElementById("searchcover"),
    profile = document.querySelector("#profile"),
    mystore = document.getElementById("mystore"),
    product = document.getElementById("products"),
    viewpost = document.getElementById('viewpost'),
    apimyStore = document.getElementById('apimyStore'),
    wrapper = document.getElementById('wrapper'),
    img = [],
    productSpec = document.querySelector('.productSpec'),
    closesidebar = document.getElementById("closesidebar"),
    opensidebar = document.getElementById("opensidebar");

img[0] = document.getElementById('img1')
img[1] = document.getElementById('img2')
img[2] = document.getElementById('img3')


function callslide() {
    let header = document.getElementById('header');

    if (i == 0) {
        header.src = img[0].src;
        i = 1

    } else if (i == 1) {
        header.src = img[1].src;
        i = 2

    } else {
        header.src = img[2].src;
        i = 0

    }
    setTimeout("callslide()", 2000)
}

function displayRemove() {
    profile.style.display = 'none'
    product.style.opacity = 0
    product.style.zIndex = -3
    viewpost.style.opacity = 0;
    viewpost.style.zIndex = -3
    apimyStore.style.opacity = 0
    apimyStore.style.zIndex = -4
    productSpec.style.display = 'none'
}

function homebt() {
    profile.style.display = 'none'

}

function spinner() {
    let spinnerdiv = document.getElementById('spinnerdiv');
    spinnerdiv.style.display = 'block';
}

function closespinner() {
    let spinnerdiv = document.getElementById('spinnerdiv');
    spinnerdiv.style.display = 'none';
}

function closesearch() {
    searchcover.style.display = 'none';
    document.getElementById('searchcover').innerHTML = ""

}

function closespec() {
    productSpec.style.display = 'none'
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
closesidebar.addEventListener('click', () => {
    let sidebar = document.querySelector('.sidebar'),
        body = document.getElementById("body");
    sidebar.style.left = "-80%"
    body.style.left = "0%"
})
opensidebar.addEventListener('click', () => {
    let body = document.getElementById("body"),
        sidebar = document.querySelector('.sidebar');
    body.style.left = "50%"
    sidebar.style.left = "-20%"
})