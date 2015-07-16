Instagram Auth

from instagram import client, subscriptions
import httplib2
from urllib import urlencode

CONFIG = {
    'client_id': '47f3adaae6a245c7bca634f7d85e8fa3',
    'client_secret': 'b4a9405a9e184d3db73a93f42f655e09',
    'redirect_uri': 'http://127.0.0.1:8515/oauth_callback'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)
api = client.InstagramAPI(access_token='234902031.47f3ada.076f43c79ab94ffa9cca1ebea75dbb40', client_secret=CONFIG['client_secret'])
print api.user_recent_media(user_id=45955562, count=5)[0]
data = api.user_recent_media(user_id=45955562, count=5)[0]

http = httplib2.Http()
data = dict(client_id=CONFIG['client_id'], redirect_uri=CONFIG['redirect_uri'], response_type='token')
resp, content = http.request("https://api.instagram.com/oauth/authorize/", "GET", urlencode(data))
print resp
print content

## getting access token
https://instagram.com/oauth/authorize/?client_id=47f3adaae6a245c7bca634f7d85e8fa3&redirect_uri=http://127.0.0.1:8515/oauth_callback&response_type=token

access_token=45955562.47f3ada.b9472e0e606b4b30ba59cdd97a7309de
user_followed_by, next = api.user_followed_by(user_id=45955562, count=5)

anzhari_p = 45955562

api.user_search(q='mcquades_legacy', count=5)
mcquades_legacy = 202628411

recent_media=api.user_recent_media(user_id=202628411, count=5) -> private user

##

working multithread

from instagram import client, subscriptions
import httplib2
from urllib import urlencode

CONFIG = {
'client_id': '47f3adaae6a245c7bca634f7d85e8fa3',
'client_secret': 'b4a9405a9e184d3db73a93f42f655e09',
'redirect_uri': 'http://127.0.0.1:8515/oauth_callback'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)
api = client.InstagramAPI(access_token='234902031.47f3ada.076f43c79ab94ffa9cca1ebea75dbb40', client_secret=CONFIG['client_secret'])
def get_user_followed_by():
from thread import start_new_thread
import time
api = client.InstagramAPI(access_token='234902031.47f3ada.076f43c79ab94ffa9cca1ebea75dbb40', client_secret=CONFIG['client_secret'])
user_followed_by, next = api.user_followed_by(45955562, count=20)
users = []
def func1(user):
print user.id
if api.user_relationship(user.id).target_user_is_private == False:
users.append(dict(user_followed_by=user, recent_media=api.user_recent_media(user_id=user.id, count=5), user_relationship=api.user_relationship(user.id)))
else:
users.append(dict(user_followed_by=user, recent_media='', user_relationship=api.user_relationship(user.id)))
for user in user_followed_by:
time.sleep(0.001)
start_new_thread(func1, (user, ))
return users
var1 = get_user_followed_by()

from instagram import client, subscriptions
import httplib2
from urllib import urlencode

CONFIG = {
'client_id': '47f3adaae6a245c7bca634f7d85e8fa3',
'client_secret': 'b4a9405a9e184d3db73a93f42f655e09',
'redirect_uri': 'http://127.0.0.1:8515/oauth_callback'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)
api = client.InstagramAPI(access_token='45955562.47f3ada.b9472e0e606b4b30ba59cdd97a7309de', client_secret=CONFIG['client_secret'])
def get_user_followed_by():
from thread import start_new_thread
import time
api = client.InstagramAPI(access_token='234902031.47f3ada.076f43c79ab94ffa9cca1ebea75dbb40', client_secret=CONFIG['client_secret'])
user_followed_by, next = api.user_followed_by(45955562, count=20)
users = []
def func1(user):
print user.id
if api.user_relationship(user.id).target_user_is_private == False:
users.append(dict(user_followed_by=user, recent_media=api.user_recent_media(user_id=user.id, count=5), user_relationship=api.user_relationship(user.id)))
else:
users.append(dict(user_followed_by=user, recent_media='', user_relationship=api.user_relationship(user.id)))
for user in user_followed_by:
time.sleep(1)
start_new_thread(func1, (user, ))
return users
var2 = get_user_followed_by()

count = 0
for var in var1:
print var['user_followed_by'].id

for var in var2:
print var['user_followed_by'].id

##

users[0]['recent_media'][0][0].like_count
users[0]['recent_media'][0][0].link
users[0]['recent_media'][0][0].images['standard_resolution'].url
users[0]['recent_media'][0][0].created_time

api.user_relationships(user.id).target_user_is_private
api.user_relationships(user.id).outgoing_status
api.user_relationships(user.id).incoming_status

