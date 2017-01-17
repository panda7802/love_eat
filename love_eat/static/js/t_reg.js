function reg() {
    text = document.getElementById("t_yzm").getAttribute("yzmVel");
    if (null == text) {
        alert("验证码获取失败，请重试");
        return;
    }
    inputYzm = document.getElementById("yzm").value;
    // console.log(hex_md5(inputYzm));
    inputYzm = hex_md5(inputYzm).substring(0, 8);
    if (inputYzm != text) {
        alert("验证码错误");
        return;
    }

    var familyName = document.getElementById("familyName").value;
    var passwd = document.getElementById("passwd").value;

    if (familyName.length < 1) {
        alert("名称必须大于6位");
        return;
    }
    if (passwd.length < 1) {
        alert("密码必须大于6位");
        return;
    }

    var sendData = "familyName=" + familyName;
    sendData += "&" + "passwd=" + hex_md5(passwd).substring(0, 8);
    $.ajax({
        type: "post",
        contentType: "application/x-www-form-urlencoded; charset=utf-8",
        async: false,
        url: "family_reg",
        data: sendData,
        cache: false,
        timeout: 6000,
        success: function (data) {
            try {
                var reg_res = new Function("return" + data)(); //转换后的JSON对象
                var res = reg_res.res;
                var action = reg_res.action;
                var msg = reg_res.msg;
                if (true != res) {
                    alert(msg);
                } else {
                    setCookie("db_family", familyName + "", 1);
                    window.location.href = action;
                }
            } catch (e) {
                alert(e)
            }

        },
        error: function (e) {
            alert("请求失败,请重试");
        }
    });
}


function check_login() {
    text = document.getElementById("t_yzm").getAttribute("yzmVel");
    if (null == text) {
        alert("验证码获取失败，请重试");
        return;
    }
    inputYzm = document.getElementById("yzm").value;
    inputYzm = hex_md5(inputYzm).substring(0, 8);
    if (inputYzm != text) {
        alert("验证码错误");
        return;
    }

    var familyName = document.getElementById("familyName").value;
    var passwd = document.getElementById("passwd").value;

    if (familyName.length < 1) {
        alert("名称必须大于6位");
        return;
    }
    if (passwd.length < 1) {
        alert("密码必须大于6位");
        return;
    }

    var sendData = "familyName=" + familyName;
    sendData += "&" + "passwd=" + hex_md5(passwd).substring(0, 8);
    $.ajax({
        type: "post",
        contentType: "application/x-www-form-urlencoded; charset=utf-8",
        async: false,
        url: "family_login",
        data: sendData,
        cache: false,
        timeout: 6000,
        success: function (data) {
            try {
                var reg_res = new Function("return" + data)(); //转换后的JSON对象
                var res = reg_res.res;
                var action = reg_res.action;
                var msg = reg_res.msg;
                if (true != res) {
                    alert(msg);
                } else {
                    setCookie("db_family", familyName + "", 1);
                    window.location.href = action;
                }
            } catch (e) {
                alert(e)
            }

        },
        error: function (e) {
            alert("请求失败,请重试");
        }
    });
}

function  login() {
    window.location.href = "login.html"
}

function  logout() {
    setCookie("db_family", "", 1);
    window.location.href = "index.html"
}
