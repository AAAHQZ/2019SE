// var DETAIL_IMAGE_SELECTOR = '[data-image-role="target"]';
var Login_Button = '[data-button="login"]';
var Signup_Button = '[data-button="signup"]';
var Username_Input = '[data-input="username"]';
var Password_Input = '[data-input="password"]';

var loginButton = document.querySelector(Login_Button);
var signupButton = document.querySelector(Signup_Button);
var username = document.querySelector(Username_Input).value;
var password = document.querySelector(Password_Input).value;

function initLogin() {
	loginButton.addEventListener('click', function () {
		$.ajax()
	});
}




function onInputFileChange() {
        var file = document.getElementById('file').files[0];
        var file2 = document.getElementById('file').value;
        // document.getElementById('classtext2').innerHTML = file2;
        var url = URL.createObjectURL(file);
        // console.log(url);
        document.getElementById("video-id").src = url;
        document.getElementById('classtext').innerHTML = "正在运行，请稍等"
        // document.getElementById("file").style.display="none";
        $.ajax({
          url:"/ajax_submit_set/",
          type:"GET",
          data:{
            'fileName': file2
          },
          success:function(ret){
            // console.log(data);
            var className = JSON.parse(ret);
            var classRow = className["str"];
            // classRow = className.join(" ");
            document.getElementById('classtext').innerHTML = classRow;
          }
        })
      }