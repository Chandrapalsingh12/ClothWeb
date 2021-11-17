if (localStorage.getItem('cart') == null){
    var cart = {};
    }
    else{
      cart = JSON.parse(localStorage.getItem('cart'));
      document.getElementById('cartsect').innerHTML = Object.keys(cart).length;
      document.getElementById('cartsectresponsive').innerHTML = Object.keys(cart).length;
    }
    
    $('.cart').click(function(){
      console.log("Cart Clicked")
      var idStr = this.id.toString();
      console.log(idStr)
      if(cart[idStr] !=undefined){
        qty = cart[idStr][0] + 1;
      }
      else{
        qty = 1;
        name = document.getElementById('name'+idStr).innerHTML;
        price = document.getElementById('itemprice'+idStr).innerHTML;
        cart[idStr] = [qty, name, parseInt(price)];
      }
      console.log(cart)
      localStorage.setItem('cart', JSON.stringify(cart));
      document.getElementById('cartsect').innerHTML = Object.keys(cart).length;
      document.getElementById('cartsectresponsive').innerHTML = Object.keys(cart).length;

    });


