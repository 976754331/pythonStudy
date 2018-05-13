#coding=utf-8
import requests
from bs4 import BeautifulSoup
from hashlib import md5
import urllib

index = 0
#此处为保存图片的位置
imgPath = 'D:\\Python27\\code\\otherCode\\pythonSpider\\pictureSpider\\jiandan\\jandan_spider\\data\\{}.{}'
headers = {'referer': 'http://jandan.net/', 'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

#将hash值解析为url
def decrypt(n, x='2Eb1rFEI8q7OYdDM6Jz4o2qeAYyNGWzI'):
    g = 4
    x = md5(x).hexdigest()
    w = md5(x[:16]).hexdigest()
    u = md5(x[16:]).hexdigest()

    t = n[:g]
    r = w + md5(w + t).hexdigest()

    n = n[g:]
    m = (n + (3 - len(n) % 3) * '=').decode('base64')

    h = range(256)
    q = [ord(r[i % 64]) for i in range(256)]
    o = 0
    for p in range(256):
        o = (o + h[p] + q[p]) & 0xFF
        h[p], h[o] = h[o], h[p]

    l = ''
    v = 0
    o = 0
    for p in m:
        v = (v + 1) & 0xFF
        o = (o + h[v]) & 0xFF
        h[v], h[o] = h[o], h[v]
        l += chr(ord(p) ^ (h[(h[v]+h[o]) & 0xFF]))
    l = l[26:]
    return l


def save_jpg(res_url):
    global index
    html = BeautifulSoup(requests.get(res_url, headers=headers).text,"lxml")
    pictures = html.find_all('span', class_="img-hash")
    x = 0
    for link in html.find_all('span', class_="img-hash"):
        hrefItem = decrypt(link.get_text())
        with open(imgPath.format(hrefItem[26: len(hrefItem)-3], hrefItem[len(hrefItem)-3: len(hrefItem)]), 'wb') as f:
            f.write(requests.get("http:" + hrefItem).content)
        index += 1
        print("%d picture is %s"%(index,hrefItem))
    pictures = []


if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    #5代表抓取5页
    for i in range(0, 5):
        save_jpg(url)
        #翻页
        url = "http:" + BeautifulSoup(requests.get(url, headers=headers).text,"lxml").find('a',class_="previous-comment-page").get('href')


"""
jandan_load_img.png
function jandan_load_img(b) {
    var d = $(b);
    var f = d.next("span.img-hash");
    var e = f.text();
    f.remove();
    var c = jde0WEAMEeGkaWOFAz0PzUw49dDNoJ6wFk(e, "2Eb1rFEI8q7OYdDM6Jz4o2qeAYyNGWzI");
    var a = $('<a href="' + c.replace(/(\/\/\w+\.sinaimg\.cn\/)(\w+)(\/.+\.(gif|jpg|jpeg))/, "$1large$3") + '" target="_blank" class="view_img_link">[查看原图]</a>');
    d.before(a);
    d.before("<br>");
    d.removeAttr("onload");
    d.attr("src", location.protocol + c.replace(/(\/\/\w+\.sinaimg\.cn\/)(\w+)(\/.+\.gif)/, "$1thumb180$3"));
    if (/\.gif$/.test(c)) {
        d.attr("org_src", location.protocol + c);
        b.onload = function() {
            add_img_loading_mask(this, load_sina_gif)
        }
    }
}

function S45fAAhlWwSoItVgdyMFW4jIPId52kxV(n, k, x, f) {
  var k = k ? k : "DECODE";
  var x = x ? x : "";
  var f = f ? f : 0;
  var g = 4;
  x = md5(x);
  var w = md5(x.substr(0, 16));
  var u = md5(x.substr(16, 16));
  if (g) {
    if (k == "DECODE") {
      var t = n.substr(0, g)
    } else {
      var b = md5(microtime());
      var d = b.length - g;
      var t = b.substr(d, g)
    }
  } else {
    var t = ""
  }
  var r = w + md5(w + t);
  var m;
  if (k == "DECODE") {
    n = n.substr(g);
    m = base64_decode(n)
  } else {
    f = f ? f + time() : 0;
    tmpstr = f.toString();
    if (tmpstr.length >= 10) {
      n = tmpstr.substr(0, 10) + md5(n + u).substr(0, 16) + n
    } else {
      var e = 10 - tmpstr.length;
      for (var p = 0; p < e; p++) {
        tmpstr = "0" + tmpstr
      }
      n = tmpstr + md5(n + u).substr(0, 16) + n
    }
    m = n
  }
  var h = new Array(256);
  for (var p = 0; p < 256; p++) {
    h[p] = p
  }
  var q = new Array();
  for (var p = 0; p < 256; p++) {
    q[p] = r.charCodeAt(p % r.length)
  }
  for (var o = p = 0; p < 256; p++) {
    o = (o + h[p] + q[p]) % 256;
    tmp = h[p];
    h[p] = h[o];
    h[o] = tmp
  }
  var l = "";
  m = m.split("");
  for (var v = o = p = 0; p  0) && l.substr(10, 16) == md5(l.substr(26) + u).substr(0, 16)) {
      l = l.substr(26)
    } else {
      l = ""
    }
  } else {
    l = base64_encode(l);
    var c = new RegExp("=","g");
    l = l.replace(c, "");
    l = t + l
  }
  return l
}
"""