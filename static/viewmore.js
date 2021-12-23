    let wrapone = document.getElementById("wrap");
    let propic = document.getElementsByClassName("propic");
    let infofancy = document.querySelector("infofancy");
    let viewpostt = document.querySelector("#forpost");
    let documentss = document.body;
    let a = [...document.getElementsByClassName("a")];
    let ammountscrolled = '';
    let check = true;
    let body = document.getElementsByTagName('body');



    document.addEventListener("DOMContentLoaded", () => {
        //  yhandler()
        enter()
        callslide()
            // buy4seller()
        suggest()

    })

    function searchengine(data, yes = false, images) {
        let searchcover = document.getElementById('searchcover');

        searchcover.innerHTML = ""

        data1 = data.username
        data2 = data.product
        data3 = data.noData

        searchcover.innerHTML = `<i onclick="closesearch()" id="closesearch" style="color: black; margin-top:30px; margin-right:160px " class="fa fa-arrow-left"></i>
        `

        if (data1) {
            searchcover.style.display = 'block';
            searchcover.innerHTML += `
            <img onclick="propicclick(this)" data-id=${data1[2]} style="width: 100px; height:100px;overflow:hidden; border-radius:100px;" src="media/${data1[1]}" alt="">
            <p style="text-align: center;"> ${data1[0]} </p`
        }

        let i = 0;
        if (data2) {
            searchcover.style.display = 'grid';
            searchcover.style.gridTemplateColumns = "repeat(2,1fr)";
            data2.forEach((data2) => {
                searchcover.innerHTML +=
                    `<article class="post4store"  data = "${data2.id}" onclick= "product_spec(this)">
                        <img class="postimg" src="media/${images[i].product_img}" alt="">
                        <p class="postdesc">${data2.description.substring(0,37)} .. </p>
                        <p style="color:rgb(145, 125, 15)"> N${data2.price} </p>
                 </article>
                `
                i++
            })
        }

        if (data3) {
            searchcover.style.display = 'block';
            searchcover.innerHTML +=
                `
         <h2>   "${data3}</h2>`
        }
    }

    function addtoMyproduct(product, images, update = false) {
        let searchcover = document.getElementById('searchcover');
        searchcover.style.display = 'none'
        let i = 0;
        viewpostt.innerHTML = "";

        if (product == null || product == -1 || images == -1 || images == null || product[i].description == "no product yet") {
            return false
        } else {
            product.forEach((product) => {
                        viewpostt.innerHTML +=
                            `
                    <article style="display:grid; grid-template-columns:repeat(1,3fr); max-width:130px; margin:13px;  margin-bottom:13px;" data="">
                        <div style="width:120px; height:140px; overflow:hidden; ">
                        ${(update == true)?` <p class="deleteDot" onclick= "dot(this)" data= ${product.id} draggable="true">...</p><a href="#" class="deleteMsg" onclick= "delmsg(this)" data= ${product.id}> Delete Post </a>`:``}
                          

                           ${(product.id == images[i].product_id)?`<img onclick="product_spec(this)" data=${product.id} class="productImg" style="width:100%; height:auto;" src="media/${images[i].product_img}" alt="">`:""}
                        </div> 
                        <span>
                       ${product.description.substring(0,37)} .....
                        </span>
                        <span style="color: #91792b; text-align:center;">
                              N${product.price}
                        </span>
                    </article>
                      `;
                i++
            })

        }
    }

    function updateProductspec(product,productImg,sproduct,sproductImg,contact,seller){
        let spec = document.getElementById('productSpec'),
        specPropic = document.getElementById("specPropic"),
        specDescription = document.getElementById('specDescription'),
        specImgs = document.getElementById('specImgs'),
        topdealsp = document.getElementById('topdealsp'),
        productSpecsugest = document.getElementById('productSpecsugest');

        spec.style.display = 'none'
        spinner()
                       
        if (product == null || product == -1 || productImg == -1 || productImg  == null, contact == -1 || contact  == null) {
            return false
        } else {
            specPropic.innerHTML = ''
            specPropic.innerHTML = `
                  ${(product.online == true)?`<div class= "online">`:`<div class= "offline">`}
                  </div>
                  <img class="propicp" style="width: 60px;  box-shadow: rgb(49, 49, 197) 2px 2px 5px; height:60px;" onclick="propicclick(this)" data-id=${product.id} src="media/${product.propic}" alt="" />
                  <h6>${product.username}</h6>
                  `

            specDescription.innerHTML=""
            specDescription.innerHTML= `
                  <h6 style="padding:0px 3px;">${product.description}</h6>
                  <h5 style="padding:0px 3px; color:gold;">N${product.price}</h5>
                 <span style="font-size: small; color:black; text-align:center;">  search tag : <span style="background-color: azure; color:blue; padding:2px; border-radius:1px;"> ${product.searchTag} </span> </span>
                   `
            specImgs.innerHTML= ""  
            specImgs.innerHTML= `<button id="moveleft" style="position: absolute; left: 4%; top:40%; font-size:larger; cusor:pointer;  z-index:1; background-color:grey; color:white;"> <
                </button>
             <button id="moveright" style="position: absolute; right: 4%; top:40%; font-size:larger; cusor:pointer;z-index:1;  background-color:grey; color:white;"> >
                </button>
                `  
            let li = document.createElement("li");
            li.classList.add('productSpecpiclist')
            productImg.forEach(img=>{
                li.innerHTML += `
                   <img class="mainspecimgs" style="width: 350px; height:350px; position:absolute;" src="media/${img.product_img}" alt="" />
                ` 
            })
              specImgs.appendChild(li) 

            
           
            productSpecsugest.innerHTML= ""
            sproduct.forEach(pro => {
                let a = "";
                sproductImg.forEach(img=>{
                 if(pro.id == img.product_id){
                       a = img.product_img
                }})
             productSpecsugest.innerHTML += `
                   <article data="">
                   <img data=${pro.id} onclick="product_spec(this)" style="max-width: 120px; height:140px; margin-left:20px;" src="media/${a}" alt="">
                     <span>
                       ${pro.description.substring(0,37)} ... <br>
                     </span>
                      <span style="color:gold;">
                       N ${pro.price} <br>
                     </span>
                     </article>  `
         })
         let contctdiv = document.getElementById('contctdiv');
         if(contctdiv != null){
         contctdiv.innerHTML = ''
            contctdiv.innerHTML = `
              <h3 class="contactnumber" style='display:none; text-align:center;'>${contact}<br>
                    <span style="color:red; font-size:medium;margin:20px;"> please drop a review on user after product
                        delivery </span>
                </h3><br><br>
                <a href="tel:${contact}"> <button onclick="msg(this)" seller=${seller} style="width: 100%; margin-bottom:30px; color:white;height:30px; border-radius:15px; background-image: linear-gradient(to bottom right, rgb(0, 255, 34), rgb(52, 107, 59));">
                contact seller </button></a> 
            `
        }
     }

       spec.style.display = 'block'
       closespinner()
       moveslide()

    }

    function addtoMyProfile(profile, product, images, reviews, update = false, advert){
        let cover = document.getElementById('cover');
        let allinfo = document.getElementById('allinfo');
        let review = document.querySelector('#reviewP');
        let recentPost = document.querySelector("#recentpost");
        let contactseller = document.getElementById('contactSeller');
        let topdeals = document.getElementById('topdeals');
        let i = 0;
        let ii = 0;
        let profilecover = document.getElementById('profile');

       

        

        profilecover.style.display= 'none'
        spinner()
        cover.innerHTML = "";

        if (profile == null || profile == -1) {
            return false
        } else { 
         cover.innerHTML += 
            ` <div class="propic">
                    ${(update == true)? `<img src= "media/${profile.propic}" onclick="propicture(event)" style:"box-shadow: 0 20px 20px rgba(4, 0, 255, 0.25);" alt="" bigpic="media/${profile.propic}" id="propicc"/>`: `<img src= "media/${profile.propic}" onclick="propicture(event)"  alt="" bigpic="media/${profile.propic}" id="propicc"/>`}
                   <br><br> <h5 class="username"> <i class="fa fa-user"></i> <span>${profile.username} </span></h5>
                    <h4 class="username" style="margin:14px;"> <i class="fa fa-id-badge"></i> <span>${profile.about}</span> </h5>
                    <h5 class="username"><i class="fa fa-male"></i><i class="fa fa-female"></i> <span>${profile.gender} </span></h4>
                    </h4>
                    <div class="links">
                        <a class="view" onclick="viewmore(event)"> market place </a>
                        ${(update == true)?'':`<a onclick="ApiDisMsg(this)" id="msgBtn" class="view"> my messages </a> <a id="mystoreBtn" onclick= "mysetting()" class="view"> SETTINGS </a>`}
                    </div>
                </div>`

                if(update == true){
                    changedp.style.display = "none"
                }else{
                     changedp.style.display = "block"
                }


            allinfo.innerHTML = `
                <a> matric verification</a>
               ${(profile.matricverified == true)? `<h5 style="color:blue;">  <i class="fa fa-star"></i> Student<h5>`:`<h5 style="color:grey;"> not a Student<h5>`}
                <a class="activated activity"> Top User</a>
                ${(profile.topuser == true)? `<h5 style="color:gold;">  <i class="fa fa-star"></i> top user <h5>`:`<h5 style="color:grey;"> not yet a top user <h5>`}
                 <a>online status</a>
                 ${(profile.online == true)?` <h5 style="color:green;"> active <h5>`:`<h5 style="color:grey;"> offline <h5>`}
            `;

            contactseller.innerHTML =`<h3 style= "display:none;" class="contactnumber">${profile.contact}<br>
                <span style="color:red; font-size:small;"> please drop a review on user after product delivery </span>
                </h3>
                <a href="tel:${profile.contact}"><button  onclick= "msg(this)" seller = ${profile.username} style="border: 5px groove rgb(0, 255, 21); background-color:white; color:black;" >CONTACT SELLER</button></a><br>
            `

            recentPost.innerHTML = ""
            if (product.length == 1 && product[i].description == "no product yet"){
            }
            else{ 
                while (i < product.length &&  i != 4) {
                    recentPost.innerHTML +=
                    `
                    <article data="">
                      ${(product[i].id == images[i].product_id)?`<img onclick="product_spec(this)" data= ${product[i].id} src = "media/${images[i].product_img}" alt="">`:""}
                      <span>
                        ${product[i].description.substring(0,37)} ...
                      </span>
                      <br>
                      <span class="pricesugg">
                        N${product[i].price}  
                      </span>
                      <br><br>
                    <article>`;
                    i++
                }      
            }   
            
            review.innerHTML=""
            if (reviews.length > 0 ) {
                while (ii < reviews.length && ii!= 5) {
                    review.innerHTML += ` 
                      <article>
                         <br><br>
                         <span>
                            ${reviews[ii].review}
                         </span>
                         <br><br>
                         <span style="color:white">
                            ${reviews[ii].username}
                         </span><br>
                         <span style="color:grey; font-size:xx-small;">
                            ${(reviews[ii].as_buyer== true)?`reviewed by buyer`:`reviewed by seller`}
                        </span>
                      </article>`
                    ii++
                }
            }
        }
        profilecover.style.display = 'block'
        closespinner()
    }

    function moveslide(){
     let mainspecimgs = [...document.getElementsByClassName('mainspecimgs')],
     moveleft =document.getElementById('moveleft'),
     moveright =document.getElementById('moveright'),

     slidebyone = 0,
     slideWidth = 350;

     if(mainspecimgs.length > 1){
       
       for (let i = 0; i < mainspecimgs.length; i++){ 
           mainspecimgs[i].style.left = slideWidth * i + "px";}
        }
           
         moveright.addEventListener('click', function(){
         let lastChild = mainspecimgs.length;
         if(slidebyone < lastChild - 1){ 
             moveSlidesProspec(mainspecimgs, "forward");
              moveright.style.opacity=1;
              slidebyone++
         }else{
            moveright.style.opacity=0;
            moveleft.style.opacity=1;
         }
     }) 
     moveleft.addEventListener('click', function(){
         if(slidebyone > 0){ 
              moveleft.style.opacity=1;
             moveSlidesProspec(mainspecimgs, "backward",);
             slidebyone--
         }else{
             moveleft.style.opacity=0;
             moveright.style.opacity=1;
         }
    }) 

    }

    function moveSlidesProspec(move, direction) {
            for (var j = 0; j < move.length; j++) {
                if (direction == "backward") {
                    move[j].style.left = +move[j].style.left.replace(/[^-\d\.]/g, "") + 350 + "px";
                } else if (direction == "forward") {
                    move[j].style.left = +move[j].style.left.replace(/[^-\d\.]/g, "") - 350 + "px";
                }
            }
    }

    function suggestproduct(data){
        let suggestproduct = document.getElementById('suggestproduct');
        let suggest1 = data['suggestion1'];
        let suggest2 = data['suggestion2'];
        let suggest3 = data['suggestion3'];
        let suggest4 = data['suggestion4'];
        
        let topdealcontainer = data.products;
        let topdealcontainerImg = data.productsrotateImg;
    
    
        let suggestImg = data['suggestionImg'];
        suggestproduct.innerHTML= ""
        suggestproduct.innerHTML= `
             <article data="${suggest1[0].id}" onclick="product_spec(this)" class="post">
             <img class="postimg" src="media/${suggestImg[0].product_img}" alt="">
             <p class="postdesc">${suggest1[0].description.substring(0,33)}..</p>
             <p class="pricesugg">N${suggest1[0].price}</p> 
             </article>

             <article data="${suggest2[0].id}" onclick="product_spec(this)" class="post">
             <img class="postimg" src="media/${suggestImg[1].product_img}" alt="">
             <p class="postdesc">${suggest2[0].description.substring(0,33)}..</p>
             <p  class="pricesugg" >N${suggest2[0].price}</p>
             </article>

             <article data="${suggest3[0].id}" onclick="product_spec(this)" class="post">
             <img class="postimg" src="media/${suggestImg[2].product_img}" alt="">
             <p class="postdesc">${suggest3[0].description.substring(0,33)}..</p>
             <p class="pricesugg">N${suggest3[0].price}</p>
             </article>

             <article data="${suggest4[0].id}" onclick="product_spec(this)" class="post">
             <img class="postimg" src="media/${suggestImg[3].product_img}" alt="">
             <p class="postdesc">${suggest4[0].description.substring(0,33)}..</p>
             <p  class="pricesugg">N${suggest4[0].price}</p>
             </article>

        `
          
        let topdeals = document.getElementById('topdeals');
        let topdealsp = document.getElementById('topdealsp');

        for(let i = 0; i < topdealcontainer.length;i++){
         topdeals.innerHTML +=
        `   
            <article data="${topdealcontainer[i].id}" onclick="product_spec(this)" class="post">
               <img class="postimg" src="media/${topdealcontainerImg[i].product_img}" alt="">
               <p class="postdesc" style = "color:black" >${topdealcontainer[i].description.substring(0,33)}..</p>
               <p  class="pricesugg">N${topdealcontainer[i].price} </p>
            </article>
        `
        } 

        for(let i = 0; i < topdealcontainer.length;i++){
         topdealsp.innerHTML +=
        `   
            <article data="${topdealcontainer[i].id}" onclick="product_spec(this)" class="post">
               <img class="postimg" src="media/${topdealcontainerImg[i].product_img}" alt="">
               <p class="postdesc" style = "color:black" >${topdealcontainer[i].description.substring(0,33)}..</p>
               <p  class="pricesugg" style = "color:yellow">N${topdealcontainer[i].price} </p>
            </article>
        `
        } 
    }