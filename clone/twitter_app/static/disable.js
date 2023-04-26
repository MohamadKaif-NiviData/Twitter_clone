
   let post = document.getElementById("txtpost")
   let btn = document.getElementById("btnsubmit")
   let file_input = document.getElementById("file_input")
   btn.disabled = true
   file_input.addEventListener("change",function(){
   
   
   if(file_input.files.length == 0){
    btn.disabled = true
   }else{
    btn.disabled = false  
   }
    
})
    post.addEventListener("keypress",(e)=>{
        const value=e.currentTarget.value
        if(value === ""){
            btn.disabled = true
        }else{
            btn.disabled = false
        }
    } );