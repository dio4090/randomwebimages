// START THE APP
var link_frame1 = "";
var link_frame2 = "";
var link_frame3 = "";

var el = document.getElementById("formCategory");
var formCategoryValue = el.options[el.selectedIndex].value;
var divFormCategoryItem = document.getElementById('divFormCategoryItem');

if(formCategoryValue === 'animals') {
    divFormCategoryItem.style.visibility='visible'
} else {
    divFormCategoryItem.style.visibility='hidden'
}

function ajustText(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function insertSelectCategoryItems(optionStr) {
    //add one option
    let select = document.getElementById('formCategoryItem');
    let option = document.createElement('option');

    option.value = optionStr;
    option.text = optionStr;
    select.add(option);
}

function checkSelectedCategory() {
    var el = document.getElementById("formCategory");
    var formCategoryValue = el.options[el.selectedIndex].value;
    var divFormCategoryItem = document.getElementById('divFormCategoryItem');

    console.log("Valor: "+formCategoryValue)

    if(formCategoryValue === 'animals') {
        divFormCategoryItem.style.visibility='visible'
    } else {
        divFormCategoryItem.style.visibility='hidden'
    }

    if(formCategoryValue === 'animals'){

        var len=$("#formCategoryItem").children('option').length;

        if(len <= 1) {
            insertSelectCategoryItems(ajustText('dog'))
            insertSelectCategoryItems(ajustText('cat'))
            insertSelectCategoryItems(ajustText('horse'))
        }
    }

}

function downloadImage1() {
    var link = document.createElement('a');
    link.href = link_frame1;
    link.download = link_frame1;
    link.target = '_blank';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function downloadImage2() {
    var link = document.createElement('a');
    link.href = link_frame2;
    link.download = link_frame2;
    link.target = '_blank';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function downloadImage3() {
    var link = document.createElement('a');
    link.href = link_frame3;
    link.download = link_frame3;
    link.target = '_blank';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

var getJSON = function(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
    var status = xhr.status;
    if (status === 200) {
        callback(null, xhr.response);
    } else {
        callback(status, xhr.response);
    }
    };
    xhr.send();
};

function getImage(imgId) {
    getJSON('https://api.randomwebimages.com/image/random',
    function(err, data) {
        if (err !== null) {
            console.log('Something went wrong: ' + err);
        } else {
            document.getElementById('img_home'+imgId).src=data.image.link;

            if(imgId === 1)
                link_frame1 = data.image.link
            else if(imgId === 2)
                link_frame2 = data.image.link
            else if(imgId === 3)
                link_frame3 = data.image.link
        }
    });
}

function getRandomNumberBetween(min,max){
    return Math.floor(Math.random()*(max-min+1)+min);
}

function loadImages() {
    getImage(1);
    getImage(2);
    getImage(3);
}

window.onload = function() {
    loadImages();
};

function refreshPage()
{
    window.location.reload();
}