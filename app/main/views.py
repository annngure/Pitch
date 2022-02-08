from flask_login import login_required
from ..models import Reviews, User



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username  = uname).first()

    if user is None:
        abort(404)
    
    return render_template('profile/profile.html', user = user)