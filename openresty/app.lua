-- ngx.say('Hello World!')
-- ngx.exit(200)
package.path = "/opt/lua-aws/?.lua;/opt/lua-resty-http/lib/?.lua;" .. package.path 

local http = require "resty.http"
local httpc = http.new()
local AWS = require ('lua-aws.init')
local util = require ('lua-aws.util')
local cjson = require ('cjson')
ngx.req.read_body()
local user_request_body = ngx.req.get_body_data()

local res, err = httpc:request_uri("http://127.0.0.1:8000/api/bucket/create_bucket_name/", {
    method = "POST",
    body = user_request_body,
    headers = {
        ["Content-Type"] = "application/json",
    },
    keepalive_timeout = 60000,
    keepalive_pool = 10
})

if err then
    ngx.say("failed to request: ", err)
    return
end

if res.status ~= 201 then
    ngx.say(res.body)
    return
end




local aws = AWS.new({
	accessKeyId = 'sample1',
	secretAccessKey = 'sample2',
	preferred_engines = preferred,
    endpoint = 'https://sample3',
    region = 'sample4'

})

-- user_request_body = (loadsring or load)("return "..user_request_body)()
-- ngx.say(user_request_body)
local data = cjson.decode(user_request_body)
ok, r = aws.S3:api():listBuckets()
for _, b in ipairs(r.Buckets) do
	if b.Name == data['name'] then
        ngx.say('Bucket already exists')
        return
	end
end
ok, r = aws.S3:api():createBucket({Bucket = data['name']})

if not ok then
    ngx.say("failed to create bucket", r)
    return
 end





ngx.say(res.body)