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
    for (var i = 200; i <=1000; i+=100) {
        htmlData += '<option value="' + i + '">' + i+ 'mm</option>';
    }
    htmlData += '<option value="1200">1200mm</option>';
    document.querySelector('.pipe-diameter').innerHTML = htmlData;
}     

function calcCost(){
    var length = document.getElementById("pipeLength").value;
    var radio = document.getElementsByName('gridRadios');
    var d = document.getElementById("pipeDiameter");
    var diameter = d.options[d.selectedIndex].value;

    var radio2 = document.getElementsByName('inlineRadioOptions');
    var pavement=0;
    radio2.forEach((node) => {
            if(node.checked)  {
                pavement =node.value;
            }
        }) 

    var cost=0;
    
    radio.forEach((node) => {
        if(node.checked)  {
            var pipetype =node.value;
            if(pipetype == "콘크리트관"){
                if(pavement=="비포장"){
                    if(diameter==300){cost = 512740*length;}
                    else if(diameter==400){cost = 580188*length;}
                    else if(diameter==500){cost = 624861*length;}
                    else if(diameter==600){cost = 705821 *length;}
                    else if(diameter==700){cost = 782918 *length;}
                    else if(diameter==800){cost = 854676 *length;}
                    else if(diameter==900){cost = 945775 *length;}
                    else if(diameter==1000){cost = 1051853  *length;}
                    else if(diameter==1100){cost = 1188358  *length;}
                    else if(diameter==1200){cost = 1313909  *length;}
                    else if(diameter==1350){cost = 1519849  *length;}
                    
                }
                else{
                    if(diameter==300){cost = 782541 *length;}
                    else if(diameter==400){cost = 859007 *length;}
                    else if(diameter==500){cost = 912820 *length;}
                    else if(diameter==600){cost = 1016585 *length;}
                    else if(diameter==700){cost = 1102578 *length;}
                    else if(diameter==800){cost = 1183365 *length;}
                    else if(diameter==900){cost = 1283451 *length;}
                    else if(diameter==1000){cost = 1398649  *length;}
                    else if(diameter==1100){cost = 1557399  *length;}
                    else if(diameter==1200){cost = 1691805  *length;}
                    else if(diameter==1350){cost = 1910605  *length;}
                    
                }
                
            }
            else if(pipetype == "강관"){
                if(pavement=="비포장"){
                    if(diameter==300){cost = 707247 *length;}
                    else if(diameter==400){cost = 827275 *length;}
                    else if(diameter==500){cost = 935411 *length;}
                    else if(diameter==600){cost = 1068860 *length;}
                    else if(diameter==700){cost = 1206659*length;}
                    else if(diameter==800){cost = 1373571 *length;}
                    else if(diameter==900){cost = 1509424 *length;}
                    else if(diameter==1000){cost = 1730822 *length;}
                    else if(diameter==1100){cost = 1990647 *length;}
                    else if(diameter==1200){cost = 2234280 *length;}
                }       
                else{
                    if(diameter==300){cost = 977038  *length;}
                    else if(diameter==400){cost = 1106094 *length;}
                    else if(diameter==500){cost = 1223371 *length;}
                    else if(diameter==600){cost = 1379624 *length;}
                    else if(diameter==700){cost = 1526319 *length;}
                    else if(diameter==800){cost = 1702260 *length;}
                    else if(diameter==900){cost = 1847090 *length;}
                    else if(diameter==1000){cost = 2077609 *length;}
                    else if(diameter==1100){cost = 2359688 *length;}
                    else if(diameter==1200){cost = 2612176 *length;}
                }                
            } 
            else if(pipetype == "주철관"){
                if(pavement=="비포장"){
                    if(diameter==80){cost = 91404 *length;}
                    else if(diameter==100){cost = 102960 *length;}
                    else if(diameter==150){cost = 139786 *length;}
                    else if(diameter==200){cost = 172293 *length;}
                    else if(diameter==300){cost = 248738 *length;}
                    else if(diameter==400){cost = 348039 *length;}
                    else if(diameter==500){cost = 453129 *length;}
                    else if(diameter==600){cost = 563069 *length;}
                    else if(diameter==700){cost = 708878 *length;}
                    else if(diameter==800){cost = 860005 *length;}
                }       
                else{
                    if(diameter==80){cost = 309684 *length;}
                    else if(diameter==100){cost = 323665 *length;}
                    else if(diameter==150){cost = 366708 *length;}
                    else if(diameter==200){cost = 405664 *length;}
                    else if(diameter==300){cost = 494561 *length;}
                    else if(diameter==400){cost = 606519 *length;}
                    else if(diameter==500){cost = 724142 *length;}
                    else if(diameter==600){cost = 846789 *length;}
                    else if(diameter==700){cost = 1005274 *length;}
                    else if(diameter==800){cost = 1169007 *length;}
                } 
            } 
            else{
                if(pavement=="비포장"){
                    if(diameter==200){cost = 476678 *length;}
                    else if(diameter==300){cost = 525101 *length;}
                    else if(diameter==400){cost = 625778 *length;}
                    else if(diameter==500){cost = 711507 *length;}
                    else if(diameter==600){cost = 810869 *length;}
                    else if(diameter==700){cost = 919311 *length;}
                    else if(diameter==800){cost = 1030780 *length;}
                    else if(diameter==900){cost = 1120686 *length;}
                    else if(diameter==1000){cost = 1252157 *length;}
                    else if(diameter==1200){cost = 1519329 *length;}
                }       
                else{
                    if(diameter==200){cost = 737848 *length;}
                    else if(diameter==300){cost = 794902 *length;}
                    else if(diameter==400){cost = 904597 *length;}
                    else if(diameter==500){cost = 999476 *length;}
                    else if(diameter==600){cost = 1121644 *length;}
                    else if(diameter==700){cost = 1238972 *length;}
                    else if(diameter==800){cost = 1359468 *length;}
                    else if(diameter==900){cost = 1458352 *length;}
                    else if(diameter==1000){cost = 1598943 *length;}
                    else if(diameter==1200){cost = 1897235 *length;}
                }           
            }
        }
    }) 
        return cost;
}


