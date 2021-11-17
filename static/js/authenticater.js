loginBtn = document.querySelector('#btn-login')
loginPage = document.querySelector('.logintoggle')

signupBtn = document.querySelector('#btn-signup')
signupPage = document.querySelector('.signuptoggle')
signupCloseBtn = document.querySelector('.clos-btn-signup')

blurBackground = document.querySelector('.background-blur')
closeBtn = document.querySelector('#close-btn')

signupBtn.addEventListener('click',()=>{
  signupPage.classList.toggle('active-signup');
  blurBackground.classList.toggle('active-BlurBackground');
});

loginBtn.addEventListener('click',()=>{
  loginPage.classList.toggle('active-login');
  blurBackground.classList.toggle('active-BlurBackground');
});

signupCloseBtn.addEventListener('click',()=>{
  signupPage.style.display="none";
  blurBackground.style.display="none";
});

closeBtn.addEventListener('click',()=>{
  loginPage.style.display="none";  
  blurBackground.style.display="none";
});

