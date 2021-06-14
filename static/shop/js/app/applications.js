// $('#myCarousel').carousel({
//     interval: 1000
// })
$(document).ready(function(){
 $('#myList a').on('click', function (e) {
    e.preventDefault()
    $(this).tab('show')
  })
  });

