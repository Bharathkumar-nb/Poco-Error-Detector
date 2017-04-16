$(function() {
    $('button').click(function() {
        var module_no = $('#opt_module').val();
        var challenge_no = $('#opt_challenge').val();
        $.ajax({
            url: '/getAnswers',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                $('#server_output').html(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});