##

from Queue import Queue
from threading import Thread

def do_stuff(q):
  while True:
    print q.get()
    q.task_done()


q = Queue(maxsize=0)
num_threads = 10

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()


for x in range(100):
  q.put(x)
q.join()

## 
Practice queue and threading

from Queue import Queue
from threading import Thread

var1 = [{'key1': 'val1'}, {'key2': 'val2'}, {'key3': 'val3'}, {'key4': 'val4'}, {'key5': 'val5'}, {'key6': 'val6'}, {'key7': 'val7'}, {'key8': 'val8'}, {'key9': 'val9'}]

def do_stuff(q):
  while True:
    print q.get()
    q.task_done()


q = Queue(maxsize=0)
num_threads = 10

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()


yahooList = []

def yahoo(var):
  yahooList.append( var)

for x in var1:
  q.put(yahoo(x))


q.join()

##

from Queue import Queue
from threading import Thread
from datetime import datetime

def do_stuff(q):
  while True:
    print q.get()
    q.task_done()


q = Queue(maxsize=0)
num_threads = 10

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()


yahooList = []

def yahoo(var):
  yahooList.append(datetime.now())

for x in range(1000):
  print x
  q.put(yahoo(x))


q.join()

for x in yahooList:
  print x


##

Now for the real things



from instagram import client, subscriptions
from Queue import Queue
from threading import Thread

CONFIG = {
'client_id': '47f3adaae6a245c7bca634f7d85e8fa3',
'client_secret': 'b4a9405a9e184d3db73a93f42f655e09',
'redirect_uri': 'http://127.0.0.1:8515/oauth_callback'
}

access_token=45955562.47f3ada.b9472e0e606b4b30ba59cdd97a7309de

unauthenticated_api = client.InstagramAPI(**CONFIG)
api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])

users = []

def get_user_followed_by():
  user_followed_by, next = api.user_followed_by(45955562, count=20)

def do_stuff(q):
  while True:
    print q.get()
    q.task_done()

q = Queue(maxsize=0)
num_threads = 10

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()

def func1(user):
  if api.user_relationship(user.id).target_user_is_private == False:
    users.append(dict(user_followed_by=user, recent_media=api.user_recent_media(user_id=user.id, count=5), user_relationship=api.user_relationship(user.id)))
  else:
    users.append(dict(user_followed_by=user, recent_media='', user_relationship=api.user_relationship(user.id)))

for user in user_followed_by:
  q.put(func1(user))
  return users

var2 = get_user_followed_by()

## more simpler case, this kinda a work

from instagram import client, subscriptions
from Queue import Queue
from threading import Thread
from thread import start_new_thread
from time import time

CONFIG = {
'client_id': '47f3adaae6a245c7bca634f7d85e8fa3',
'client_secret': 'b4a9405a9e184d3db73a93f42f655e09',
'redirect_uri': 'http://127.0.0.1:8515/oauth_callback'
}

access_token='45955562.47f3ada.b9472e0e606b4b30ba59cdd97a7309de'

unauthenticated_api = client.InstagramAPI(**CONFIG)
api = client.InstagramAPI(access_token='45955562.47f3ada.b9472e0e606b4b30ba59cdd97a7309de', client_secret=CONFIG['client_secret'])

def do_stuff(q):
  while True:
    user_followed_by = api.user(45955562)
    print q.get(), user_followed_by.id
    q.task_done()


q = Queue(maxsize=0)
num_threads = 10

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()

time1 = time()
for i in range(50):
  q.put(i)


time2 = time()

print 'Execution time: ', time2 - time1

 ## now let's try something more complex

from instagram import client, subscriptions
from Queue import Queue
from threading import Thread
from thread import start_new_thread
from time import time

CONFIG = {
'client_id': '47f3adaae6a245c7bca634f7d85e8fa3',
'client_secret': 'b4a9405a9e184d3db73a93f42f655e09',
'redirect_uri': 'http://127.0.0.1:8515/oauth_callback'
}

access_token='234902031.47f3ada.076f43c79ab94ffa9cca1ebea75dbb40'
user_id = '45955562'

unauthenticated_api = client.InstagramAPI(**CONFIG)
api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])

users = []

def func1(user):
  if api.user_relationship(user.id).target_user_is_private == False:
    users.append(dict(user_followed_by=user, recent_media=api.user_recent_media(user_id=user.id, count=5), user_relationship=api.user_relationship(user.id)))
    print user.id
  else:
    users.append(dict(user_followed_by=user, recent_media='', user_relationship=api.user_relationship(user.id)))
    print user.id

