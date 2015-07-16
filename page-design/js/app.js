// When scrolled to bottom of page, request data to /user_followed_by/, then insert the data into the view

//import insert-user;


function app() {
    // When scrolled to bottom of page, request data to /user_followed_by/, then insert the data into the view
    $(window).scroll(function() {
        if($(window).scrollTop() + $(window).height() > $(document).height() - 10) {
            $.post('/user_followed_by', { req_more: 'true' }, function(response){
                var response = JSON.parse(response);
                console.log(response);
//                for(var i = 0; i < response.length; i++) {
//                    console.log(response[i].username)
//                }
//                document.getElementById("followed-by").appendChild(content)
            });
        }
    });
}

window.onload = app();
