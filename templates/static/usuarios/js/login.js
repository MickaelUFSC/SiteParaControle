var btnSignin = document.querySelector("button#sign-in");
var btnSignup = document.querySelector("button#sign-up");

var body = document.querySelector("body");

btnSignin.addEventListener("click", function () {
   body.className = "sign-out"; 
});

btnSignup.addEventListener("click", function () {
    body.className = "sign-in";
})