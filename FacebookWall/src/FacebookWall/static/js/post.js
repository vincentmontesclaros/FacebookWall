function divClicked() {
    var post_id = $("#edit-post").data('index');
    var divHtml = $("div[class=post-container][id="+post_id+"]").html();
    var newDiv = $('<div class="well well-lg" id=well-' + post_id + '><textarea name="content" id="edit-' + post_id + '" rows="3" class="form-control">' + divHtml + '</textarea><div class="post-button"><button class="btn btn-primary btn-sm" id="edit-button" type="submit" value="submit">Edit</button></div>');
    $("div[class=post-container][id="+post_id+"]").replaceWith(newDiv);
    var strLength= $("#edit-" + post_id).val().length * 2;
    $("#edit-" + post_id).focus();
    $("#edit-" + post_id)[0].setSelectionRange(strLength, strLength)
    // $("#edit-" + post_id).blur(editableTextBlurred);
}

function editableTextBlurred() {
    var post_id = $("#edit-post").data('index');
    var html = $(this).val();
    var viewableText = $('<div class="post-container" id="' + post_id + '"">' + html + '</div>' );
    $("#edit-post-" + post_id).replaceWith(viewableText);
    viewableText.click(divClicked);
}

$(document).ready(function() {
    $("#edit-post").click(divClicked);
     
    $(document).on('click', '#edit-button', function(event) {
        var post_id = $("#edit-post").data('index');
        $("#new_content").val($("#edit-" + post_id).val());
        $("#post_id").val(post_id);
        console.log($('#edit_post'))
        $("#edit_post").attr("action", "post/" + post_id + "/edit/").submit();
        console.log($('#edit_post').getAttribute("action"))
    });
});