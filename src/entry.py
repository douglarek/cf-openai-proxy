from js import fetch, Request, Response, URL


async def on_fetch(request, env):
    url = URL.new(request.url)
    url.hostname = "api.openai.com"
    if hasattr(env, "OPENAI_HOST") and env.OPENAI_HOST:
        url.hostname = env.OPENAI_HOST
    request = Request.new(url.toString(), request)
    api_key = request.headers.get("Authorization")
    if api_key == "Bearer " + env.TOKEN:
        request.headers["Authorization"] = "Bearer " + env.OPENAI_API_KEY
    response = await fetch(request)
    return Response.new(response.body, response)
