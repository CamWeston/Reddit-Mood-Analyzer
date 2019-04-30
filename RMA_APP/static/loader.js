$(function() {
    //Initialize Loading Screen
    $("#loader").hide();
    $("#homeForm").submit(function( event ) {

    //Fade out the content on home
        $("#homeForm").fadeOut("slow", function(){
            $("nav").fadeOut();
            $("footer").fadeOut();
            $("#loader").fadeIn();
            //Display loading screen
            $(function () {
                var formData = $("#homeForm").serializeArray();
                var subredditName = formData[0].value;
                count = 0;
                //Display funny messages to keep the user distracted
                wordsArray = ["Feeling r/" + subredditName +" up, down and out",
                 "Getting to know r/"+ subredditName + " on personal level",
                  "Hiring a therapist for r/"+ subredditName,
                   "r/"+ subredditName + " is beginning to show their emotions",
                   "r/"+subredditName + " is getting emotional",
                   "r/"+subredditName + " is really feeling it",
                   "The shrinks are getting to work"];
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
