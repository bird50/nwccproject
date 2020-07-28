$('.autoplay').slick({
  slidesToShow: 5,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
  responsive: [
      {
          breakpoint: 769,
          settings: {
              arrows: false,
              centerMode: true,
              centerPadding: '0px',
              slidesToShow: 4,
          }
      },
      
      {
          breakpoint: 426,
          settings: {
              arrows: false,
              centerMode: true,
              centerPadding: '0px',
              slidesToShow: 2,
          }
      }
  ]
});