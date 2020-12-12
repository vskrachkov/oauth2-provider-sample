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
