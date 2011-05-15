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