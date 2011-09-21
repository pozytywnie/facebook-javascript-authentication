var isAuthenticated = false;

function login(access_token, success) {
    var local_configuration = configuration['facebook_javascript_authentication'];
    success = success || function() {};
    $.post(local_configuration['authenticate'], {access_token: access_token},
        callback = function(response) {
            isAuthenticated = true;
            if(response.status == 'ok' && typeof success != 'undefined')
                success();
        }
    );
}

function loginDialog(success, perms) {
    /*
     * Login user using Facebook authorisation mechanism.
     *
     * Displays standard Facebook login popup if neaded.
     */
    perms = perms || '';
    FB.login(function(response) {
        if (response.session) {
            login(response.session.access_token, success=success);
        }
    }, {perms: perms});
}

function fakeClick(node) {
    if(node.is('a')) {
        href = node.attr('href');
        if(node.attr('target').toLowerCase() == '_top')
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
