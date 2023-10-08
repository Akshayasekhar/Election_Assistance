function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}


function validate(){
        var username = document.getElementById("username");
        var password = document.getElementById("password");

        if(username.value=="admin" && password.value=="1234")
        {
            alert("success");
            return true;
        }
        else{
            alert("error");
            return false;
          }
        }