$(function(){
	// 对表单内容进行验证的变量
	var error_name = false;
	var error_password = false;

	$('#name').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	// 对用户名进行判断
	function check_user_name(){
		var len = $('#name').val().length;
		if(len==0)
		{
			$('#name').next().html('请输入用户名');
			$('#name').next().show();
			error_name = true;
		}
		else
		{
			$('#name').next().hide();
			error_name = false;
			// 判断当前用户是否存在
			$.get('/user/register_exits/?uname='+$('#name').val(),function (data) {
				if(data.count == 0){
					$('#name').next().html('用户名不存在');
					$('#name').next().show();
					error_name = true;
				}else{
					$('#name').next().hide();
					error_name = false;
				}
			});
		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len == 0)
		{
			$('#pwd').next().html('请输入密码')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}
	}
	// 登陆判断
	$('#login_form').submit(function() {
		check_user_name();
		check_pwd();
		return error_name === false && error_password === false;
	});
});