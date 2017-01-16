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
    var sendData ="familyName=" + familyName + "&" + "passwd=" + passwd;
    $.ajax({
        type: "get",
        contentType: "application/x-www-form-urlencoded; charset=utf-8",
        async: false,
        url: "famili_reg",
        data: sendData,
        cache: false,
        timeout: 6000,
        success: function (data) {
            alert(data);
        },
        error:function(e) {
            alert("请求失败,请重试");
            console.log(e.XMLHttpRequest.status);
        }
    });
}
