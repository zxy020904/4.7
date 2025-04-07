// 解析微博链接，提取用户名
function extractUsername(input) {
    // 兼容不同微博链接格式
    const regex = /weibo\.com\/(?:u\/|profile\/)?([a-zA-Z0-9_]+)/;
    const match = input.match(regex);
    return match ? match[1] : input;
}

// 单个账号检测
function detectBot() {
    let input = document.getElementById("username").value.trim();
    if (!input) {
        alert("请输入微博链接");
        return;
    }

    let username = extractUsername(input);  // 解析微博账号

    fetch("/detect", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ username })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById("result");
        resultDiv.classList.remove("d-none", "alert-danger", "alert-success");

        if (data.isBot) {
            resultDiv.classList.add("alert-danger");
            resultDiv.innerHTML = `🚨 <strong>${username}</strong> 可能为机器人！`;
        } else {
            resultDiv.classList.add("alert-success");
            resultDiv.innerHTML = `✅ <strong>${username}</strong> 可能是正常用户！`;
        }
    })
    .catch(error => {
        console.error("请求失败", error);
        alert("检测失败，请检查网络连接或稍后再试！");
    });
}

// 处理 CSV 文件上传
function uploadCSV() {
    const fileInput = document.getElementById("fileUpload");
    if (fileInput.files.length === 0) {
        alert("请先选择一个 CSV 文件");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.length === 0) {
            alert("CSV 文件为空，请上传有效的文件！");
            return;
        }

        const botCount = data.filter(user => user.isBot).length;
        const normalCount = data.length - botCount;
        updateChart(botCount, normalCount);  // 更新图表
    })
    .catch(error => {
        console.error("上传失败", error);
        alert("上传失败，请检查网络连接或稍后再试！");
    });
}
