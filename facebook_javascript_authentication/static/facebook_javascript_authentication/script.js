var isAuthenticated = false;

function login(access_token, success) {
    var local_configuration = configuration['facebook_javascript_authentication'];
    success = success || function() {};
    $.post(local_configuration['authenticate'], {access_token: access_token},
        callback = function(response) {
            isAuthenticated = true;
            if(response.status == 'ok' && typeof success != 'undefined')
                success(response);
        }
    );
}

function updateIsAuthenticatedOnFBStatusChanged(){
    FB.Event.subscribe('auth.statusChange', function(response) {
        isAuthenticated = (response['status'] == 'connected');
    });
}

function loginDialog(success, scope) {
    /*
     * Login user using Facebook authorisation mechanism.
     *
     * Displays standard Facebook login popup if neaded.
     */
    scope = scope || '';
    FB.login(function(response) {
        if (response.authResponse) {
            login(response.authResponse.accessToken, success=success);
        }
    }, {scope: scope});
}

function fakeClick(node) {
    if(node.is('a')) {
        var href = node.attr('href');
        var target = node.attr('target');
        if(typeof target != 'undefined' && node.attr('target').toLowerCase() == '_top')
            top.location = href;
        else
            window.location = href;
    } else {
        node.click();
    }
}

function initLoginRequired(permissions) {
    function requireLogin() {
        var node = $(this);
        var isButton = node.is('button, input[type=submit]')
        function resubmit() {
            // unbind, so fakeClick doesn't see handler on node
            node.unbind('click', requireLogin);
            if(isButton)
                node.attr('disabled', false);
            fakeClick(node);
        }
        function cancel() {
            if(isButton)
                node.attr('disabled', false);
        }
        if(!isAuthenticated) {
            if(isButton)
                node.attr('disabled', true);
            loginDialog(resubmit, permissions, cancel);
            return false;
        }
    }
    $(function() {
        $('.login-required').click(requireLogin);
    });
}
