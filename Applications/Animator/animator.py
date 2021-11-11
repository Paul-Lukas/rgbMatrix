from flask import render_template
from flask.views import View


class ListAnimations(View):

    def dispatch_request(self):
        content = {"test", "test2", "test3"}
        return render_template('/Applications/Animator/templates/animList.html', content=content)
