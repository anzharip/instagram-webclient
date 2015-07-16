import bottle
import beaker.middleware
from bottle import route, redirect, post, run, request, response, hook, template, static_file
from instagram import client, subscriptions
import json
from Queue import Queue
from threading import Thread
from types import *
from time import time


bottle.debug(True)

session_opts = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}

app = beaker.middleware.SessionMiddleware(bottle.app(), session_opts)

CONFIG = {
    'client_id': '47f3adaae6a245c7bca634f7d85e8fa3',
    'client_secret': 'b4a9405a9e184d3db73a93f42f655e09',
    'redirect_uri': 'http://127.0.0.1:8515/oauth_callback'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)

@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']

def process_tag_update(update):
    print(update)

reactor = subscriptions.SubscriptionsReactor()
reactor.register_callback(subscriptions.SubscriptionType.TAG, process_tag_update)

# Static Routes
@route('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@route('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/images')

@route('/fonts/<filename:re:.*\.ttf>')
def images(filename):
    return static_file(filename, root='static/fonts')

@route('/')
def home():
    try:
        url = unauthenticated_api.get_authorize_url(scope=["likes","comments", "relationships"])
        return template('login', url=url)
    except Exception as e:
        print(e)

@route('/oauth_callback')
def on_callback():
    code = request.GET.get("code")
    if not code:
        return 'Missing code'
    try:
        access_token, user_info = unauthenticated_api.exchange_code_for_access_token(code)
        if not access_token:
            return 'Could not get access token'
        api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
        request.session['access_token'] = access_token
        print access_token
    except Exception as e:
        print(e)
    return find_user()

@route('/find_user')
def find_user():
	return template('find_user')

@route('/user_followed_by')
def user_followed_by():
    username = request.GET.get('username')
    access_token = request.session['access_token']
    content = ''
    if not access_token:
        return 'Missing Access Token'
    try:
        time1 = time()
        request.session['endOfFile'] = False
        api = client.InstagramAPI(access_token=access_token, 
                                  client_secret=CONFIG['client_secret'])
        user_search = api.user_search(q=username, count=1)
        user_info = api.user(user_search[0].id)
        request.session['user_info'] = user_info
#        user_followed_by, next = api.user_followed_by(user_info.id)
#        print user_followed_by
        users = []
        def func1(user):
            if api.user_relationship(user[1].id).target_user_is_private == False:
                users.append([user[0], dict(user_followed_by=user[1], 
                                            recent_media=api.user_recent_media(user_id=user[1].id, 
                                            count=5)[0], 
                                            user_relationship=api.user_relationship(user[1].id))])
#                print user[1].id
            else:
                users.append([user[0], dict(user_followed_by=user[1], recent_media={}, 
                                            user_relationship=api.user_relationship(user[1].id))])
#                print user[1].id

        q = Queue(maxsize=0)
        num_threads = 50

        def do_stuff(q):
            while True:
                func1(q.get())
                q.task_done()

        for i in range(num_threads):
            worker = Thread(target=do_stuff, args=(q,))
#            print 'Worker Started!'
            worker.setDaemon(True)
            worker.start()

#        api = client.InstagramAPI(access_token=access_token, 
#                                  client_secret=CONFIG['client_secret'])
        user_followed_by, next = api.user_followed_by(user_id=user_info.id, count=15)
        request.session['next_url'] = next
        num = 0
        for user in user_followed_by:
            user = [num, user]
#            print user
            q.put(user)
            num = num + 1

        q.join()
        users.sort(key=lambda pair: pair[0])
        
        for user in users:
            recent_media_ = []
            if isinstance(user[1]['recent_media'], list) == True: 
                for media in user[1]['recent_media']:     
                    tags = []
                    if hasattr(media, 'tags'):
                        for tag in media.tags:
                            tags.append(tag.__dict__)
                    media.tags = tags

                    comments = []
                    if hasattr(media, 'comments'):
                        for comment in media.comments:
                            comment.created_at = comment.created_at.isoformat()
                            comment.user = comment.user.__dict__
                            comments.append(comment.__dict__)
                    media.comments = comments

                    if hasattr(media, 'caption'):
                        if type(media.caption) is not NoneType:
                            if hasattr(media.caption, 'created_at'):
                                media.caption.user = media.caption.user.__dict__
                                media.caption.created_at = media.caption.created_at.isoformat()
                            media.caption = media.caption.__dict__

                    if hasattr(media, 'user'):
                        media.user = media.user.__dict__

                    if hasattr(media, 'created_time'):
                        media.created_time = media.created_time.isoformat()

                    if hasattr(media, 'images'):
                        media.images['low_resolution'] = media.images['low_resolution'].__dict__
                        media.images['standard_resolution'] = media.images['standard_resolution'].__dict__
                        media.images['thumbnail'] = media.images['thumbnail'].__dict__  

                    if hasattr(media, 'videos'):
                        media.videos['low_resolution'] = media.videos['low_resolution'].__dict__
                        media.videos['standard_resolution'] = media.videos['standard_resolution'].__dict__
                        media.videos['low_bandwidth'] = media.videos['low_bandwidth'].__dict__  

                    likes = []
                    if hasattr(media, 'likes'):
                        for like in media.likes:
                            likes.append(like.__dict__)
                    media.likes = likes

                    if hasattr(media, 'location'):
                        if hasattr(media.location, 'point'):
                            if type(media.location.point) is not NoneType:
                                media.location.point = media.location.point.__dict__
                        media.location = media.location.__dict__            
                    recent_media_.append(media.__dict__)
            user[1]['recent_media'] = recent_media_
            user[1]['user_followed_by'] = user[1]['user_followed_by'].__dict__
            user[1]['user_relationship'] = user[1]['user_relationship'].__dict__
        data = {'user_info': user_info, 'users': users}
        content = template('user_followed_by', **data)
    except Exception as e:
        print(e)
    print 'Execution time: ', time() - time1
#    print json.dumps(users)
    return content

@post('/user_followed_by')
def post_user_followed_by():
    if request.forms.get('req_more') == 'true':
        access_token = request.session['access_token']
        users = []
        if not access_token:
            return 'Missing Access Token'
        try:
            if request.session['endOfFile'] == False:
                api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
                
                def func1(user):
                  if api.user_relationship(user[1].id).target_user_is_private == False:
                      users.append([user[0], dict(user_followed_by=user[1], 
                                                  recent_media=api.user_recent_media(user_id=user[1].id, 
                                                  count=5)[0], 
                                                  user_relationship=api.user_relationship(user[1].id))])
                  else:
                      users.append([user[0], dict(user_followed_by=user[1], recent_media={}, 
                                                  user_relationship=api.user_relationship(user[1].id))])
                q = Queue(maxsize=0)
                num_threads = 50

                def do_stuff(q):
                    while True:
                        func1(q.get())
                        q.task_done()

                for i in range(num_threads):
                    worker = Thread(target=do_stuff, args=(q,))
                    worker.setDaemon(True)
                    worker.start()

                user_followed_by, next = api.user_followed_by(with_next_url=request.session['next_url'], count=15)
                request.session['next_url'] = next
                num = 0
                for user in user_followed_by:
                    user = [num, user]
                    q.put(user)
                    num = num + 1

                q.join()
                users.sort(key=lambda pair: pair[0])

                for user in users:
                    recent_media_ = []
                    if isinstance(user[1]['recent_media'], list) == True: 
                        for media in user[1]['recent_media']:     
                            tags = []
                            if hasattr(media, 'tags'):
                                for tag in media.tags:
                                    tags.append(tag.__dict__)
                            media.tags = tags

                            comments = []
                            if hasattr(media, 'comments'):
                                for comment in media.comments:
                                    comment.created_at = comment.created_at.isoformat()
                                    comment.user = comment.user.__dict__
                                    comments.append(comment.__dict__)
                            media.comments = comments

                            if hasattr(media, 'caption'):
                                if type(media.caption) is not NoneType:
                                    if hasattr(media.caption, 'created_at'):
                                        media.caption.user = media.caption.user.__dict__
                                        media.caption.created_at = media.caption.created_at.isoformat()
                                    media.caption = media.caption.__dict__

                            if hasattr(media, 'user'):
                                media.user = media.user.__dict__

                            if hasattr(media, 'created_time'):
                                media.created_time = media.created_time.isoformat()

                            if hasattr(media, 'images'):
                                media.images['low_resolution'] = media.images['low_resolution'].__dict__
                                media.images['standard_resolution'] = media.images['standard_resolution'].__dict__
                                media.images['thumbnail'] = media.images['thumbnail'].__dict__  

                            if hasattr(media, 'videos'):
                                media.videos['low_resolution'] = media.videos['low_resolution'].__dict__
                                media.videos['standard_resolution'] = media.videos['standard_resolution'].__dict__
                                media.videos['low_bandwidth'] = media.videos['low_bandwidth'].__dict__  

                            likes = []
                            if hasattr(media, 'likes'):
                                for like in media.likes:
                                    likes.append(like.__dict__)
                            media.likes = likes

                            if hasattr(media, 'location'):
                                if hasattr(media.location, 'point'):
                                    if type(media.location.point) is not NoneType:
                                        media.location.point = media.location.point.__dict__
                                media.location = media.location.__dict__            
                            recent_media_.append(media.__dict__)
                    user[1]['recent_media'] = recent_media_
                    user[1]['user_followed_by'] = user[1]['user_followed_by'].__dict__
                    user[1]['user_relationship'] = user[1]['user_relationship'].__dict__
                
                if next == None:
                    request.session['endOfFile'] = True
            else:
                return 'End of List'
        except Exception as e:
            print(e)
        return json.dumps(users)


bottle.run(app=app, host='127.0.0.1', port=8515, reloader=True)