q = Queue(maxsize=0)
num_threads = 100

def do_stuff(q):
  while True:
    func1(q.get())
    q.task_done()

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()


api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
user_followed_by, next = api.user_followed_by(user_id=user_id, count=50)

time1 = time()
for user in user_followed_by:
  q.put(user)


print user.id
q.join()
time2 = time()
print 'Execution time: ', time2 - time1

# the threading and queueing works, but the order in the list is messed up

# now let's restructure with a dict instead

from instagram import client, subscriptions
from Queue import Queue
from threading import Thread
from thread import start_new_thread
from time import time

CONFIG = {
'client_id': '47f3adaae6a245c7bca634f7d85e8fa3',
'client_secret': 'b4a9405a9e184d3db73a93f42f655e09',
'redirect_uri': 'http://127.0.0.1:8515/oauth_callback'
}

access_token='234902031.47f3ada.076f43c79ab94ffa9cca1ebea75dbb40'
user_id = '45955562'

unauthenticated_api = client.InstagramAPI(**CONFIG)
api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])

users = []

def func1(user):
  if api.user_relationship(user.id).target_user_is_private == False:
    users.append(dict(user_followed_by=user, recent_media=api.user_recent_media(user_id=user.id, count=5), user_relationship=api.user_relationship(user.id)))
    print user.id
  else:
    users.append(dict(user_followed_by=user, recent_media='', user_relationship=api.user_relationship(user.id)))
    print user.id

q = Queue(maxsize=0)
num_threads = 100

def do_stuff(q):
  while True:
    func1(q.get())
    q.task_done()

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()


api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
user_followed_by, next = api.user_followed_by(user_id=user_id, count=50)

time1 = time()
for user in user_followed_by:
  q.put(user)


print user.id
q.join()
time2 = time()
print 'Execution time: ', time2 - time1

##

from instagram import client, subscriptions
from Queue import Queue
from threading import Thread
from thread import start_new_thread
from time import time

CONFIG = {
'client_id': '47f3adaae6a245c7bca634f7d85e8fa3',
'client_secret': 'b4a9405a9e184d3db73a93f42f655e09',
'redirect_uri': 'http://127.0.0.1:8515/oauth_callback'
}

access_token='234902031.47f3ada.076f43c79ab94ffa9cca1ebea75dbb40'
user_id = '45955562'

unauthenticated_api = client.InstagramAPI(**CONFIG)
api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])

users = []

api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
user_followed_by, next = api.user_followed_by(user_id=user_id, count=50)

def do_stuff(q):
  while True:
    func1(q.get())
    q.task_done()

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()



for user in user_followed_by:
  count = 0
  q.put([count, user])
  
  ##
  
from instagram import client, subscriptions
from Queue import Queue
from threading import Thread
from thread import start_new_thread
from time import time

CONFIG = {
'client_id': '47f3adaae6a245c7bca634f7d85e8fa3',
'client_secret': 'b4a9405a9e184d3db73a93f42f655e09',
'redirect_uri': 'http://127.0.0.1:8515/oauth_callback'
}

access_token='234902031.47f3ada.076f43c79ab94ffa9cca1ebea75dbb40'
user_id = '45955562'

unauthenticated_api = client.InstagramAPI(**CONFIG)
api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])

users = []

def func1(user):
  if api.user_relationship(user[1].id).target_user_is_private == False:
    users.append([user[0], dict(user_followed_by=user[1], recent_media=api.user_recent_media(user_id=user[1].id, count=5)[0], user_relationship=api.user_relationship(user[1].id))])
    print user[1].id
  else:
    users.append([user[0], dict(user_followed_by=user[1], recent_media={}, user_relationship=api.user_relationship(user[1].id))])
    print user[1].id

q = Queue(maxsize=0)
num_threads = 100

def do_stuff(q):
  while True:
    func1(q.get())
    q.task_done()

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()

api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
user_followed_by, next = api.user_followed_by(user_id=user_id, count=50)

num = 0
for user in user_followed_by:
  user = [num, user]
  q.put(user)
  num = num + 1

q.join()
users.sort(key=lambda pair: pair[0])

import copy
usersx = copy.deepcopy(users)
for user in usersx:
    if isinstance(user[1]['recent_media'], list) == True: 
        for media in user[1]['recent_media']:
            user[1]['recent_media'] = []
            user[1]['recent_media'].append(media.__dict__)
    user[1]['user_followed_by'] = user[1]['user_followed_by'].__dict__
    user[1]['user_relationship'] = user[1]['user_relationship'].__dict__
    
