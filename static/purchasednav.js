let i = 0,
    probtn = document.querySelector("#probtn"),
    producbtn = document.querySelector("#producbtn"),
    mystoreBtn = document.getElementById('mystoreBtn'),
    togglemenu = document.getElementById('toggle-menu'),

    /*not buttons*/

    sections = document.getElementById('section'),
    searchcover = document.getElementById("searchcover"),
    profile = document.querySelector("#profile"),
    mystore = document.getElementById("mystore"),
    product = document.getElementById("products"),
    viewpost = document.getElementById('viewpost'),
    apimyStore = document.getElementById('apimyStore'),
    topsearch = document.getElementById('topsearch'),
    header = document.getElementById('header'),
    productSpec = document.querySelector('.productSpec');


let docs = document.documentElement;
let recom_i = 0;
let recom_ii = 0;
let recommends = [];

recommends[0] = document.getElementById('img1')
recommends[1] = document.getElementById('img2')



function clearREcommend() {
    document.getElementById('suggestions').style.opacity = '0'
    document.getElementById('topsellers').style.opacity = '0'
    document.getElementById('topsellers').style.transform = 'translateY(0px)'
    document.getElementById('advertTp').style.opacity = '0'
    document.getElementById('advertTp').style.transform = 'translateY(0px)'
}

function callrecomend() {
    if (recom_i <= 2) {
        if (recom_i == 0) {
            clearREcommend()
            let suggested = document.getElementById('suggestions');
            suggested.style.opacity = 1
            recom_i++

        } else if (recom_i == 1) {

            clearREcommend()
            let suggested = document.getElementById('topsellers');
            suggested.style.opacity = 1
            suggested.style.transform = 'translateY(-180px)'
            recom_i++

        } else {

            clearREcommend()
            let suggested = document.getElementById('advertTp');
            suggested.style.opacity = 1
            suggested.style.transform = 'translateY(-370px)'
            document.advertTpImg.src = recommends[recom_ii].src
            if (recom_ii >= recommends.length - 1) {
                recom_ii = 0
            } else {
                recom_ii++
            }
            recom_i = 0
        }
    }
    setTimeout("callrecomend()", 10000)
}

function displayRemove() {
    header.style.opacity = 0
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
    productSpec.style.display = 'none'
    topsearch.style.opacity = 0
    topsearch.style.zIndex = -1
    wrapone.style.opacity = 0
    wrapone.style.zIndex = -2
    navbarlinks.style.transform = 'translateX(-100%)'
}

function homebt() {
    let homebt2 = document.querySelector("#homebt2");
    let header = document.getElementById('header');
    let loginview = document.querySelector('.loginview');
    remover()
    displayRemove()

    header.style.opacity = 1
    homebt2.classList.add('active')
    header.style.backgroundColor = 'rgb(0, 255, 76)'
    wrapone.style.opacity = 1
    wrapone.style.zIndex = 1
    topsearch.style.opacity = 1
    topsearch.style.zIndex = 1

    if (loginview) {
        loginview.style.display = 'block'
    }
}

function secdisplay() {
    let createacct = document.getElementById('createacct');
    let section = document.getElementById('section');
    let loginview = document.querySelector('.loginview');
    let header = document.getElementById('header');

    remover()
    displayRemove()


    header.style.opacity = 1
    section.style.display = 'block'
    createacct.classList.add('active')
    loginview.style.display = 'none'

    let value = {
        section: 'section',
        createacct: 'createacct'
    }

    localStorage = window.localStorage.setItem('sectionData', JSON.stringify(value))
}

function remover() {
    let navs2 = [...document.querySelectorAll("#navbarlinks li a")];
    navs2.forEach(nav => nav.classList.remove('active'))
}

function closesearch() {
    searchcover.style.transform = 'translateY(-120vh)'
    document.getElementById('searchcover').innerHTML = ""
}

function closemsgDisplay() {
    document.getElementById('msgDisplay').style.zIndex = -5
    document.getElementById('msgDisplay').style.display = 'none'
}

togglemenu.addEventListener('click', function() {
    let navbarlinks = document.getElementById('navbarlinks');
    navbarlinks.style.opacity = 1

    if (navbarlinks.style.transform = 'translateX(-100%)') {
        navbarlinks.style.transform = 'translateX(0px)'
    } else {
        navbarlinks.style.transform = 'translateX(-100%)'
    }

})


function enter() {
    let searchbox = document.getElementById("searchbox");
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

function closespec() {
    let product_spec = document.getElementById('productSpec');
    product_spec.style.display = 'none'
}