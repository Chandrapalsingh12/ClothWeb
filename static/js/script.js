burger = document.querySelector('.burger')
navbar = document.querySelector('.nav-bar')
leftNav = document.querySelector('.left-nav')
middleNav = document.querySelector('.middle-nav')
rightNav = document.querySelector('.right-nav')
logog = document.querySelector('.reslogo')
nav_close = document.querySelector('.responsive-searchbar');


burger.addEventListener('click',()=>{
    navbar.classList.toggle('h-nav');
    leftNav.classList.toggle('v-cls');
    middleNav.classList.toggle('v-cls');
    rightNav.classList.toggle('v-cls');
    nav_close.classList.toggle('s-3');
    // logog.classList.toggle('logotoggle');
})








// Slider

var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 3000); 
}
messageshid = document.querySelector('.messagecls');

setTimeout(() => { 
  messageshid.style.display="none";

 },3000)

$('.slick-slider').slick({
  slidesToShow: 4,
  infinite: false,
  slidesToScroll: 1,
  autoplay: false,
  autoplaySpeed: 2000,
  prevArrow:'<i class="left-arrow fas fa-chevron-left"></i>',
  nextArrow:`<i class="right-arrow fas fa-chevron-right"></i>`,
  responsive: [
    {
      breakpoint: 1124,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: false,
      }
    },
    {
      breakpoint: 1050,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    },
  ]
});

$('.allitems').slick({
  slidesToShow: 7,
  slidesToScroll: 1,
  autoplay: false,
  autoplaySpeed: 2000,
  infinite:false,
  prevArrow:false,
  nextArrow:false,
  responsive: [
    {
      breakpoint: 1224,
      settings: {
        slidesToShow: 5,
        slidesToScroll: 3,
        infinite: false,
      }
    },
    {
      breakpoint: 1124,
      settings: {
        slidesToShow: 4,
        slidesToScroll: 3,
        infinite: false,
      }
    },
    {
      breakpoint: 1050,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    }
  ]
});


document.querySelector("#showprod").addEventListener("click",()=>{
  alert("Your Product Added successfully to the cart ")
})
