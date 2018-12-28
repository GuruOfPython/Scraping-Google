import re

def get_url(raw_url):
    match = re.findall(r"url\(\'([^)^\']+)", raw_url)[0]
    if "https" not in match:
        match = "http:" + match
    return match



raw_url = "background-image:-webkit-linear-gradient(top, rgba(0,0,0,0), rgba(0,0,0,0.5)),url('//geo1.ggpht.com/cbk?panoid=PlKo-BPkSGkjVeifwnt6_g&output=thumbnail&cb_client=search.LOCAL_UNIVERSAL.gps&thumb=2&w=158&h=78&yaw=263.92426&pitch=0&thumbfov=100');height:78px;width:158px"
get_url(raw_url=raw_url)
