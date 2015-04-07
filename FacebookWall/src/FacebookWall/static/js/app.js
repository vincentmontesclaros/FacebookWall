function editableTextBlurred() {
    var post_id = $(".edit-post").data('index');
    var html = $(this).val().replace(/\r\n|\r|\n/g,"\n");
    var viewableText = $('<div class="post-container" id="' + post_id + '"">' + html + '</div>' );
    $("#edit-post-" + post_id).replaceWith(viewableText);
    viewableText.click(divClicked);
}

$(document).ready(function() {
    var post_id;

    $("a").on("click", function (e) {
        post_id = $(this).attr("id");
        var divHtml = $('div[class=post-container][id="post/'+post_id+'"]').html();
        // console.log(divHtml)
        var newDiv = $('<div class="well well-lg" id=well-' + post_id + '><textarea name="content" id="edit-' + post_id + '" rows="3" class="form-control">' + divHtml + '</textarea><div class="post-button"><button class="btn btn-default btn-sm" id="cancel-edit" type="submit" value="submit">Cancel</button>&nbsp<button class="btn btn-primary" id="edit-button" type="submit" value="submit">Edit</button></div>');
        console.log(post_id)
        $('div[class=post-container][id="post/'+post_id+'"]').replaceWith(newDiv);
        var strLength = $("#edit-" + post_id).val().length * 2;
        $("#edit-" + post_id).focus();
        $("#edit-" + post_id)[0].setSelectionRange(strLength, strLength)
    });
     
    $(document).on('click', '#edit-button', function(event) {
        $("#new_content").val($("#edit-" + post_id).val());
        $("#post_id").val(post_id);
        $("#edit_post").attr("action", "post/" + post_id + "/edit/").submit();
    });

    $(document).on('click', '#cancel-edit', function(event) {
        $("#edit_post").attr("action", "post/" + post_id + "/edit/").submit();
    });

    jQuery(function(){
        $("#register").click(function(){
            $(".error").hide();
            var hasError = false;
            var passwordVal = $("#id_password").val();
            var checkVal = $("#id_confirm_password").val();
            if (passwordVal == '') {
                $("#id_password").after('<span class="error">Please enter a password.</span>');
                hasError = true;
            } else if (checkVal == '') {
                $("#id_confirm_password").after('<span class="error">Please re-enter your password.</span>');
                hasError = true;
            } else if (passwordVal != checkVal ) {
                $("#id_confirm_password").after('<span class="error">Passwords do not match.</span>');
                hasError = true;
            }
            if(hasError == true) {return false;}
        });
    });
});