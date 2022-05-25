//pipeInfo

function addConcreteDiameter(){
    let htmlData = '';
    htmlData += '<option selected>파이프 관경을 선택해주세요</option>';
    for (var i = 300; i <=1200; i+=100) {
        htmlData += '<option value="' + i + '">' + i+ 'mm</option>';
    }
    htmlData += '<option value="1350">1350mm</option>';
    document.querySelector('.pipe-diameter').innerHTML = htmlData;
}        

function addSteelDiameter(){
    let htmlData = '';
    htmlData += '<option selected>파이프 관경을 선택해주세요</option>';
    for (var i = 300; i <=1200; i+=100) {
        htmlData += '<option value="' + i + '">' + i+ 'mm</option>';
    }
    document.querySelector('.pipe-diameter').innerHTML = htmlData;
}    

function addIronDiameter(){
    let htmlData = '';
    htmlData += '<option selected>파이프 관경을 선택해주세요</option>';
    htmlData += '<option value="80">80mm</option>';
    htmlData += '<option value="100">100mm</option>';
    htmlData += '<option value="150">150mm</option>';

    for (var i = 200; i <=800; i+=100) {
        htmlData += '<option value="' + i + '">' + i+ 'mm</option>';
    }
    document.querySelector('.pipe-diameter').innerHTML = htmlData;
}    

function addPlasticDiameter(){
    let htmlData = '';
    htmlData += '<option selected>파이프 관경을 선택해주세요</option>';
    for (var i = 200; i <=1200; i+=100) {
        htmlData += '<option value="' + i + '">' + i+ 'mm</option>';
    }
    document.querySelector('.pipe-diameter').innerHTML = htmlData;
}     