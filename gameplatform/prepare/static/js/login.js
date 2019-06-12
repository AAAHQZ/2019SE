// var DETAIL_IMAGE_SELECTOR = '[data-image-role="target"]';
var Login_Button = '[data-button="login"]';
var Signup_Button = '[data-button="signup"]';
var Username_Input = '[data-input="username"]';
var Password_Input = '[data-input="password"]';

var loginButton = document.querySelector(Login_Button);
var signupButton = document.querySelector(Signup_Button);

// var password = document.querySelector(Password_Input).value;
function initLogin() {
	loginButton.addEventListener('click', function () {
		var username = document.querySelector(Username_Input).value;
		var password = document.querySelector(Password_Input).value;
		$.ajax({
			url:"/logIn/",
			type:"GET",
			data:{
				'userID': username,
				'userPassword': password
			},
			success:function(ret) {
				var returnData = JSON.parse(ret);
				var logInStatus = returnData["logInStatus"];
				if (logInStatus = 1) {
					console.log('登陆成功!');
				} else if (logInStatus = 2) {
					console.log('昵称不存在!');
				} else if (logInStatus = 3) {
					console.log('密码错误!');
				}
			}
		})
	});
}


// function test() {
// 	loginButton.addEventListener('click', function () {
// 		var username = document.querySelector(Username_Input).value;
// 		console.log(username);
// 	});
// }
// test();
initLogin();