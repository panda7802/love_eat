yzm_path = "/static/yzm/"

/**
*生成验证码
*/
function gen_yzm() {
	document.getElementById("t_yzm").src = "/static/img/loading.jpg";
	document.getElementById("yzm").value = "";
	setTimeout(function() {
		$.ajax({
			type:"get",
			contentType : "application/x-www-form-urlencoded; charset=utf-8",
	        async : true,
			url:"gen_yzm",
			data:"",
			cache:false,
			// dataType:"string",
			timeout : 6000,
			success:function(data) {
				var yzm_res = new Function("return " + data)(); //转换后的JSON对象
        		var res = yzm_res.res;
        		var text = yzm_res.text;
        		var path = yzm_res.path;
        		if (T_SUCCESS != res) {
        			alert("生成验证码失败,请重试");	
        		} else {
        			document.getElementById("t_yzm").src = yzm_path + path;
        			document.getElementById("t_yzm").setAttribute("yzmVel",text);
        		}
			},
			error:function(e) {
				alert("获取验证码请求失败,请重试");
			}
		});
	}, 1000);

}