<!DOCTYPE html>
<html lang="en">
<head>

  <!-- Basic Page Needs
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <meta charset="utf-8">
  <title>Your page title here :)</title>
  <meta name="description" content="">
  <meta name="author" content="">

  <!-- Mobile Specific Metas
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <meta name="viewport" content="width=device-width, initial-scale=1">


  <!-- CSS
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <link rel="stylesheet" href="css/bootstrap.min.css">
<!--  <link rel="stylesheet" href="css/bootstrap-theme.min.css">-->

  <!-- Favicon
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <link rel="icon" type="image/png" href="images/favicon.png">

</head>
<body>

  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">
    <div class="row user-profile" style="margin-top: 5%">
      <div class="col-md-offset-4 col-md-2">
        <img src={{user_info.profile_picture}} height="150" width="150">
      </div>
      <div class="col-md-2">
        <h4>{{user_info.username}}</h4>
        {{user_info.full_name}}<br>
        {{user_info.bio}}<br>
        {{user_info.website}}<br>
      </div>
    </div>
    <div class="row" id="followed-by">
      <h2>Followed by: </h2>
      %for user in users:
          <div class="row" style="margin: 1%">
            <div class="col-md-2">
              <a href="https://instagram.com/{{user[1]['user_followed_by']['username']}}" target="_blank"><img src="{{user[1]['user_followed_by']['profile_picture']}}" height="150" width="150"></a>
            </div>
            <div class="col-md-2">
                <p><h4>{{user[1]['user_followed_by']['username']}}</h4></p>
                <div id="follow-button-{{user[1]['user_followed_by']['id']}}">
                    <p><a class="btn btn-primary btn-sm" href="#">Follow</a></p>
                </div>
                Follows: {{user[1]['user_relationship']['outgoing_status']}}</br>
                Followed: {{user[1]['user_relationship']['incoming_status']}}</br>
                Private User: {{user[1]['user_relationship']['target_user_is_private']}}</br>
            </div>
            <div class="col-md-8">
                <table class="table table-responsive">
                    <tr>
                        %for media in user[1]['recent_media']:
                        <td>
                            <img src="{{media['images']['low_resolution']['url']}}" height="200" width="200" style="margin: 1%">
                        </td>
                        %end
                    </tr>
                </table>
            </div>
          </div>
      %end
    </div>
  </div>
    
  <script src="js/jquery-2.1.4.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  <script src="js/app.js"></script>

<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
</body>
</html>
