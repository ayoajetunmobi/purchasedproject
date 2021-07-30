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
    profile.style.opacity = 1;
    profile.style.zIndex = 2;
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

function mystoredisplay() {
    let mystore = document.getElementById("mystore");
    mystore.style.zIndex = 4
    mystore.style.opacity = 1
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


advertBtn.addEventListener('click', function(e) {
    e.preventDefault()
    apimyStore.innerHTML = ""
    apimyStore.innerHTML = `
            <div class="close" style="position: absolute; top:6%">
                <a href="#" id="close" onclick="disapp()"><i style="color: black;" class="fa fa-arrow-left"></i></a>
            </div>
            <h2 style="color:red;letter-spacing:2px;">Purchased ...</h2>
            <br>
            <h3> advertisement plan </h3>
    `
    apimyStoreDispay()
})

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
          <li onclick="displayMsg(this)" msgid=${data[i].id} data="${data[i].message}" Rview = "${data[i].user_to_review}" contacted = ${data[i].contacted} class ="mesageliststyle">${data[i].message}...... </li> <br>
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

reportbugBtn.addEventListener("click", function(e) {
    e.preventDefault()
    apimyStore.innerHTML = ""
    apimyStore.innerHTML = `
  <div class="close" style="position: absolute; top:6%">
                <a href="#" id="close" onclick="disapp()"><i style="color: black;" class="fa fa-arrow-left"></i></a>
            </div>
            <h2 style="color:red;letter-spacing:2px;">Purchased ...</h2>
            <br>

            <h6 style="letter-spacing:2px; text-align: center; color:rgb(0, 255, 34); font-weight:500;">REPORT BUG or SUGESTION</h6>
            <div style="position: absolute; height:100%; width:80%; left:2% ;top:0%; overflow:scroll;">
                <div style="position:fixed; top:40%; height:50%; width:99%;margin:0px auto; ">
                    <textarea name="reportUser" id="reportUser" cols="30" rows="10"></textarea><br><br><br>
                    <input type="submit" style="text-align:center;color:white;background-color:rgb(66, 223, 66); border-radius:5px;" value="REPORT BUG">
                    <input type="submit" style="text-align:center;color:white;background-color:rgb(66, 223, 66); border-radius:5px;" value="SUGEST">
                </div>
            </div>
            `
    apimyStoreDispay()
})
reportusaBtn.addEventListener('click', function(e) {
    e.preventDefault()
    apimyStore.innerHTML = ''
    apimyStore.innerHTML = `
     <div class="close" style="position: absolute; top:6%">
                <a href="#" id="close" onclick="disapp()"><i style="color: black;" class="fa fa-arrow-left"></i></a>
            </div>
            <h2 style="color:red;letter-spacing:2px;">Purchased ...</h2>
            <br>

            <h6 style="letter-spacing:2px; text-align: center; color:rgb(0, 255, 34); font-weight:500;"> REPORT USER </h6>
            <div style="position: absolute; height:100%; width:80%; left:2% ;top:0%; overflow:scroll;">
                <div style="position:fixed; top:40%; height:50%; width:99%;margin:0px auto; ">
                <input type= "text" placeholder="Culprit Username"><br><br>

                    <textarea name="reportUser" id="reportUser" cols="30" placeholder="report user" rows="10"></textarea><br><br><br>
                    <input type="submit" style="text-align:center;color:white;background-color:rgb(66, 223, 66); border-radius:5px;" value="REPORT USER">
                </div>
            </div>
            `
    apimyStoreDispay()
})
termscdBtn.addEventListener('click', function(e) {
    e.preventDefault()
    apimyStore.innerHTML = ""
    apimyStore.innerHTML = `
            <div class="close" style="position: absolute; top:6%">
                <a href="#" id="close" onclick="disapp()"><i style="color: black;" class="fa fa-arrow-left"></i></a>
            </div>
            <h2 style="color:red;letter-spacing:2px;">Purchased ...</h2>
            <br>
            <h3> terms and conditions plan </h3>
    `
    apimyStoreDispay()
})
tipsBtn.addEventListener('click', function(e) {
    e.preventDefault()
    apimyStore.innerHTML = ""
    apimyStore.innerHTML = `
            <div class="close" style="position: absolute; top:6%">
                <a href="#" id="close" onclick="disapp()"><i style="color: black;" class="fa fa-arrow-left"></i></a>
            </div>
            <h2 style="color:red;letter-spacing:2px;">Purchased ...</h2>
            <br>
            <h3> tips to succeed </h3>
    `
    apimyStoreDispay()
})
deactBtn.addEventListener('click', function(e) {
    e.preventDefault()
    apimyStore.innerHTML = ''
    apimyStore.innerHTML = `
     <div class="close" style="position: absolute; top:6%">
                <a href="#" id="close" onclick="disapp()"><i style="color: black;" class="fa fa-arrow-left"></i></a>
            </div>
            <h2 style="color:red;letter-spacing:2px;">Purchased ...</h2>
            <br>

            <div style="position: absolute; height:100%; width:80%; left:2% ;top:0%; overflow:scroll;">
                <div style="position:fixed; top:40%; height:50%; width:99%;margin:0px auto; ">
                <label> why are you deactivating your account ? </label>
                    <textarea name="reportUser" id="reportUser" cols="30" rows="10"></textarea><br><br><br>
                    <input type="submit" style="text-align:center;color:white;background-color:rgb(66, 223, 66); border-radius:5px;" value="DEACTIVATE">
                </div>
            </div>
            `
    apimyStoreDispay()
})
cover.addEventListener('click', function(e) {
    let mystoreBtn = document.getElementById('mystoreBtn');

    if (e.target != mystoreBtn) {
        mystore.style.opacity = 0
        mystore.style.zIndex = -4
    }
})

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