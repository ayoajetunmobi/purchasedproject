function propicture(event) {
    var elem = event.target,
        elemID = elem.getAttribute('id'),
        bigpropic = document.getElementById('bigpropic'),
        bigoverlay = document.getElementById("bigpic-overlay"),
        newImg = new Image();


    // If we click an element with the attribute "bigpic", show a bigger bigpicture
    if (elem.hasAttribute('bigpic')) {
        event.preventDefault();

        newImg.onload = function() {
            bigpropic.src = this.src
        }
        bigpropic.src = '';
        newImg.src = elem.getAttribute('bigpic');
        bigoverlay.classList.add('visible');
    }
    // If we click any of these 2 elements, close the lightbox
    if (elemID == 'bigpropic' || elemID == 'bigpic-overlay') {
        event.preventDefault();

        bigoverlay.classList.remove('visible');
    }
}

function viewmore(event) {
    let viewpost = document.getElementById('viewpost');

    displayRemove()
    viewpost.style.opacity = 1;
    viewpost.style.zIndex = 3;
}

function producappear() {
    displayRemove()
    product.style.zIndex = 3
    product.style.opacity = 1
}

function disapp() {
    let viewmore = document.getElementById('viewpost'),
        profile = document.getElementById('profile'),
        product = document.getElementById('products');

    viewmore.style.opacity = 0;
    viewmore.style.zIndex = -3;
    product.style.opacity = 0;
    product.style.zIndex = -3;
    profile.style.zIndex = 2;
    profile.style.display = 'block';
    apimyStore.style.zIndex = -4
    apimyStore.style.opacity = 0
}

function myclick() {
    let image = document.getElementById('image');
    let newinput = document.createElement("input");
    newinput.type = "file"
    newinput.name = "images"
    newinput.accept = ".jpg, .JPG, .png, .PNG"
    let br = document.createElement("br")
    image.appendChild(newinput)
    image.appendChild(br)
}

function mysetting() {
    let settings = document.getElementById("settings");
    settings.style.display = "block"
}

function apimyStoreDispay() {
    let apimyStore = document.getElementById("apimyStore");

    apimyStore.style.opacity = 1
    apimyStore.style.zIndex = 4
}

/**my store functionality */
let advertBtn = document.getElementById("advertBtn"),
    msgBtn = document.getElementById("msgBtn"),
    reportbugBtn = document.getElementById("reportbugBtn"),
    reportusaBtn = document.getElementById("reportusaBtn"),
    termscdBtn = document.getElementById("termscdBtn"),
    tipsBtn = document.getElementById("tipsBtn"),
    deactBtn = document.getElementById("deactBtn"),
    cover = document.getElementById('cover');


function getmsg(data) {
    let apimyStore = document.getElementById('apimyStore');
    apimyStoreDispay()
    apimyStore.innerHTML = ""
    apimyStore.innerHTML = `
            <div class="close" style="position: absolute; top:6%">
                <a href="#" id="close" onclick="disapp()"><i style="color: black;" class="fa fa-arrow-left"></i></a>
            </div>
            <h2 style="color:red;letter-spacing:2px;">Purchased ...</h2>
            <br>
          <h3>messages</h3>
    `
    li(data)
}

function li(data) {
    let apimyStore = document.getElementById('apimyStore');
    let i = 0;
    let div = document.createElement('div');
    while (i < data.length) {
        div.innerHTML +=
            `
          <li onclick="displayMsg(this)" msgid=${data[i].id} data="${data[i].message}" Rview = "${data[i].user_to_review}" contacted = ${data[i].contacted} class ="mesageliststyle">${data[i].message.substring(0,30)}  ... </li> <br>
          `
        i++
    }
    return apimyStore.appendChild(div)
}

function displayMsg(elem) {
    let msg = elem.getAttribute('data');
    let contacted = elem.getAttribute('contacted');
    let review = elem.getAttribute('Rview');
    let msgid = elem.getAttribute('msgid');
    let msgDisplay = document.getElementById('msgDisplay');
    let msgplace = document.getElementById('msgplace');
    let reviewplace = document.getElementById('reviewplace');

    msgDisplay.style.display = 'block'
    msgDisplay.style.zIndex = 5

    msgplace.innerHTML = ''
    msgplace.innerHTML = `
    ${msg}
    `
    reviewplace.innerHTML = ''
    reviewplace.innerHTML = `
        <h2>Review User</h2>
            <input id="reviewdata" style="width: 80%; height:40%;" type="text" maxlength="80"><br><br><br>
            <input onclick = "signals(this)" msgid=${msgid} signal = 2 contacted = ${contacted} user_review = ${review} style="width: 80%; height:30px;color:white; border-radius:16px; text-align:center; background-color:green;" type="submit" value="REVIEW">
    `

}

/**delete product functionality */
function dot(e) {
    let ls = [];
    let id = e.getAttribute("data");
    let deleteMsg = [...document.getElementsByClassName("deleteMsg")];
    let del = deleteMsg.find((item) => item.getAttribute("data") == id);
    del.style.display = 'block'
}

function delmsg(e) {
    let data = e.getAttribute('data');
    let del = document.getElementById('delprod');
    del.setAttribute("data", data)
    let marpicDelete = document.getElementById('marpicDelete');
    marpicDelete.style.display = 'block'
    e.style.display = 'none'
}

function closedel() {
    let marpicDelete = document.getElementById('marpicDelete');
    marpicDelete.style.display = 'none'
}

function closesettings() {
    let settings = document.getElementById('settings');
    settings.style.display = 'none'
}

