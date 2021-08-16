    let wrapone = document.getElementById("wrap");
    let propic = document.getElementsByClassName("propic");
    let infofancy = document.querySelector("infofancy");
    let viewpostt = document.querySelector("#forpost");
    let documentss = document.body;
    let a = [...document.getElementsByClassName("a")];

    document.addEventListener("DOMContentLoaded", () => {
        yhandler()
        enter()
        callrecomend()
    })

    function displaypost(posts, images) {
        let i = 0
        result = ""
        posts.forEach((post) => {
                    result +=
                        `<div class="pos1">
                <a href="#" class="a">${post.username}</a>
                <div style="margin:0px auto">
                    ${(post.online)?`<div class="online"></div>`:`<div class="offline"></div>`}
                    <img class="propicp" onclick="propicclick(this)" data-id=${post.user_id} src="media/${post.profile_pic}" alt="" />
                </div>
                <div class='article' data=5>
                    ${(post.matricverified)?` <h5 style="position: absolute; top:-5%; right:7%; color:blue;"> <i class="fa fa-star" style = "color:blue;"></i></h5>`:''}
                   ${(post.topuser)?` <h5 style="position: absolute; top:-5%; right:7%; color:gold;"> <i class="fa fa-star"></i></h5>`:''}
                    <img class="slidep" onclick="product_spec(this)" data=${post.id} src="media/${images[i].product_img}" alt="">
                </div>
                <div class="describe">
                    <h4> ${post.searchTag}...</h4>
                </div>
                <div class="pricinp">
                    <h5> N${post.price} </h5>
                </div>
            </div>
                `;
                i++
        });
        wrapone.innerHTML += result
    }

    function searchengine(data, yes = false, images) {

        let searchcover = document.getElementById('searchcover');
        searchcover.innerHTML = ""

        data1 = data.username
        data2 = data.product
        data3 = data.noData

        searchcover.innerHTML = `<i onclick="closesearch()" id="closesearch" style="color: black; margin-top:20px;" class="fa fa-arrow-left"></i>`

        if (data1) {
            searchcover.innerHTML += `
            <div class="scontent"  onclick="propicclick(this)" data-id=${data1[2]} >
                <img class="propicp" style="width:70px; height:70px; margin-left:40px" src="media/${data1[1]}" alt=""><br>
                 <h2>${data1[0]}</h2>
            </div><br>`
        }
       
            let i= 0;
            if (data2) {
                data2.forEach((data2) => {
                searchcover.innerHTML += `
                  <div class="scontent" data = "${data2.id}" onclick= "product_spec(this)" style="height:250px; min-width:230px">
                  <img style="height:190px; min-width:100%"   src="media/${images[i].product_img}" alt="">
                  <h4>${data2.searchTag}...</h4>
                  </div><br>`
                  i++
            })
        }
        
        if (data3) {
            searchcover.innerHTML += `
            <div class="scontent">
                  <h2>   "${data3} or LOGIN" </h2>
            </div><br>`
        }
    }

    function addtoMyproduct(product, images, update= false) {
        let i = 0;
        viewpostt.innerHTML = "";
        if (product == null || product == -1 || images == -1 || images == -null) {
            return false
        } else {
            product.forEach(product => {
                viewpostt.innerHTML +=
                 `
                    <article style="display:grid; grid-template-columns:repeat(1,3fr); max-width:130px; margin:13px;  margin-bottom:13px;" data="">
                        <div style="width:120px; height:140px; overflow:hidden; ">
                        ${(update == true)?` <p class="deleteDot" onclick= "dot(this)" data= ${product.id} draggable="true">...</p><a href="#" class="deleteMsg" onclick= "delmsg(this)" data= ${product.id}> Delete Post </a>`:``}
                          

                           ${(product.id == images[i].product_id)?`<img onclick="product_spec(this)" data=${product.id} class="productImg" style="width:100%; height:auto;" src="media/${images[i].product_img}" alt="">`:""}
                        </div> 
                        <span>
                       ${product.searchTag} .....
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
        contactView = document.getElementById('contactView'),
        productSpecsugest = document.getElementById('productSpecsugest')

        ;
        spec.style.display='block'
        spec.style.zIndex = 4


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
                  ${product.description}
                   <br><br> <span style="font-size: medium; color:white; text-align:center;">  search tag : <span style="background-color: azure; color:blue; padding:2px; border-radius:1px;"> ${product.searchTag} </span> </span>
                   `
            specImgs.innerHTML= ""  
            productImg.forEach(img=>{
            specImgs.innerHTML+=`
                <li class="productSpecpiclist">
                   <img style="width: 100%; height:350px;" src="media/${img.product_img}" alt="" />
                </li>
                `  
            })
            contactView.innerHTML=""
            contactView.innerHTML = `
            <h3 class="contactnumber" style='display:none; text-align:center;'>${contact}<br>
            <span style="color:red; font-size:medium;"> please drop a review on user after product delivery </span>
            </h3><br><br>
              <button onclick= "msg(this)" seller = ${seller} style="width: 100%; margin-bottom:30px; color:white;height:30px; border-radius:15px; background-image: linear-gradient(to bottom right, rgb(0, 255, 34), rgb(52, 107, 59));">contact seller</button>
            `
            productSpecsugest.innerHTML=""
            sproduct.forEach(pro => {
                let a = "";
                sproductImg.forEach(img=>{
                 if(pro.id == img.product_id){
                       a = img.product_img
                }})
                 productSpecsugest.innerHTML += `
                   <article data="">
                   <img data=${pro.id} onclick="product_spec(this)" style="max-width: 120px; height:140px; margin-left:20px;border:1px groove yellow;" src="media/${a}" alt="">
                     <span>
                       ${pro.searchTag}....... <br>
                     </span>
                     </article>
            `
            
         })

        }
    }

      function addtoMyProfile(profile, product, images, reviews, update = false, advert){
        let cover = document.getElementById('cover');
        let advertImg = document.getElementById('advertImg');
        let allinfo = document.getElementById('allinfo');
        let review = document.querySelector('#reviewP');
        let recentPost = document.querySelector("#recentpost");
        let contactseller = document.getElementById('contactSeller');
        let i = 0;
        let ii = 0;

        cover.innerHTML = "";

        if (profile == null || profile == -1) {
            return false
        } else { 
         cover.innerHTML += 
            ` <div class="propic">
                    ${(update == true)? `<img src= "media/${profile.propic}" onclick="propicture(event)" style:"box-shadow: 0 20px 20px rgba(4, 0, 255, 0.25);" alt="" bigpic="media/${profile.propic}" id="propicc"/>`: `<img src= "media/${profile.propic}" onclick="propicture(event)"  alt="" bigpic="media/${profile.propic}" id="propicc"/>`}
                    <h5 class="username"> <i class="fa fa-user"></i> <span>${profile.username} </span></h5>
                    <h4 class="username"> <i class="fa fa-id-badge"></i> <span>${profile.about}</span> </h4>
                    <h4 class="username"><i class="fa fa-male"></i><i class="fa fa-female"></i> <span>${profile.gender} </span></h4>
                    </h4>
                    <div class="links">
                        <a class="view" onclick="viewmore(event)"> market place </a>
                        ${(update == true)?'':`<a onclick="producappear()" id="producbtn" class="view"> create product </a> <a id="mystoreBtn" onclick= "mystoredisplay()" class="view"> My Store </a>`}
                    </div>
                </div>`

            allinfo.innerHTML = `
                <a >F.Name</a>
                <h5> ${profile.firstname} </h5>
                <a class="activated activity"> L.Name</a>
                <h5>${profile.lastname} </h5>
                <a> matric verification</a>
               ${(profile.matricverified == true)? `<h5 style="color:blue;">  <i class="fa fa-star"></i> Student<h5>`:`<h5 style="color:grey;"> not a Student<h5>`}
                <a class="activated activity"> Top User</a>
                ${(profile.topuser == true)? `<h5 style="color:gold;">  <i class="fa fa-star"></i> top user <h5>`:`<h5 style="color:grey;"> not yet a top user <h5>`}
                 <a>online status</a>
                 ${(profile.online == true)?` <h5 style="color:green;"> active <h5>`:`<h5 style="color:grey;"> offline <h5>`}
            `;
            contactseller.innerHTML =
                `<h3 style= "display:none;" class="contactnumber">${profile.contact}<br>
            <span style="color:red; font-size:small;"> please drop a review on user after product delivery </span>
            </h3>
            <button  onclick= "msg(this)" seller = ${profile.username} style="background-image: linear-gradient(to bottom right, rgb(0, 255, 34), rgb(52, 107, 59))" >CONTACT SELLER</button>`


            
            advertImg.style.display = "block"
            advertImg.innerHTML=''
            advertImg.innerHTML = `<img style="display:block;" src="media/${advert}" alt=""/>`

            recentPost.innerHTML = ""
            if (product.length > 0) {
                while (i < product.length &&  i != 4) {
                    recentPost.innerHTML += `
                    <article data="">
                      ${(product[i].id == images[i].product_id)?`<img onclick="product_spec(this)" style= " border:1px solid yellow" data= ${product[i].id} src = "media/${images[i].product_img}" alt="">`:""}
                      <span>
                        ${product[i].searchTag}  
                      </span>
                      <br><br>
                    <article>`;
                        i++
                }       
            }
            review.innerHTML=""
            if (reviews.length > 0) {
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
    }