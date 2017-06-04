$(function() {
    $('button').click(function() {
        console.log(editor.getValue())
        $.ajax({
            url: '/getAnswers',
            data: 'code='+encodeURIComponent(editor.getValue()),
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