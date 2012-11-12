import requests
from Queue import Queue
import re
q = Queue()


def rake(url):
    req = requests.get(url)
    print gen_embed(**lexical_parser(req))


def lexical_parser(req):
    looking_for = [
        ('disqus_shortname', re.compile(r'http://(.*)\.disqus\.com/embed\.js')),
        ('disqus_identifier', re.compile(r'disqus_identifier\s*=\s*["\'](.*)["\']\s*;?')),
    ]

    ret = {}

    for dest, regex in looking_for:
        search_result = re.search(regex, req.text)
        if search_result:
            ret[dest] = search_result.groups()[0]

    return ret


def gen_embed(disqus_shortname, disqus_identifier):
    return """
        <div id="disqus_thread"></div>
        <script type="text/javascript">
            /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
            var disqus_shortname = '%s'; // required: replace example with your forum shortname
            var disqus_identifier = '%s';

            /* * * DON'T EDIT BELOW THIS LINE * * */
            (function() {
                var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
                dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
                (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
            })();
        </script>
        <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
        <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>
    """ % (disqus_shortname, disqus_identifier)


if __name__ == '__main__':
    rake('http://www.cnn.com/2012/06/15/politics/obama-interrupted/index.html')
    # rake('https://www.google.com/a/northisup.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/a/northisup.com/&ss=1&ltmpl=default&ltmplcache=2')
    rake('http://northisup.com/blog/a-new-sith-or-revenge-of-the-hope-mirror/')
