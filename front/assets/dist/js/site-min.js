var link_frame1="",link_frame2="",link_frame3="";function ajustText(e){return e.charAt(0).toUpperCase()+e.slice(1)}function insertSelectCategoryItems(e){let t=document.getElementById("formCategoryItem"),n=document.createElement("option");n.value=e,n.text=e,t.add(n)}function checkSelectedCategory(){var e=document.getElementById("formCategory"),t=e.options[e.selectedIndex].value,n=document.getElementById("divFormCategoryItem");(console.log("Valor: "+t),n.style.visibility="animals"===t?"visible":"hidden","animals"===t)&&($("#formCategoryItem").children("option").length<=1&&(insertSelectCategoryItems(ajustText("dog")),insertSelectCategoryItems(ajustText("cat")),insertSelectCategoryItems(ajustText("horse"))))}function downloadImage1(){var e=document.createElement("a");e.href=link_frame1,e.download=link_frame1,e.target="_blank",document.body.appendChild(e),e.click(),document.body.removeChild(e)}function downloadImage2(){var e=document.createElement("a");e.href=link_frame2,e.download=link_frame2,e.target="_blank",document.body.appendChild(e),e.click(),document.body.removeChild(e)}function downloadImage3(){var e=document.createElement("a");e.href=link_frame3,e.download=link_frame3,e.target="_blank",document.body.appendChild(e),e.click(),document.body.removeChild(e)}var getJSON=function(e,t){var n=new XMLHttpRequest;n.open("GET",e,!0),n.responseType="json",n.onload=function(){var e=n.status;t(200===e?null:e,n.response)},n.send()};function getImage(e){getJSON("https://api.randomwebimages.com/image/random",(function(t,n){null!==t?console.log("Something went wrong: "+t):(document.getElementById("img_home"+e).src=n.image.link,1===e?link_frame1=n.image.link:2===e?link_frame2=n.image.link:3===e&&(link_frame3=n.image.link))}))}function getRandomNumberBetween(e,t){return Math.floor(Math.random()*(t-e+1)+e)}function loadImages(){getImage(1),getImage(2),getImage(3)}function refreshPage(){window.location.reload()}window.onload=function(){loadImages()},checkSelectedCategory();