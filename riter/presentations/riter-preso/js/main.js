$( document ).ready(function() {

    var contentPlacement = $('.header').position().top + $('.header').outerHeight();
    $('#timeline').css('margin-top', contentPlacement + 0.5);


  $("#timeline-link").click(function() {
      $('html, body').animate({
          scrollTop: $("#timeline").offset().top - ($('.header').outerHeight())
      }, 500);
  });

  $("#characters-link").click(function() {
      $('html, body').animate({
          scrollTop: $("#characters").offset().top - ($('.header').outerHeight())
      }, 500);
  });

  $("#samples-link").click(function() {
      $('html, body').animate({
          scrollTop: $("#samples").offset().top - ($('.header').outerHeight())
      }, 500);
  });

  $("#application-link").click(function() {
      $('html, body').animate({
          scrollTop: $("#application").offset().top - ($('.header').outerHeight())
      }, 500);
  });

  $( ".image" ).each(function(index) {
    $(this).on("click", function(){
       $(this).nextAll('.modal').removeClass('hide').addClass('show');
       $('.uber').addClass('fade');
       $('body').css('overflow','hidden');
    });
});

  $(".uber").click(function() {
  if ($(this).hasClass('fade')) {
        $('.modal').addClass('hide');
        $(this).removeClass('fade');
        $('body').css('overflow','auto');
    }
});

});