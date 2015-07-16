// When scrolled to bottom of page, request data to /user_followed_by/, then insert the data into the view

//import insert-user;


function app() {
    // When scrolled to bottom of page, request data to /user_followed_by/, then insert the data into the view
    $(window).scroll(function() {
        if($(window).scrollTop() + $(window).height() > $(document).height() - 10) {
            $.post('/user_followed_by', { req_more: 'true' }, function(response){
                if (response == "End of List") {
                    alert(response);
                } else {
                    var response = JSON.parse(response);
    //                console.log(response[0]);
                    var content = ''
                    for(var i = 0; i < response.length; i++) {
    //                    console.log(response[i][1])
                        var profile_pic = 
                            "<div class=\"col-md-2\">\n" + 
                                "\t<a href=\"https://instagram.com/" + response[i][1]['user_followed_by']['username'] + "\" target=\"_blank\">\n" + 
                                    "\t\t<img src=\"" + response[i][1]['user_followed_by']['profile_picture'] + 
                                        "\" height=\"150\" width=\"150\">\n" + 
                                "\t</a>\n" + 
                            "</div>\n";
    //                    console.log(profile_pic);
                        var user_info = 
                            "<div class=\"col-md-2\">\n" + 
                                "\t<p><h4>" + response[i][1]['user_followed_by']['username'] + "</h4></p>\n" +
                                "\t<div id=\"follow-button-" + response[i][1]['user_followed_by']['id'] + "\">\n" +
                                    "\t\t<p><a class=\"btn btn-primary btn-sm\" href=\"#\">Follow</a></p>\n" + 
                                "\t</div>\n" + 
                                "\tFollows: " + response[i][1]['user_relationship']['outgoing_status'] + "</br>\n" + 
                                "\tFollowed: " + response[i][1]['user_relationship']['incoming_status'] + "</br>\n" + 
                                "\tPrivate User: " + response[i][1]['user_relationship']['target_user_is_private'] + "</br>\n" + 
                            "</div>\n";
//                        console.log(user_info);
    //                    console.log("response[i][1]['recent_media'].length " + response[i][1]['recent_media'].length);
    //                    console.log("response[i][1]['recent_media'] == 0 " + response[i][1]['recent_media'] == 0);
                        var medias = '';
                        for(var j = 0; j < response[i][1]['recent_media'].length; j++) {
                            if (response[i][1]['recent_media'].length == 0) {
                                medias = '';
                            } else {
    //                            console.log(response[i][1]['recent_media'][j]['images']['standard_resolution']['url']);
                                medias = medias + 
                                    "\t\t\t<td>\n" + 
                                        "\t\t\t\t<img src=\"" + 
                                            response[i][1]['recent_media'][j]['images']['standard_resolution']['url'] + 
                                            "\" height=\"200\" width=\"200\" style=\"margin: 1%\">\n" + 
                                    "\t\t\t</td>\n";

                            }
                        }

                        var recent_media = 
                            "<div class=\"col-md-8\">\n" + 
                                "\t<table class=\"table table-responsive\">\n" + 
                                    "\t\t<tr>\n" + 
                                        medias + 
                                    "\t\t</tr>\n" + 
                                "\t</table>\n" + 
                            "</div>\n";

    //                    console.log(recent_media);


                        content = content + 
                            "<div class=\"row\" style=\"margin: 1%\">\n" + 
                            profile_pic + user_info + recent_media + 
                            "</div>\n";
                    }
    //                document.getElementById("followed-by").appendChild(content)
                    $('#followed-by').append(content);                    
                }
            });
        }
    });
}

window.onload = app();
