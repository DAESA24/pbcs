---
created: 2025-12-17T17:37:34 (UTC -06:00)
tags: []
source: https://medium.com/gitconnected/7-fastapi-extensions-so-powerful-i-stopped-using-flask-forever-9c6e9a4fbb5a
author: Arslan Qutab
---

# 7 FastAPI Extensions So Powerful, I Stopped Using Flask Forever | by Arslan Qutab | Level Up Coding

> ## Excerpt
> 7 FastAPI Extensions So Powerful, I Stopped Using Flask Forever From authentication to background tasks here’s what made FastAPI my go-to for every new project. I still remember the night I …

---
## From authentication to background tasks here’s what made FastAPI my go-to for every new project.

[

![Arslan Qutab](https://miro.medium.com/v2/resize:fill:32:32/1*A0qsvGWoXRVdhyLk8YQDEw.jpeg)



](https://medium.com/@arslanshoukatali?source=post_page---byline--9c6e9a4fbb5a---------------------------------------)

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*Z4_8S92aHU40JyUW)

I still remember the night I rage-quit Flask. I was halfway through building an API for a side project, nothing fancy, just a personal task manager, and Flask decided to throw me into dependency hell. Plugins felt half-baked, **middleware** was clunky, and don’t even get me started on async support. I spent more time fixing Flask than building my app.

That’s when I switched to **FastAPI**. And not just **FastAP**I the real magic came when I discovered a set of extensions that made me feel like I was coding with superpowers. Some of these are so good that going back to Flask would feel like willingly downgrading to dial-up internet.

Let me walk you through the 7 extensions that made me ditch Flask forever.

## 1\. FastAPI Users: Authentication That Doesn’t Make You Cry

Every time I had to roll my own authentication in Flask, I felt like I was reinventing the wheel with square edges. Then I met FastAPI Users, a plug-and-play authentication and user management library.

It supports JWT, OAuth2, and even social logins out of the box. No boilerplate madness.

```
<span id="e52f" data-selectable-paragraph=""><span>from</span> fastapi <span>import</span> FastAPI<br><span>from</span> fastapi_users <span>import</span> FastAPIUsers<br><span>from</span> fastapi_users.db <span>import</span> SQLAlchemyUserDatabase<br><br>app = FastAPI()<br><br><br>fastapi_users = FastAPIUsers(user_db, [auth_backend], User, UserCreate, UserUpdate, UserDB)<br><br>app.include_router(fastapi_users.get_auth_router(auth_backend), prefix=<span>"/auth"</span>)</span>
```

Now instead of spending three nights debugging OAuth flows, I get authentication running in minutes.

## 2\. FastAPI-Mail: Email Done the Right Way

Sending emails in Flask always felt like wiring a bomb with one wrong config and nothing worked. FastAPI-Mail made it painless.

```
<span id="5423" data-selectable-paragraph=""><span>from</span> fastapi_mail <span>import</span> FastMail, MessageSchema, ConnectionConfig<br><br>conf = ConnectionConfig(<br>    MAIL_USERNAME=<span>"me@gmail.com"</span>,<br>    MAIL_PASSWORD=<span>"app-password"</span>,<br>    MAIL_FROM=<span>"me@gmail.com"</span>,<br>    MAIL_PORT=<span>587</span>,<br>    MAIL_SERVER=<span>"smtp.gmail.com"</span>,<br>    MAIL_TLS=<span>True</span><br>)<br><br>fm = FastMail(conf)<br>message = MessageSchema(subject=<span>"Test Email"</span>, recipients=[<span>"test@example.com"</span>], body=<span>"Hello FastAPI"</span>)<br><br><span>await</span> fm.send_message(message)</span>
```

I use this in production for password resets and notifications. it just works.

## 3\. FastAPI-SocketIO: Real-Time Without the Pain

I used to bolt SocketIO onto Flask, and it always felt like duct-taping a rocket to a bicycle. With FastAPI-SocketIO, real-time features feel native.

```
<span id="6159" data-selectable-paragraph=""><span>from</span> fastapi <span>import</span> FastAPI<br><span>from</span> fastapi_socketio <span>import</span> SocketManager<br><br>app = FastAPI()<br>sio = SocketManager(app=app)<br><br><span>@sio.on(<span><span>"message"</span></span>)</span><br><span>async</span> <span>def</span> <span>handle_message</span>(<span>sid, data</span>):<br>    <span>await</span> sio.emit(<span>"response"</span>, {<span>"msg"</span>: <span>f"Got: <span>{data}</span>"</span>}, to=sid)</span>
```

Last time I built a chat dashboard with this, the setup was smoother than any Flask hack I’d ever tried.

## 4\. FastAPI-Limiter: Throttle Like a Pro

Every public API I’ve built eventually got abused. With Flask, I hacked together middleware. With FastAPI, I just added FastAPI-Limiter.

```
<span id="3d23" data-selectable-paragraph=""><span>from</span> fastapi <span>import</span> FastAPI, Depends<br><span>from</span> fastapi_limiter.depends <span>import</span> RateLimiter<br><br>app = FastAPI()<br><br><span>@app.get(<span><span>"/data"</span>, dependencies=[Depends(<span>RateLimiter(<span>times=<span>5</span>, seconds=<span>60</span></span>)</span>)]</span>)</span><br><span>async</span> <span>def</span> <span>get_data</span>():<br>    <span>return</span> {<span>"msg"</span>: <span>"You’re within the rate limit!"</span>}</span>
```

Now I don’t wake up to someone spamming my endpoints a million times a second.

## 5\. FastAPI-Caching: Speed Without the Headache

Caching in Flask was… let’s just say creative. With FastAPI-Caching, I don’t have to think about it.

```
<span id="1b2c" data-selectable-paragraph=""><span>from</span> fastapi <span>import</span> FastAPI<br><span>from</span> fastapi_cache <span>import</span> FastAPICache<br><span>from</span> fastapi_cache.backends.inmemory <span>import</span> InMemoryBackend<br><br>app = FastAPI()<br><br><span>@app.on_event(<span><span>"startup"</span></span>)</span><br><span>async</span> <span>def</span> <span>startup</span>():<br>    FastAPICache.init(InMemoryBackend())<br><br><span>@app.get(<span><span>"/cached"</span></span>)</span><br><span>@cache(<span>expire=<span>60</span></span>)</span><br><span>async</span> <span>def</span> <span>get_cached_data</span>():<br>    <span>return</span> {<span>"msg"</span>: <span>"This response is cached!"</span>}</span>
```

For APIs under heavy load, this is a lifesaver.

## 6\. FastAPI-CrudRouter — CRUD in 5 Lines

In Flask, I always had to hand-roll my CRUD endpoints. With **FastAPI-CrudRouter**, I literally save hours.

```
<span id="7c4e" data-selectable-paragraph=""><span>from</span> fastapi <span>import</span> FastAPI<br><span>from</span> fastapi_crudrouter <span>import</span> SQLAlchemyCRUDRouter<br><br>app = FastAPI()<br><br>router = SQLAlchemyCRUDRouter(schema=ItemSchema, db_model=ItemModel, db=session)<br>app.include_router(router)</span>
```

Boom. Full CRUD API. Done before my coffee gets cold.

## 7\. FastAPI-Plugins: One Extension to Rule Them All

Finally, FastAPI-Plugins feels like a toolbox bundled into one. It gives you Redis, Scheduler, Caching, and logging, all ready to go.

```
<span id="bf7f" data-selectable-paragraph=""><span>from</span> fastapi_plugins <span>import</span> RedisSettings, depends_redis, redis_plugin<br><br>app = FastAPI()<br><br><span>@app.on_event(<span><span>"startup"</span></span>)</span><br><span>async</span> <span>def</span> <span>on_startup</span>():<br>    <span>await</span> redis_plugin.init_app(app, config=RedisSettings())<br><br><span>@app.get(<span><span>"/redis"</span></span>)</span><br><span>async</span> <span>def</span> <span>get_redis</span>(<span>redis=Depends(<span>depends_redis</span>)</span>):<br>    <span>await</span> redis.<span>set</span>(<span>"key"</span>, <span>"value"</span>)<br>    <span>return</span> <span>await</span> redis.get(<span>"key"</span>)</span>
```

This one made me realize: FastAPI doesn’t just replace Flask it leaps over it.

## Final Thoughts

When I look back, Flask feels like driving a beat-up Honda Civic while FastAPI (with these extensions) feels like stepping into a Tesla. Same concept, but a completely different experience.

The pro tip I’ll leave you with: don’t just learn FastAPI learn its ecosystem. These libraries aren’t “nice-to-haves”; they’re the reason I stopped touching Flask entirely.

So next time you’re about to scaffold a new project, ask yourself: why settle for Flask when FastAPI is giving you rocket fuel?
