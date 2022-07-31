let controldetail_img = 0;
let settingbtn = document.getElementById("settingbtn");
let viewAllProBtn = document.getElementById('viewAllProBtn');
let morecatBtn = document.getElementById("morecatBtn");
let screening = screen.width;
let close = [...document.querySelectorAll('.close')];
let closeprofilePage = document.getElementById('closeprofilePage');

function spinner() {
    let spinnerdiv = document.getElementById('spinnerdiv');
    spinnerdiv.style.display = 'block';
}

function closespinner() {
    let spinnerdiv = document.getElementById('spinnerdiv');
    spinnerdiv.style.display = 'none';
}

// function updatehomeProd(product1, product2, productImg) {
//     let productConCov = document.getElementById('productConCov');
//     product1.forEach((product) => {
//                 let img = productImg.find(img => img.product_id == product.id);
//                 let vat = parseInt(product.id);
//                 productConCov.innerHTML +=
//                     ` 
//                <div class="productcover" onclick="location.href ='http://shopatpurchased.com/productspec/${vat}';">
//                 <div class="productimg">
//                     ${(product.id == img.product_id)?`<img src='media/${img.product_img}' alt='' />`:``}
//                 </div>
//                 <div class="productdetails">
//                 <h5>${(product.description).substring(0, 50)} ... </h5>
//                 <h5>${product.searchTag}</h5>
//                 <h3>${product.price}</h3>
//                 <h6 style="color: #ff9966" data=${product.id}>

//                             <a href="tel:${product.conduct}" onclick="displayNum(${product.contact})" style="color: #66ff66; margin-left: 20px">
//                             <i class="fa fa-phone"></i> contact seller
//                             </a>
//                 </h6>
//                 </div>
//              </div>
//             `
//     })

//     product2.forEach((product) => {
//                 let img = productImg.find(img => img.product_id == product.id);
//                 let vat1 = parseInt(product.id);
//                 productConCov.innerHTML +=
//                     ` 
//                 <div class="productcover" onclick="location.href ='http://shopatpurchased.com/productspec/${vat1}';">
//                 <div class="productimg">
//                     ${(product.id == img.product_id)?`<img src='media/${img.product_img}' alt='' />`:``}
//                 </div>
//                 <div class="productdetails">
//                 <h5>$${(product.description).substring(0, 50)}...</h5>
//                 <h5>${product.searchTag}</h5>
//                 <h3>${product.price}</h3>
//                 <h6 style="color: #ff9966" data=${product.id}>

//                             <a href="tel:${product.contact}" onclick="displayNum(${product.contact})" style="color: #66ff66; margin-left: 20px">
//                             <i class="fa fa-phone"></i> contact seller
//                             </a>
//                 </h6>
//                 </div>
//              </div>
//             `
//     })

//   }

function callslide() {
    let displayimg = document.getElementById("aboutdetail_img1");
    let displayimg2 = document.getElementById("aboutdetail_img2");

    if (controldetail_img == 0) {
        displayimg.style.display = "block";
        displayimg2.style.display = "none";
        controldetail_img = 1;
    } else {
        displayimg.style.display = "none";
        displayimg2.style.display = "block";
        controldetail_img = 0;
    }
    setTimeout("callslide()", 3000)
}

function searchengine(data, yes = false, images) {
    let searchcover = document.getElementById('searchcover');

    searchcover.innerHTML = ""

    data1 = data.username
    data2 = data.product
    data3 = data.noData

    if (data1) {
        searchcover.style.display = 'block';
        searchcover.innerHTML += `
            <i onclick="closesearch()" id="closesearch" style="color: black;" class="fa fa-arrow-left"></i><br><br>
            <img style="width: 100px; height:100px;overflow:hidden; border-radius:100px;" src="media/${data1[1]}" onclick="location.href ='http://shopatpurchased.com/profileupdate/${parseInt(data1[2])}';">
            <p style="text-align: center;"> ${data1[0]} </p`
    }

    let i = 0;
    if (data2) {
        searchcover.style.display = 'block';
        searchcover.innerHTML = `,br><br><i onclick="closesearch()" id="closesearch" style="color: black;" class="fa fa-arrow-left"></i><br><br>`
        data2.forEach((data2) => {
            searchcover.innerHTML +=
                `
     <div class="productcover deleteMsg" data=${data2.id}  onclick="location.href ='http://shopatpurchased.com/productspec/${parseInt(data2.id)}';">
          <div class="productimg">
            <img src="media/${images[i].product_img}" alt="image here" />
          </div>
          <div class="productdetails">
             <h5>${data2.description.substring(0,150)}</h5>
            <h5>${data2.searchTag}</h5>
            <h4> N${data2.price}.00</h4>
          </div>
        </div>`
            i++
        })
    }

    if (data3) {
        searchcover.style.display = 'block';
        searchcover.innerHTML +=
            `
                <i onclick="closesearch()" id="closesearch" style="color: black;" class="fa fa-arrow-left"></i><br><br>
         <h2>   "${data3}</h2>`
    }
}