function showCost(){
    var length = document.getElementById("pipeLength").value;
    var radio = document.getElementsByName('gridRadios');
    var pipetype;
    radio.forEach((node) => {
        if(node.checked)  {
            pipetype =node.value;
        }
    }) 

    var d = document.getElementById("pipeDiameter");
    var diameter = d.options[d.selectedIndex].value;

    var radio2 = document.getElementsByName('inlineRadioOptions');
    var pavement;
    radio2.forEach((node) => {
            if(node.checked)  {
                pavement=node.value;
            }
        }) 
    var cost=0;
    cost=Math.round(calcCost()/10000);
    
    if(!length||!pipetype||diameter=='파이프 관경을 선택해주세요' ||!pavement){
        alert("하수관의 정보를 빠짐없이 입력해주세요!");
    }else{
        let htmlData = '';
        htmlData += '<div class="container px-4 px-lg-5">';
        htmlData += '<table class="table">';
        htmlData += '<thead><tr><th scope="col">하수관 정보</th><th scope="col">입력한 정보</th></tr></thead>';
        htmlData += '<tbody>';
        htmlData += '<tr><th scope="row">파이프 총 길이</th><td>'+length+'m</td></tr>';
        htmlData += '<tr><th scope="row">하수관 종류</th><td>'+pipetype+'</td></tr>';
        htmlData += '<tr><th scope="row">파이프의 관경</th><td>'+diameter+'mm</td></tr>';
        htmlData += '<tr><th scope="row">도로 포장 상태</th><td>'+pavement+'도로</td></tr>';
        htmlData += '<tr style="border-top:solid 2px black"><th scope="row">예상 교체 비용</th><td>약 '+cost+'만원</td></tr>';
        htmlData += '</tbody>';
        htmlData += '</table>';
        htmlData += '</div>';

        document.location.href='#page2';
        
        // 홈버튼 활성화
        const target = document.getElementById('gohomeBtn');
        target.disabled = false;

        document.querySelector('.cost-result').innerHTML = htmlData;
    }
 
}     
