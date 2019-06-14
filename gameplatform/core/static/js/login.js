
var Login_Button = '[data-button="login"]';
var Signup_Button = '[data-button="signup"]';
var Username_Input = '[data-input="username"]';
var Password_Input = '[data-input="password"]';
var Input_Warning = '[data-warning="inputWarning"]'

var loginButton = document.querySelector(Login_Button);
var signupButton = document.querySelector(Signup_Button);
var inputWarning = document.querySelector(Input_Warning);

function initLogin() {
	loginButton.addEventListener('click', function () {
		var username = document.querySelector(Username_Input).value;
		var password = document.querySelector(Password_Input).value;
		if (username.length == 0) {
			inputWarning.innerText = "账号不能为空";
		} else if (password.length == 0) {
			inputWarning.innerText = "密码不能为空";
		} else {
			inputWarning.innerText = "";
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
					if (logInStatus == 1) {
						inputWarning.innerText = "登陆成功!";
						console.log('登陆成功!');
					} else if (logInStatus == 2) {
						inputWarning.innerText = "昵称不存在!";
						console.log('昵称不存在!');
					} else if (logInStatus == 3) {
						inputWarning.innerText = "密码错误!";
						console.log('密码错误!');
					}
				}
			})
		}
	});

	signupButton.addEventListener('click', function () {
		var username = document.querySelector(Username_Input).value;
		var password = document.querySelector(Password_Input).value;
		if (username.length == 0) {
			inputWarning.innerText = "账号不能为空";
		} else if (password.length == 0) {
			inputWarning.innerText = "密码不能为空";
		} else {
				inputWarning.innerText = "";
				$.ajax({
				url:"/signUp/",
				type:"GET",
				data:{
					'userID': username,
					'userPassword': password
				},
				success:function(ret) {
					var returnData = JSON.parse(ret);
					var signUpStatus = returnData["signUpStatus"];
					if (signUpStatus == 0) {
						inputWarning.innerText = "昵称已存在!";
						console.log('昵称已存在!');
					} else if (signUpStatus == 1) {
						inputWarning.innerText = "注册成功!";
						console.log('注册成功!');
					}
				}
			})
		}
	});
}

initLogin();