function closesearch() {
    searchcover.style.display = 'none';
    document.getElementById("searchinput").value = ""

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

function display_profile(e) {
    let profile = document.getElementById('profile');
    profile.style.display = "block"
}

function reviewpagedis(e) {
    let reviewpage = document.getElementById('reviewpage');
    reviewpage.style.display = "block";
    reviewpage.style.zIndex = 2;
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

settingbtn.addEventListener('click', function(event) {
    let settings = document.getElementById('settings');
    settings.style.display = "block"
    settings.style.zIndex = 2;
})



function viewall() {
    let viewAllProdCov = document.getElementById('viewAllProdCov');
    viewAllProdCov.style.display = "block";
    viewAllProdCov.style.zIndex = 2;
}

morecatBtn.addEventListener('click', function(e) {
    let morecatCover = document.getElementById('morecatCover');
    morecatCover.style.display = "block";
    morecatCover.style.zIndex = 2;
    if (screening < 590) {
        morecatCover.style.display = "block";
        morecatCover.style.zIndex = 2;
        morecatCover.style.left = '0%';
    }
})

close.forEach(element => element.addEventListener('click', (e) => {
    let viewAllProdCov = document.getElementById('viewAllProdCov');
    let settings = document.getElementById('settings');
    let reviewpage = document.getElementById('reviewpage');
    let morecatCover = document.getElementById('morecatCover');

    viewAllProdCov.style.display = "none";
    viewAllProdCov.style.zIndex = 0;
    settings.style.display = "none";
    settings.style.zIndex = 0;
    reviewpage.style.display = "none"
    reviewpage.style.zIndex = 0;

    if (screening < 590) {

        morecatCover.style.zIndex = 2;
        morecatCover.style.left = '-100%';
    } else {
        morecatCover.style.display = "none";
        morecatCover.style.zIndex = 0;
    }
}))

closeprofilePage.addEventListener('click', (e) => {
    let profile = document.getElementById('profile');
    profile.style.display = "none"
})

function delcovDisplay(e) {
    let data = e.getAttribute('data');
    let del = document.getElementById('delprod');
    del.setAttribute("data", data)
    let deleteCov = document.getElementById('deleteCov');
    deleteCov.style.display = 'block'

}

function closedel() {
    let deleteCov = document.getElementById('deleteCov');
    deleteCov.style.display = 'none'
}

function settingfunc(event) {
    let data = event;
    let settingsFunc = document.getElementById('settingsFunc');

    if (data == 2) {

        settingsFunc.innerHTML =
            `<br><br><br>
            <a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> Change Password </h5><br>
            <div style="height: 50%; width:100%">             
                <input id="settingactionInput" type="password" style="width:98%; height:20%; background-color:rgb(255, 255, 255);border:none;" placeholder= "new password">
                <input id="settingactionInput2" type="password" style="width:98%; height:20%; background-color:rgb(255, 255, 255);border:none;" placeholder= "confirm password"">
            </div>
            <br>
            <div style="width: 100%; text-align:center; background-color:#ffffff; border-top:0.3px solid black; color:rgb(255, 0, 0);
            font-weight:700">
                <input type = "submit" value = SUBMIT onclick = "apisettings(2)">
            </div>
            `
        settingsFunc.style.display = 'block'
    }

    if (data == 3) {

        settingsFunc.innerHTML =
            `<br><br><br>
            <a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> Edit About </h5><br>
            <div style="height: 50%; width:100%">             
                <textarea id="settingactionInput" style="width:98%; height:20%; background-color:rgb(255, 255, 255);border:none;" maxlength="150" placeholder= "edit about(150 words)"></textarea>
            </div>
            <br>
            <div style="width: 100%; text-align:center; background-color:#ffffff; border-top:0.3px solid black; color:rgb(255, 0, 0);
                font-weight:700">
               <input type = "submit" value = SUBMIT onclick = "apisettings(3)">
            </div>
            `
        settingsFunc.style.display = 'block'
    }
    if (data == 4) {

        settingsFunc.innerHTML =
            `<br><br><br>
            <a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> Edit Contact </h5><br>
            <div style="height: 40%; width:100%">             
                <input  id="settingactionInput" type = "number" style="width:98%; height:20%; background-color:rgb(255, 255, 255);border:none;" placeholder= "new number">
            </div>
            <br>
            <div style="width: 100%; text-align:center; background-color:#ffffff; border-top:0.3px solid black; color:rgb(255, 0, 0);
                font-weight:700">
               <input type = "submit" value = SUBMIT onclick = "apisettings(4)">
            </div>
            `
        settingsFunc.style.display = 'block'
    }

    if (data == 5) {

        settingsFunc.innerHTML =
            `<br><br><br>
            <a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> Make Suggestion </h5><br>
            <div style="height: 70%; width:100%">             
                <textarea id="settingactionInput" style="width:98%; height:40%; background-color:rgb(255, 255, 255);border:none;" maxlength="150" placeholder= "suggest something  (150 words)"></textarea>    </div>
            <br>
            <div style="width: 100%; text-align:center; background-color:#ffffff; border-top:0.3px solid black; color:rgb(255, 0, 0);
                font-weight:700">
               <input type = "submit" value = SUBMIT onclick = "apisettings(5)">
            </div>
            `
        settingsFunc.style.display = 'block'
    }
    if (data == 6) {

        settingsFunc.innerHTML =
            `<br><br><br>
            <a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> Report User </h5><br>
            <div style="height: 50%; width:100%"> 
                <textarea id="settingactionInput" style="width:98%; height:20%; background-color:rgb(255, 255, 255);border:none;" maxlength="150" placeholder= "culprit username"></textarea>
                <textarea id="settingactionInput2" style="width:98%; height:20%; background-color:rgb(255, 255, 255);border:none;" maxlength="150" placeholder= "report user (150 words)"></textarea></div>
            <div style="width: 100%; text-align:center; background-color:#ffffff; border-top:0.3px solid black; color:rgb(255, 0, 0);
                font-weight:700">
               <input type = "submit" value = SUBMIT onclick = "apisettings(6)">
            </div>
            <br>
            `
        settingsFunc.style.display = 'block'
    }
    if (data == 7) {

        settingsFunc.innerHTML =
            `<br><br><br>
            <a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> about us </h5><br>
            <h5> Purchased is an online market that
operates within LASU. Purchased focuses
most on customer satisfaction. It aims to
be the best online market in LASU.
On our online store we have a wide
selection of products and services. Our
website has hundreds of buyers and
sellers. You can contact a seller to get a
product on the site. Sellers make delivery
only within the campus. Site users can give
good or bad reviews about other users.
Contact our admin on any issue you might
be having.
Follow us on;
Instagram : www.instagram.com/
purchased.tech </h5>
            `
        settingsFunc.style.display = 'block'
    }

    if (data == 9) {


        settingsFunc.innerHTML =
            `<br>
            <br>
            <br>
            <a href="#" onclick = "settingeditoserverclose()"><i style="color: rgb(0, 0, 0);" class="fa fa-arrow-left"></i>
            </a>
            <h5 style="text-align: center; color:red;"> Deactive Account </h5><br>
            <div style="height: 70%; width:100%">             
                <textarea id="settingactionInput" style="width:98%; height:40%; background-color:rgb(255, 255, 255);border:none;" maxlength="150" placeholder= "why are you deactivating your account(150 words)"></textarea>
            </div>
            <br>
            <div style="width: 100%; text-align:center; background-color:#ffffff; border-top:0.3px solid black; color:rgb(255, 0, 0);
                font-weight:700">
               <input type = "submit" value = SUBMIT onclick = "apisettings(9)">
            </div>
            `
        settingsFunc.style.display = 'block'
    }
}

function settingeditoserverclose() {
    let settingsFunc = document.getElementById('settingsFunc');
    settingsFunc.style.display = 'none'
}

function openchangedpPage() {
    let changedpPage = document.getElementById('changedpPage');
    changedpPage.style.display = 'block'
}

function closechangedpPage() {
    let changedpPage = document.getElementById('changedpPage');
    changedpPage.style.display = 'none'
}

function propicture(event) {
    var elem = event.target,
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
        bigoverlay.style.display = 'block';

    }
    // If we click any of these 2 elements, close the lightbox
    if (elem.hasAttribute('close') || elem.getAttribute('close') == 'yes') {
        event.preventDefault();
        bigoverlay.style.display = 'none';
    }
}

function displayNum(event) {
    let numberDisp = document.querySelector('.numberDisp'),
        numberDispNUm = document.getElementById('numberDisp');
    numberDispNUm.innerHTML = `${event}`
    numberDisp.style.display = 'block'
}

function closenumdisp() {
    let numberDisp = document.querySelector('.numberDisp');
    numberDisp.style.display = 'none'
}