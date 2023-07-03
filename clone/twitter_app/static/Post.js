function CreatePost(){
   let post = document.getElementById("txtpost")
   let btn = document.getElementById("btnsubmit")
   // let file_input = document.getElementById("file_input")
    var user_id = document.getElementById('user_id')
    if(post ){
        console.log(post.value,'yes')
        console.log(user_id.value)
    }else{
        console.log('no')
    }
       fetch('http://127.0.0.1:8000/Tweet', {
        method: 'POST',
        body: JSON.stringify({
            user:user_id.value,
            post: post.value,


        }),
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
              'Content-type': 'application/json; charset=UTF-8',
        },
        credentials: "same-origin",
    }).then((response) =>
       {
           response.json()

       })
        .then((json) => {
            console.log(json)
            // var forms = document.getElementById('forms')
            // forms.innerHTML=`Post Creared`
            // post.value="Post Creared"
        })

}