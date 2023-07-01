function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}




function Like(t_id) {
    console.log(t_id)
    var user_id = document.getElementById('user_id')
    if (user_id) {
        console.log(user_id.value
            , 'yes id')
    } else {
        console.log('no id')
    }

    fetch('http://127.0.0.1:8000/Like', {
        method: 'POST',
        body: JSON.stringify({
            tweet: t_id,
            user: user_id.value,

        }),
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
            'Content-type': 'application/json; charset=UTF-8',
        },
        credentials: "same-origin",
    }).then((response) =>
        response.json())
        .then((json) => console.log(json));


}