function settingfunc(event) {
    let data = event;

    if (data == 2) {
        settingDiscontrol()
        editpagetofserver.innerHTML =
            `
            <a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> Change Password </h5><br>
            <div style="height: 70%; width:100%">             
                <input id="settingactionInput" type="password" style="width:98%; height:40%; background-color:rgb(255, 255, 255);border:none;" placeholder= "new password">
                <input id="settingactionInput2" type="password" style="width:98%; height:40%; background-color:rgb(255, 255, 255);border:none;" placeholder= "confirm password"">
            </div>
            <br>
            <div style="width: 100%; text-align:center; background-color:#ffffff; border-top:0.3px solid black; color:rgb(255, 0, 0);
            font-weight:700">
                <input type = "submit" value = SUBMIT onclick = "apisettings(2)">
            </div>
            `
        editpagetofserver.style.display = 'block'
    }

    if (data == 3) {
        settingDiscontrol()
        editpagetofserver.innerHTML =
            `
            <a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> Edit About </h5><br>
            <div style="height: 70%; width:100%">             
                <textarea id="settingactionInput" style="width:98%; height:40%; background-color:rgb(255, 255, 255);border:none;" placeholder= "edit about"></textarea>
            </div>
            <br>
            <div style="width: 100%; text-align:center; background-color:#ffffff; border-top:0.3px solid black; color:rgb(255, 0, 0);
                font-weight:700">
               <input type = "submit" value = SUBMIT onclick = "apisettings(3)">
            </div>
            `
        editpagetofserver.style.display = 'block'
    }
    if (data == 4) {
        settingDiscontrol()
        editpagetofserver.innerHTML =
            `
            <a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> Edit Contact </h5><br>
            <div style="height: 70%; width:100%">             
                <input  id="settingactionInput" type = "number" style="width:98%; height:40%; background-color:rgb(255, 255, 255);border:none;" placeholder= "new number">
            </div>
            <br>
            <div style="width: 100%; text-align:center; background-color:#ffffff; border-top:0.3px solid black; color:rgb(255, 0, 0);
                font-weight:700">
               <input type = "submit" value = SUBMIT onclick = "apisettings(4)">
            </div>
            `
        editpagetofserver.style.display = 'block'
    }

    if (data == 5) {
        settingDiscontrol()
        editpagetofserver.innerHTML =
            `
            <a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> Make Suggestion </h5><br>
            <div style="height: 70%; width:100%">             
                <textarea id="settingactionInput" style="width:98%; height:40%; background-color:rgb(255, 255, 255);border:none;" placeholder= "suggest something"></textarea>
            </div>
            <br>
            <div style="width: 100%; text-align:center; background-color:#ffffff; border-top:0.3px solid black; color:rgb(255, 0, 0);
                font-weight:700">
               <input type = "submit" value = SUBMIT onclick = "apisettings(5)">
            </div>
            `
        editpagetofserver.style.display = 'block'
    }
    if (data == 6) {
        settingDiscontrol()
        editpagetofserver.innerHTML =
            `<a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> Report User </h5><br>
            <div style="height: 70%; width:100%"> 
                <textarea id="settingactionInput" style="width:98%; height:40%; background-color:rgb(255, 255, 255);border:none;" placeholder= "culprit username"></textarea>         
                <textarea id="settingactionInput2" style="width:98%; height:40%; background-color:rgb(255, 255, 255);border:none;" placeholder= "report user"></textarea>
            </div>
            <div style="width: 100%; text-align:center; background-color:#ffffff; border-top:0.3px solid black; color:rgb(255, 0, 0);
                font-weight:700">
               <input type = "submit" value = SUBMIT onclick = "apisettings(6)">
            </div>
            <br>
            `
        editpagetofserver.style.display = 'block'
    }
    if (data == 7) {
        settingDiscontrol()
        editpagetofserver.innerHTML =
            `
            <a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> Terms and Conditions </h5><br>
            <h6> shopatpurchased is a product that looks to shorten the bridge between buyers and 
            sellers around LASU.
            It is aimed at giving more preference to student enterpreneurs. We try to encourage them
            by getting your products out to potential buyers.
            we are doing our best to keep the platform safe, clearly read the tips to succed and stay safe as
            we would not be held responsible for any damages after user has been contacted. </h6>
            `
        editpagetofserver.style.display = 'block'
    }

    if (data == 9) {
        settingDiscontrol()

        editpagetofserver.innerHTML =
            `
            <a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> Deactive Account </h5><br>
            <div style="height: 70%; width:100%">             
                <textarea id="settingactionInput" style="width:98%; height:40%; background-color:rgb(255, 255, 255);border:none;" placeholder= "why are you deactivating your account"></textarea>
            </div>
            <br>
            <div style="width: 100%; text-align:center; background-color:#ffffff; border-top:0.3px solid black; color:rgb(255, 0, 0);
                font-weight:700">
               <input type = "submit" value = SUBMIT onclick = "apisettings(9)">
            </div>
            `
        editpagetofserver.style.display = 'block'
    }


}

function settingDiscontrol() {

    let settingsList = document.querySelector('.settingsList');
    let settingsHeader = document.querySelector('.settingsHeader');
    let editpagetofserver = document.getElementById('editpagetofserver');


    settingsList.style.display = 'none'
    settingsHeader.style.display = 'none'

    editpagetofserver.innerHTML = ""
}

function settingeditoserverclose() {

    let settingsList = document.querySelector('.settingsList');
    let settingsHeader = document.querySelector('.settingsHeader');
    let editpagetofserver = document.getElementById('editpagetofserver');


    settingsList.style.display = 'block'
    settingsHeader.style.display = 'block'
    editpagetofserver.style.display = 'none'

    editpagetofserver.innerHTML = ""
}

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