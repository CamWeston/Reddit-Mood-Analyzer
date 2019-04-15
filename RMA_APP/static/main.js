$(function() {
    $("#loader").hide();
    $("#homeForm").submit(function( event ) {
        $("#homeForm").fadeOut("slow", function(){
            $("nav").fadeOut();
            $("footer").fadeOut();
            $("#loader").fadeIn();
            $(function () {
                var formData = $("#homeForm").serializeArray();
                var subredditName = formData[0].value;
                console.log(subredditName);
                count = 0;
                wordsArray = ["Feeling r/" + subredditName +" up, down and out",
                 "Getting to know r/"+ subredditName + " on personal level",
                  "Therapist-ing r/"+ subredditName,
                   "r/"+ subredditName + " is beginning to show their emotions"];
                setInterval(function () {
                count++;
                $("#loadingMessage").fadeOut(600, function () {
                $(this).text(wordsArray[count % wordsArray.length]).fadeIn(400);
                    });
                }, 2000);
            });
        });
    });
});

