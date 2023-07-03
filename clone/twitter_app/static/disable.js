
   let post = document.getElementById("txtpost")
    let btn = document.getElementById("btnsubmit")
   // let file_input = document.getElementById("file_input")
   

//    file_input.addEventListener("change",function(){
//    if(file_input.files.length == 0){
//     btn.disabled = true
//    }else{
//     btn.disabled = false
//    }
// })
    post.addEventListener("input",(e)=>{
        console.log(e.currentTarget.value);
        const Value=e.currentTarget.value
       
        
        if(Value === "" || Value.trim() == "" ){
            btn.disabled = true
        }else{
            btn.disabled = false

        }

    } );