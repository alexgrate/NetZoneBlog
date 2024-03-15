window.addEventListener("scroll", function(){
    const header = document.querySelector("#header-2"); // Select the #header-2 element
    header.classList.toggle("sticky", window.scrollY > 0);
});

var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
document.getElementById("date").innerHTML = new Date().toLocaleDateString(undefined, options);


let Sidemenu =  document.querySelector('#sidebar')
let Sidebar = document.querySelector('#menu-icon')
let closeSidebar = document.querySelector('#closeMenu-icon')

Sidebar.onclick = () => {
    Sidemenu.classList.toggle('active')
    searchForm.classList.remove('active')
}

document.getElementById('closeMenu-icon').addEventListener('click', function() {
    document.getElementById('sidebar').classList.remove('active');
});


let searchForm = document.querySelector('#search')

document.querySelector('#search-btn').onclick = () =>{
    searchForm.classList.toggle('active')
    Sidemenu.classList.remove('active')
}


var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 10,
    freeMode: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        400: {
            slidesPerView: 2,
            spaceBetween: 10,
        },
        786: {
            slidesPerView: 3,
            spaceBetween: 10,
        },
        1024: {
            slidesPerView: 4,
            spaceBetween: 10,
        },
        },
  });

var swiper = new Swiper(".myMoviesSwiper", {
    slidesPerView: 1,
    spaceBetween: 10,
    freeMode: true,
    pagination: {
    el: ".swiper-pagination",
    clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        400: {
            slidesPerView: 2,
            spaceBetween: 10,
        },
        786: {
            slidesPerView: 3,
            spaceBetween: 10,
        },
        1024: {
            slidesPerView: 4,
            spaceBetween: 10,
        },
        },
});

var swiper = new Swiper(".myEntertainSwiper", {
    slidesPerView: 3,
    grid: {
      rows: 1,
    },
    spaceBetween: 30,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    autoplay: {
        delay: 2000, // Set the delay in milliseconds (e.g., 5000ms = 5 seconds)
        disableOnInteraction: false, // Set to false to continue autoplay even when user interacts with the swiper
    },
    loop: true, // Enable infinite loop
    breakpoints: {
        50: {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        400: {
            slidesPerView: 1,
            spaceBetween: 10,
        },
        786: {
            slidesPerView: 2,
            spaceBetween: 10,
        },
        1024: {
            slidesPerView: 3,
            spaceBetween: 10,
        },
    },
});


let rightbar = document.getElementsByClassName('right');
let rightbarContent = document.getElementsByClassName('most_viewed');

window.onscroll = () => {
    let scrollTop = window.scrollY
    let viewportHeight = window.innerHeight
    let contentHeight = rightbarContent.getBoundingClientRect().height

    if(scrollTop >= contentHeight - viewportHeight) {
        rightbarContent.style.position = "fixed"
    }
    else{
        rightbarContent.style.position = ""
    }
}

function handleClick(event) {
    event.preventDefault();}



// ****************

// HOME.HTML SECTION

// *****************

const loadBtn = document.getElementById('load-btn')
const spinner = document.getElementById('spinner-box')
const total = JSON.parse(document.getElementById('json-total').textContent)
const alert = document.getElementById('alert')

function loadmoreAnime(){
    var _current_item = $('.latest_news_box').length
    const anime_container = document.getElementById('latest_news_container')

    $.ajax({
        url : 'load/',
        type : 'GET',
        data : {
            'total_anime' : _current_item
        },
        beforeSend : function(){
            loadBtn.classList.add('not-visible')
            spinner.classList.remove('not-visible')
        },
        success : function(response){
            const data = response.animes
            spinner.classList.add('not-visible')

            data.map(anime => {
                anime_container.innerHTML +=`<div class="latest_news_box">

                                                <div class="latest_img">
                                                    <img src="${ anime.Movie_Img }" alt="">
                                                </div>


                                                <div class="latest_news_text">

                                                    <span class="uil uil-video left-icon"></span>


                                                    <div class="latest_news_writeup">
                                                    <span onclick="window.location.href='${anime.Netblog_category_link}'" class="tag">${anime.Movie_Type}</span>
                                                    <a href="${anime.Netblog_pages_link}">${ anime.Movie_Title }</a>
                                                        ${ anime.Movie_Season ? `<a href="${anime.Netblog_season_categories_link}" class="sub_title">${anime.Movie_Season} - ${anime.Movie_Episode}</a>` : ''}
                                                        <p>${ anime.Movie_Body }</p>
                                                        <a href="${anime.Netblog_pages_link}" class="btn btn-secondary">View more</a>
                                                    </div>
                                                    
                                                </div>
                                            </div>`



            })
            if(_current_item == total){
                alert.classList.remove('not-visible')
            }else{
                loadBtn.classList.remove('not-visible')
            }
        },
        error : function(err){
            console.log(err)
        }
    })
}

loadBtn.addEventListener('click', () => {
    loadmoreAnime()
})

// ****************

// END OF HOME.HTML SECTION

// *****************


