# oauth2-provider-sample

### Resource owner (password based flow)
Send request to authorization server
```
curl -XPOST localhost:8000/oauth2/token/ \
-d "grant_type=password&username=<username>&password=<password>" \
-u "<client_id>:<client_secret>"
```

Authorization server response
```
{
    "access_token": "3vmmxQ0anI5onZr8yYQBYjPpk1ahwf",
    "expires_in": 86400,
    "token_type": "Bearer",
    "scope": "view_user",
    "refresh_token": "KeZ9JMD7wU3wLrbTXLAorUDkHt6tLN"
}
```

### Client credentials flow
Send request to authorization server
```
curl -XPOST localhost:8000/oauth2/token/ -d "grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>"
```

Authorization server response
```
{
    "access_token": "14TIDcNBtpUtWCHBTdrV4r5hA2TJUj",
    "expires_in": 86400,
    "token_type": "Bearer",
    "scope": "view_user"
}
```

### Implicit grant
Send request to authorization server
```
curl -XGET localhost:8000/oauth2/authorize/ -d "client_id=KY4yGW3AnOCfnMDrzdb3WVBmiE7xdeCFu0GO8Xz8&response_type=token&redirect_uri=http://localhost:8002/" 
```
Authorization server redirects user to authorization page.
If user authorizes client, then authorization server redirects to `redirect_uri`

### Authorization code grant
Send request to authorization server
```
curl -XGET localhost:8000/oauth2/authorize/ -d "client_id=KY4yGW3AnOCfnMDrzdb3WVBmiE7xdeCFu0GO8Xz8&response_type=code&redirect_uri=http://localhost:8002/" 
```
Authorization server redirects user to authorization page.
If user authorizes client, then authorization server redirects to `redirect_uri`