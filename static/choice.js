$(document).ready(function(){
	console.log("JS logged")

	$('.choice').click(function(){
		var choice =  $(this).children('a').text();
		var id = $(this).children('input').val();
		var name = $('#name').val();
		console.log(name);
		console.log(choice);
		console.log(id);

		$.ajax({
		    type: 'POST',
		    // Provide correct Content-Type, so that Flask will know how to process it.
		    contentType: 'application/json',
		    // Encode your data as JSON.
		    data: JSON.stringify({
		    	"id" : id,
		    	"name" : name,
		    	"choice" : choice
		    }),
		    // This is the type of data you're expecting back from the server.
		    dataType: 'text',
		    url: '/api/userchoice',
		    success: function (e) {
		        console.log(e);
		    }
});
	});
});