usersx = copy.deepcopy(users)
for user in usersx:
    if isinstance(user[1]['recent_media'], list) == True: 
        for media in user[1]['recent_media']: 
            for comment in media.comments:
                if comment.created_at:
                    comment.created_at = comment.created_at.isoformat()
                if comment.user:
                    comment.user = comment.user.__dict__
                media.comments = []
                media.comments.append(comment.__dict__)
            media.created_time = media.created_time.isoformat()
            if media.caption:
                media.caption = media.caption.__dict__
            user[1]['recent_media'] = []
            user[1]['recent_media'].append(media.__dict__)
    user[1]['user_followed_by'] = user[1]['user_followed_by'].__dict__
    user[1]['user_relationship'] = user[1]['user_relationship'].__dict__


print json.dumps(usersx)

## 

from instagram import client, subscriptions
from Queue import Queue
from threading import Thread
from thread import start_new_thread
from time import time

CONFIG = {
'client_id': '47f3adaae6a245c7bca634f7d85e8fa3',
'client_secret': 'b4a9405a9e184d3db73a93f42f655e09',
'redirect_uri': 'http://127.0.0.1:8515/oauth_callback'
}

access_token='234902031.47f3ada.076f43c79ab94ffa9cca1ebea75dbb40'
user_id = '45955562'

unauthenticated_api = client.InstagramAPI(**CONFIG)
api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])

users = []

def func1(user):
  if api.user_relationship(user[1].id).target_user_is_private == False:
    users.append([user[0], dict(user_followed_by=user[1], recent_media=api.user_recent_media(user_id=user[1].id, count=5)[0], user_relationship=api.user_relationship(user[1].id))])
    print user[1].id
  else:
    users.append([user[0], dict(user_followed_by=user[1], recent_media={}, user_relationship=api.user_relationship(user[1].id))])
    print user[1].id

q = Queue(maxsize=0)
num_threads = 100

def do_stuff(q):
  while True:
    func1(q.get())
    q.task_done()

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()

api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
user_followed_by, next = api.user_followed_by(user_id=user_id, count=50)

num = 0
for user in user_followed_by:
  user = [num, user]
  q.put(user)
  num = num + 1

q.join()
users.sort(key=lambda pair: pair[0])

import copy
usersx = copy.deepcopy(users)
for user in usersx:
    if isinstance(user[1]['recent_media'], list) == True: 
        for media in user[1]['recent_media']: 
            tags = []
            if hasattr(media, 'tags'):
                for tag in media.tags:
                    tags.append(tag.__dict__)
                
            user[1]['recent_media'].append(media.__dict__)
    user[1]['user_followed_by'] = user[1]['user_followed_by'].__dict__
    user[1]['user_relationship'] = user[1]['user_relationship'].__dict__

print json.dumps(usersx)
    

##




from instagram import client, subscriptions
from Queue import Queue
from threading import Thread
from thread import start_new_thread
from time import time
import copy
import json
from types import *

CONFIG = {
'client_id': '47f3adaae6a245c7bca634f7d85e8fa3',
'client_secret': 'b4a9405a9e184d3db73a93f42f655e09',
'redirect_uri': 'http://127.0.0.1:8515/oauth_callback'
}

access_token='234902031.47f3ada.076f43c79ab94ffa9cca1ebea75dbb40'
user_id = '45955562'

unauthenticated_api = client.InstagramAPI(**CONFIG)
api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])

users = []

def func1(user):
  if api.user_relationship(user[1].id).target_user_is_private == False:
    users.append([user[0], dict(user_followed_by=user[1], recent_media=api.user_recent_media(user_id=user[1].id, count=5)[0], user_relationship=api.user_relationship(user[1].id))])
    print user[1].id
  else:
    users.append([user[0], dict(user_followed_by=user[1], recent_media={}, user_relationship=api.user_relationship(user[1].id))])
    print user[1].id

q = Queue(maxsize=0)
num_threads = 100

def do_stuff(q):
  while True:
    func1(q.get())
    q.task_done()

for i in range(num_threads):
  worker = Thread(target=do_stuff, args=(q,))
  worker.setDaemon(True)
  worker.start()

api = client.InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
user_followed_by, next = api.user_followed_by(user_id=user_id, count=50)

num = 0
for user in user_followed_by:
  user = [num, user]
  q.put(user)
  num = num + 1

q.join()
users.sort(key=lambda pair: pair[0])


usersx = copy.deepcopy(users)
for user in usersx:
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
#    print user[1]['recent_media']
    user[1]['user_followed_by'] = user[1]['user_followed_by'].__dict__
    user[1]['user_relationship'] = user[1]['user_relationship'].__dict__

print json.dumps(usersx)