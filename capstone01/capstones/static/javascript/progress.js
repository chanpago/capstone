//progress bar 부분
    var progressBar = $('.progress-bar');
    var progressNumber=0;

    var intervalId= setInterval(function(){  //progress bar 동작
   
            progressNumber+=2;
            progressBar.css('width',progressNumber+'%');
            progressBar.attr('aria-valuenow',progressNumber);
            //console.log(progressNumber);

            if(progressNumber=="100"){
                clearInterval(intervalId);

                //버튼 동작
                $('.btn-outline-secondary').unbind('click');
                document.getElementById('icon2').innerHTML='<i class="bi2 bi-check-circle"></i>';
            }
    },100);

  

    // const a =  document.querySelector('.progress-bar');
    // a.addEventListener(showIcon());

    // function showIcon() {
    //     // document.getElementById('icon2').innerHTML='<i class="bi2 bi-check-circle"></i>';
    //     if(a.width==514){
    //         document.getElementById('icon2').innerHTML='<i class="bi2 bi-check-circle"></i>';
    //     }
    // }