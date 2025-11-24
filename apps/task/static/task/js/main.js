// 取得csrf token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// 更新task狀態
async function updateTask(id, status) {
    const targetURL = '/api/v1/task/' + id;
    const csrftoken = getCookie('csrftoken');  // 取得 CSRF token
    const response = await fetch(
        targetURL,
        {
            method: 'POST',
            headers: {
                    'Content-Type': 'application/json',  // 使用json格式
                    'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(                    // body(POST)
                {
                    "status": status,
                }
            )
        }
    )
    return response
}
document.addEventListener("DOMContentLoaded", function() {
    const card = document.querySelector(".card");
    const objectId = card.dataset.id
    const select = document.getElementById("status");

    // 當select標籤 異動時
    select.addEventListener("change", function (event) {
        
        console.log("選擇的值:", this.value);
        console.log("Object id:", objectId);
        // var targetURL = '/api/v1/task/' + objectId;
        // console.log(targetURL);
        const response = updateTask(objectId, this.value);
    })
})
