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
var form = document.getElementById('forms')
form.addEventListener('submit',function (e){

        e.preventDefault()
        var tweet_id= document.getElementById(`t_id1{{t.id}}`).value
        console.log(tweet_id,'tweet_id')
        var user_id = document.getElementById(`user_id1{{user.id}}`).value
        console.log(user_id,'user_id')

        fetch('http://127.0.0.1:8000/Like',{
                method:'POST',
                body:JSON.stringify({
                        tweet:tweet_id,
                        user:user_id,
                        value:'Unlike'
                }),
                headers: {
          "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
                    'Content-type': 'application/json; charset=UTF-8',
        },
             credentials: "same-origin",
        }).then((response)=>{
                response.json()
                console.log(response)
        })

            .then((json)=>{
                   console.log(json)
            })

})

function Unlike(t_id){
    console.log(t_id)
    var user_id = document.getElementById('user_id1')
    if(user_id){
        console.log(user_id.value,'yes tweet_id')
    }else{
        console.log('no tweet_id')
    }
 fetch('http://127.0.0.1:8000/Like',{
                method:'POST',
                body:JSON.stringify({
                        tweet:t_id,
                        user:user_id.value,

                }),
                headers: {
          "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
                    'Content-type': 'application/json; charset=UTF-8',
        },
             credentials: "same-origin",
        }).then((response)=>{
                response.json()
                console.log(response)
        })

            .then((json)=>{
                   console.log(json)
            })



}