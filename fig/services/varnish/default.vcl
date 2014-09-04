vcl 4.0;
import std;

include "backends.vcl";

sub vcl_recv {
    include "backend_hint.vcl";
    if (req.url ~ "^/admin" || req.http.cookie ~ "sessionid" ){
        return (pass);
    } else {
        unset req.http.Cookie;
    }
    return (hash);
}

sub vcl_hit {
   if (obj.ttl >= 0s) {
       // A pure hit, deliver it
       return (deliver);
   }
   if (obj.ttl + obj.grace > 0s) {
       // Object is in grace, deliver it
       // Automatically triggers a background fetch
       return (deliver);
   }
   // fetch & deliver once we get the result
   return (fetch);
}

# Happens after reading the backend response headers
sub vcl_backend_response {
  set beresp.grace = 5m;
  set beresp.ttl = 5s;
  return (deliver);
}
